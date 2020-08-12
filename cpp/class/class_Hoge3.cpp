#include <iostream>
using namespace std;

class Hoge{
private:
  int private_var;


public:
  const char *str;

  Hoge(){ // コンストラクタ
    cout << "initialization!! \n\n";
    str = "Hello World";
  }
  
  void print();
};


void Hoge::print(){
  cout << str;
}



int main(){
  Hoge hoge;
  hoge.print();
  
  return 0;
}
