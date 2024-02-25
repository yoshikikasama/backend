
# 構成管理

## ChangeLog.rst

---
### 書くこと
- #<チケット番号><追加・変更・削除した機能がわかる短い説明>
  - dev、本番、開発者の個人環境へのデプロイごとにその環境で行うコマンドライン操作等
    - pip install
    - tox -r
    - ファイル・ディレクトリ作成
    - rundeck設定変更

### パッケージ管理

---
 以下のファイル・ディレクトリで管理する。
- constraints.txt
- requirements.txt
- requirements_dev.txt
- run-requires.txt
- tests-require.txt
- wheelhouse/  

 使い方
- 直接依存しているパッケージはrun-requires.txtに記載する
- パッケージのバージョンは、直接・間接依存に関わらずconstraints.txtに記載する。
<br>
<br>
<br>

## Pythonコーディング
---
### TypeHints
---
- PEPに従う

### Docstring
---
- docstringはreStructuredText記法で書く
- 関数、メソッドのdocstring:
    - 引数と戻り値の記述は、Sphinxで扱える形式で記載
    - クラスのdocstring
      - クラスの目的を必ず書く
    - モジュールのdocstring
      - できるだけ書く
      - 後で「この関数どこに置こうかな」という場合に適切なモジュール設定をする。
      - このモジュールはどんな目的なのだろう？というのがすぐにわかるようにする。
