# Section1  環境構築

## 自己紹介
crashRT
- KMC3回生（45代）
- 京大情報学科3回生（計算機）
- 3DCGとか映像制作とかwebアプリとか
  - 紅萠祭のビラ作った人

<img src="https://www.kmc.gr.jp/guidance/2023/image/bira-1.jpg" width="480px"> <img src="https://www.kmc.gr.jp/guidance/2023/image/bira-3.jpg" width="480px">
- Slackだと#2023-crashrt-memoとか#crashrt-memoとかに生息
- 最近車で出かけるのに少しハマっている
- サイト：<https://crashrt.work>

スプレッドシートのリンクをSlackに貼ります．自己紹介・進捗確認用です．気軽に書き込んで下さい．


## 今日の目標

- 今後の準備
- python を自分のPC上で動かせるようにすること

## プログラミングって何？Pythonとは？？

### プログラミングって何がしたいの？

- コンピュータになんかするよう命令したい
  - この命令はあいまいであってはいけない．コンピュータに誤解されたら困るので

料理のレシピを例に考えてみましょう．
例えば，以下のような文がレシピの中にあったとします．

> パスタに粉チーズを少々かける．

さて，「少々」とはどれくらいか？
人によって違うはず．

<details>
<summary>こんな感じでチーズをかける人がいるかもしれない</summary>

[![Image from Gyazo](https://i.gyazo.com/d111a68eb7e7f3bf9859ddf4000ad99c.jpg)](https://gyazo.com/d111a68eb7e7f3bf9859ddf4000ad99c)

</details>

この場合，具体的な量を書けばあいまいさがなくなり，みんな同じことをするようになるはず．
例えば，こんな感じにするといいでしょう．
> パスタに粉チーズを1gかける．

ちろんこの例はちょっと極端で，料理が得意な人ならいい感じの量に調整してくれると思います．
でも，コンピューターは「いい感じにやっとく」みたいなことはしてくれないので，細かく指示を出す必要があります．
プログラムを書くときはコンピューターにしてほしいことを明確にして，それを細かく書くことを意識すると良いかもしれません．

### プログラミング言語って何？

- プログラムを記述するための言語

コンピューターへの命令を記述するときは，プログラミング言語を使います．
例えば，CやC#, Java，Python, Ruby, Rust, OCamlなどがあります．

実際にはコンピューターはプログラミング言語そのものを理解しているわけではなくて，
コンパイラやインタプリタなどがコンピューターが理解できる形式に変換してくれている，
という話もあったりしますが細かいので今回は置いておきます．


### Python って何？

このプログラミング入門では，Pythonというプログラミング言語を使っていきます．
雑に特徴を挙げると，

良い点：
- 簡潔で，読みやすく書きやすい
- 書かないと行けないコードの量が少ない ※コード：プログラミング言語で書かれた命令
- 人気がある

悪い点：
- 速度が遅い
- 実行前に検査が行われないので，実行時にエラーが出ることがある
  - 実行する前に検査して，事前に良くない部分を教えてくれる言語もある（JavaとかRustとか）
  - Pythonはとりあえず実行してみて，無理になったらなんかだめだった～って言ってくる


そんなPythonについて，これから見ていきます．

## 環境構築
自分のパソコンでプログラミングしてPythonを動かすには準備が必要です．

### Python
Windows の場合
- Microsoft Store で python3.10 を検索，インストール

Mac の場合
- 公式インストーラーをダウンロードする．
  - <https://www.python.org/downloads/macos/> へアクセスし，
    Stable Releases の下にあるPython 3.10.10 のすぐ下 "Download MacOS 64-bit universal2 installer" をクリック
  - ダウンロードしたインストーラーを実行し，インストール
    - 多分色々出ると思いますが，許可・続けるで進めて大丈夫です．心配だったら画面のスクショをSlackに貼ってください．
    - 設定はデフォルトのままで大丈夫なはず


確認
- Power Shell（Windows）またはターミナル（Mac）を開く
- `python3 -V` と入力して，バージョンが表示されればOK\
  こんな感じ↓
  数字は3から始まっていればOKです
```
$ python3 -V
Python 3.10.8
```

### VSCode
- <https://code.visualstudio.com/> にアクセス，ダウンロード・インストール
  - 実行等は許可して大丈夫；設定はデフォルトのままでOK
- VSCode を起動
- 左のアイコンからExtensions(4つの四角のアイコン)を選択
- Python を検索し，インストール
  - Python のプログラミングを補助してくれるやつが入ります

[![Image from Gyazo](https://i.gyazo.com/f9b545ac64727ad9a8e68285349e2b68.png)](https://gyazo.com/f9b545ac64727ad9a8e68285349e2b68)


## はじめてのプログラミング
準備が整ったので，詳しいことは置いといてとりあえずプログラミングしてみます．
何やってるかはそのうち分かるので，なんか動いてる～！ってなれば今回はOK．

### Hello World!
まずは，定番のHello World!をやってみましょう．
やることは，`Hello, World!` と表示させるだけ．

- VSCode を起動
- ツールバーから，File > Open Folder
- 自由にフォルダーを選択
  - 例えば，ドキュメントに「2023-programming」という新規フォルダを作成してそれを選択
- 下の画像の，「フォルダ作成」のところをクリックして，`section1`などのフォルダを作成
- `section1` フォルダを選択した状態で，「ファイル作成」をクリック
  → `hello_world.py` という名前のファイルを作成

[![Image from Gyazo](https://i.gyazo.com/bd2191719fa6881a51419be9ba1b13e9.png)](https://gyazo.com/bd2191719fa6881a51419be9ba1b13e9)

- `hello_world.py`に以下の1行を書き込みます
```python
print('Hello, World!')
```

- 右上の実行ボタンをクリック
[![Image from Gyazo](https://i.gyazo.com/be1575f751db6c2dab3317fbab9e2eb2.png)](https://gyazo.com/be1575f751db6c2dab3317fbab9e2eb2)

- ウィンドウの下の方にパネルが増えて，そこに `Hello, World!` と表示されたら成功！
プログラミングできましたね！
```
Hello, World!
```

※ もし表示されなかったら教えて下さい．なにかがうまく動いていないので．


### Fizz Buzz
Fizz Buzz では，
1から100までの数字を表示するが，3の倍数のときはFizz，5の倍数のときはBuzz，3と5の倍数のときはFizz Buzzと代わりに表示します．

- `section1` フォルダを選択した状態で，「ファイル作成」をクリック
  → `fizz_buzz.py` という名前のファイルを作成

- `fizz_buzz.py`に以下のように書き込む
```python
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

- 右上の実行ボタンをクリック

<details>
<summary>実行結果</summary>

```
FizzBuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
```
</details>

## 今日のまとめ

- プログラミングが何なのか少しわかった気持ちになった
- PythonとVSCodeをインストールした
- VSCodeでコードを書いて実行した


## 参考文献
- Lubanovic, B. (2015). 入門Python3. オライリー・ジャパン.
- コーリー・アルソフ (2018). 独学プログラマー Python言語の基本から仕事のやり方まで (1st ed.). 日経BP社.
- 京大工学部専門科目 プログラミング入門 (2021) 授業資料
- 京大工学部専門科目 アルゴリズムとデータ構造 (2021) 授業資料