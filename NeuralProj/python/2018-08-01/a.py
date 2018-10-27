# coding:utf-8
import tensorflow as tf
import numpy as np
# 设损失函数 loss = (w + 1)^2，令w初始值为5,反向传播就是求最优w，即求最小loss对应的w值

# 定义待优化参数w初值赋为5
w = tf.Variable(tf.constant(5, dtype = tf.float32))

a = tf.constant(6, dtype = tf.float32)

# 定义损失函数
loss = tf.square(w + 1)

# 定义反向传播方法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

# 生成会话

with tf.Session() as sess:
	
	print "a is ", sess.run(a) 
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print "w is ", sess.run(w)
	
	for i in range(40):
		sess.run(train_step)
		w_val = sess.run(w)
		loss_val = sess.run(loss)
		print "在第 %s 轮迭代后： w 是 %f, 损失函数是 %f." % (i, w_val, loss_val)


