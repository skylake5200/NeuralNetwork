# coding:utf-8
import tensorflow as tf

w = tf.Variable(tf.random_normal([2,3], stddev=2, mean=0, seed=1))

print w

print "\n"


with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	print w
	
