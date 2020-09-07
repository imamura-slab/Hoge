### table of contents
- [継承](#user-content-継承inheritance)
- [多段階継承](#user-content-多段階継承)
- [多重継承](#user-content-多重継承)
- [継承とポインタ](#user-content-継承とポインタ)


***
***
# 継承(Inheritance)
- あるクラスを別のクラスに「継承」しその機能を受け継ぐ
- 継承するクラスを`基本クラス`または`基底クラス`と呼び, 基本(基底)クラスを継承したクラスを`派生クラス`という
```
class 派生クラス名 : [アクセス指定子] 基本(基底)クラス名 {
      member;
};
```

***
- 上記の継承時に用いるアクセス指定子は基底クラスの`publicなメンバ`をどのように継承するかを決定する. 指定しなかった場合は`private`になる.
  | 継承時のアクセス指定子 | 派生クラスからのアクセス | オブジェクトを用いた外部(例えばmain関数)からのアクセス |
  |:---:|:---:|:---:|
  |public     |可|  可|
  |protected  |可|不可|  
  |private    |可|不可|

- 被保護 : publicとprivateの中間的なアクセス指定子`protected`
  - protectedで指定されたメンバは被保護メンバと呼ばれ, これは派生クラスからもアクセスできる非公開メンバである.
    |アクセス指定子|派生クラスからのアクセス|外部からのアクセス|
    |:---:|:---:|:---:|
    |public   |可  |継承時のアクセス指定子次第|
    |protected|可  |不可|
    |private  |不可|不可|

```
こちらのアクセス指定子は
class Hoge{
public:
  ....
protected:
  ...
private:
  ....
};
ってときのお話
```



***
- 継承時のコンストラクタ
  - コンストラクタは, 基底クラス, 派生クラスの順番で実行される
  - 基底クラスのコンストラクタに引数を渡す場合は次のようにする
  ```
  派生クラス名(arg-list) : 基底クラス名(arg-list){
    処理...
  }
  ```

- 継承時のデストラクタ
  - 派生クラスのオブジェクトが破棄されると, デストラクタはコンストラクタとは逆順である, 派生クラス, 基底クラスの順に実行される



***
- 継承を使用し, さらに基底クラスでコンストラクタ初期化を行った例を示す (ついでにデフォルト引数も使ってみてます)


- inheritance1.cpp](./src/inheritance1.cpp)
  - 基底クラス : Pokemon
    - メソッド : print_data()
  - 派生クラス : Pikachu, Togepi
    - メソッド : cry()

```cpp
#include <iostream>
#include <string>     // 文字列比較用(compare())
using namespace std;

class Pokemon{                              // 今回, 基底クラスとして扱う
public:
  const char *name;
  int lebel;
  const char *type1, *type2;

  Pokemon(const char *name="Pikachu",      // 基底クラスコンストラクタ {
	  const char *type1="Electric",    //
	  const char *type2="",		   //
	  int lebel=1){			   //
    this->name  = name;			   //
    this->lebel = lebel;		   //
    this->type1 = type1;		   //
    this->type2 = type2;		   //
  }					   // 基底クラスコンストラクタ }
  
  void print_data(){
    cout << "\n";
    cout << "name  : " << name  << "\n";
    cout << "lebel : " << lebel << "\n";
    cout << "type1 : " << type1 << "\n";
    cout << "type2 : " << type2 << "\n";
  }
};


class Pikachu : public Pokemon{                               // Pokemonクラスを継承
public:
  Pikachu(const char *name="Pikachu",                         // 派生クラスコンストラクタ {
	  const char *type1="Electric",			      // 
	  const char *type2="",				      // 
	  int lebel=1) : Pokemon(name, type1, type2, lebel){} // 派生クラスコンストラクタ }

  void cry(){
    cout << "\nピカー！\n";
  }
};


class Togepi : public Pokemon{
public:
  Togepi(const char *name="Pikachu",                          // 派生クラスコンストラクタ {
	 const char *type1="Electric",			      // 
	 const char *type2="",				      // 
	 int lebel=1) : Pokemon(name, type1, type2, lebel){}  // 派生クラスコンストラクタ }

  void cry(){
    cout << "\nチョッゲプリィイイイイイイ！！\n";
  }
};

  
int main(){
  Pikachu p_obj;                    // 派生クラスでインスタンス化
  Togepi  t_obj("Togepi", "Fairy"); // 派生クラスでインスタンス化
  
  p_obj.print_data();               // 基底クラスのメソッド使えるよ
  p_obj.cry();                      // もちろん派生クラスのメソッドも使えるよ

  t_obj.print_data();
  t_obj.cry();
  
  return 0;
}


>>> name  : Pikachu
>>> lebel : 1
>>> type1 : Electric
>>> type2 : 
>>> 
>>> ピカー！
>>> 
>>> name  : Togepi
>>> lebel : 1
>>> type1 : Fairy
>>> type2 : 
>>> 
>>> チョッゲプリィイイイイイイ！！
```



***
# 多段階継承
- "ある基底クラスから派生したクラス"を基底クラスとして派生クラスを生成すること
- 派生クラスの基底クラスが継承している基底クラスを`間接基底クラス`という
```
	間接基底クラス
	      |
	  基底クラス
	      |
	  派生クラス
```
- コンストラクタは 間接基底クラス -> 基底クラス -> 派生クラス の順に実行される
- デストラクタは 派生クラス -> 基底クラス -> 間接基底クラス の順に実行される(コンストラクタの逆順)



***
# 多重継承
- 派生クラスが複数の基底クラスを継承すること
```
	基底クラス1  基底クラス2
	       \    /
	      派生クラス
```
- 多重継承を行うときは次のように記述する
```
class 派生クラス名 : [アクセス指定子] 基底クラス名1, [アクセス指定子] 基底クラス名2,...{
      .....
};
```

- コンストラクタは左の基底クラスから順に実行され, 最後に派生クラスのコンストラクタが実行される
- デストラクタは最初に派生クラスが実行され, その後右の基底クラスから順に実行される



## 多重継承の問題点
- 同じクラスを複数回継承してしまうことがある
```
	      基底クラス1
	        |     |
	派生クラス1 派生クラス2
	        |     |
	      派生クラス3
```
- 次のプログラム例は基底クラス(Base)を2度継承しており, obj.nameが曖昧になる. そのためコンパイルが通らない.
- [inheritance2.cpp](./src/inheritance2.cpp)
```cpp
#include <iostream>
using namespace std;

class Base{
public:
  const char* name;
};

class Derived1 : public Base{
public:
  int age;
};

class Derived2 : public Base{
public:
  const char* sex;
};

class Derived3 : public Derived1, public Derived2{
public:
  void print(){
    cout << "name: " << name << endl;
    cout << " age: " << age  << endl;
    cout << " sex: " << sex  << endl;
  }
};


int main(){
  Derived3 obj;

  obj.name = "野原しんのすけ";
  obj.age  = 5;
  obj.sex  = "male";
  obj.print();

  return 0;
}

>>> コンパイルエラー
```

- **仮想基底クラス** を用いることで上記の問題を解決できる
- やりかたはとても簡単.  継承時に`virtual`を付けるだけ!!
  - `virtual アクセス指定子 基底クラス名` の順でも良いし,
    `アクセス指定子 virtual 基底クラス名` の順でも良い
- [inheritance3.cpp](./src/inheritance3.cpp)
```cpp
#include <iostream>
using namespace std;

class Base{
public:
  const char* name;
};

class Derived1 : virtual public Base{   // 変更点: virtual追加
public:
  int age;
};

class Derived2 : virtual public Base{   // 変更点: virtual追加
public:
  const char* sex;
};

class Derived3 : public Derived1, public Derived2{
public:
  void print(){
    cout << "name: " << name << endl;
    cout << " age: " << age  << endl;
    cout << " sex: " << sex  << endl;
  }
};


int main(){
  Derived3 obj;

  obj.name = "野原しんのすけ";
  obj.age  = 5;
  obj.sex  = "male";
  obj.print();

  return 0;
}


>>> name: 野原しんのすけ
>>>  age: 5
>>>  sex: male
```



***
# 継承とポインタ
- クラス型のポインタ変数には`派生クラスのアドレスを代入`できる
```
Derived_class derived_obj;
Base_class *base_obj = &derived_obj;
```
- ただし, 基底クラスのポインタは基底クラスの情報しか持たない
  - たとえ, 派生クラスのオブジェクトを指していても派生クラスのメンバは呼び出せない
- [inheritance4.cpp](./src/inheritance4.cpp)
  - base_obj->age しようとするとコンパイルエラー
  
```cpp
#include <iostream>
using namespace std;

class Base{
public:
  const char* name;
};

class Derived : public Base{
public:
  int age;
};


int main(){
  Derived derived_obj;
  Base *base_obj = &derived_obj;                        // 派生クラスのアドレスを代入
  
  derived_obj.name = "野原しんのすけ";
  derived_obj.age  = 5;


  cout << "derived name : " << derived_obj.name << endl;
  cout << "derived age  : " << derived_obj.age  << endl;
  cout << "base    name : " << base_obj->name   << endl;
  //cout << "base    age  : " << base_obj->age    << endl;   // コンパイルエラー
  
  return 0;
}


>>> derived name : 野原しんのすけ
>>> derived age  : 5
>>> base    name : 野原しんのすけ
```


- この機能により, 同名のメンバを持つクラス間で面白い現象が発生する
  - 基底クラスと派生クラスでメンバ名が衝突している場合, クラスを明示しなかったときは常に自分のクラスのメンバを優先する
  - しかし, ポインタが指すオブジェクトは基底クラスの情報しかないので, 基底クラスのメンバを呼び出すという現象が発生する
- [inheritance5.cpp](./src/inheritance5.cpp)

```cpp
#include <iostream>
using namespace std;

class Base{
public:
  void print(){
    cout << "Base だよ" << endl;
  }
};

class Derived : public Base{
public:
  void print(){
    cout << "Derived だよ" << endl;
  }
};


int main(){
  Derived derived_obj;
  Base *base_obj = &derived_obj;                        // 派生クラスのアドレスを代入
  
  derived_obj.print();
  base_obj->print();    // 派生クラスのアドレスを与えたけど 基底クラスの方が実行されるよ
  
  return 0;
}


>>> Derived だよ
>>> Base だよ
```

- これを, より発展させると動的なポリモーフィズムが実現できる
  - ポリモーフィズム(多態性・多様性) : 同じ名前のメソッドを複数のクラスで使用できるようにし, そのメソッドを通して暗黙的に複数のインスタンスの動作を切り替えることをできるようにすること
  - -> [関数のオーバーライド](./../override)


