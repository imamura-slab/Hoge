# 動的メモリの割り当て

- もちろんC言語の`malloc()関数`も使用できるが, C++では推奨されない
- C++には独自のメモリ割り当て演算子`new 演算子`がある
  - 割り当てるべきバイト数を自動で計算してくれる
  - 割り当てたメモリへのポインタを返す
  - メモリを割り当てられなかったときは`例外`を生成する
  - 解放するときには`delete 演算子`を使用する

```
new type;
```
```
delete pointer;
```

- [alloc_mem1.cpp](./src/alloc_mem1.cpp)

```cpp
#include <iostream>
using namespace std;

int main(){
  int *p;
  p = new int;          // 割り当て失敗時の処理は行なっていない

  *p = 100;
  cout << *p << endl;

  delete p;
  return 0;
}

>>> 100
```



***
## オブジェクトの割り当て
```
new Object(initializer);
```

- delete した後にデストラクタが呼び出される
- [alloc_mem2.cpp](./src/alloc_mem2.cpp)

```cpp
#include <iostream>
using namespace std;

class Hoge{
public:
  Hoge(const char *str){
    cout << str << endl;
  }
  ~Hoge(){
    cout << "+++++ destructorだよ +++++" << endl;
  }
};

int main(){
  Hoge *obj;
  obj = new Hoge("hogehogehoge");

  cout << endl;
  cout << "今からdeleteするよ" << endl;
  delete obj;
  cout << "　　　deleteしたよ" << endl;
  
  return 0;
}


>>> hogehogehoge
>>> 
>>> 今からdeleteするよ
>>> +++++ destructorだよ +++++
>>> 　　　deleteしたよ
```


***
## 配列の割り当て
```
new type[size];
```

- 配列の先頭ポインタを返す
- ただし配列の場合, `初期化できない`ことに注意
- delete の構文も少し違う

```
delete [] pointer;
```

- [alloc_mem3.cpp](./src/alloc_mem3.cpp)
```cpp
#include <iostream>
using namespace std;

class Hoge{
public:
  int id;
  ~Hoge(){
    cout << id << " : " <<"+++++ destructorだよ +++++" << endl;
  }
  void set_id(int id){
    this->id = id;
  }
};

int main(){
  int N = 10;
  
  Hoge *obj;
  obj = new Hoge[N];

  for(int i=0;i<N;i++){
    obj[i].set_id(i);
  }
  
  cout << endl;
  cout << "今からdeleteするよ" << endl;
  delete [] obj;
  cout << "　　　deleteしたよ" << endl;
  
  return 0;
}

// 後ろの要素から解放されるみたい
>>> 今からdeleteするよ
>>> 9 : +++++ destructorだよ +++++
>>> 8 : +++++ destructorだよ +++++
>>> 7 : +++++ destructorだよ +++++
>>> 6 : +++++ destructorだよ +++++
>>> 5 : +++++ destructorだよ +++++
>>> 4 : +++++ destructorだよ +++++
>>> 3 : +++++ destructorだよ +++++
>>> 2 : +++++ destructorだよ +++++
>>> 1 : +++++ destructorだよ +++++
>>> 0 : +++++ destructorだよ +++++
>>> 　　　deleteしたよ
```



