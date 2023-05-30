# Section7 モジュール

今までの回で，Pythonの基本的な文法やデータ型，制御構文，関数，クラスについて説明しました．
今回はそれらを用いてプログラムを作成する上で役に立つ情報について説明していきます．
具体的にはモジュール，外部ライブラリ，ファイル入出力，そしてより良いコードを書くためのコツについて説明します．

## モジュール・import


**困難は分割せよ**

大きなものを一度に作ろうとするのは難しいことが多いです．
そこで，作りたいものを小さな部品に分割して，それらを組み合わせて作ることが多いです．
例えばパソコンは，CPU，メモリ，ハードディスク，ディスプレイ，キーボード，マウスなどの部品を組み合わせて作られています．
このようにモジュールに分けることで，作るものが小さくなりそれぞれの部品を作るのは見通しが立ちやすくなります．
また，使う部品を入れ替えることなどもできるため，改良・拡張などもしやすくなります．
（メモリを交換して16GBから32GBに変更するみたいに）

ソフトウェアも同じで，大きなものを一度に作るのは難しいので，小さな部品に分割して作ることが多いです．
（もし数千行のコードを一つのファイルに書いたら...修正する場所を探すだけでも苦労しそうです）
この小さな部品のことをモジュールと呼びます．
モジュールは一つのファイルだったり，複数のファイルを集めたパッケージだったりします．


### import 文の基本

外部のファイルに書いたものを使うには，`import`文を使います．

例えば `cat.py`というファイルに以下のようなコードを書いたとします．

```python
class Cat():
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("にゃーん")
    
    def get_name(self):
        return self.name
```

このファイルの中で定義されているクラス`Cat`を別のファイルで使いたいとします．
そのときには，以下のように`import`文を使います．


```python
import cat

tama = cat.Cat("タマ")
tama.meow()
```

`import`文を使うと，`cat.py`の中で定義されているクラスや関数を使うことができます．
`import`文を使うときには，`import`したファイル名の後に`.`をつけて，その後に`import`したいクラス名や関数名を書きます．
`cat.Cat`は，`cat.py`の中で定義されている`Cat`クラスを使うという意味です．

### 別名でimport

`import cat as neko` のように，別名で`import`することもできます．
その場合は，`cat.Cat`の代わりに`neko.Cat`と書くことになります．

```python
import cat as neko

tama = neko.Cat("タマ")
tama.meow()
```

### 必要なものだけimport

`cat.py`の中には，`Cat`クラス以外にも，`BlackCat`クラスが定義されているとします．
このとき，`BlackCat`クラスは使わないので，`import`しないようにしたいとします．
このようなときは，`from cat import Cat`のように書きます．


```python
from cat import Cat

tama = Cat("タマ")
tama.meow()
```

`from cat import Cat`と書くと，`cat.py`の中で定義されている`Cat`クラスだけを`import`します．
このように書いたときは，`cat.Cat`の代わりに`Cat`と書きます．

## パッケージ

複数のファイルをまとめて，一つのパッケージとして扱うこともできます．
`cat.py`の他に`dog.py`というファイルを作って，これらをまとめて`animal`パッケージとしてまとめたいとします．
そのときは，`animal`というフォルダを作り，その中に`cat.py`と`dog.py`を入れます．
`animal`をパッケージとしてPythonに認識させるには，`animal`フォルダの中に`__init__.py`というファイルを作る必要があります．
中身は空で大丈夫です．

```
animal
├── __init__.py
├── cat.py
└── dog.py
```

animalフォルダと同じ階層に，`app.py`というフォルダを作り，animalパッケージの中の`cat.py`と`dog.py`を使ってみます．

```
├── animal
│   ├── __init__.py
│   ├── cat.py
│   └── dog.py
└── app.py
```

```python
from animal import dog, cat

tama = cat.Cat("タマ")
tama.meow()

poti = dog.Dog("ポチ")
poti.woof()
```

`from animal import dog, cat`と書くと，`animal`パッケージの中の`dog.py`と`cat.py`を`import`します．

このように複数のファイルをまとめてパッケージとして扱うことで，より大きなプログラムを作ることができるようになります．

### モジュールを使った例

モジュールがどのように使われるのか想像がつかないと思うので，実際にモジュールを使った例を紹介します．
ここでは，DjangoというWebアプリケーションフレームワークで作られたWebアプリを例にします．
僕のサイト(https://crashrt.work)は，Djangoを使って作りました．

DjangoでWebアプリを作ると，このようなディレクトリ構造になることが多いです．
ここでは，トップページとプロジェクトを説明するページがある場合について考えてみます．

```
├── manage.py
├── top
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── projects
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Webサービス勉強会ではないので詳しくは見ませんが，
トップページとプロジェクトページでは全然役割が違う場合などは，このようにモジュールに分けておくと便利です．
各ページの中でも，

- `models.py`では，データベース関連の処理
- `views.py`では，ページの表示に必要な処理
- `urls.py`では，どのURLにアクセスしたときに行う処理を指定

などのように，役割ごとにファイルを分けておくと，プログラムが見やすくなります．



