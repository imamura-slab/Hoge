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

