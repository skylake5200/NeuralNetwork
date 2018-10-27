# coding:utf-8
import tensorflow as tf

a = tf.constant([[1.0,2.0]]) # 1行两列
b = tf.constant([[3.0],[4.0]]) # 2行一列
result = tf.matmul(a,b)
print result

with tf.Session() as sess:
	print sess.run(result)
