# 関数のオーバーライド

- オーバーライド : `仮想関数`による動的なポリモーフィズム
- オーバーロードはコンパイル時の静的なポリモーフィズムだが, オーバーライドは実行時に決定される動的で強力なポリモーフィズム
- 仮想関数を含むクラスをポリモーフィッククラスと呼ぶ


## 仮想関数
- 仮想関数 : 一般に基底クラスは汎用的な情報しか含まず, その機能を拡張させていく形で派生クラスを作っていく. そのとき基底クラスのメンバ関数を`再定義`することができる. そのような関数のこと.
- 基底クラスで virtual宣言 することで再定義可能であることを明示する. (多段階継承でも一番上の基底クラスだけ)
  - 通常のメンバ関数宣言に`virtual`を付けるだけ
  - 呼び出しは通常のメンバ関数と全く同じ
```
virtual member-function-declarator
```

- [override1.cpp](./src/override1.cpp)
  - 必ず再定義しなければならないというわけではない(Fooのように). その場合は最後に再定義したクラスのメンバ関数が参照される. 
```cpp
#include <iostream>
using namespace std;

class Hoge{
public:
  virtual void print(){        // virtual
    cout << "hoge" << endl;
  }
};

class Fuga : public Hoge{
public:
  void print(){                // 再定義
    cout << "fuga" << endl;
  }
};

class Piyo : public Fuga{
public:
  void print(){                // 再定義
    cout << "piyo" << endl;
  }
};

class Foo : public Piyo{       // 再定義していない
};


int main(){
  Hoge hoge_obj;
  Fuga fuga_obj;
  Piyo piyo_obj;
  Foo  foo_obj;

  Hoge *hoge_po=&hoge_obj, *fuga_po=&fuga_obj, *piyo_po=&piyo_obj, *foo_po=&foo_obj;

  hoge_po->print();
  fuga_po->print();
  piyo_po->print();
  foo_po->print();

  return 0;
}


>>> hoge
>>> fuga
>>> piyo
>>> piyo


// virtual を付けなかったとき
>>> hoge
>>> hoge
>>> hoge
>>> hoge
```

<details>
<summary>補足</summary>

- 通常の関数やフレンド関数, メンバ関数などはコンパイル時にアドレスが判明する. これらはコンパイル時点でそれぞれの関数を呼ぶアドレス情報が確定されるため, 関数の呼び出しにかかるオーバーヘッドが少なく, 効率が良い. このようにコンパイル時点で確定している情報を`コンパイル時バインディング`と呼ぶ. 
  - 高速に動作するが柔軟性に欠ける
- オーバーライドのような, オブジェクト指向において, 実行時に決定される情報を`実行時バインディング`と呼ぶ.
  - オーバーヘッドが大きくなるが非常に高い柔軟性がある
</details>




## 仮想関数とデストラクタ
仮想関数のデストラクタには注意！
- デストラクタは派生クラスから基底クラスへ向かって順番に呼び出される. デストラクタが仮想関数を呼び出したとき派生クラスの情報はすでに崩壊している可能性がある. 
- そのため, C++のデストラクタはオーバーライドを行わない. デストラクタで仮想関数を呼び出しても実体関数にアクセスせずに, デストラクタが発生しているクラスの仮想関数を呼び出す.
- [override2.cpp](./src/override2.cpp)
  - 仮想関数 : func()
  - 基底クラス : Hanzawa, 派生クラス : Naoki
  - 派生クラスのインスタンスobjが破壊されると ~Hanzawa() が呼び出され, その中で仮想関数`func()`が呼び出される.
    - 派生クラスのインスタンスが, デストラクタを呼び出しているため, 派生クラスのfunc()が呼び出されることを期待するがそうはならない. 基底クラスのfunc()が呼び出される.
```cpp
#include <iostream>
using namespace std;

class Hanzawa{
public:
  virtual void func(){
    cout << "倍返しだ" << endl;
  }
  ~Hanzawa(){
    this->func();
  }
};

class Naoki : public Hanzawa{
public:
  void func(){
    cout << "100倍返しだ" << endl;
  }
};


int main(){
  Naoki obj;

  return 0;
}


>>> 倍返しだ
```



## 純粋仮想関数
- 再定義して使用することを前提とした仮想関数の場合(基底クラスで定義しても使わない場合)は, `純粋仮想関数`として宣言する
```
virtual type function(arg-list) = 0;
```
- この仮想関数はこのクラスの派生クラスで再定義されることを意味し, このクラスでは一切定義しない. つまり, この関数は`再定義されなければ使えない`.
- また, 純粋仮想関数を持つクラスを`抽象クラス`と呼ぶ. 抽象クラスは未完成なクラスで, オブジェクトを作ることができない. 
- [override3.cpp](./src/override3.cpp)
```cpp
#include <iostream>
using namespace std;

class Base{                        // 抽象クラス
public:
  virtual void print() = 0;        // 純粋仮想関数
};

class Hoge : public Base{
public:
  void print(){
    cout << "ほげほげ" << endl;
  }
};

int main(){
  Hoge hoge_obj;
  Base *po = &hoge_obj;

  po->print();
  
  return 0;
}


>>> ほげほげ
```


