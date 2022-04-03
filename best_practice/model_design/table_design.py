"""テーブル設計

■NULLをなるべく避ける
 NULLを許容するとアプリケーション側で「NULLの場合」を扱う処理や仕様が必要になり、プログラムが煩雑になる。
 NULL可能の回避方法
 ・仕様として受け入れない
 ・デフォルト値を使う
 ・NULL不可にして空文字や0を設定

■一意制約をつける
 仕様上、想定しないデータがあればできるだけ一意制約をつける。
 「ユーザーは同じ商品に一つしか商品レビューをつけられない」という仕様であれば、「商品レビュー」tableの
 「ユーザー」と「商品」の二つのカラムに一意制約をつける。
■参照頻度が低いカラムはテーブルをわける
 テーブルのカラムが増えると参照やJOINが遅くなる問題がある。参照した時のデータ転送時に、データ量が多くなり、
 JOINする際に、必要な一時テーブルの容量が多くなるため。
 以下の場合にテーブルを分離する
 ・「ユーザープロフィール」テーブル
  ・自己紹介文
  ・誕生日
  ・趣味
 ・「支払い」テーブル
  ・決済方法
  ・カードの情報
■予備カラムを用意しない
 予備カラムの問題点
  ・カラム名が意味を説明できない・・・「yobi_001はキャンペーンIDが入っている」と直感的にわからない
  ・事前に決めた型でしか扱えない・・・文字列型として数値や日付を管理する必要がでてくる。外部キーを貼れない。
  ・事前に決めたカラムの大きさで使うしかない。
 必要になった際にカラムを追加するので十分。
■bool値ではなく日時にする
 class Article(modes.Model):
     published = models.BooleanField("公開済みフラグ", default=False)
     published_at = models.DataTimeField("公開日時", default=None, null=True, blank=True)
 publishedというカラムを用意しなくても、published_atカラムを使えば、公開されたかどうかは判定できる。
 NULLの場合は「非公開」であり、データがある場合は「公開済み」と扱う。
 日時で状態が切り替わるような値や記録としてつける値の場合にはbool値でなく日時にすると良い。
 ・記事公開済みフラグ→記事公開日時
 ・メール送信済みフラグ→メール送信日時
 ・商品販売中フラグ→商品販売開始日時、終了日時
 ・課金停止フラグ→課金停止日時
 ・トークン失効フラグ→トークン失効日時
 ・支払い処理完了フラグ→支払い処理完了日時
 ・同期済みフラグ→同期日時
 以下の値はbool値が設定された日時が必要ないのでbool値が望ましい。
 ・メールマガジン購読中のような設定値
 ・アンケートやフィードバックのチェックボックスの値

"""