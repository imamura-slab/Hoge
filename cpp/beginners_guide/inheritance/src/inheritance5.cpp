#include <iostream>
using namespace std;

class Base{
public:
  void print(){
    cout << "Base だよ" << endl;
  }
};

class Derived : public Base{
public:
  void print(){
    cout << "Derived だよ" << endl;
  }
};


int main(){
  Derived derived_obj;
  Base *base_obj = &derived_obj;                        // 派生クラスのアドレスを代入
  
  derived_obj.print();
  base_obj->print();    // 派生クラスのアドレスを与えたけど 基底クラスの方が実行されるよ
  
  return 0;
}
