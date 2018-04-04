#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:24:48 2018

@author: yiwei
"""

for i in range(1,int(input())+1):
	s, k = input().split()
	k = int(k)
	neg_w = -1 * (k + 1)
	pos_w = 1
	s = map(lambda p: pos_w if p == '+' else neg_w, s)
	t = 0
	state = 0

	for p in s:
		if state > 0 and p < 0:
			state = p
		else:
			state += p

		if state == k * neg_w:
			t += 1
			state = 0
			continue

		if state == neg_w + pos_w * (k - 1) + neg_w:
			state = 0
			t += 2
			continue

		if state == neg_w + pos_w + neg_w:
			break

		if state == neg_w + pos_w * k:
			break

	if state < 0:
		t = 'IMPOSSIBLE'
	print('Case #{}: {}'.format(i, t))