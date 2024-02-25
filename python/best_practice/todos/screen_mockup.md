# 画面モックアップ

■ 文字だけで伝えず、画像や画面で伝える

- 開発せずに作りたいものの価値を確認するために画面モックアップを作成する。
- Balsamiq Mockup のようなツールを使っても良い。
- 画面モックアップを描き出す理由は「画面の仕様」を決めることではなく、その仕様から本当に必要なものができるか、どういったデータ設計が必要か、システム設計が必要かを読み取ることにある。
- 遷移、入力、表示に注目して画面モックアップを描く。
  - 遷移：この画面はどこからきてどこに行くのだろう。
  - 入力：この画面では何を入力するのだろう。
  - 表示：この画面ではどんな情報が表示されるのだろう。(表示しなくて良いのだろう)
- コアになる画面から描く。

- お弁当の検索: 初期段階ではお弁当の名前とお店の名前からのみ検索します。検索は DB の Like 検索で十分
- お届け先住所: ユーザーはいつお届け先住所を入力するでしょうか？複数登録できて、よく使う住所を一つ設定しておけると良いか
- 配達時間の目安: 何をもとに配達時間は算出されるべきか。店舗の住所とユーザーのお届け先住所から算出しているのか。算出は曖昧な時間で済ませるべきか、地理的な情報だけでなく、メニューの準備にかかる時間も加算すべき。
- 配達の早い順: 店舗の住所とお届け先住所からプログラムで計算するのであれば DB のソートは不可能。地理情報の扱える DB を使って 2 点間の距離を算出して距離から大まかな時間を算出できればソートはできそう。
- 評価: 1-5 でつけれられるもの。商品ごとのレビューの平均を算出したもの。
- 評価の高い順: 商品のレビューの平均を計算して並べ替えるのは時間がかかりそう。平均評価を 5 分ごとや 10 分ごとに算出して別途管理するのもあり。

■ 最小で実用できる部分から実装する

- 何かを作る上でコストと締切は無視できない。初期に必須の機能と不要な機能を分類するのも良い。