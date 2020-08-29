#include <iostream>
#include <string>

using namespace std;

class Monster;    // 宣言しておかないと下の方でエラーになる
class Player;
class NPC;

class Monster {
  private:
    string name;
    friend void getName(Monster &, Player &, NPC &);  // 同じフレンド関数を

  public:
    Monster(string name) {
      Monster::name = name;
    }
};

class Player {
  private:
    string name;
    friend void getName(Monster &, Player &, NPC &);  // 異なるクラスに

  public:
    Player(string name) {
      Player::name = name;
    }
};

class NPC {
  private:
    string name;
    friend void getName(Monster &, Player &, NPC &);  // 宣言しておく

  public:
    NPC(string name) {
      NPC::name = name;
    }
};

// 1つのフレンド関数で異なるクラスのプライベートメンバに同時にアクセス可能
void getName(Monster &obj_m, Player &obj_p, NPC &obj_n) {
  cout << "モンスター : " << obj_m.name << endl
    << "プレイヤー : " << obj_p.name << endl
    << "NPC : " << obj_n.name << endl;
}  

int main() {
  Monster m = Monster("ゴブリン");
  Player p  = Player("たろう");
  NPC n     = NPC("シャンクス");
  
  getName(m, p, n);

  return 0;
}
