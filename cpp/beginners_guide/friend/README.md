# フレンド

## フレンド関数
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
  cout << m.hp << endl;      // hpメンバはprivateなので, 直接アクセスしようとするとエラー

  return 0;
}



>>> ERROR!
```

ここで, クラスの中にfriend指示子を付けた関数宣言を書き, クラスの外にその定義を書くと, その関数(フレンド関数)を通して, クラスのprivateメンバにアクセスできる.

- friend関数の宣言は, privateでもpublicでもよい.
- friend関数の引数は, 1つ以上の(同クラスの)オブジェクト.

([friend_2.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/friend/src/friend_2.cpp))
```c++
class Monster {
  private:
    int hp;
    friend int getHp(Monster &);    // friend関数の宣言(クラス内)

  public:
    Monster(int hp) {
      Monster::hp = hp;
    }
};

int getHp(Monster &obj) {           // friend関数の定義(クラス外)
  return obj.hp;                    // friend関数の中では, privateメンバにアクセスできる.
}

int main() {
  Monster m = Monster(50);
  
  cout << getHp(m) << endl;         // friend関数に, hpメンバにアクセスしてもらう

  return 0;
}


>>> 50
```

- あくまで, friend関数はクラスのメンバではない. 身内ではなく友達.
- なので,
  m.getHp()
  のように, クラスのメンバとして呼ぶことはできない.

friend関数の宣言さえ書いておけば, そのクラスのprivateメンバに同一のフレンド関数からアクセスできる.
([friend_3.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/friend/src/friend_3.cpp))
```c++
class Monster;
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

void getName(Monster &obj_m, Player &obj_p, NPC &obj_n) {
  cout << "モンスター : " << obj_m.name << endl
    << "プレイヤー : " << obj_p.name << endl
    << "NPC : " << obj_n.name << endl;
}  // 1つのフレンド関数で異なるクラスのプライベートメンバに同時にアクセス可能

int main() {
  Monster m = Monster("ゴブリン");
  Player p  = Player("たろう");
  NPC n     = NPC("シャンクス");
  
  getName(m, p, n);

  return 0;
}



>>> モンスター : ゴブリン
    プレイヤー : たろう
    NPC : シャンクス
```

## フレンドクラス
フレンド関数の進化版.
- フレンドクラス内のメソッドはすべてフレンド関数扱いになる.
- クラスAの定義内で, friendクラスを付けたクラスBを宣言しておくと, クラスBからは自由にクラスAのメンバにアクセスできる. なので, main関数などからは, クラスBのメソッドを使ってクラスAにアクセスできる.
([friend_4.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/friend/src/friend_4.cpp))
```c++
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



>>> 100
    たろう
```

## 所感
- あまり使いどころがわからない.
- getterとかでよくね？
- クラスの定義が長くなったからクラスの外に関数定義を書きたい
  って時とかは有効なのかもしれない.
