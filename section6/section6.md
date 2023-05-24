# Section6 クラス

## 1. クラスとは

### クラスの定義
クラスそのものの説明の前に、定義の方法について説明します。
以下にクラスの定義の方法を示します。

```python
class ClassName:
    pass
```
`class_name` はクラスの名前、 `pass` の部分に実装内容を記述します。
実装内容は一つインデントします(関数と同じ)。
クラス名は単語の先頭を大文字にするのが一般的です。

クラスの利用方法
```python
x = ClassName()
```
と書くと変数xにClassNamenのインスタンスが代入されます。

製品作成で例えば場合
```
クラス : どのようなものかを定義した設計書  
インスタンス化 : 設計書から製品を作成すること  
インスタンス : 製品
```
となります。クラスを利用するためには必ずインスタンス化が必要になります。

### メソッド
クラス内の関数をメソッドと呼びます。
メソッドの宣言は、クラス外と同じようにdefを使用して宣言します。

クラス外で宣言した場合と異なる点は、メソッドは必ず１つ以上の引数を持つことです。

実装例
```python
class SampleClass1 :
    def method1(self):
        print("Hello World!")
instance = SampleClass1()     # インスタンス化
instance.method1()            # メソッドの呼び出し
```
メソッドを定義する際には、 `self` という引数を指定します。この `self` というのは、インスタンス自身を表す引数で、必ず１番初めの引数として記述します。

実装例2
```python
class TestClass:
    x = "変数1"

    def test_method1(self):
        print(self.x)

    def test_method2(self, arg1):
        print("引数1:" + arg1)

testClass = TestClass()
testClass.test_method1() # ⇒ 変数1
testClass.test_method2("引数Test") # ⇒ 引数1:引数Test
```

### コンストラクタ
コンストラクタは、インスタンスを生成したときに一度だけ呼び出されるメソッドです。
基本的には対象のクラスのインスタンスを初期化するために利用します。

コンストラクタを定義するには、「init」という特殊な名前でメソッドを定義する必要があります。
するとインスタンス作成時にこのメソッドが呼び出されます。

```python
class SampleClass:
    def __init__(self):
        self.aaa = 2020
        self.bbb = "Hello World"

ins = SampleClass()
print(ins.aaa)
print(ins.bbb)
```

コンストラクタに引数を渡すこともできます。
```python
class TestClass3:
    val = []
    def __init__(self, val1, val2):
        # 初期化
        self.val.append(val1)
        self.val.append(val2)
        print("init:" + str(self.val))

testClass3 = TestClass3(1, 2)
```

### デストラクタ
Pythonのクラスには、オブジェクトが破棄される際に自動的に実行される特殊メソッドであるデストラクタ（Destructor）があります。デストラクタは、オブジェクトが不要になったときにリソースの解放や後処理を行うために使用されます。例えば、ファイルやデータベースの接続をクローズしたり、メモリの解放を行ったりする場合に便利です。

```python
class SampleClass():
    # コンストラクタ
    def __init__(self):
        self.aaa = 2020
        self.bbb = "Hello World"
    # デストラクタ
    def __del__(self):
        print("さようなら")
ins = SampleClass()
print(ins.aaa)
print(ins.bbb)
del ins # インスタンスの破棄
```

### 変数
pythonのクラス内に定義できる変数について説明します。
pythonのクラスで定義できる変数には、２種類あります。
１つは、クラス変数で、もう１つはインスタンス変数です。

クラス変数は、クラス内で定義する変数のことで、全てのインスタンスで共通となる変数です。
クラスの定義文直下に記述することで、クラス変数になります。
```python
class SampleClass:
    a = 'Hello World!'    # クラス変数
    def s_method1(self):
        print(self.a)

ins1 = SampleClass()      # インスタンス１
ins1.s_method2()
ins2 = SampleClass()      # インスタンス２
ins2.s_method2()
```

インスタンス変数は、クラス変数と異なりインスタンスに依存する変数です。つまり、インスタンスごとに異なる値になる変数です。
インスタンス変数は、メソッドの直下で "self" の属性として定義します。
```python
class SampleClass():
    def __init__(self,aaa):
        self.aaa = aaa           # 引数aaaの値をインスタンス変数の初期値とする

ins1 = SampleClass("Hello!")     # 引数aaaに「Hello!」を渡す
print(ins1.aaa)
ins2 = SampleClass("Good Bye!")  # 引数aaaに「Good Bye!」を渡す
print(ins2.aaa)
```

#### 練習問題
クラス変数とインスタンス変数が同じ変数名だった場合はどうなるでしょうか

クラスExample内に同名のクラス変数valとインスタンス変数valを定義し、そのクラスのインスタンスから変数valを `print` を用いて呼び出してください。

