# コピーコンストラクタ
- コピーコンストラクタはオブジェクトの初期化時に呼び出されるもので, 宣言時, 引数, 戻り値の3つの動作でコピーがとられたときに実行される
- 関数名はコンストラクタと同様にクラス名と同じで, const指定のコピー元のオブジェクトの参照を受け取るようにする
```
class-name(const class-type &obj)
```
- ただしコピーコンストラクタは`代入では作用しない`.
- [copy_constructor1.cpp](./src/copy_constructor1.cpp)
```
#include <iostream>
using namespace std;

class Hoge{
public:
  const char *str;
  
  Hoge(){this->str = "引数ないよ\n";}                            // コンストラクタ
  Hoge(const char *str){this->str = str;}                        // コンストラクタ
  Hoge(const Hoge &obj){this->str = "コピーコンストラクタ\n";}   // コピーコンストラクタ
};

int main(){
  Hoge obj1("引数与えたよ\n");
  Hoge obj2 = obj1;                 // コピーコンストラクタが呼び出される
  Hoge obj3;
  
  cout << "obj1 : " << obj1.str;
  cout << "obj2 : " << obj2.str;
  cout << "obj3 : " << obj3.str;
  
  obj3 = obj1;                      // 初期化ではなく代入なので
  cout << "obj3 : " << obj3.str;    // コピーコンストラクタは呼び出されない
  
  return 0;
}


>>> obj1 : 引数与えたよ
>>> obj2 : コピーコンストラクタ
>>> obj3 : 引数ないよ
>>> obj3 : 引数与えたよ
```



- コピーコンストラクタは, 関数にオブジェクトを値渡しするとき, 関数から呼び出し元にオブジェクトを値渡しするときにも呼び出される
- [copy_constructor2.cpp](./src/copy_constructor2.cpp)
```
#include <iostream>
using namespace std;

class Hoge{
public:
  Hoge(){cout << "コンストラクタ\n";}                        // コンストラクタ
  Hoge(const Hoge &obj){cout << "コピーコンストラクタ\n";}   // コピーコンストラクタ
};

Hoge getHoge(Hoge obj){
  return obj;
}

int main(){
  Hoge obj;
  obj = getHoge(obj);
  return 0;
}


>>> コンストラクタ
>>> コピーコンストラクタ           // 関数にオブジェクトを渡したとき
>>> コピーコンストラクタ           // 戻り値としてオブジェクトを受け取ったとき
```



