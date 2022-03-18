"""ユニットテスト

■テストにテスト対象と同等の実装を書かない

■1つのテストメソッドでは1つの項目のみ確認する

■テストしにくい実装は設計が悪い

■ベストプラクティス
・関数の引数やフィクスチャーに大げさな値が必要な設計にしない
・処理を分離して全ての動作確認に全てのデータが必要ないようにする
・関数やクラスを分離して、細かいテストは分離した関数、クラスを対象に行う
　（分離した関数を呼び出す関数では細かいテストは書かないようにする。)

fixture(conftest)をうまく活用する。
parametrizeをうまく活用する。
"""
from best_practice.unittest.sales import load_sales
import main
import pytest


def test_calc_md5():
    actual = main.calc_md5('This is Content ')
    assert actual == "e61994e96b20e3965b61de16077e18c7"


class TestValidate:
    # 変数と結果をパラメータでテストコードに渡すことで、1つのテストメソッドで複数パターンのテストを行うことができる
    @pytest.mark.parametrize('text', ['a', 'a' * 50, 'a' * 100])
    def test_valid(self, text):
        """検証が正しい場合
        """
        # Trueでreturnされるかどうか
        assert main.validate(text)

    @pytest.mark.parametrize('text', ['', 'a' * 101])
    def test_invalid(self, text):
        """検証が正しくない場合
        """
        # Falseでreturnされるかどうか
        assert not main.validate(text)

# 読みやすくするためにテストコードを準備(Arrange)と実行(Act)と検証(Assert)に
class TestSignupAPIView:

    # fixture：テストの前処理を行うための機能
    @pytest.fixture
    def target_api(self):
        return '/api/signup'

    def test_do_signup(self, target_api, django_app):
        # 準備
        from account.models import User

        params = {
            "email": "signup@example.com",
            "name": "yamadataro",
            "password": "xxxxxx"
        }
        # 実行
        res = django_app.post_json(target_api, params=params)

        # 検証
        user = User.objects.all()[0]
        expected = {
            "status_code": 201,
            "user_email": "signup@example.com"
        }
        actual = {
            "status_code": res.status_code,
            "user_email": user.email
        }
        assert expected == actual

class TestLoadSales:
    def test_invalid_row(self, tmpdir):
        test_file = tmpdir.join('test.csv')
        test_file.write("""id,item_id,price
        1,1,100
        2,1,100
        """)
        
        sum_price, actual_sales = load_sales(test_file.strpath)
        assert sum_price == 0
        assert len(actual_sales) == 0

    def test_invalid_type_amount(self, tmpdir):
        # テストのたびにCSVファイルを毎度用意する必要がある。
        test_file = tmpdir.join('test.csv')
        test_file.write("""id,item_id,price,amount
        1,1,100,foobar
        2,1,100,2
        """)
        sum_price, actual_sales = load_sales(test_file.strpath)
        assert sum_price == 400
        assert len(actual_sales) == 1

        