#include <iostream>
using namespace std;

class Piyo;        // 前方宣言

class Hoge{
public:
  Hoge(Piyo &obj);
  //Hoge(Piyo &obj){cout << obj.str << "\n";}   // これじゃダメだった
};


// Hoge::Hoge(Piyo &obj){                       // この位置でもダメ
//   cout << obj.str << "\n";                   // 
// }                                            // 

class Piyo{
public:
  const char *str;
  Piyo(const char *str){this->str = str;}
};

Hoge::Hoge(Piyo &obj){
  cout << obj.str << "\n";
}


int main(){
  Piyo piyo_obj("ピヨピヨ");
  Hoge hoge_obj(piyo_obj);
  return 0;
}
