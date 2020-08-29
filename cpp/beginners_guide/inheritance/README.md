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
- [inheritance1.cpp](./src/inheritance1.cpp)
  - 基底クラス : Pokemon
    - メソッド : print_data()
  - 派生クラス : Pikachu, Togepi
    - メソッド : cry()
```
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


# 多重継承
- 派生クラスが複数の基底クラスを継承すること
```
	基底クラス1  基底クラス2
	       \        /
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


