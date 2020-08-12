#include <iostream>
using namespace std;

class Hoge{
private:
  int private_var;


public:
  const char *str;
  void print();
};


void Hoge::print(){
  cout << str;
}



int main(){
  Hoge hoge;
  hoge.str = "Hello World";
  hoge.print();

  return 0;
}
