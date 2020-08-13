#include <iostream>
using namespace std;

class Hoge{
private:
  int private_var;

public:
  const char *str;

  Hoge(const char *a){
    cout << a;
    str = "いいかい! もっとも「むずかしい事」は! \n";  
  }

  ~Hoge(){                               // デストラクタ {
    cout << "自分を乗り越える事さ! \n";	 // 
  }				         // デストラクタ }
  
  void print();
};


void Hoge::print(){
  cout << str;
}

int main(){
  Hoge hoge("もっとも「むずかしい事」は!\n");
  hoge.print();
  
  return 0;
}

