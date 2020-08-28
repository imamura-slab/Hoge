# フレンド

通常, クラスのprivateメンバに, クラス外からアクセスしようとすると, エラーになる.

([friend_1.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/friend/src/friend_1.cpp))
```c++
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
