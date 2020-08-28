#include <vector>
#include <string>
#include <iostream>

int main(void)
{
  /* int 型の可変長配列 */
  std::vector<int> v = {2, 3, 5};

  v.push_back(7);  // のびる
  v.push_back(11); // のびる
  v.push_back(13); // どこまでも
  for (int i = 0; i < v.size(); i++) { // .size()でサイズ取得
    std::cout << v.at(i) << " "; // .at()メソッド／[]演算子で参照
  }
  std::cout << std::endl;

  /* 空になるまで pop */
  while (!v.empty()) {
    std::cout << "poped " << v.back() << " -> ";
    v.pop_back();
  }
  std::cout << "empty!" << std::endl;
  
  /* string 型でも構造体でもクラスでも */
  std::vector<std::string> s = {"hoge", "huga", "piyo"};
  for (std::string e : s) {      // | 範囲ベース for 文
    std::cout << e << std::endl; // | を使ったアクセスの
  }                              // | 記述（eはelementの意）
  
  /* 2次元の可変長配列 */
  std::vector<std::vector<int> > vv(5, std::vector<int>(7, 9)); // 5x7の2次元配列
                                                                // を5で初期化
  // std::vector<std::vector<float>> vv(); 
  //                              ~~ コンパイラのバージョンによってはエラー
  for (std::vector<int> ve : vv) {
    for (int e : ve) {
      std::cout << e << " ";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
  
  return 0;
}
