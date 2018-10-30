# include <iostream>
# include <math.h>
using namespace std;

// 激活函数
double ReLU(double x) {
	  
	return x > 0 ? x : 0;
}

double sigmoid(double x) {
	
	return 1 / (1 + exp(-x));
}

double tanh(double x) {

	return (1 - (exp(-2 * x))) / (1 + exp(-2 * x));
}
