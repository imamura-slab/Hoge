#include <iostream>

class Monster {
  private:
    int hp;

  public:
    Monster(int hp) {
      Monster::hp = hp;
    }
};

int main() {
  Monster m = Monster(50);   // 引数50をコンストラクタに渡して, インスタンス生成
  m.hp = 10;      // hpメンバはprivateなので, 直接アクセスしようとするとエラー

  return 0;
}
