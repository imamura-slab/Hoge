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
  - 必ず再定義しなければならないというわけではない(foo). その場合は最後に再定義したクラスのメンバ関数が参照される. 
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
  void print(){
    cout << "fuga" << endl;
  }
};

class Piyo : public Fuga{
public:
  void print(){
    cout << "piyo" << endl;
  }
};

class Foo : public Piyo{
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



