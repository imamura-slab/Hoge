# オーバーロード

## 関数のオーバーロード
- `引数の数`あるいは`データ型`が異なる場合は関数名が同じ関数を多重定義できる. (戻り値が違うだけでは不十分)
- [overload1.cpp](./src/overload1.cpp)
```cpp
#include <iostream>
using namespace std;

void foo(){                                        // 引数なしならこっちを実行
  cout << "アリーヴェ デルチ!（さよならだ）\n";	   // 
}						   // 

void foo(const char *str){			   // 引数ありならこっちを実行
  cout << str;					   // 
}						   // 

int main(){
  foo();
  foo("ボラーレ・ヴィーア（飛んで行きな）\n");
  return 0;
}


>>> アリーヴェ デルチ!（さよならだ）
>>> ボラーレ・ヴィーア（飛んで行きな）
```


- コンストラクタのオーバーロードも可能 (デストラクタは不可)
- [overload2.cpp](./src/overload2.cpp)
```cpp
#include <iostream>
using namespace std;

class Hoge{
public:
  const char *str;
  Hoge(){cout << "だが断る\n";}       // コンストラクタのオーバーロード
  Hoge(const char *str){cout << str;} // コンストラクタのオーバーロード
};


int main(){
  Hoge hoge1;                         //
  Hoge hoge2("でも断る\n");	      //
  return 0;
}


>>> だが断る
>>> でも断る
```

## 演算子のオーバーロード
- 関数だけでなく**演算子**も多重定義することができる．
  - オーバーロード可能な演算子
    - 算術演算子（`+`, `-`, `*`, `/`, `%`, ...）
    - 比較演算子（`<`, `>`, `<=`, `>=`, `==`, `!=`, ...）
    - 論理演算子（`!`, `&&`, `||`）
    - ビット演算子（`~`, `&`, `|`, `^`, ...）
    - e.t.c.（`=`, `[]`, `()`, `new`, `delete`, ...）
    - **オーバーロードできない演算子もあることに注意**（`::`, `?:`, ...）
      - [参考](https://programming-place.net/ppp/contents/cpp/language/019.html#cant_overload_op)
  - クラスのメンバ関数として定義する．
  ```
  type operator operator-symbol(parameter-list)
  ```

- [overload3.cpp](./src/overload3.cpp)

```c++
#include <iostream>

using namespace std;

class Hoge
{
private:
  const char *str;
  
public:
  Hoge() { cout << "だが断る" << endl; }         // ユーザ定義のコンストラクタ
  Hoge(const char *str) { cout << str << endl; } // コンストラクタのオーバーロード

  /* 演算子 + のオーバーロード */
  char* operator+(Hoge rhs)
  {
    return "ナニッ！？"; // 引数使え警告でるけど無視
  } 
};

int main(void)
{
  Hoge hoge1;
  Hoge hoge2("でも断る");
  cout << hoge1 + hoge2 << endl; // Hogeクラス + Hogeクラス
  return 0;
}
```

```
>>> だが断る
>>> でも断る
>>> ナニッ！？
```
