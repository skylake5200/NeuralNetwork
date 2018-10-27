# coding:utf-8
import pickle

files = open("data.dat","rb")
data_save = pickle.load(files)
files.close()

print data_save

