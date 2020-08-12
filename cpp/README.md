# C++ の勉強
- 参考サイト
  - [C++入門](http://wisdom.sakura.ne.jp/programming/cpp/)

## ヘッダ
```
#include <iostream>
using namespace std;
```


## 標準入出力
- 標準出力には`std::cout`, 標準入力には`std::cin`を使用する.  
  ヘッダに`using namespace std`と記述することで, `cout`や`cin`だけでよくなる.
  
### 標準出力
```
cout << "hoge \n";
cout << 2020 << "/" << 8 << "/" << 12 << "\n" ;


>>> hoge
>>> 2020/8/12
```

### 標準入力
- `value`には, 入力された値を格納する`変数`を指定する. (`アドレス`ではない)
```
cin >> value;
```


## [クラス](https://github.com/imamura-slab/Hoge/tree/master/cpp/class)
### 基本形
```
class [tag [: base-list]]{
member-list
} [declarators];
```

tag : クラス型の名前を指定

base-list : ベースクラスの名前を指定

member-list : クラスのメンバ, またはフレンドを宣言

declarators : オブジェクトを1つ以上宣言


### コンストラクタ
- オブジェクト生成時に自動で呼び出される
  - オブジェクトが初期値として持つべき値などをここで設定する
- コンストラクタ関数はクラスと同じ名前の関数. 戻り値は存在しない

```
class class-name{
    class-name(){  // コンストラクタ
        初期化処理などをココで行う
    }
}
```

