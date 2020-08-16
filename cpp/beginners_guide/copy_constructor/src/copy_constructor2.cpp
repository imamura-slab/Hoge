#include <iostream>
using namespace std;

class Hoge{
public:
  Hoge(){cout << "コンストラクタ\n";}                            // コンストラクタ
  Hoge(const Hoge &obj){cout << "コピーコンストラクタ\n";}   // コピーコンストラクタ
};

Hoge getHoge(Hoge obj){
  return obj;
}

int main(){
  Hoge obj;
  obj = getHoge(obj);
  return 0;
}

