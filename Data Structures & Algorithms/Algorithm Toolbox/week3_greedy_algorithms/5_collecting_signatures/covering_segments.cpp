#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
  int start, end;
};

vector<int> optimal_points(vector<Segment> &segments) {
  vector<int> points;
  std::sort(segments.begin(), segments.end(),
			  [](const Segment& a, const Segment& b) { return a.end < b.end; });
	vector<bool> covered(segments.size(), false);
	int point = -1;
	int j = 0;
	for (size_t i = 0; i < segments.size(); ++i) {
		if (not covered[i]) {
			point = segments[i].end;
			points.push_back(point);
			covered[i] = true;
			j = i + 1;
			while (j < segments.size() and
				   (segments[j].start <= point and segments[j].end >= point)) {
				covered[j] = true;
				j++;
			}
		}
	}
  return points;
}

int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
