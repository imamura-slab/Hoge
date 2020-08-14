#include <iostream>
using namespace std;

void foo(){                                        // 引数なしならこっちを実行
  cout << "アリーヴェ デルチ!（さよならだ）\n";	   // 
}						   // 

void foo(const char *str){			   // 引数ありならこっちを実行
  cout << str;					   // 
}						   // 

int main(){
  foo();
  foo("ボラーレ・ヴィーア（飛んで行きな）\n");
  return 0;
}

