#include <iostream>
using namespace std;

class Hanzawa{
public:
  virtual void func(){
    cout << "倍返しだ" << endl;
  }
  ~Hanzawa(){
    this->func();
  }
};

class Naoki : public Hanzawa{
public:
  void func(){
    cout << "100倍返しだ" << endl;
  }
};


int main(){
  Naoki obj;

  return 0;
}
