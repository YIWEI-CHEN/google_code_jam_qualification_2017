#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:24:48 2018

@author: yiwei
"""

for i in range(1,int(input())+1):
	s, k = input().split()
	k = int(k)
	t = 0
	for j in range(len(s) - k + 1):
		# print(s)
		if s[j] == '-':
			s = s[:j] + ''.join('-+'[p == '-'] for p in s[j: j + k]) + s[j + k:]
			t += 1
	if '-' in s:
		t = 'IMPOSSIBLE'
	print('Case #{}: {}'.format(i, t))