#include <iostream>
using namespace std;

class Hoge{
private:
  int private_var;


public:
  const char *str;

  Hoge(const char *a){   // 引数 a を受け取る
    cout << a << "\n";   // 表示
    str = "By ドラえもん\n";  
  }
  
  void print();
};


void Hoge::print(){
  cout << str;
}



int main(){
  const char *str = "人にできて、きみだけにできないなんてことあるもんか。";
  Hoge hoge(str);     // 引数を与える
  hoge.print();
  
  return 0;
}

