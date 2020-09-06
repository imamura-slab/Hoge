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

- フレンド関数の宣言は, privateでもpublicでもよい.
- フレンド関数の引数は, 1つ以上のクラスオブジェクト.

([friend_2.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/friend/src/friend_2.cpp))
```c++
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

```
```
>>> 50
```

- あくまで, フレンド関数はクラスのメンバではない. 身内ではなく友達.
- なので,  
  m.getHp()  
  のように, クラスのメンバとして呼ぶことはできない.

フレンド関数の宣言さえ書いておけば, そのクラスのprivateメンバに同一のフレンド関数からアクセスできる.

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



>>> モンスター : ゴブリン
    プレイヤー : たろう
    NPC : シャンクス
```

## フレンドクラス
フレンド関数の進化版
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


```
```
>>> 100
    たろう
```

## 演算子のオーバーロード
演算子のオーバーロードについても, クラスの外に定義を書いて, フレンド関数に登録することで, クラス内のプライベートメンバにアクセスすることが可能.
([オーバーロード])(https://github.com/imamura-slab/Hoge/tree/234417bf359431a9d52a569e9eb8ac6366e7f101/cpp/beginners_guide/overload))のようにクラス内に書いてもいいし, フレンドを使ってクラス外に書いてもよい.

- 以下のプログラムは, 複素数クラスについて, +演算子と<<演算子をオーバーロードするサンプルプログラム.
([overload.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/friend/src/overload.cpp)
 ```c++

#include <iostream>

using namespace std;

// 複素数クラス
class Complex {
  private:
    double re;
    double im;
    friend Complex operator+(Complex c1, Complex c2);     // +演算子のオーバーロードをフレンド関数に登録
    friend ostream &operator<<(ostream &os, Complex c);   // <<演算子のオーバーロードをフレンド関数に登録
  public:
    Complex() {}
    Complex(double real, double imag) {
      re = real;
      im = imag;
    }
};

Complex operator+(Complex c1, Complex c2) {               // フレンド関数に登録しているので, Complex型のreやimにアクセス可能
  Complex result;
  result.re = c1.re + c2.re;
  result.im = c1.im + c2.im;
  return result;
}

ostream &operator<<(ostream &os, Complex c) {             // 第1引数は演算子の左側, 第2引数は演算子の右側に対応
                                                          // つまり, ostream型 << Complex型 となるような演算子<<を定義
  cout << "(" << c.re << ", " << c.im << "i)" << endl;
  return os;
}

int main() {
  Complex c1(2, 3);
  Complex c2(4, 5);

  Complex c3;
  c3 = c1 + c2;

  cout << c3;

  return 0;
}


 ```
 ```
 >>> (6, 8i)
 ```

## 所感
- あまり使いどころがわからない.
- getterメソッドとかでよくね？
- クラスの定義が長くなったからクラスの外に関数定義を書きたい.
  って時とかは有効なのかもしれない.
