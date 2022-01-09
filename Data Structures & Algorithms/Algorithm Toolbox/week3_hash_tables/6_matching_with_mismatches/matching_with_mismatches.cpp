#include <iostream>
#include <vector>

using namespace std;

vector<int> solve(int k, const string &text, const string &pattern) {
	vector<int> pos;
	return pos;
}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(0);
	int k;
	string t, p;
	while (cin >> k >> t >> p) {
		auto a = solve(k, t, p);
		cout << a.size();
		for (int x : a)
			cout << " " << x;
		cout << "\n";
	}
}
