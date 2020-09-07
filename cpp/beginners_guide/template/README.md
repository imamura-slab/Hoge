# テンプレート関数

- `内部処理は同じ`だがデータ型が異なる関数があるとき, 全てのデータ型の関数をオーバーロードでサポートするのも一つの方法だが, 面倒でソースの可読性も低下させてしまう.
  - この作業をすべてコンパイラに任せてしまおう -> `テンプレート関数(汎用関数)`
  ```
  template <class type> function-declarator  (こっちが一般的)
  または
  template <typename type> function-declarator
  ```
- [template1.cpp](./src/template1.cpp)

```cpp
#include <iostream>
using namespace std;

template <class T> void println(T out){  // テンプレート関数
  cout << out << endl;
}

int main(){
  println("string");
  println(3);
  println(3.14);

  return 0;
}

>>> string
>>> 3
>>> 3.14
```


```
           template <class T> void println(T out)               テンプレート関数
              /               |              \                  インスタンシエート
void println(char *)  void println(int)  void println(double)   生成された関数
```
- ソース上のテンプレート関数を各データ型専用の関数に変換する工程を`インスタンシエート`と呼び, コンパイル後に各データ型用に作られた関数を`生成された関数`と呼ぶ.


### 複数の型を受け取るテンプレート関数
- [template2.cpp](./src/template2.cpp)
```cpp
#include <iostream>
using namespace std;

template <class T1, class T2> void println(T1 var1, T2 var2){  // テンプレート関数
  cout << var1 << " : " << var2 << endl;
}

int main(){
  println("円周率", 3.1415926535);   // (string, double)
  println(1, 1.618);                 // (int, double)    黄金比

  return 0;
}


>>> 円周率 : 3.14159
>>> 1 : 1.618
```


***
# テンプレートのオーバーライド
