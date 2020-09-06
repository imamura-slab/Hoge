#include <iostream>

using namespace std;

// 複素数クラス
class Complex {
  private:
    double re;
    double im;
    friend Complex operator+(Complex c1, Complex c2);     // +演算子のオーバーロードをフレンド関数に登録
    friend ostream &operator<<(ostream &os, Complex c);   // <<演算子のオーバーロードをフレンド関数に登録
  public:
    Complex() {}
    Complex(double real, double imag) {
      re = real;
      im = imag;
    }
};

Complex operator+(Complex c1, Complex c2) {               // フレンド関数に登録しているので, Complex型のreやimにアクセス可能
  Complex result;
  result.re = c1.re + c2.re;
  result.im = c1.im + c2.im;
  return result;
}

ostream &operator<<(ostream &os, Complex c) {             // 第1引数は演算子の左側, 第2引数は演算子の右側に対応
                                                          // つまり, ostream型 << Complex型 となるような演算子<<を定義
  cout << "(" << c.re << ", " << c.im << "i)" << endl;
  return os;
}

int main() {
  Complex c1(2, 3);
  Complex c2(4, 5);

  Complex c3;
  c3 = c1 + c2;

  cout << c3;

  return 0;
}
