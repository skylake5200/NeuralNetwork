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
	float data[N][2]; // 保存数据信息 体积v - 质量m
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
		if (y > c){
			
			cout << "第" << k + 1 << "件零件合格，其体积为" << data[k][0] << ", 质量为" << data[k][1] << endl;
			arrtemp[val][0] = data[k][0];
			arrtemp[val][1] = data[k][1];
			val++;
		}

		
    }
	// 将合格零件的信息保存到文件中, 第三列中保存y的值
	result_to_file(arrtemp, val);
	return 0;
}
