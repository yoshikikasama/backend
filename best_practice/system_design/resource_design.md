# リソース設計

■ファイルパスはプログラムからの相対パスで組み立てる

- 実行するディレクトリによってファイルやモジュールが見つからずにimportエラーとなる。
- どこからプログラムが実行されても適切に動くようにパスを組み立てるようにする。
```python

# projects/scripts/read_csv.py
# projects/scripts/target.csv
  
import csv
from pathlib import Path

# 起点となるプログラムがあるパス
here = Path(__file__).parent
CSV_PATH = here / 'target.csv'

with CSV_PATH.open(mode='r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)
```
- pythonでは__file__でそのファイルへのパスを取得できる。そこから現在のディレクトリのパスを取得して、  
&nbsp;相対的な外部ファイルまでのパスを組み立てれば、どこからプログラムが実行されてもファイルが見つかる。  
&nbsp;DjangoでもBASE_DIRで起点となるパスを定義してそれを利用してパスを組み立てたりする。

■ファイルを格納するディレクトリを分散させる

- 作成したすべてのファイルを1つのディレクトリに置くと、パフォーマンスの低下などの問題が生じる。
- データベースで自動採番されるIDなどを利用してディレクトリを分けるなどする。

■一時的な作業ファイルは絶対に競合しない名前を使う

- アクセス数が少ない場合でも偶然タイミングがあってしまえば、競合問題が発生する。
- Pythonであればtempfileモジュールを使用すれば、ファイル名の競合を避けて、一時的なファイル作成ができる。
```python
import tempfile

with tempfile.NamedTemporaryFile(prefix='receipt-') as f:
    f.write(data)
    send_file(f.name)

# withブロックを抜けるとファイルは自動的に削除される
```

■セッションデータの保存にはRDBかKVSを使用する

- セッションをwebアプリケーションサーバーのファイルシステムに保存すると以下の問題がある
    - セッションファイル数に比較してDISKへの負荷が増える
    - セッションファイルが増え続け、DISKが溢れる
    - 複数のアプリケーションサーバーを多重化した場合、どちらのサーバーにセッションがあるかによってログイン状態が変わってしまう

- RDBにセッションを保存すると、複数のwebアプリケーションサーバーでセッションデータを共有できる。  
&nbsp;RDBのセッションデータも削除するようにmanage.py clearsessionsコマンドを1日1回呼び出すようにcronやsystemd.timerを設定しておく。  
- Redis(KVS)の良い点は利用期限を過ぎたセッションデータが自動的に削除されること。
