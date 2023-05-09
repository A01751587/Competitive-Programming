#include <bits/stdc++.h>

using namespace std;

vector<long long> pascal(int n)
{
    if (n == 1) {
        return vector<long long> {1, 1};
    }
    auto rec = pascal(n - 1);
    vector<long long> result = {1};
    result.reserve(rec.size() + 1);
    //result.reserve(n + 1);
    for (int i = 0; i < rec.size() - 1; i++) {
        result.push_back(rec[i] + rec[i + 1]);
    }
    result.push_back(1);
    return result;

}

int main()
{
    int n;

    cin >> n;

    if (n == 0) {
        cout << "1";
        return 0;
    }

    auto v = pascal(n);
    // for (int x : v) {
    //     cout << x << " ";
    // }
    // cout << "\n";

    auto first_time = true;

    for(int i = 0; i <= n; ++i) {
        if (first_time) {
            first_time = false;
        } else {
            cout << "+";
        }
        auto px = n - i;
        auto py = i;
        if (v[i] != 1) {
            cout << v[i];
        }
        //x
        if (px == 1) {
            cout << "x";
        } else if (px > 1) {
            cout << "x^" << px;
        }
        //y
        if (py == 1) {
            cout << "y";
        } else if (py > 1) {
            cout << "y^" << py;
        }
    }

    return 0;
}