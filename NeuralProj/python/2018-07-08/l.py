# coding:utf-8
import tensorflow as tf

# 创建一个张量
a = 1
b = 2

c = tf.add(a,b)
print c

print "\n"

with tf.Session() as sess:
	
	print sess.run(c)
