#include <iostream>
using namespace std;

class Hoge{
public:
  Hoge(const char *str){
    cout << str << endl;
  }
  ~Hoge(){
    cout << "+++++ destructorだよ +++++" << endl;
  }
};

int main(){
  Hoge *obj;
  obj = new Hoge("hogehogehoge");

  cout << endl;
  cout << "今からdeleteするよ" << endl;
  delete obj;
  cout << "　　　deleteしたよ" << endl;
  
  return 0;
}
