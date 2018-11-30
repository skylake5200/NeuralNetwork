# include "iostream"
# include "tools.h"
# include "cte_data.h"
# include "stdlib.h"
# include "unistd.h" //sleep(int second)函数库

# define INPUT_SIZE 2    // 输入节点数
# define HIDE_SIZE 3     // 隐藏层节点数
<<<<<<< HEAD
# define HIDE_NUM 1      // 隐藏层数
# define OUTPUT_SIZE 1   // 输出层节点数

=======
# define OUTPUT_SIZE 2   // 输出层节点数
>>>>>>> 80211dca5a9cc91d048be63372d44dccc835c967
# define LEARNING_RATE 0.01 // 学习率
using namespace std;

// 我不能实现自动的函数求导，所以我的BP算法是针对特定的网络结构以及特定的损失函数来优化权值的
// 损失函数选择 loss = 1/2 * [(y1 - y1_)^2 + (y2 - y2_)^2]
void BP(float *y, float *y_, float *A, float *W1, float *W2, float *X){

	// 首先优化第二层的权重
	// (y1 - y1_) * (y1 - y1 ^ 2)
	int hs, os, is;
	for (hs = 0; hs < HIDE_SIZE; hs++){

		for (os = 0; os < OUTPUT_SIZE; os++){

			float shared = (y[os] - y_[os]) * (y[os] - y[os] * y[os]);
			*(W2 + 2 * hs + os) = *(W2 + 2 * hs + os) - shared * A[hs] * LEARNING_RATE;
		}
	}
	// 再更新前一层的权重
	for (is = 0; is < INPUT_SIZE; is++){

		for (hs = 0; hs < HIDE_SIZE; hs++){
			
			float shared1 = (y[0] - y_[0]) * (y[0] - y[0] * y[0]);
			float shared2 = (y[1] - y_[1]) * (y[1] - y[1] * y[1]);
			float shared3 = (A[hs] - A[hs] * A[hs]) * X[is];
			*(W1 + HIDE_SIZE * is + hs) = *(W1 + HIDE_SIZE * is + hs) - ((shared1 * *(W2 + OUTPUT_SIZE * hs) + shared2 * *(W2 + OUTPUT_SIZE * hs + 1)) * shared3) * LEARNING_RATE;

		}
	}
}
int main(int argc, char** argv){
	
	// N为数据对个数
	int N = 1000;
	// 产生数据N对数据
	// void cte_data(int N = 100, int precision = 2, const char* path = "./cpt_data.txt")
	// cte_data(N);
	
	float data[N][2]; // 保存从文件中读取的数据信息 x y 
	// 初始化两组权值和一个偏置（这里最好写一个数组保存）
	float W1[INPUT_SIZE][HIDE_SIZE]; // = {{2.0, 5.0, 8.0}, {3.0, 1.0, 6.0}};	
	init_W(*W1, INPUT_SIZE, HIDE_SIZE);
	cout << "初始W1矩阵为：\n";
	print (&W1[0][0], INPUT_SIZE, HIDE_SIZE);
		
<<<<<<< HEAD
	float W2[3][2];
	init_W(*W2, 3, 2);
=======
	float W2[HIDE_SIZE][OUTPUT_SIZE]; // = {{5.0, 1.0}, {8.0, 3.0}, {4.0, 6.0}};
	init_W(*W2, HIDE_SIZE, OUTPUT_SIZE);
>>>>>>> 80211dca5a9cc91d048be63372d44dccc835c967
	cout << "初始W2矩阵为：\n";
	print (&W2[0][0], HIDE_SIZE, OUTPUT_SIZE);	
	
	// 将数据从文本中读取到二维数组data中
	// void get_data(float (*data)[2], int N = 100, const char* path = "./cpt_data.txt")
	get_data(data, N);

	// y_中保存正确的输出结果，我希望完成的是  通过给定的结果来训练权值，实现异或运算
	float y_[N][2];
	// 正确输出的集合y_为二维数组
	for (int i = 0; i < N; i++) {
		
		float x = data[i][0], y = data[i][1];
		if ((x <= 5 && y <= 5) || (x >= 5 && y >= 5) ) {
			
			y_[i][0] = 0.75;
			y_[i][1] = 0.75;

		}else{
			y_[i][0] = 0.25;
			y_[i][1] = 0.25;
		}
	}
<<<<<<< HEAD
			

	// A为中间层输出向量，Y为输出向量
	float *A, *y, *Y;

	// 最大训练轮数
	int max_iter = 1;
	// 训练 Just Do It!
	for (int iter = 0; iter < max_iter; iter++) {
			
		for (int i = 0; i < N; i++) {

			A = matmul(data[0], *W1, 2, 3); // A为隐藏层的输出向量,在此进行保存
        	        y = matmul(A, *W2, 3, 2); // y为输出层的向量
	                Y = softmax(y);

			// 更新权重
			for (int j = 0; j < HIDE_NUM; j++) {
				
				
				

			}

		}	
	}
	
=======
	/**
	float *A, *y;
	A = matmul(data[0], *W1, INPUT_SIZE, HIDE_SIZE);
	y = matmul(A, *W2, HIDE_SIZE, OUTPUT_SIZE);
	cout << "输出A和y的值：" << endl;
	print (A, 1, 3);
	print (y, 1, 2);
	*/

	// 循环迭代1000次
	int iters = 20000;
	float *A, *y;
	for (int iter = 0; iter < iters; iter++){
		for (int i = 0; i < N; i++){

			A = matmul(data[i], *W1, INPUT_SIZE, HIDE_SIZE);
       			y = matmul(A, *W2, HIDE_SIZE, OUTPUT_SIZE);
			// 方向传播，优化权重
			BP(y, y_[i], A, *W1, *W2, data[i]);
		}
	}
	cout << "更新后的权值矩阵W1" << endl;
	print (&W1[0][0], 2, 3);

	cout << "更新后的权值矩阵W2" << endl;
	print (&W2[0][0], 3, 2);

	float T[] = {2.5, 7.5};
	A = matmul(T, *W1, 2, 3);
	y = matmul(A, *W2, 3, 2);
	cout << "输出最终结果[" << y[0] << ", " << y[1] << "]" << endl;
	

	/**
	测试结果为：数据集没有问题
	int k = 0;
	cout << "数据集测试：" << endl;
	for (int i = 0; i < N; i++){

		
		if ((data[i][0] <= 5 && data[i][1] <= 5) || (data[i][0] >= 5 && data[i][1] >= 5)){
			k++;
			cout << "第" << k << "个" << " " << y_[i][0] << " " << y_[i][1] << endl;
		}
	
	}*/
>>>>>>> 80211dca5a9cc91d048be63372d44dccc835c967
	return 0;
}
