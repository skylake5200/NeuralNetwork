# coding:utf-8
import pickle

dic = {"name":"张三",1:110,2:"skylake"}
files = open("data.dat","wb")
pickle.dump(dic,files)
files.close()
