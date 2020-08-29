# コンテナクラス

- 共通のメソッド（の中でよく使いそうなやつ）
  - `bool empty(void)`: 空かどうかを判定
  - `size_t size(void)`: 要素数を取得
  - `void clear(void)`: コンテナを空にする
  - `iterator begin(void)`, `iterator end(void)`: イテレータを取得
    - ソートのときに使う（`<algolism>`ヘッダをインクルード）
    - `sort(v.begin(), v.end());`
  - `void insert(T)`: 要素を挿入
  - `void erase(T)`: 要素を削除

## 配列

### 固定長配列
- `<array>`ヘッダをインクルード
- 宣言と初期化
  ```cpp
  std::array<[型], [要素数]> a{...};
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
### 可変長配列
- `<vector>`ヘッダをインクルード
- 宣言
  ```cpp
  std::vector<[型やクラス]> v;
  std::vector<[型やクラス]> v([要素数]);
  std::vector<[型やクラス]> v([要素数], [初期値]);
  std::vector<std::vector<[型やクラス]> > v([行数], std::vector<[型やクラス]>, [列数]);
  ...
  ```
- メソッド
  - `void push_back(T)`: 末尾へ要素を追加 
  - `void resize(void)`: 要素数のリサイズ
  - などなど
- プログラム例
   - [ソースコード](src/vector.cpp)
   - 出力
     ```
     $ g++ -std=c++11 vector.cpp && ./a.out
     2 3 5 7 11 13 
     poped 13 -> poped 11 -> poped 7 -> poped 5 -> poped 3 -> poped 2 -> empty!
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

## 連想配列
- key→valueの対応を構築するデータ構造
- `<map>`ヘッダをインクルード
- 宣言
  `std::map<keyの型, valueの型> map;`
- プログラム例
   - [ソースコード](src/map.cpp)
   - 出力
     ```
     $ g++ -std=c++11 map.cpp && ./a.out
     ・ぎゅうにく を 2 個買います
     ・ぎゅうにゅう を 1 個買います
     ・さとう を 1 個買います
     ・しょうゆ を 1 個買います
     ・じゃがいも を 3 個買います
     ・にんじん を 2 個買います
     ぎゅうにゅう はいらないです
     ・ぎゅうにく を 2 個買います
     ・さとう を 1 個買います
     ・しょうゆ を 1 個買います
     ・じゃがいも を 3 個買います
     ・にんじん を 2 個買います
     ぎゅうにく を 2 個買いました
     さとう を 1 個買いました
     しょうゆ を 1 個買いました
     じゃがいも を 3 個買いました
     にんじん を 2 個買いました
     
     ```
