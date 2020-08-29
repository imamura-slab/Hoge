#include <iostream>
using namespace std;

class Base{
public:
  const char* name;
};

class Derived1 : virtual public Base{   // 変更点: virtual追加
public:
  int age;
};

class Derived2 : virtual public Base{   // 変更点: virtual追加
public:
  const char* sex;
};

class Derived3 : public Derived1, public Derived2{
public:
  void print(){
    cout << "name: " << name << endl;
    cout << " age: " << age  << endl;
    cout << " sex: " << sex  << endl;
  }
};


int main(){
  Derived3 obj;

  obj.name = "野原しんのすけ";
  obj.age  = 5;
  obj.sex  = "male";
  obj.print();

  return 0;
}
