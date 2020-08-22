# コンテナクラス

## array
- `<array>`ヘッダをインクルード
- 宣言と初期化
  ```cpp
  std::array<[type], [# of elements]> a{...};
  ```
- 参照
  - 演算子`[]`またはメソッド`.at()`

- [ソースコード](src/array.cpp)
```
$ g++ array.cpp && ./a.out 
array size: 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
array e is empty: true
array size: 2x3
3.14 3.14
3.14 3.14
3.14 3.14

$ 
```
