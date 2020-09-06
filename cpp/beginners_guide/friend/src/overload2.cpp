#include <iostream>

using namespace std;

class Point {
  private:
    double x;
    double y;
    friend ostream &operator<<(ostream &os, Point p);
  public:
    Point(double x_coord, double y_coord) {
      x = x_coord;
      y = y_coord;
    }
};

ostream &operator<<(ostream &os, Point p) {
  cout << "(" << p.x << ", " << p.y << ")";
  return os;
}

int main() {
  Point p = Point(2, 3);
  cout << p << endl;
  
  return 0;
}

