"""CSV操作
aws cliの初期設定
aws configure
設定の確認
~/.aws/

boto3 Client APIとResource API
Client API・・・リソースを操作する場合も参照系と同様に、対象のリソースIDを引数に加えてメソッドを実行する。
Resource API・・・リソースを操作する場合には対象のリソースを「object」として取得してからobjectのもつメソッドを呼び出して操作する。
BytesIO・・・メモリ上でバイナリデータを扱うための機能です。Python の標準ライブラリ io に含まれています。バイナリデータとは主に画像や音声などのデータのことです。コンピューターで扱うデータは全てバイナリデータなのですが、テキストデータと対比して用いられます。
TextIOWrapper・・・テキストモード

1.　s3　bucketの作成
2.　「test.csv」のupload
3. csvファイルの読み込み
4. s3上のcsvファイルから特定の値を抽出
5. 作成したobject,bucketの削除

"""
import io
import csv
import json
import boto3

BUCKET_NAME = "yoshiki-s3-2022-bucket"
KEY = "test.csv"


def s3_client():
    s3 = boto3.client('s3')
    return s3


def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-northeast-1'
        }
    )


def create_bucket_policy(bucket_name):
    # IAMポリシーでアクセスする許可と拒否の条件をJSON形式で記述したものがPolicyドキュメント
    bucket_policy = {
        # policy statementの現行version
        "Version": "2012-10-17",
        "Statement": [
            {
                # Statement ID(任意のID)
                "Sid": "AddPerm",
                # リソースへのアクセスを許可するには、Effect 要素を Allow に
                "Effect": "Allow",
                # ステートメントのアクションやリソースへのアクセスが許可されているアカウントまたはユーザー
                "Principal": {
                    "AWS": "arn:aws:iam::068788852374:user/yoshiki.kasama"
                },
                # s3に対する全てのactionを許可
                "Action": ["s3:*"],
                # ステートメントで取り扱う一連のオブジェクトを指定します。
                "Resource": ["arn:aws:s3:::yoshiki-s3-2022-bucket/*"]
            }
        ]
    }
    policy_string = json.dumps(bucket_policy)
    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )


def upload_file(bucket_name, key):
    file_path = "./csv_files/test.csv"
    s3_client().upload_file(file_path, bucket_name, key)


def get_csv_file(bucket_name, key):
    response = s3_client().get_object(Bucket=bucket_name, Key=key)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('get_object succeeded!')
    body = io.TextIOWrapper(io.BytesIO(response['Body'].read()))
    # print(body)
    # print(type(body))
    for row in csv.DictReader(body):
        print(row)


# def select_object(bucket_name, key):
#     response = s3_client().select_object_content(
#         Bucket=bucket_name,
#         Key=key,
#         Expression='Select name from S3Objects',
#         ExpressionType='SQL',
#         InputSerialization={'CSV': {'FileHeaderInfo': 'Use'}},
#         OutputSerialization={'JSON': {}}
#     )
#     for event in response['Payload']:
#         if 'Records' in event:
#             print(event['Records']['Payload'].decode())

def list_buckets(bucket_name):
    response = s3_client().list_objects_v2(
        Bucket=bucket_name
    )
    keys = []
    for data in response['Contents']:
        keys.append(data['Key'])
    return keys


def delete_objects(bucket_name, keys):
    objects = []
    for k in keys:
        objects.append({
            'Key': k,
        })
    response = s3_client().delete_objects(
        Bucket=bucket_name,
        Delete={
            'Objects': objects,
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('delete_objects succeeded')


def delete_bucket(bucket_name):
    response = s3_client().delete_bucket(
        Bucket=bucket_name
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 204:
        print('delete_bucket succeeded')


def main():
    response = create_bucket(BUCKET_NAME)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("create bucket succeeded!")
    create_bucket_policy(BUCKET_NAME)
    upload_file(BUCKET_NAME, KEY)
    get_csv_file(BUCKET_NAME, KEY)
    # select_object(BUCKET_NAME, KEY)
    keys = list_buckets(BUCKET_NAME)
    delete_objects(BUCKET_NAME, keys)
    delete_bucket(BUCKET_NAME)


if __name__ == '__main__':
    main()
