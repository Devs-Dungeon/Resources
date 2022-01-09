#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;

vector< int > partition3(vector<int> &a, int l, int r) {
  int x = a[l];
  int lt = l;
  int gt = r;
  int i = l;
  while (i <= gt)
  {
    if (a[i] < x)
    {
      swap(a[i], a[lt]);
      lt++;
      i++;
    }
    else if (a[i] > x)
    {
      swap(a[i], a[gt]);
      gt--;
    }
    else
    {
      i++;
    }
  }

  return vector<int>{lt, gt};
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  vector< int > num = partition3(a, l, r);

  randomized_quick_sort(a, l, num[0] - 1);
  randomized_quick_sort(a, num[1] + 1, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
}
