#include <iostream>
using namespace std;

class Hoge{
public:
  virtual void print(){        // virtual
    cout << "hoge" << endl;
  }
};

class Fuga : public Hoge{
public:
  void print(){
    cout << "fuga" << endl;
  }
};

class Piyo : public Fuga{
public:
  void print(){
    cout << "piyo" << endl;
  }
};

class Foo : public Piyo{
};


int main(){
  Hoge hoge_obj;
  Fuga fuga_obj;
  Piyo piyo_obj;
  Foo  foo_obj;

  Hoge *hoge_po=&hoge_obj, *fuga_po=&fuga_obj, *piyo_po=&piyo_obj, *foo_po=&foo_obj;

  hoge_po->print();
  fuga_po->print();
  piyo_po->print();
  foo_po->print();

  return 0;
}
