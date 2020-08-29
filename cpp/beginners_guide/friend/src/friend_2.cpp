#include <iostream>

using namespace std;

class Monster {
  private:
    int hp;
    friend int getHp(Monster &);    // フレンド関数の宣言(クラス内)
                                    // 仮引数の識別子(&の後)は書いても書かなくてもOK

  public:
    Monster(int hp) {
      Monster::hp = hp;
    }
};

int getHp(Monster &obj) {           // フレンド関数の定義(クラス外)
  return obj.hp;                    // フレンド関数の中では, 渡されたクラスオブジェクトのprivateメンバにアクセスできる.
}

int main() {
  Monster m = Monster(50);
  
  cout << getHp(m) << endl;         // フレンド関数に, hpメンバにアクセスしてもらう

  return 0;
}
