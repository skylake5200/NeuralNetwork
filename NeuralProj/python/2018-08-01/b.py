# coding:utf-8
import tensorflow as tf
import numpy as np
# 设损失函数 loss = (w + 1)^2，令w初始值为5,反向传播就是求最优w，即求最小loss对应的w值
# 动态学习率--基于指数衰减的学习率

LEARNING_RATE_BASE = 0.1 # 初始学习率
LEARNING_RATE_DECAY = 0.99 # 学习率衰减率
LEARNING_RATE_STEP = 1 # 喂入多少轮BATCH_SIZE后，更新一次学习率；一般设置为：总样本数 / BATCH_SIZE

# 定义待优化参数w初值赋为5
w = tf.Variable(tf.constant(5, dtype = tf.float32))


# 运行了多少轮BATCH_SIZE的计数器，初始值为0,设置为不可被训练
global_step = tf.Variable(0, trainable = False)

# 定义指数下降学习率

learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, LEARNING_RATE_STEP, LEARNING_RATE_DECAY, staircase = True)

# 定义损失函数
loss = tf.square(w + 1)

# 定义反向传播方法
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step = global_step)

# 生成会话

with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print "w is ", sess.run(w)
	
	for i in range(40):
		sess.run(train_step)
		w_val = sess.run(w)
		learning_rate_val = sess.run(learning_rate)
		loss_val = sess.run(loss)

		global_step_val = sess.run(global_step)
		print "在第 %s 轮迭代后： w 是 %f, 损失函数是 %f." % (i, w_val, loss_val)
		print "当前为第 %s 轮训练，当前学习率为 %f" % (global_step_val, learning_rate_val)


