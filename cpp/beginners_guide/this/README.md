# thisポインタ

- メンバ関数ではthisポインタが存在する. これはメンバ関数が実行されたときのオブジェクトのポインタを指す.
- メンバ関数内でメンバ変数を指すとき, メンバ変数を直接名指しで指名していたが, 実際はthisポインタを省略した形である. 
- [this1.cpp](./src/this1.cpp)
```cpp
#include <iostream>
using namespace std;

class Hoge{
public:
  const char *str;
  Hoge(const char *str){this->str = str;}  
  void func(){cout << this->str;}          // ここの this-> はなくてもOK
};

int main(){
  Hoge hoge[3] = {"ズキュウウウン\n", "メメタア\n", "メギャン\n"};
  for(int i=0;i<3;i++){
    hoge[i].func();
  }
}


>>> ズキュウウウン
>>> メメタア
>>> メギャン
```

___
- thisポインタを使う必要がない場所では通常, thisを省略することが多い
- thisは例えば自分自身のオブジェクトをメンバ関数から他の関数へ渡すときに使う
- [this2.cpp](./src/this2.cpp)
```cpp
#include <iostream>
using namespace std;

class Hoge{
public:
  const char *str;
  Hoge(const char *str){this->str = str;}  
  void call();
};

void print(Hoge *hoge){
  cout << hoge->str;
}

void Hoge::call(){
  print(this);      // this!!
}

int main(){
  Hoge hoge[3] = {"ズキュウウウン\n", "メメタア\n", "メギャン\n"};
  for(int i=0;i<3;i++){
    hoge[i].call();
  }
}


>>> ズキュウウウン
>>> メメタア
>>> メギャン
```

