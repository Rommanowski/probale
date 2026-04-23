#include <iostream>
#include <random>
#include <map>
using namespace std;

pair<int, int> generate(uniform_real_distribution<double>& gen, default_random_engine& rng) {
    double x = gen(rng);

    pair<int, int> result;
    if (x < 0.5)
        result.first = 1;
    else if (x < 0.7)
        result.first = 2;
    else if (x < 0.9)
        result.first = 3;
    else
        result.first = 4;

    if (result.first == 1) {
        double y = gen(rng);
        if (y < 0.2)
            result.second = 1;
        else
            result.second = 4;
    }
    else if (result.first == 2) {
        result.second = 1;
    }
    else if (result.first == 3) {
        double y = gen(rng);
        if (y < 0.5)
            result.second = 2;
        else
            result.second = 4;
    }
    else {
        result.second = 3;
    }
    return result;
}

int main()
{
    random_device rd;
    default_random_engine rng(rd());
    uniform_real_distribution<double> gen(0.0, 1.0);

    int stats[4][4]{};
    for (int i = 0; i < 100000; i++) {
        pair<int, int>xy = generate(gen, rng);
        stats[xy.first - 1][xy.second - 1]++;
    }
    cout << "XY>\t1\t2\t3\t4\n";
    for (int x = 0; x < 4; x++) {
        cout << x + 1 << "  \t";
        for (int y = 0; y < 4; y++) {
            cout << stats[x][y] << "\t";
        }
        cout << endl;
    }
    return 0;
}

