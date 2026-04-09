#include <iostream>
#include <vector>
#include <numeric>

extern "C" double change_val(double);

int main() {
    srand(time(NULL));
    double a = ((double) rand() / (RAND_MAX));
    std::cout << a << std::endl;

    std::cout << "\nExc 1:" << std::endl;
    std::cout << change_val(a) << std::endl;

    std::cout << "\nExc 2:" << std::endl;
    std::vector<double> probs = {0.1, 0.25, 0.25, 0.4};
    std::vector<double> sums(probs.size());
    std::partial_sum(probs.begin(), probs.end(), sums.begin());

    int chosen_val = -1;
    for(size_t i=0; i<sums.size(); ++i) {
        if(a < sums[i]) {
            chosen_val = i;
            break;
        }
    }

    std::cout << chosen_val << std::endl;

    return 0;
}