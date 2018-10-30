# include <iostream>
# include "time.h"
# include "stdio.h"
# include "stdlib.h"
using namespace std;
int max(int x, int y){

	return x > y ? x : y;
}
// 返回 0 - 1之间的随机数，保留两位小数
float _01_rand() {
	
	// N可以确定产生的精度，比如需要两位小数，N = 99，三位小数 N = 999
	int N = 99;
	// 初始化rand()的起始值(程序调用速度过快的时候，产生的随机数是一样的)
	srand((unsigned) time(0));

	return rand() % (N + 1) / (float) (N + 1);
}

void softmax(float *arr_y) {

	



}
// 交叉熵
void cross_entropy() {



}
