# クラス

## 基本例 ([class_Hoge.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge.cpp))
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
    void print()          // メンバ関数(メソッド)
};

void Hoge::print(){
    cout << str;
}
```


## コンストラクタ
- コンストラクタ内で`str`を初期化しているので, main内の`hoge.str = "..."`が不要に. ([class_Hoge3.cpp](https://github.com/imamura-slab/Hoge/tree/master/cpp/class/src/class_Hoge3.cpp))
```
class Hoge{
public:
  const char *str;
  Hoge(){                             // コンストラクタ {
    cout << "initialization!! \n\n";
    str = "Hello World";       
  }                                   // コンストラクタ }
  void print();
};

void Hoge::print(){
    cout << str;
}

int main(){
  Hoge hoge;
  hoge.print();
  return 0;
}
```


