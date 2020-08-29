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
  cout << m.hp << endl;      // hpメンバはprivateなので, 直接アクセスしようとするとエラー

  return 0;
}
