#include <iostream>
#include <random>
#include <vector>
#include <tuple>

using namespace std;

/*double quantileA(double y)
{
    return 100 * y + 50;
}*/

extern "C" double quantileA(double);

double quantileB(double y)
{
    if (y <= 0.05) {
        return 1;
    }
    if (y <= 0.2) {
        return 2;
    }
    if (y <= 0.45) {
        return 3;
    }
    return 4;
}

int main()
{
    random_device rand_dev;
    mt19937 generator(rand_dev());
    uniform_real_distribution<double> dist(0, 1);

    const int N = 100000;

    vector<double> numbersA;
    vector<int> numbersB;

    for (int i = 0; i < N; i++) {
        numbersA.push_back(quantileA(dist(generator)));
        numbersB.push_back(quantileB(dist(generator)));
    }

    vector<tuple<double, double, int>> distributionA;
    vector<int> distributionB(4, 0);

    for (int i = 0; i < 10; i++) {
        distributionA.push_back(make_tuple(50 + 10 * i, 50 + 10 * (i + 1), 0));
    }

    for (double num : numbersA) {
        int i = (num - 50) / 10;
        get<2>(distributionA[i])++;
    }

    for (int num : numbersB) {
        distributionB[num-1]++;
    }

    for (auto dist : distributionA) {
        cout << get<0>(dist) << " - " << get<1>(dist) << ": " << get<2>(dist) << endl;
    }

    for (int i = 0; i < 4; i++) {
        cout << i + 1 << ": " << distributionB[i] << endl;
    }
}
