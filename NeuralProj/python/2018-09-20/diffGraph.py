# coding:utf-8
import tensorflow as tf

a = tf.constant([2., 3.], name = "a")
print (a.graph is tf.get_default_graph())
