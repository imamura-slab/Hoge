#include <iostream>

using namespace std;

class Hoge
{
private:
  const char *str;
  
public:
  Hoge() { cout << "だが断る" << endl; }         // ユーザ定義のコンストラクタ
  Hoge(const char *str) { cout << str << endl; } // コンストラクタのオーバーロード

  /* 演算子 + のオーバーロード */
  char* operator+(Hoge rhs)
  {
    return "ナニッ！？"; // 引数使え警告でるけど無視
  } 
};

int main(void)
{
  Hoge hoge1;
  Hoge hoge2("でも断る");
  cout << hoge1 + hoge2 << endl; // Hogeクラス + Hogeクラス
  return 0;
}
