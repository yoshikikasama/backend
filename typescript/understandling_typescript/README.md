# Backend study directory

## Typescript

### Command

```txt
npm install lite-server --save-dev
```

別 tab で typescript のコンパイラを watch mode で起動

```txt
npx tsc <file_name> --watch(or --w)
```

typescript で一つのプロジェクトフォルダであることを認識させる

```txt
npm tsc --init
```

### memo

- クラスとインスタンス
  - Object
    - プログラミングコードで扱う物
    - クラスのインスタンス（＝クラスに定義に基づくオブジェクト）
    - オブジェクトリテラル（中括弧）の定機の代わりにオブジェクトを作成する手段
  - Class
    - オブジェクトの設計図（理論上の定義）
    - オブジェクトの構造を定義する（どういうプロパティやメソッドがあるか）
    - 同じ構造の似たオブジェクトを繰り返し 作成する手順を簡単にする
- property
  - オブジェクト（もの）が持っているデータや特徴
  - 例えば、「りんご」というオブジェクトがあったとしたら、りんごには次のような特徴があるやろ？
    - 色：赤
    - サイズ：小さい
    - 味：甘い
  - これをプログラムで書くと、こんな感じ：
  - ```javascript
    const apple = {
      color: "red", // 色
      size: "small", // サイズ
      taste: "sweet", // 味
    };
    ```
  - ここで、color、size、taste が「プロパティ」や！
- decorator
  - クラス、プロパティ、メソッド、アクセサ（getter/setter）、またはメソッドのパラメータに追加できる特殊な関数です。 デコレータは、クラスやその要素の動作を「修飾」または「拡張」するために使われます。
    大丈夫です！TypeScript 初心者向けに、1 からわかりやすく説明します。
- 1. デコレータとは何か
  - デコレータは、「**特定のクラスやその部品に対して追加の処理を加える**」仕組みです。
  - たとえば、何かを作るたびに「記録を残したい」と考えたとします。クラスやプロパティにデコレータを付けると、そのクラスが使われたタイミングで自動的に何かを実行できます。
- 2. デコレータの基本構造

```typescript
function SimpleDecorator(target: any, propertyName: string) {
  console.log("デコレータが実行されました！");
  console.log("target:", target); // 対象の情報
  console.log("propertyName:", propertyName); // プロパティの名前
}

class Example {
  @SimpleDecorator // デコレータを使う
  myProp: string = "Hello";
}
```

- どういう仕組みか

  - **`SimpleDecorator`**: デコレータ関数です。対象に対して追加処理をします。
  - **`@SimpleDecorator`**: この行で`SimpleDecorator`関数を`myProp`というプロパティに「適用」しています。
  - 実行すると、`SimpleDecorator`の中身（`console.log`）が動きます。

  - `target`と`propertyName`とは？
  - `target`: デコレータが適用されているものが属している場所を表します。
    - クラスの中で使われると、そのクラスの情報が入ります。
    - 例えば、上の例では`Example`クラスの情報が`target`に入ります。
  - `propertyName`: デコレータが修飾しているプロパティの名前です。
  - 上の例では`myProp`というプロパティが修飾されているので、`propertyName`には`"myProp"`が渡されます。

-　 1. オブジェクト（object）とは？

- オブジェクトとは何か
- オブジェクトはデータの集まりです。
- 名前（プロパティ）とその値をまとめて管理します。
- 例えば：

```javascript
const person = {
  name: "太郎",
  age: 25,
};
```

- person はオブジェクト。
- 中には、name と age というプロパティが含まれています。
- オブジェクトは特定の型がない（柔軟）
- JavaScript/TypeScript では、オブジェクトは動的にプロパティを追加・変更できます。
- クラスを使わずに、直接オブジェクトを作成することもできます。

```javascript
const dynamicObject = {};
dynamicObject.newProperty = "追加されたプロパティ";
console.log(dynamicObject.newProperty); // → "追加されたプロパティ"
```

- 3. デスクリプタ（descriptor）とは？
  - デスクリプタは、プロパティの詳細設定を書くオブジェクトです。
  - 基本構造
  - デスクリプタは以下のような「設定項目」を含むオブジェクトです：

| 項目         | 説明                                                     | デフォルト |
| ------------ | -------------------------------------------------------- | ---------- |
| value        | プロパティの値。person.name のように使える。             | undefined  |
| writable     | 値を変更できるかどうか。true なら書き換え可能。          | false      |
| enumerable   | プロパティが for...in や Object.keys()で見えるかどうか。 | false      |
| configurable | 削除や再定義が可能かどうか。                             | false      |

