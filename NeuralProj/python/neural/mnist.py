# coding:utf-8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST数据集相关常数
INPUT_NODE = 784              # 输入层的节点数。对于MNIST数据集，这个就等于图片的像素
OUTPUT_NODE = 10              # 输出层的节点数，十分类

# 配置神经网络的参数
LAYER1_NODE = 500             # 隐藏层的节点数，在这里使用只有一个隐藏层的网络结构

BATCH_SIZE = 100              # 一个训练batch中的训练数据个数。数字越小时，训练过程越接近随机梯度下降；数字越大时，训练越接近梯度下降

LEARNING_RATE_BASE = 0.8      # 基础的学习率
LEARNING_RATE_DECAY = 0.99    # 学习率的衰减率

REGULARIZATION_RATE = 0.0001  # 描述模型复杂度的正则化项在损失函数中的系数
TRAINING_STEPS = 30000        # 训练轮数
MOVING_AVERAGE_DECAY = 0.99   # 滑动平均衰减率
 
