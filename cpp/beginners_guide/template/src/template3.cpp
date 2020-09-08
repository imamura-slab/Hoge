#include <iostream>
using namespace std;

template <class T> void println(T var){  // テンプレート関数
  cout << var << endl;
}

void println(float val){                 // テンプレート関数のオーバーロード (引数がfloat型のとき)
  cout << val << 'f' << endl;
}

int main(){
  float  pi = 3.14;
  double PI = 3.14;
  
  println("string");
  println(3);
  println(pi);
  println(PI);

  return 0;
}
