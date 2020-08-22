#include <array>
#include <iostream>

int main(void)
{
  /* 1次元配列 */
  std::array<int, 4> a{1, 2, 3, 4};
  // std::array<int, 4> a{1, 2, 3, 4, 5}; // 初期化要素数によるエラー
  std::cout << "array size: " << a.size() << std::endl;
  std::cout << a[0] << " "  << a[1] << " "               // | 配列の要素
            << a[2] << " "  << a[3] << " " << std::endl; // | を出力する
  for (int i = 0; i < a.size(); i++) { // サイズ分だけ繰り返す
    std::cout << a.at(i) << " "; // .at() メソッドによるアクセス 
  }                                   
  std::cout << std::endl;
  for (auto itr = a.begin(); itr != a.end(); itr++) { // |
    std::cout << *itr << " ";                         // | イテレータによるアクセス
  }                                                   // | 
  std::cout << std::endl;
  for (auto& e : a) {      // | 
    std::cout << e << " "; // | 範囲 for 文による記述 
  }                        // | 
  std::cout << std::endl;
  
  std::array<int, 0> e; // 空の配列
  std::cout << "array e is empty: " << std::boolalpha << e.empty() << std::endl;

  /* 2次元配列 */
  std::array<std::array<double, 2>, 3> b;
  std::cout << "array size: " << b[0].size() << "x" << b.size() << std::endl;
  for (int i = 0; i < b.size(); i++) {
    b[i].fill(3.14); // すべての要素を 3.14 埋め
    for (int j = 0; j < b[i].size(); j++) {
      std::cout << b[i][j] << " ";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
    
  return 0;
}
