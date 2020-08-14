# クラス

## 基本例
- ([class_Hoge.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge.cpp))
```
class Hoge{
private:                        // 外部からのアクセス不可
    int private_var;            // メンバ変数
		                
public:                         // 外部からのアクセス可
    const char *str;            
    void print(){               // メンバ関数(メソッド)
        cout << str;
    }   
};

int main(){
   Hoge hoge;
   hoge.str = "Hello World";
   hoge.print();
   return 0;
}


>>> Hello World
```

- クラス内でプロトタイプ宣言だけ行い, クラスの外部で関数定義を行うこともできる. ([class_Hoge2.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge2.cpp))
```
class Hoge{
public:  
    const char *str;
    void print()          // プロトタイプ宣言
};

void Hoge::print(){       // 関数定義 {
    cout << str;          //
}                         // 関数定義 }
```


## コンストラクタ
- コンストラクタ内で`str`を初期化しているので, main内の`hoge.str = "..."`が不要に. ([class_Hoge3.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge3.cpp))
```
class Hoge{
public:
  const char *str;
  Hoge(){                             // コンストラクタ {
    cout << "initialization!! \n\n";  //
    str = "Hello World";              //
  }                                   // コンストラクタ }
  void print();
};

void Hoge::print(){
    cout << str;
}

int main(){
  Hoge hoge;
                       // hoge.str = "Hello World"; 不要
  hoge.print();
  return 0;
}
```

- コンストラクタは引数を受け取ることもできる. ([class_Hoge3.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge3.cpp))
```
class Hoge{
public:
  const char *str;

  Hoge(const char *a){         // 引数 a を受け取る
    cout << a << "\n";         // 表示
    str = "By ドラえもん\n";  
  }
  
  void print();
};

void Hoge::print(){
  cout << str;
}

int main(){
  const char *str = "人にできて、きみだけにできないなんてことあるもんか。";
  Hoge hoge(str);     // 引数を与える
  hoge.print();
  
  return 0;
}

>>> 人にできて、きみだけにできないなんてことあるもんか。
>>> By ドラえもん
```

## デストラクタ
- ([class_Hoge5.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge5.cpp))
```
class Hoge{
public:
  const char *str;

  Hoge(const char *a){
    cout << a;
    str = "いいかい! もっとも「むずかしい事」は! \n";  
  }

  ~Hoge(){                               // デストラクタ {
    cout << "自分を乗り越える事さ! \n";	 // 
  }				         // デストラクタ }
  
  void print();
};

void Hoge::print(){
  cout << str;
}

int main(){
  Hoge hoge("もっとも「むずかしい事」は!\n");
  hoge.print();
  return 0;
}


>>> もっとも「むずかしい事」は!
>>> いいかい! もっとも「むずかしい事」は!
>>> 自分を乗り越える事さ!
```