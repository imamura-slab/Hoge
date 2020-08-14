#include <iostream>
using namespace std;

const char *str = "試合終了ですよ...? \n";

class Hoge{
public:
  const char *str = "そこで";
  void print(const char *str);
};

void Hoge::print(const char *str){
  cout << str << Hoge::str << ::str;
}

int main(){
  Hoge hoge;
  hoge.print("あきらめたら");
  return 0;
}

  
 
