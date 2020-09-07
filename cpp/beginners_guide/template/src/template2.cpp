#include <iostream>
using namespace std;

template <class T1, class T2> void println(T1 var1, T2 var2){  // テンプレート関数
  cout << var1 << " : " << var2 << endl;
}

int main(){
  println("円周率", 3.1415926535);   // (string, double)
  println(1, 1.618);                 // (int, double)    黄金比

  return 0;
}
