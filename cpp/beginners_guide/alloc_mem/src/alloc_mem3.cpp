#include <iostream>
using namespace std;

class Hoge{
public:
  int id;
  ~Hoge(){
    cout << id << " : " <<"+++++ destructorだよ +++++" << endl;
  }
  void set_id(int id){
    this->id = id;
  }
};

int main(){
  int N = 10;
  
  Hoge *obj;
  obj = new Hoge[N];

  for(int i=0;i<N;i++){
    obj[i].set_id(i);
  }
  
  cout << endl;
  cout << "今からdeleteするよ" << endl;
  delete [] obj;
  cout << "　　　deleteしたよ" << endl;
  
  return 0;
}
