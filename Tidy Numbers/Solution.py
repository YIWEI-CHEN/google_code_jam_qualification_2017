#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:00:24 2018

@author: yiwei
"""

for c in range(1,int(input())+1):
	n = input()
	tidy = n
	
	while True:
		big = None
		for i in range(len(tidy) - 1):
			if tidy[i] > tidy[i + 1]:
				big = i
				break
		if big is None:
			break
		tidy = tidy[:big] + str(int(tidy[big]) - 1) + ''.join('9' for _ in tidy[big + 1: ])

	print('Case #{}: {}'.format(c, int(tidy)))