#include <iostream>
using namespace std;

class Hoge{
public:
  const char *str;
  
  Hoge(){this->str = "引数ないよ\n";}                            // コンストラクタ
  Hoge(const char *str){this->str = str;}                        // コンストラクタ
  Hoge(const Hoge &obj){this->str = "コピーコンストラクタ\n";}   // コピーコンストラクタ
};

int main(){
  Hoge obj1("引数与えたよ\n");
  Hoge obj2 = obj1;                 // コピーコンストラクタが呼び出される
  Hoge obj3;
  
  cout << "obj1 : " << obj1.str;
  cout << "obj2 : " << obj2.str;
  cout << "obj3 : " << obj3.str;
  
  obj3 = obj1;                      // 初期化ではなく代入なので
  cout << "obj3 : " << obj3.str;    // コピーコンストラクタは呼び出されない
  
  return 0;
}
