#include <iostream>
using namespace std;

class Hoge{
private:
  int private_var;


public:
  const char *str;

  Hoge(const char *a){          // 引数 a を受け取る
    cout << a << "\n\n";  // 表示
    str = "Hello World";  
  }
  
  void print();
};


void Hoge::print(){
  cout << str;
}



int main(){
  Hoge hoge("Hi!");      // 引数を与える
  hoge.print();
  
  return 0;
}

