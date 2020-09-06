#include <iostream>
using namespace std;

class Base{
public:
  const char* name;
};

class Derived : public Base{
public:
  int age;
};


int main(){
  Derived derived_obj;
  Base *base_obj = &derived_obj;                        // 派生クラスのアドレスを代入
  
  derived_obj.name = "野原しんのすけ";
  derived_obj.age  = 5;


  cout << "derived name : " << derived_obj.name << endl;
  cout << "derived age  : " << derived_obj.age  << endl;
  cout << "base    name : " << base_obj->name   << endl;
  //cout << "base    age  : " << base_obj->age    << endl;   // コンパイルエラー
  
  return 0;
}
