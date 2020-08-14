#include <iostream>
using namespace std;

class Hoge{
public:
  const char *str;
  Hoge(const char *str){this->str = str;}  
  void func(){cout << this->str;}          // ここの this-> はなくてもOK
};


int main(){
  Hoge hoge[3] = {"ズキュウウウン\n", "メメタア\n", "メギャン\n"};
  for(int i=0;i<3;i++){
    hoge[i].func();
  }
}

