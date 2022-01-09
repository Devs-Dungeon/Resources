#include <math.h>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

constexpr double distance(const pair<long long, long long>& a,
						  const pair<long long, long long>& b) {
	return sqrt((b.first - a.first) * (b.first - a.first) +
				(b.second - a.second) * (b.second - a.second));
}

double naive_minimal_distance(vector<pair<long long, long long>>& points) {
	double d = numeric_limits<double>::max();
	for (long long i = 0; i < points.size() - 1; i++) {
		for (long long j = i + 1; j < points.size(); j++) {
			d = min(d, distance(points[i], points[j]));
		}
	}
	return d;
}

bool less_than_on_x(pair<long long, long long>& a,
					pair<long long, long long>& b) {
	return (a.first == b.first) ? (a.second < b.second) : (a.first < b.first);
}

bool less_than_on_y(pair<long long, long long>& a,
					pair<long long, long long>& b) {
	return (a.second == b.second) ? (a.first < b.first) : (a.second < b.second);
}

void merge(vector<pair<long long, long long>>& points, long long low,
		   long long high) {
	if (low >= high) return;

	long long mid = low + (high - low) / 2;
	long long i = low, j = mid + 1;
	vector<pair<long long, long long>> vec;
	vec.reserve(high - low + 1);

	while (i <= mid and j <= high) {
		if (less_than_on_y(points[i], points[j])) {
			vec.emplace_back(points[i].first, points[i].second);
			i++;
		} else {
			vec.emplace_back(points[j].first, points[j].second);
			j++;
		}
	}
	while (i <= mid) {
		vec.emplace_back(points[i].first, points[i].second);
		i++;
	}
	while (j <= high) {
		vec.emplace_back(points[j].first, points[j].second);
		j++;
	}

	for (size_t k = 0; k < vec.size(); k++) { points[low + k] = vec.at(k); }
}

double minimal_distance(vector<pair<long long, long long>>& points,
						long long low, long long high) {
	if (low >= high) return numeric_limits<double>::max();
	if (high - low == 1) {
		if (not less_than_on_y(points[low], points[high])) {
			swap(points[low], points[high]);
		}
		return distance(points[low], points[high]);
	}

	long long mid = low + (high - low) / 2;
	auto mid_point = points.at(mid);  // This is important

	double d = min(minimal_distance(points, low, mid),
				   minimal_distance(points, mid + 1, high));

	vector<pair<long long, long long>> strip_points;

	merge(points, low, high);
	for (long long i = low; i <= high; i++) {
		if (abs(points[i].first - mid_point.first) <= d) {
			strip_points.emplace_back(points[i].first, points[i].second);
		}
	}

	for (long long i = 0; i < strip_points.size() - 1; i++) {
		for (long long j = i + 1; j < strip_points.size() and j - i < 8; j++) {
			d = min(d, distance(strip_points[i], strip_points[j]));
		}
	}
	return d;
}

int main() {
	size_t n;
	cin >> n;
	vector<pair<long long, long long>> points(n);
	long long x, y;
	for (size_t i = 0; i < n; i++) {
		cin >> x >> y;
		points[i] = make_pair(x, y);
	}
	sort(points.begin(), points.end(), &less_than_on_x);

	cout << fixed;
	cout << setprecision(9) << minimal_distance(points, 0, points.size() - 1)
		 << endl;
}
