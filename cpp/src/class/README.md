# クラス

## 基本例
```
class Hoge{
private:              // 外部からのアクセス不可
    int private_var;  // メンバ変数


public:  // 外部からのアクセス可
    const char *str;
    void print(){     // メンバ関数(メソッド)
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

- クラス内でプロトタイプ宣言だけをして, クラスの外部で関数定義を行うこともできる
```
class Hoge{
public:  
    const char *str;
    void print()     // メンバ関数(メソッド)
};

void Hoge::print(){
    cout << str;
}
```


## コンストラクタ
```
class Hoge{
public:
  const char *str;

  Hoge(){ // コンストラクタ
    cout << "initialization!! \n\n";
    str = "Hello World";
  }
  
  void print();
};

...

int main(){
  Hoge hoge;
  hoge.print();

  return 0;
}
```


