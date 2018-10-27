# coding:utf-8
import tensorflow as tf
import numpy as np

BATCH_SIZE = 8
SEED = 23455

write = tf.summary.FileWriter("/tmp/demo/1")
# 预测酸奶日销量。x1、x2是影响日销量的因素
# 建模前，应该先采集的数据有：每日x1、x2和销量y_（即已知答案，最佳情况：产量 = 销量）
# 拟构造数据集X，Y_：y_ = x1 + x2 噪声：-0.05 ～ +0.05 拟合可以预测销量的函数

rdm = np.random.RandomState(SEED)  # 返回的对象是什么呢？源码需要解析
X = rdm.rand(32,2)                 # 函数需要详细解析

# X数据已经生成
# 现在生成Y_数据
# rdm.rand() / 10 - 0.05 是将噪声限制在 -0.05 ～ +0.05之间
Y_ = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for (x1, x2) in X] #以这种方式生成Y_，有点看不懂 以前没见过



print "Y_ : \n", Y_
# 定义神经网络的输入、参数和输出，定义前向传播过程
x = tf.placeholder(tf.float32, shape = (None, 2))
y_ = tf.placeholder(tf.float32, shape = (None, 1))

# 这里随机生成的w1本质上和上面X Y_是否是一样的呢  第一个参数表示两行一列
w1 = tf.Variable(tf.random_normal([2,1], stddev = 1, seed = 1))
y = tf.matmul(x, w1)

# 定义损失函数及反向传播方法
# 定义损失函数为MES，反向传播方法为梯度下降法

loss_mse = tf.reduce_mean(tf.square(y_ - y))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss_mse)

# 生成会话，训练轮数为 STEPS
with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)

	STEPS = 20000

	for i in range(STEPS):
		
		start = (BATCH_SIZE * i) % 32
		end = start + BATCH_SIZE
		sess.run(train_step, feed_dict = {x : X[start : end], y_ : Y_[start : end]})

		if i % 500 == 0:
			print "在迭代%d轮后，w1的值为：\n" %(i)
			print sess.run(w1),"\n"
	print "最终w1为：\n", sess.run(w1)
write.add_graph(sess.graph)
