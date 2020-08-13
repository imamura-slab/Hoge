# スコープ
## スコープ解決演算子 ::

|    変数の種類|     変数 var|
|:----:|----:|
|  ローカル変数|          var|
|    メンバ変数|クラス名::var|
|グローバル変数|        ::var|


- [scope1.cpp](./src/scope1.cpp)
```
#include <iostream>
using namespace std;

const char *str = "試合終了ですよ...? \n";  // グローバル変数

class Hoge{
public:
  const char *str = "そこで";               // メンバ変数
  void print(const char *str);
};

void Hoge::print(const char *str){          // ローカル変数
  cout << str << Hoge::str << ::str;
}

int main(){
  Hoge hoge;
  hoge.print("あきらめたら");
  return 0;
}

  
>>> あきらめたらそこで試合終了ですよ...? 
```