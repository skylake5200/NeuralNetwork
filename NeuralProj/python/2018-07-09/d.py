# coding:utf-8
# 生产一批零件将体积x1和重量x2作为特征输入到NN，通过NN后输出一个值
import tensorflow as tf

# 定义输入变量
X = tf.constant([[0.7,0.5]])
w1 = tf.Variable(tf.random_normal([2,3], stddev = 1, seed = 1))
w2 = tf.Variable(tf.random_normal([3,1], stddev = 1, seed = 1))

a = tf.matmul(X, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
	
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print sess.run(y)

