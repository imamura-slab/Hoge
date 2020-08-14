# オーバーロード
- `引数の数`あるいは`データ型`が異なる場合は関数名が同じ関数を多重定義できる. (戻り値が違うだけでは不十分)
- [overload1.cpp](./src/overload1.cpp)
```
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
```
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



