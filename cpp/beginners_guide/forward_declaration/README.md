# 前方宣言
- クラスのメンバとして, 他のクラスのオブジェクトを保有したり, メンバ関数型のクラスのオブジェクトを受け取る場合がある.
  これが相互に行われた場合, `一方のクラスがまだ定義されていない`という問題が発生する.
- 下記のコード例のように, class A の定義の時点で B はまだ定義されていない. 
```
class A{
  void getB(B &);
};

class B{
  .....
};
```

- これを解決する方法が`前方宣言`である.
  ```
  class class-name;
  ```
  をクラス定義よりも前に記述することで指定したclass-nameクラスを宣言したことになる. 


- [forward_declaration1.cpp](./src/forward_declaration1.cpp)
```cpp
#include <iostream>
using namespace std;

class Piyo;        // 前方宣言

class Hoge{
public:
  Hoge(Piyo &obj);
  //Hoge(Piyo &obj){cout << obj.str << "\n";}   // これじゃダメだった
};


// Hoge::Hoge(Piyo &obj){                       // この位置でもダメ
//   cout << obj.str << "\n";                   // 
// }                                            // 

class Piyo{
public:
  const char *str;
  Piyo(const char *str){this->str = str;}
};

Hoge::Hoge(Piyo &obj){
  cout << obj.str << "\n";
}


int main(){
  Piyo piyo_obj("ピヨピヨ");
  Hoge hoge_obj(piyo_obj);
  return 0;
}


>>> ピヨピヨ
```

