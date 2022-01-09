#include <bits/stdc++.h>

using namespace std;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here
    int numRefill = 0, currRefill = 0;
    int n = stops.size();
    if(stops[0]>tank)
        return -1;
    else
        numRefill = 1;
    while(currRefill<n-1)
    {
        int lastRefill = currRefill;
        while(currRefill < n-1 && (stops[currRefill+1] - stops[lastRefill])<=tank){
            currRefill++;
        }
        if(currRefill == lastRefill)
            return -1;
        if(stops[currRefill]<=dist)
            numRefill++;
    }
    numRefill -= 1;
    return numRefill;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n+1);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);
    stops[n] = d;
    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
