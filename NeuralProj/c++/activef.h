# include <iostream>
# include <math.h>
using namespace std;

// 激活函数
float ReLU(float x) {
	  
	return x > 0 ? x : 0;
}

float sigmoid(float x) {
	
	return 1 / (1 + exp(-x));
}

float tanh(float x) {

	return (1 - (exp(-2 * x))) / (1 + exp(-2 * x));
}
