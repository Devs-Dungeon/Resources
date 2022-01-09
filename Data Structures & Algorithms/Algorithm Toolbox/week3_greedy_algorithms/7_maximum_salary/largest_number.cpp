#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

string largest_number(vector<string> a) {
  //write your code here
  std::stringstream ret;
	std::sort(a.begin(), a.end(), [](const string& a, const string& b) {
		return (a + b) < (b + a);
	});
	std::reverse(a.begin(), a.end());

	for (auto&& i : a) { ret << i; }
	string result;
	ret >> result;
  return result;
}

int main() {
  int n;
  std::cin >> n;
  vector<string> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  std::cout << largest_number(a);
}
