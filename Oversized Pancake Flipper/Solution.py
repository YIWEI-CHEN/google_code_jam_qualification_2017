#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:24:48 2018

@author: yiwei
"""

for i in range(1,int(input())+1):
	s, k = input().split()
	k = int(k)
	s = ''.join(map(lambda p: '0' if p == '+' else '1', s))
	s = int(s, 2)
	x = int('1' * k, 2)
	t = 0

	while s:
		s_len = len('{:b}'.format(s))
		if s_len - k < 0:
			t = 'IMPOSSIBLE'
			break
		s ^= x << (s_len - k)
		t += 1
	print('Case #{}: {}'.format(i, t))