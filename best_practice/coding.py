"""コード実装

関数名
・動詞：get_, calculate_, is_
・取得できるものの名詞: current_date, as_dict
・役割: json_parser

■getの置き換え
load: ファイルなどの読み込みをする
fetch/retrieve:　外部(APIなど)からデータを取得する。
search: 何らかの検索処理(IDでの取得でなく、条件での取得)が発生する
calc: 副作用(外部へのアクセスや読み込み、IO)なしに計算だけする。
increase/decrease: 値を加算/減算する
merge: 2つのデータを合わせて1つのデータにする
render: 文字列や画像を処理して描画する。
filter: 複数のデータから要素を取り込む
aggregate: 複数の情報から集計、計算する。
build/constract: 何らかの情報から文字列やオブジェクトを作成する。
escape/sanitize: 文字列をエスケープ、サニタイズ処理をする。

■saveの置き換え
dump: あるデータソースから別のファイルなどにデータをまとめて保存する。
create: 更新でなく新規作成する。
update: 新規作成でなく、更新する。
patch: 部分的に情報を更新する。
remove/delete: 削除する
sync: 作成、削除、更新を行なって2つのデータソースの値を同じにする
memorize: メモリージョウンい一時的に記録する
publish: 隠されていた情報を外部に公開する

■sendの置き換え
notify: 外部のサービスやオブジェクト間での通知をする

■他におすすめの単語
flatten: 階層構造を持つオブジェクトを1階層にする
minimize: 値を最小化する
validate/ verify: 値が正しいかを確認、検証する(checkより意味が狭い)
"""
