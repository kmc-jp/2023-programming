# Section5 関数

## 1. 関数とは

### 関数定義
関数とは、特定の処理や計算を行うためのコードのまとまりを指します。Pythonにおける関数はdefキーワードを用いて定義されます。関数は、任意の数の引数を受け取り、結果を返すことができます。

以下に、関数の基本的な形式を示します：

```python
def function_name(argument1, argument2):
    # ここに処理を書く
    return result
```

ここで、function_nameは関数の名前で、argument1とargument2は関数が受け取る引数です。resultは関数の処理結果で、これがreturnによって呼び出し元に返されます。

### 関数の利点

1. コードの再利用： 同じ処理を何度も書く代わりに、一度関数として定義しておけば何度でも呼び出すことができます。これはコードの重複を防ぎ、保守性と可読性を向上させます。

2. モジュラリティ： 関数を使うと、コードを独立した部品に分割することができます。各関数は特定のタスクを遂行し、それぞれが独立してテストや修正が可能です。

3. 抽象化： 関数は特定の処理をカプセル化し、それを行う詳細からユーザーを遮断します。これにより、コードの抽象レベルが上がり、より複雑な処理を簡単に理解し、管理することができます。

4. エラーの特定と修正： コードを関数に分割すると、エラーが生じた際に問題を特定しやすくなります。それぞれの関数が特定のタスクを担当しているため、その関数内で問題が生じると予想されるエラーを特定しやすくなります。

5. コードの可読性： 適切に名前をつけられた関数を使用すると、その関数が何を行っているかをすぐに理解することができます。これにより、コード全体の流れが読みやすくなります。

6. スコープの制限： 関数内部で定義された変数は、その関数内部でのみ有効です。これにより、変数のスコープを制限し、不意の変数変更や名前の衝突を避けることができます。

## 2. 関数定義の基本

Pythonにおける関数は、defキーワードを使って定義されます。以下に、その基本的な形式を示します：

```python
def function_name(argument1, argument2):
    # ここに処理を書く
    return result
```

この例では、function_nameは関数の名前、argument1とargument2は関数が受け取る引数を示しています。# ここに処理を書くの部分で関数が実行する処理を記述します。resultは関数の処理結果で、これがreturnによって呼び出し元に返されます。returnは省略可能で、その場合、関数はNoneを返します。

関数を定義した後、その名前とともに括弧()を使って関数を呼び出します。引数がある場合、それらは括弧内に指定します。以下にその例を示します：

```python
# 関数の定義
def greeting(name):
    return f"Hello, {name}!"

# 関数の呼び出し
message = greeting("Alice")
print(message)  # 出力: Hello, Alice!

```

この例では、greetingという名前の関数を定義しています。引数としてnameを受け取り、挨拶文を返します。関数の呼び出しはgreeting("Alice")の形で行われ、その結果はmessage変数に代入されます。最後にprint関数を使って、その結果を表示しています。

## 3. 引数

### 引数の渡し方

パラメータは、関数の定義部分に記述される変数のことです。これは関数が受け取る「入力」を指定するための「プレースホルダー」のようなものです。
引数は基本的に、定義した関数のパラメータの順番に従って渡されます。たとえば、以下の関数addでは、最初の引数はxに、2番目の引数はyに対応します。

```python
def add(x, y):
    return x + y

print(add(3, 4))  # 出力: 7
```

### デフォルト引数

関数のパラメータにはデフォルトの値を設定することが可能で、これをデフォルト引数といいます。このデフォルト値は、関数呼び出し時に対応する引数が提供されない場合に使用されます。

```python
def greet(name='Guest'):
    print(f"Hello, {name}!")

greet("Alice")  # 出力: Hello, Alice!
greet()  # 出力: Hello, Guest!
```

### キーワード引数

関数を呼び出す際に、引数をパラメータ名と一緒に指定することができます。これをキーワード引数といいます。キーワード引数を使用すると、引数の順番を気にする必要がなくなり、コードの可読性も向上します。

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type='hamster', pet_name='Harry')  # キーワード引数を使用
```

## 4. 戻り値

### 戻り値の意味と使用方法

「戻り値」または「返り値」は、関数が呼び出し元に返す結果のことを指します。戻り値はreturnキーワードを使って指定します。

```python
def add(x, y):
    return x + y

