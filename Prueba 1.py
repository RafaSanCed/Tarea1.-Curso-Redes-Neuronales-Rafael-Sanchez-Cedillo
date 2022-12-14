# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:36:35 2022

@author: rafae
"""

import mnist_loader
import network_SGD_fric
import pickle
import network
import network_tanh

training_data, validation_data , test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)
test_data = list(test_data)
net=network_SGD_fric.Network([784,30,10])
net.SGD_fric( training_data, 100, 10, 0.5, 0.0001, test_data=test_data)
archivo = open("red_prueba1.pkl",'wb')
pickle.dump(net,archivo)
archivo.close()