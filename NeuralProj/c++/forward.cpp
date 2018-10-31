# include "iostream"
# include "tools.h"
# include "cte_data.h"
# include "activef.h"
# include "stdlib.h"
# include "unistd.h" //sleep(int second)函数库

# define INPUT_SIZE 2    // 输入节点数
# define HIDE_SIZE 3     // 隐藏层节点数
# define OUTPUT_SIZE 1   // 输出层节点数

# define LEARNING_RATE 0.01 // 学习率
using namespace std;


int main(){
	
	// N为数据对个数
	int N = 100;
	// 产生数据N对数据
	cte_data();
	
	float data[N][2]; // 保存从文件中读取的数据信息 x y 
	// 初始化两组权值和一个偏置（这里最好写一个数组保存）
	float W1[2][3];	
	init_W(*W1, 2, 3);
	cout << "初始W1矩阵为：\n";
	print (&W1[0][0], 2, 3);
		
	float W2[3][2];
	init_W(*W2, 3, 1);
	cout << "初始W2矩阵为：\n";
	print (&W2[0][0], 3, 2);	
	
	// 将数据从文本中读取到二维数组data中
	get_data(data);

	float y_[N][2];
	// 正确输出的集合y_为二维数组
	for (int i = 0; i < N; i++) {
		
		int x = data[i][0], y = data[i][1];
		if ((x <= 5 && y <= 5) || (x >= 5 && y >= 5) ) {
			
			y_[i][0] = 0;
			y_[i][1] = 1;

		}else{
			y_[i][0] = 1;
			y_[i][1] = 0;
		}
	}
	cout << "正确答案：\n" ;
	print (&y_[0][0], N, 2);		

	float *A, *y;
	A = matmul(data[0], *W1, 2, 3);
	y = matmul(A, *W2, 3, 2);

	
	cout << y[0] << " " << y[1] << endl;
	return 0;
}
