# include <iostream>
# include "time.h"
# include "stdio.h"
# include "stdlib.h"
# include "math.h"
# include "unistd.h"
# include "activef.h"
using namespace std;
// 函数声明
float _01_rand();
void print (float *arr, int row, int column);
void init_W (float *W, int row, int column);
float *matmul (float *InPut, float *W, int row, int column);



// 打印数组
void print (float *arr, int row, int column) {
	printf("[\n");
	 for (int i = 0; i < row; i++) {

                for (int j = 0; j < column; j++) {

                        cout << *(arr + column * i + j) << " ";
                }
		cout << endl;
        }
	printf("]\n");
}
// 初始化权重,数组是顺序存储的，二维数组也是
void init_W (float *W, int row, int column) {

	for (int i = 0; i < row; i++) {

		for (int j = 0; j < column; j++) {

			*(W + column * i + j) = _01_rand();
		}
	} 
}

// 简单模拟矩阵乘法，这里是用两个二维数组相乘，返回一个数值
/**
	InPut [0.2 0.3] 1 x 2

	W1 [ 
     		0.1 0.3 0.5
     		0.2 0.5 0.6
   	]  2 x 3

	result = 1 x 3

	[x1 x2 x3]

	W2 [
     		0.6 0.2
     		0.1 0.1
     		0.9 0.4
   	] 3 x 2

	y = 1 x 2
**/
float *matmul (float *InPut, float *W, int row, int column) {
	
	float *arr = (float *) malloc(sizeof(float) * column);
	float sum = 0.0;
	for (int i = 0; i < column; i++) {
		
		for (int j = 0; j < row; j++) {
		
			sum += *(W + column * j) * InPut[j];

		}
		// 将输出结果经过激活函数
		arr[i] = sigmoid(sum);
	}
	return arr;
}


int max (int x, int y){

	return x > y ? x : y;
}
// 返回 0 - 1之间的随机数，保留两位小数
float _01_rand() {
	
	// N可以确定产生的精度，比如需要两位小数，N = 99，三位小数 N = 999
	int N = 99;
	// 初始化rand()的起始值(程序调用速度过快的时候，产生的随机数是一样的)
	// srand(time(NULL));
	return rand() % (N + 1) / (float) (N + 1);
}

float* softmax (float *arr_y, int N = 100) {
	
	static float arr_temp[100];
	float sum = 0.0;
	
	for (int i = 0; i < N; i++) {
		
		sum += exp(arr_y[i]);	

	}
	for (int j = 0; j < N; j++) {
		
		arr_temp[j] = arr_y[j] / sum; 

	}
	
	return arr_temp;
}
// 交叉熵
void cross_entropy() {



}
