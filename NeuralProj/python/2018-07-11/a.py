# coding:utf-8
# 生产一批零件将体积x1和重量x2作为特征输入到NN，通过NN后输出一个值
import tensorflow as tf

# 导入模块生成数据集
import numpy as np
BATCH_SIZE = 8 # 表示一次喂入神经网络多少组值，这个值不能太大
seed = 23455 #  seed值确定后，生成的随机数便确定

# 基于seed产生随机数 
rng = np.random.RandomState(seed)

print "rng is : \n",rng

# 随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入数据集
X_Set = rng.rand(32, 2)

# 从X这个32行2列的矩阵中 取出一行 判断如果和小于1 给Y赋值1 否则赋值0
# 作为输入数据集标签（即正确答案）
# 因为我手头没有数据集，只能虚拟一些数据进行训练
Y = [[int(x0 + x1 < 1)] for (x0, x1) in X_Set]

print "X_Set:\n",X_Set
print "Y:\n",Y


# 定义神经网络的输入变量
# X = tf.constant([[0.7,0.5]])
X = tf.placeholder(tf.float32, shape = (None, 2))
y_ = tf.placeholder(tf.float32, shape = (None, 1))


w1 = tf.Variable(tf.random_normal([2,3], stddev = 1, seed = 1))
w2 = tf.Variable(tf.random_normal([3,1], stddev = 1, seed = 1))

a = tf.matmul(X, w1)
y = tf.matmul(a, w2)


# 定义损失函数以及反向传播方法
# 使用均方误差作为损失函数，类似于蚁群算法中的信息素浓度函数，粒子群中的适应度函数
# loss实际上是什么呢
loss = tf.reduce_mean(tf.square(y - y_))
# train_step是什么呢
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
# train_step = tf.train.MomentumOptimizer(0.001, 0.9).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

with tf.Session() as sess:
	# 对所有已定义的变量和图表进行初始化？有什么用呢？	
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	# 输出未经训练的参数取值
	print "w1:\n", sess.run(w1)
	print "\n"
	print "w2:\n", sess.run(w2)

	# 训练模型
	STEPS = 3000
	
	for i in range(STEPS):
		start = (i * BATCH_SIZE) % 32
		end = start + BATCH_SIZE
		
		if i == 0 :
			print "start = ", start, "\n"
			print "end = ", end, "\n"
		# 在运行过程中添加数据---如何去理解呢？
		sess.run(train_step, feed_dict = {X : X_Set[start: end], y_ : Y[start: end]})
		if i % 500 == 0:
			total_loss = sess.run(loss, feed_dict = {X : X_Set, y_ : Y})
			print("在第 %d 步训练后，损失函数值为 %g" % (i, total_loss))
	# 输出训练后的参数取值
	print "\n"
	
	print "w1:\n", sess.run(w1)
	print "w2:\n", sess.run(w2)