- 4. 実例を使った詳しい説明
  - プロパティを定義してみよう
  - Object.defineProperty を使って、オブジェクトに新しいプロパティを追加します：

```javascript
const person = {};

// プロパティ "name" を追加
Object.defineProperty(person, "name", {
  value: "太郎", // 値
  writable: true, // 書き換え可能
  enumerable: true, // 他のコードから見えるようにする
  configurable: true, // 削除や再定義が可能
});

// 値を確認
console.log(person.name); // → '太郎'
```

- 1. プロトタイプとは？
  - 基本的なイメージ: オブジェクト同士が「共有する仕組み」。
  - JavaScript では、すべてのオブジェクトが「隠れたリンク」で別のオブジェクトに接続されています。
  - このリンク先のことをプロトタイプと言います。

```javascript
const person = {
  greet() {
    console.log("こんにちは！");
  },
};

const taro = Object.create(person); // `person` をプロトタイプとして持つオブジェクトを作成
taro.greet(); // → "こんにちは！"
```

- taro は person をプロトタイプとして持っています。
- taro 自身には greet メソッドは存在しませんが、プロトタイプから引っ張ってきて使っています。

- JavaScript ではクラスも内部的にはプロトタイプを使っています。
- クラスを定義すると、メソッドがすべてそのクラスのプロトタイプに登録されます。

```javascript
class Person {
  greet() {
    console.log("こんにちは！");
  }
}

const taro = new Person();
taro.greet(); // → "こんにちは！"
```

- このとき、内部的には以下のような関係になります：
- Person クラスのメソッド（greet）は、Person.prototype に保存される。
- taro オブジェクトは Person.prototype をプロトタイプとして参照している。

```javascript
console.log(taro.__proto__ === Person.prototype); // → true
```

JavaScript でクラスを定義すると、裏では以下のような「プロトタイプを使ったオブジェクト構造」が自動的に作られます。

```javascript
class Example {
  greet() {
    console.log("こんにちは！");
  }
}
```

- 裏で行われていること
- Example 関数が作成される
- 実は、class は constructor 関数を作るための「糖衣構文（便利な書き方）」です。
- 書き換えると、以下と同じ意味になります：

```javascript
function Example() {
  // クラスのコンストラクタ
}
Example.prototype.greet = function () {
  console.log("こんにちは！");
};
```

- Example.prototype が自動的に作られる
  - プロトタイプは、クラスや関数の「共有メソッドの保存場所」です。
  - クラスで定義したメソッド（例: greet）は、この Example.prototype に追加されます。
- constructor プロパティが設定される
  - JavaScript では、すべてのプロトタイプオブジェクトに constructor というプロパティが自動的に追加されます。
  - このプロパティは、そのプロトタイプが属する関数（クラス）を指します。
  - つまり、Example.prototype.constructor === Example が成り立ちます。

-　デコレータファクトリ

- 「パラメータを受け取ってデコレータを返す関数」です。通常のデコレータはそのまま適用されますが、デコレータファクトリは設定を追加できるようにする仕組みです。
- デコレータファクトリ:

```typescript
@SomeDecoratorFactory("設定値")
```

```typescript
function Logger(logString: string) {
  console.log("LOGGER ファクトリ");
  return function (constructor: Function) {
    console.log(logString);
    console.log(constructor);
  };
}

@Logger("ログ出力中 - PERSON") // デコレータファクトリ
class Person {
  name = "Max";

  constructor() {
    console.log("Personオブジェクトを作成中...");
  }
}
```

- Logger 関数は「文字列（logString）」を受け取るデコレータファクトリです。
- この関数は、「デコレータ関数」を返します。
- デコレータ関数の第一引数 constructor は、デコレータが適用されたクラスのコンストラクタを指します。
- Logger 関数が呼ばれる
  - 引数 logString に "ログ出力中 - PERSON" が渡される。
  - "LOGGER ファクトリ" がコンソールに表示される。
- デコレータ関数が返される
  - Logger 関数はデコレータ関数を返します。
  - デコレータ関数はクラスが定義された直後に呼び出されます。
- デコレータ関数が実行される
  - constructor には Person クラスのコンストラクタが渡されます。
  - logString の値がコンソールに表示されます。
  - constructor（クラスの定義そのもの）がコンソールに表示されます。
