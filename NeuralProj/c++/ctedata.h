# include <fstream>
# include <iostream>
# include <stdlib.h>
# include <stdio.h>
# include <time.h>
# include <iomanip>
using namespace std;
/**
	fstream 中定义了三个新的数据类型:
	type ofstream 文件写操作，用于创建文件并写入信息
	type ifstream 文件读操作，从存储设备读入到内存中
	type fstream  文件读写操作，对打开的文件可以进行读写操作，同时具有ofstream和instream两种功能
**/

// 这里的N是合格的零件数
void result_to_file(float (*data)[2], int N, const char* path = "./result.txt"){

	
	ofstream outfile;
	outfile.open(path);
	for (int i = 0; i < N; i++){
		
		// 将数据输出到文件中
		outfile << data[i][0] << " " << data[i][1] << endl;
	}
	outfile.close();

}

// 参数包括生成数据对个数N，精度的要求precision, 文件路径path
void cte_data(int N = 100, int precision = 2, const char* path = "./cpt_data.txt"){

	// 零件的体积v(0, 3) 以及质量m(0, 1) 作为衡量一个零件是否合格的标准
	// 文件中生成两列数据，第一列表示零件的体积，第二列表示零件的质量	
	ofstream outfile;
	outfile.open(path);
	// rand随机数每次执行时都是相同的，若要不同，需要动态更改seed
	srand((unsigned int) time(NULL));
	// 向文件写入数据 100行
	cout << "RAND_MAX = " << RAND_MAX << endl;
	// 结果保留两位小数
	for (int i = 1; i <= N; i ++){
		// 怎么会出现负数？ - 3 * rand()之后。超出了四个字节的最大长度，所以用负数来表示了
		// cout << "rand(" << i << ") = " << 3 * (rand() / (double) RAND_MAX) << endl;
		outfile << fixed << setprecision(precision) << 0 + 3 * (rand() / (double) RAND_MAX) << " " << rand() / (double) RAND_MAX << endl;
	}
	
	outfile.close();
}

// 将声明一个由2个指向float的指针组成的数组，函数的参数不能是数组
// 从函数中返回二维数组太复杂了，直接将数据指针作为参数传入即可
void get_data(float (*data)[2], int N = 100, const char* path = "./cpt_data.txt"){ // 从文本数据库中读取数据

	string str;
	float temp;
	ifstream infile;
	infile.open(path);

	// 创建二维数组，数组大小为 N * 2
	// float data[N][2];
	int j = 0;
	int flag = 1; //作为一个标志位
	int k;
	for (int i = 0; i < 2 * N; i++){
		// 这里读取的是每个word以空格分割
		infile >> str;
		temp = atof(str.c_str());
		// i是偶数的时候存储
		k = i / 2;	
		data[k][j] = temp;

		j++;
		if (j == 2) j = 0;		
	}
	infile.close();
}