result = add(3, 4)  # 関数の戻り値を変数に代入
print(result)  # 出力: 7
```

この例では、add関数は引数xとyの和を戻り値として返します。関数の戻り値は、関数呼び出しの結果として得られ、ここではそれをresultという変数に代入しています。

### 複数の戻り値

Pythonの関数は複数の値を一度に返すことができます。これはタプルを使って実現されます。

```python
def add_and_subtract(x, y):
    return x + y, x - y

result = add_and_subtract(5, 3)
print(result)  # 出力: (8, 2)
```

この例では、add_and_subtract関数は和と差の2つの結果を返しています。戻り値はタプルとして得られ、その結果をresultという変数に代入しています。

## 5. 変数のスコープ

### ローカル変数とグローバル変数

「ローカル変数」は、特定の関数内でのみ定義・利用される変数のことを指します。その一方、「グローバル変数」は、プログラム全体、すなわちどの関数からでもアクセス可能な変数を指します。

```python
x = 10  # グローバル変数
y = 4   # グローバル変数

def print_x():
    # print(x) をx = 5より前に書くとエラーになる
    x = 5  # ローカル変数
    print(x)  # 出力: 5
    print(y)  # 出力: 4

print_x()
print(x)  # 出力: 10
```

### globaキーワード

```python
x = 10  # グローバル変数

def change_x():
    global x  # グローバル変数 'x' を参照
    x = 5

change_x()
print(x)  # 出力: 5
```

### nonlocalキーワード

nonlocalキーワードは、ネストした関数（関数の中に定義された別の関数）の中で、外側の関数の変数を参照するために使用されます。

```python
def outer():
    x = "local"
    def inner():
        nonlocal x  # 1つ外側の関数 'outer' の変数 'x' を参照
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
```

このコードを実行すると、inner関数内でxの値が"nonlocal"に変更され、その変更がouter関数のスコープにも影響を与えるため、次の出力が得られます。

```python
inner: nonlocal
outer: nonlocal
```

## 6. ラムダ関数

### ラムダ関数の定義と利用方法

ラムダ関数は無名関数または匿名関数とも呼ばれ、名前を持たない小さな関数を定義するために使用されます。ラムダ関数はlambdaキーワードを使って定義されます。

```python
square = lambda x: x ** 2

print(square(5))  # 出力: 25
```

### ラムダ関数の利点・欠点

利点：
- ラムダ関数はコードを簡潔にするために使われます。特にmap()、filter()、sort()などの組み込み関数と一緒に使われることが多いです。
- ラムダ関数は、一時的な使用や短い関数を定義する場合に便利です。

限界：
- ラムダ関数は一行のコードに制限されているため、複雑な処理を行うことはできません。
- ラムダ関数は簡潔さを重視するため、コードの可読性を損なう可能性があります。特に複数のラムダ関数がネストされた場合などです。

## 7. 再帰関数

再帰関数とは、関数の中で自身を呼び出す関数のことを指します。再帰関数を使うと、ループを使わずに繰り返し処理を行うことができます。

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 出力: 120
```

この例では、factorial関数を定義しています。この関数は引数nに対する階乗を計算します。

## 8. 内部関数とクロージャ

内部関数（またはネストされた関数）は、関数の中に定義された関数です。これらの関数は、それを囲む関数内でのみ呼び出すことができます。

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function(5)

print(outer_function(10))  # 出力: 15
```

クロージャは、自身が定義されたスコープ内の変数へのアクセスを保持できる関数です。外部関数が終了した後でも、内部関数は外部関数の変数にアクセスすることができます。

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function  # inner_functionを戻り値として返す

closure = outer_function(10)
print(closure(5))  # 出力: 15
```

inner_functionではローカル変数yと外部の変数への参照xを持っており、それが関数オブジェクトとなります。
したがって、closureは同じ関数だったとしても外部の変数によって動作が変わります。
これを応用すれば、関数に記憶領域を持たせることができます。

```python

def outer_function(x):
    def getX():
        return x
    def setX(val):
        nonlocal x
        x = val
    return getX, setX

closure_getX, closure_setX = outer_function(10)

# getXとsetXによって変数xに対してアクセスできるようになった
```