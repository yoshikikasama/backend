# 関数設計

■ 関数名

- 動詞：get*, calculate*, is\_
- 取得できるものの名詞: current_date, as_dict
- 役割: json_parser

■get の置き換え

- load: ファイルなどの読み込みをする
- fetch/retrieve:　外部(API など)からデータを取得する。
- search: 何らかの検索処理(ID での取得でなく、条件での取得)が発生する
- calc: 副作用(外部へのアクセスや読み込み、IO)なしに計算だけする。
- increase/decrease: 値を加算/減算する
- merge: 2 つのデータを合わせて 1 つのデータにする
- render: 文字列や画像を処理して描画する。
- filter: 複数のデータから要素を取り込む
- aggregate: 複数の情報から集計、計算する。
- build/constract: 何らかの情報から文字列やオブジェクトを作成する。
- escape/sanitize: 文字列をエスケープ、サニタイズ処理をする。

■save の置き換え

- dump: あるデータソースから別のファイルなどにデータをまとめて保存する。
- create: 更新でなく新規作成する。
- update: 新規作成でなく、更新する。
- patch: 部分的に情報を更新する。
- remove/delete: 削除する
- sync: 作成、削除、更新を行なって 2 つのデータソースの値を同じにする
- memorize: メモリージョウンい一時的に記録する
- publish: 隠されていた情報を外部に公開する

■send の置き換え

- notify: 外部のサービスやオブジェクト間での通知をする

■ 他におすすめの単語

- flatten: 階層構造を持つオブジェクトを 1 階層にする
- minimize: 値を最小化する
- validate/ verify: 値が正しいかを確認、検証する(check より意味が狭い)

- point: github の検索機能に調べたい英単語を入力して、どのような処理に英単語が使われているかを調べてみるのもいい。

■is*, has*ではじまる変数名、関数名の場合は bool で return し、外部へのアクセス、データ保存や読み込み、値の変換などの副作用がないようにする。

■ 再利用性の低い処理は、main()にまとめる。

■ リストや辞書をデフォルト引数にしない

```python:
def foo(values=[]):
```

- python ではデフォルト引数の値は関数やメソッドの呼び出しのたびに初期化されない。
- 関数をデフォルト引数で呼び出すたびにリストの値が変わってしまう。
- リスト、辞書、集合は None で設定し関数内で空のリストや辞書を指定する。

```python:
def foo(values=None):
    values = values or []
```

■ コレクションをデフォルト引数にせず int や str を受け取る

- 関数の再利用性が低くなるため。
- 単体テストも楽になる。

■index 番号に意味を持たせない。

- タプルで管理して、インデックス番号に意味を持たせると、意味を覚えなきゃいけないのでやりづらい。
- タプルで管理せずに辞書やクラスで管理するようにする。

```python
@dataclass
class Sale:
    sale_id: int
    item_id: int
    amount: int
def validate_sales(sale):
    if not item_exists(sale.item_id):
        raise...
    if sale.amount < 1:
        raise...
```

- 明示的に index が必要な時は enumerate を使用する。

```python:
for n, item in enumerate(items, start=1):
    print(n, "個目を処理中")
```

■ 関数の引数に可変長引数(\*args, \*\*kwargs)を乱用しない

- class が期待していない値を受け取れ、エラーにもならなくなる。
- 個別の引数で指定する。

```python
class User:
    def __init__(self,name, mail=None):
        self.name=name
        self.mail=mail
```

■ コメントにはなぜを書く

- コメントは処理が複雑な場合だけ、なぜそう書くのかを記載する。

■ コントローラーには処理を書かない。

- main 関数や Django の View のような場所には、処理全体の制御のみを記載する。

- Django
  - Form:入力のバリデーションチェック、HTML の画面に入力フォームを表示する。フォームから送信されたデータの検証をする。
  - Template：値の描画。テンプレートと値から HTML を描画して、ブラウザー上の画面を表示する。
  - Model:データベースに情報の保存。
  - validators: member_permission check など
