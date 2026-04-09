#include <iostream>
#include <random>
#include <ctime>
using namespace std;
extern __stdcall float random(float x);

int main(){
	default_random_engine generator(time(NULL));
	uniform_real_distribution<double> distribution(0.0,1.0);
	double x = distribution(generator);
	float to_asm = x;
	cout << "Random number: " << to_asm << endl;
	cout << "Random number from asm: " << random(to_asm) << endl;
}