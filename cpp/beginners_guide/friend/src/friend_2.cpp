#include <iostream>

using namespace std;

class Monster {
  private:
    int hp;
    friend int getHp(Monster &);

  public:
    Monster(int hp) {
      Monster::hp = hp;
    }
};

int getHp(Monster &obj) {
  return obj.hp;
}

int main() {
  Monster m = Monster(50);
  
  cout << getHp(m) << endl;

  return 0;
}
