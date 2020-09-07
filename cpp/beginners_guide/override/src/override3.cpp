#include <iostream>
using namespace std;

class Base{                        // 抽象クラス
public:
  virtual void print() = 0;        // 純粋仮想関数
};

class Hoge : public Base{
public:
  void print(){
    cout << "ほげほげ" << endl;
  }
};

int main(){
  Hoge hoge_obj;
  Base *po = &hoge_obj;

  po->print();
  
  return 0;
}
