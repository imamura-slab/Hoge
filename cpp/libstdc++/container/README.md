# コンテナクラス

## 固定長配列
- `<array>`ヘッダをインクルード
- 宣言と初期化
  ```cpp
  std::array<[type], [# of elements]> a{...};
  ```
- 参照
  - 演算子`[]`またはメソッド`.at()`

- プログラム例
   - [ソースコード](src/array.cpp)
   - 出力
     ```
     $ g++ -std=c++11 array.cpp && ./a.out 
     array size: 4
     1 2 3 4
     1 2 3 4
     1 2 3 4
     1 2 3 4
     array e is empty: true
     array size: 3x2
     3.14 3.14
     3.14 3.14
     3.14 3.14
     
     $ 
     ```
