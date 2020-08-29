# インライン関数
- [inline1.cpp](./src/inline1.cpp)
```cpp
#include <iostream>
using namespace std;

inline int func(int x){  // インライン関数 {
  return int(x * 1.1);	 // 
}			 // インライン関数 }

int main(){
  cout << func(100);
  return 0;
}

>>> 110
```

___
- クラス内で定義したメンバ関数の場合は`inline`を指定しなくても, インライン化可能な場合は自動的にインライン化される


