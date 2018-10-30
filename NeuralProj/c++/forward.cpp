# include "iostream"
# include "tools.h"
# include "cte_data.h"
# include "activef.h"
# include "stdlib.h"
# include "unistd.h" //sleep(int second)函数库
using namespace std;

int main(){
	
	// N为数据对个数
	int N = 100;
	// 产生数据N对数据
	cte_data();
	
	float data[N][2]; // 保存数据信息 x y 
	// 初始化两个权值
	float w1 = 0.2, w2 = 0.5, b = 0.2;
	// 设定一个阈值c
	float c = 0.7; 
	get_data(data);
	
	// 临时数组
	int val = 0; // 计数用的
	float arrtemp[N][2];		
	for (int k = 0; k < N; k++){
  		
		// 经过累加求和后的输出y
		// double y = tanh(data[k][0] * w1 + data[k][1] * w2 + b);
		double y = data[k][0] * w1 + data[k][1] * w2 + b;
		
	}
	return 0;
}
