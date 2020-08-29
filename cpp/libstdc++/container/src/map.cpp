#include <map>
#include <string>
#include <cassert>
#include <iostream>

int main(void)
{
  /* 文字列を key，int を value とする連想配列 */
  std::map<std::string, int> memo;

  /* 〆(._.)ﾒﾓﾒﾓ */
  memo["ぎゅうにく"] = 2;
  memo["じゃがいも"] = 3;
  memo["にんじん"] = 2;
  memo["ぎゅうにゅう"] = 1;
  memo["しょうゆ"] = 1;
  memo["さとう"] = 1;
  for (const auto& e : memo) {
    std::cout << "・"
              << e.first << " を "         // key を first で取得
              << e.second << " 個買います" // value を second で得取
              << std::endl;
  }
  
  /* データの削除 */
  std::cout << "ぎゅうにゅう はいらないです" << std::endl;
  memo.erase("ぎゅうにゅう");
  for (const auto& e : memo) {
    std::cout << "・"
              << e.first << " を "         // key を first で取得
              << e.second << " 個買います" // value を second で得取
              << std::endl;
  }

  /* おかいもの */
  for (const auto& e : memo) {
    std::cout << e.first << " を "         
              << e.second << " 個買いました" 
              << std::endl;
    memo.erase(e.first); // 買ったものはメモから削除
  }
  std::cout << std::endl;
  assert(memo.empty()); // ぜんぶ買ったハズ
  
  return 0;
}
