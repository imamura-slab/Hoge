#include <iostream>
using namespace std;

inline int func(int x){  // インライン関数 {
  return int(x * 1.1);	 // 
}			 // インライン関数 }

int main(){
  cout << func(100);
  return 0;
}
