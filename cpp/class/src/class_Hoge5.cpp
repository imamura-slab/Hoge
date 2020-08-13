#include <iostream>
using namespace std;

class Hoge{
private:
  int private_var;

public:
  const char *str;

  Hoge(){
    cout << "constructor \n";
    str = "Hello World! \n";  
  }

  ~Hoge(){                      // デストラクタ {
    cout << "destructor \n";	// 
  }				// デストラクタ }
  
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

