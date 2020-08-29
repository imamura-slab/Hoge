#include <iostream>
#include <string>

using namespace std;

class Player {
  private:
    int hp;
    string name;
    friend class NPC;

  public:
    Player(int hp, string name) {
      Player::hp = hp;
      Player::name = name;
    }
};

class NPC {
  public:
    int getHp(Player &obj) {
      return obj.hp;
    };
    string getName(Player &obj) {
      return obj.name;
    };
};

int main() {
  Player p = Player(100, "たろう");
  NPC n = NPC();

  cout << n.getHp(p) << endl;
  cout << n.getName(p) << endl;

  return 0;
}
