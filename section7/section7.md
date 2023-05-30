# Section7 モジュール

今までの回で，Pythonの基本的な文法やデータ型，制御構文，関数，クラスについて説明しました．
今回はそれらを用いてプログラムを作成する上で役に立つ情報について説明していきます．
具体的にはモジュール，外部ライブラリ，ファイル入出力，そしてより良いコードを書くためのコツについて説明します．

## モジュール・import

### import 文の基本

モジュールは，Pythonのコードを複数のファイルに分けて作り，それらを使おうとするときに使う機能です．
今までは一つのファイルにコードを書いてきました．
しかし，作るものが大きくなってくると，数百，数千行のコードを書くことになるので，
一つのファイルにコードを書くのは大変です．
そこで，コードを複数のファイルに分けて書くことで，コードの管理をしやすくします．

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



