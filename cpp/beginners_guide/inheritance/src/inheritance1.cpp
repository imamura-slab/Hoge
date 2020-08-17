#include <iostream>
#include <string>     // 文字列比較用(compare())
using namespace std;

class Pokemon{                              // 今回, 基底クラスとして扱う
public:
  const char *name;
  int lebel;
  const char *type1, *type2;

  Pokemon(const char *name="Pikachu",      // 基底クラスコンストラクタ {
	  const char *type1="Electric",    //
	  const char *type2="",		   //
	  int lebel=1){			   //
    this->name  = name;			   //
    this->lebel = lebel;		   //
    this->type1 = type1;		   //
    this->type2 = type2;		   //
  }					   // 基底クラスコンストラクタ }
  
  void print_data(){
    cout << "\n";
    cout << "name  : " << name  << "\n";
    cout << "lebel : " << lebel << "\n";
    cout << "type1 : " << type1 << "\n";
    cout << "type2 : " << type2 << "\n";
  }
};


class Pikachu : public Pokemon{                               // Pokemonクラスを継承
public:
  Pikachu(const char *name="Pikachu",                         // 派生クラスコンストラクタ {
	  const char *type1="Electric",			      // 
	  const char *type2="",				      // 
	  int lebel=1) : Pokemon(name, type1, type2, lebel){} // 派生クラスコンストラクタ }

  void cry(){
    cout << "\nピカー！\n";
  }
};


class Togepi : public Pokemon{
public:
  Togepi(const char *name="Pikachu",                          // 派生クラスコンストラクタ {
	 const char *type1="Electric",			      // 
	 const char *type2="",				      // 
	 int lebel=1) : Pokemon(name, type1, type2, lebel){}  // 派生クラスコンストラクタ }

  void cry(){
    cout << "\nチョッゲプリィイイイイイイ！！\n";
  }
};

  
int main(){
  Pikachu p_obj;                    // 派生クラスでインスタンス化
  Togepi  t_obj("Togepi", "Fairy"); // 派生クラスでインスタンス化
  
  p_obj.print_data();               // 基底クラスのメソッド使えるよ
  p_obj.cry();                      // もちろん派生クラスのメソッドも使えるよ

  t_obj.print_data();
  t_obj.cry();
  
  return 0;
}
