#include <iostream>
#include <random>
#include <map>
using namespace std;
/*
1. 
Wygenerowac rzeczywiste <50,150>
10 podprzedzialow
2.  P(1)=0,1
    P(2)=0,2
    P(3)=0,3
    P(4)=0,4
*/
extern "C" double transform(double);

/*double transform_a(double n) {
    return n * 100 + 50;
}*/

int transform_b(double n) {
    if (n < 0.1)
        return 1;
    if (n < 0.3)
        return 2;
    if (n < 0.6)
        return 3;
    return 4;
}

int main()
{
    random_device rd;
    default_random_engine rng(rd());
    uniform_real_distribution<double> gen(0.0, 1.0);
    vector<double> arr;
    map<pair<double, double>, int> count;

    for (int i = 0; i < 100000; i++) {
        double num = gen(rng);
        double proc = transform(num);
        arr.push_back(proc);
    }
    for (int level = 0; level < 10; level++) {
        pair<double, double> range = make_pair(50 + (10 * level), 50 + (10 * level) + 10);
        count[range] = 0;
    }
    for (double n : arr) {
        for (int i = 0; i < 10; i++) {
            pair<double, double> range = make_pair(50 + (10 * i), 50 + (10 * i) + 10);
            if (n >= range.first && n <= range.second) {
                count[range]++;
                break;
            }
        }
    }
    for (int i = 0; i < 10; i++) {
        pair<double, double> range = make_pair(50 + (10 * i), 50 + (10 * i) + 10);
        cout << "(" << range.first << ", " << range.second << "): " << count[range]<<endl;
    }
    cout << endl;
    arr.clear();
    int count2[4] = { 0,0,0,0 };
    for (int i = 0; i < 100000; i++) {
        double num = gen(rng);
        arr.push_back(transform_b(num));
        count2[transform_b(num) - 1]++;
    }
    for (int i = 0; i < 4; i++)
        cout << i+1 << ": " << count2[i]<<endl;
    return 0;
}
