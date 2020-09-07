#include <iostream>
using namespace std;

template <class T> void println(T out){  // テンプレート関数
  cout << out << endl;
}

int main(){
  println("string");
  println(3);
  println(3.14);

  return 0;
}