### 継承
継承とは、他のクラスと同じインスタンス変数、メソッドをもつクラスを定義できる機能です。
この機能により似た機能を持ったクラスをより効率的に作成することができます。
継承を行うには、クラス定義のときにクラス名の後ろに「(継承するクラス名)」とつけて定義することでできます。

```python
class Parent:
    parent_val = "Parent"

    def parent_function(self):
        print("ParentMethod:" + self.parent_val)

class Child(Parent):
    child_val = "Child"

    def child_function(self):
        print("ChildMethod:" + self.child_val)

child = Child()
print(child.parent_val) # ⇒ Parent
print(child.child_val) # ⇒ Child
child.parent_function() # ⇒ ParentMethod:Parent
child.child_function() # ⇒ ChildMethod:Child
```

同じ名前のメソッドが定義されていた場合はどうなるでしょうか
```python
class Parent:
    val = "Parent"

    def all_function(self):
        print("ParentMethod:" + self.val)

class Child(Parent):
    val = "Child"

    def all_function(self):
        print("ChildMethod:" + self.val)

parent = Parent()
print(parent.val) # ⇒ Parent
parent.all_function() # ⇒ ParentMethod:Parent
child = Child()
print(child.val) # ⇒ Child
child.all_function() # ⇒ ChildMethod:Child
```
このように継承元と継承先に同じ名前の変数、メソッドが定義されている場合、作成したインスタンスのクラスの内容が優先されます。

#### 練習問題
では、継承元と継承先のクラス内でそれぞれコンストラクタが定義されていた場合はどちらが優先されるでしょうか

継承元のクラスParentと継承先のクラスChild内にそれぞれコンストラクタを定義し、コンストラクタ内で `print` 関数を呼び出し、別の文字を出力するようにしてください。
その後外からクラスChildのインスタンスを作成してみましょう。

# 2. オブジェクト指向プログラミング

## 2.1. クラスの定義とインスタンス化
クラスはオブジェクトの設計図やテンプレートのようなものであり、共通の属性と振る舞いを持つオブジェクトを作成するためのものです。以下は、クラスの定義とそのクラスからインスタンスを作成する例です。

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine started.")

# Carクラスからインスタンスを作成
my_car = Car("Toyota", "Camry", 2021)
```

上記の例では、"Car"という名前のクラスを定義しています。クラスは__init__メソッド（コンストラクタ）とstart_engineメソッドを持っています。__init__メソッドは、新しいCarオブジェクトが作成される際に呼び出され、属性を初期化します。`start_engine` メソッドは、Carオブジェクトがエンジンを始動させるためのメソッドです。

## 2.2. インスタンスの属性とメソッドのアクセス
インスタンスは、クラスから作成されたオブジェクトであり、属性やメソッドにアクセスすることができます。以下の例では、インスタンスの属性にアクセスし、メソッドを呼び出しています。

```python
print(my_car.make)  # 属性へのアクセス
my_car.start_engine()  # メソッドの呼び出し
```

上記のコードでは、my_carインスタンスのmake属性にアクセスし、start_engineメソッドを呼び出しています。

## 2.3. 継承とポリモーフィズム
継承は、既存のクラスを拡張し、新しいクラスを作成するための機能です。以下は、継承とポリモーフィズムの例です。

```python
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    
    def start_engine(self):
        print("Engine not applicable for electric cars.")

my_electric_car = ElectricCar("Tesla", "Model S", 2022, "100 kWh")
my_electric_car.start_engine()
```

上記の例では、ElectricCarクラスがCarクラスを継承しています。ElectricCarクラスはstart_engineメソッドをオーバーライドして、電気自動車の場合に適切なメッセージを表示するようにしています。
継承先のクラス内で `super()` を用いることで継承元のメソッドを呼び出すことができます。

## 2.4. カプセル化とアクセス制御
カプセル化は、データや振る舞いを隠蔽し、外部からのアクセスを制限するための仕組みです。Pythonでは、アンダースコア _ を使って属性やメソッドを非公開にすることが一般的です。

```python
class Person:
    def __init__(self, name, age):
        self._name = name  # 非公開属性
        self._age = age  # 非公開属性
    
    def get_name(self):
        return self._name
    
    def _internal_method(self):
        # 非公開メソッド
        pass

person = Person("Alice", 25)
print(person.get_name())
```
上記の例では、Personクラスの_nameと_age属性を非公開にし、get_nameメソッドを介して名前を取得します。また、_internal_methodメソッドは内部で使用される非公開メソッドです。

以上が、Pythonのオブジェクト指向プログラミングの基本的な概念と使い方の説明です。オブジェクト指向プログラミングは、プログラムをよりモジュール化し、再利用性や保守性を高めるための重要なアプローチです。


