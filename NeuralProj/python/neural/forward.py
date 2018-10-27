# -*-coding:utf-8-*-
import tensorflow as tf
import numpy as np

# 我想要给定一批零件的长度l和质量v来确定该零件是否合格
# 我们将零件的长度l和质量v作为每个零件的特征向量
# 并设置一个阈值，如果输出结果大于这个阈值的话，则合格，否则不合格
# 随机生成一组数据

# 初始化第一层和第二层的连接权重
# w这些参数初始时一般都是随机给定的

# normal是正态分布，标准差为1,name属性有什么用呢？
w1 = tf.Variable(tf.random_normal([2,3], stddev = 1, seed = 1), name = "w1")
w2 = tf.Variable(tf.random_normal([3,1], stddev = 1, seed = 1), name = "w2")

# 偏置 有什么用？
# 定义一个输入变量
x = tf.constant([[0.7, 0.9]])

# 定义前向传播
# tf.matmul只能进行矩阵之间的相乘，而不能进行矩阵和向量之间的乘法
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
	# 初始化所有的变量
	init_op = tf.global_variables_initializer()
	
	sess.run(init_op)
	print float(sess.run(y))













