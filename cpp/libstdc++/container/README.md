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
     ```sh
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

## 可変長配列
- `<vector>`ヘッダをインクルード
- コンストラクト
  ```cpp
  std::vector<[型やクラス]> v;
  std::vector<[型やクラス]> v([要素数]);
  std::vector<[型やクラス]> v([要素数], [初期値]);
  std::vector<std::vector<[型やクラス]> > v([行], std::vector<[型やクラス]>, [列]);
  ...
  ```
- メソッド
  - `.size()`: 配列サイズを取得
  - `.pushback()`: 末尾へ要素を追加 
  - `.empty()`: 空かどうかを判定
  - `.resize()`: 要素数のリサイズ
  - などなど

- プログラム例
   - [ソースコード](src/vector.cpp)
   - 出力
     ```sh
     $ g++ -std=c++11 vector.cpp && ./a.out
     0 1 2 3 4 5 
     poped 5 -> poped 4 -> poped 3 -> poped 2 -> poped 1 -> poped 0 -> empty!
     hoge
     huga
     piyo
     9 9 9 9 9 9 9 
     9 9 9 9 9 9 9 
     9 9 9 9 9 9 9 
     9 9 9 9 9 9 9 
     9 9 9 9 9 9 9 

     $
     ```
