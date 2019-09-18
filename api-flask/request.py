# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:58:45 2019

@author: utilisateur
"""
import requests

num = 10
r = requests.post('http://localhost:5000/your.number.' + str(num))
print(r.json())