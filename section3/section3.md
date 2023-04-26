## 1. はじめに

### 1.1. 自己紹介

こんにちは！この資料では、Pythonプログラミング言語の初心者向けの解説を行います。私はKMC3回生、情報学科3回生の進捗ゼミです。

- 普段は自宅ネットワーク/サーバーをいじっています。
- 最近部室にサーバーラックを置こうとしている張本人です。
- プロトコル開発やデスクトップソフトウェアを開発していたりもします。
- おすすめチャンネル`#infra`,`#linux`,`#sysop`,`#ハーフラック勉強会`

### 1.2. 今日の目標

今日の目標は、前回学んだ型，演算子，変数の概念を用いて便利な**データ構造**と呼ばれるものを知ることです。
- リスト
    - [1,2,3,4,5,･･･]ってどう表現するの
- タプル
    - (x,y)ってどう表現するの
- 辞書
    - (名前:segre,代:45代)ってどう表現するの

### 1.3. 前回の復習
ここで前回の復習をします。

## 2. リスト
## 2.1. リスト
リストは、複数の値を格納できるデータ構造です。リストは角かっこ（[ ]）でくくり、各要素はカンマで区切って記述します。リスト内には任意のデータ型の値を格納できます。
例えば、次のように記述することで、数値や文字列を含むリストを作成することができます。
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange", "kiwi"]
mixed_list = [1, "apple", 2.5, True]
```

リストに格納された値には、要素のインデックスを使ってアクセスできます。Pythonでは、リストの最初の要素のインデックスは0から始まります。
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])    # 1
print(numbers[3])    # 4
print(numbers[-1])   # 5
print(numbers[0:2])  # [1,2]
print(numbers[2:-1]) # [3,4]
print(numbers[3:])   # [4,5]
```

## 2.2. リストの操作
また、リストに対して様々な操作が可能です。以下は、代表的な操作の例です。
```python
# リストの要素の数を取得する
print(len(numbers))  # 5

# リストの結合をする
mixed = numbers + fruits
print(mixed)  # [1, 2, 3, 4, 5, 'apple', 'banana', 'orange', 'kiwi']

# 値を代入する
numbers[0] = 0
print(numbers) # [0, 2, 3, 4, 5]

# リストに要素を追加する
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# リストから要素を削除する
numbers.remove(3)
print(numbers)  # [1, 2, 4, 5, 6]

# リストの要素を逆順にする
numbers.reverse()
print(numbers)  # [6, 5, 4, 2, 1]
```

### 2.3. 練習
1. リストの作成

    以下の仕様を満たすリストを作成し、要素を出力してください。
    
    仕様:
    要素数は4つ  
    要素には、任意の文字列または整数を使用する

    例:
    ```python
    [1, 'apple', 'banana', 3.5]
    ```

1. リストの要素の更新

    以下のリストを定義し、2番目の要素を'orange'に更新してください。
    ```python
    ['apple', 'banana', 'kiwi', 'grape']
    ```

    更新後:
    ```python
    ['apple', 'orange', 'kiwi', 'grape']
    ```

1. リストのスライス

    以下のリストを定義し、2つの要素（'kiwi'と'grape'）をスライスして取得してください。

    ```python
    ['apple', 'banana', 'kiwi', 'grape', 'orange']
    ```

    出力:
    ```python
    ['kiwi', 'grape']
    ```

## 3. タプル
## 3.1. タプル
タプルは、リストと同じように複数の値を格納できるデータ構造ですが、リストと異なり、一度作成したら変更できない不変のオブジェクトです。タプルは丸かっこ( )でくくり、各要素はカンマで区切って記述します。
```python
fruits = ("apple", "banana", "orange", "kiwi")
mixed_tuple = (1, "apple", 2.5, True)
```

タプルに格納された値には、リストと同じように要素のインデックスを使ってアクセスできます。
```python
fruits = ("apple", "banana", "orange", "kiwi")
print(fruits[0])  # "apple"
print(fruits[3])  # "kiwi"
```

以下に、タプルに対して可能な操作をいくつか示します。
```python
# タプルの要素の数を取得する
print(len(fruits))  # 4

# タプルの要素をカウントする
print(mixed_tuple.count(2.5))  # 1

# タプル内の要素のインデックスを取得する
print(mixed_tuple.index("apple"))  # 1
```

## 3.2. 練習

1. タプルの作成
    以下の仕様を満たすタプルを作成し、要素を出力してください。

    仕様:

    要素数は5つ
    要素には、任意の文字列または整数を使用する  

    例:
    ```python
    (1, 'apple', 'banana', 3.5, 'orange')
    ```

1. タプルの要素のアクセス
    以下のタプルを定義し、2つ目の要素と4つ目の要素を取得して、それぞれ出力してください。

    タプル: (1, 'apple', 'banana', 3.5, 'orange')

    出力:
    ```python
    'apple'
    3.5
    ```

# 4. 辞書
## 4.1 辞書
辞書は、キーと値のペアを格納できるデータ構造です。辞書は波かっこ（{ }）でくくり、各キーと値はコロン（:）で区切って記述します。各ペアはカンマで区切って記述します。
```python
person = {"name": "John", "age": 30}
```

辞書に格納された値には、キーを使ってアクセスできます。
```python
person = {"name": "John", "age": 30}
print(person["name"])  # "John"
print(person["age"])  # 30
```

また、辞書に対して様々な操作が可能です。以下は、代表的な操作の例です。
```python
# 辞書に新しいキーと値のペアを追加する
person["country"] = "USA"
print(person)  # {"name": "John", "age": 30, "country": "USA"}

# 辞書からキーと値のペアを削除する
person.pop("age")
print(person)  # {"name": "John", "country": "USA"}

# 辞書のキーをリストとして取得する
print(list(person.keys()))  # ["name", "country"]

# 辞書の値をリストとして取得する
print(list(person.values()))  # ["John", "USA"]
```

## 4.2 練習
1. 辞書の作成
    以下の仕様を満たす辞書を作成し、要素を出力してください。

    仕様:

    キーには、'apple', 'banana', 'kiwi'の3つの文字列を使用する
    値には、それぞれの果物の価格を任意の数値で設定する
    例:
    ```python
    {'apple': 100, 'banana': 80, 'kiwi': 120}
    ```

2. 辞書の要素のアクセス
    以下の辞書を定義し、'banana'の価格を取得して、出力してください。

    ```python
    {'apple': 100, 'banana': 80, 'kiwi': 120}
    ```

    出力:
    ```python
    80
    ```

# 5. まとめ
Pythonには、リスト、タプル、辞書という3つの重要なデータ型があります。
```python
numbers = [1, 2, 3, 4, 5]
fruits = ("apple", "banana", "orange", "kiwi")
person = {"name": "John", "age": 30}
```