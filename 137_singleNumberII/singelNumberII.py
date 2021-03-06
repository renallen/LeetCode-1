"""
Single Number II
Given an array of integers, every element appears three times except
for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        a = b = 0
        for i in A:
            c = ~(a | b)
            b = (b & ~i) | (a & i)
            a = (a & ~i) | (c & i)

	return a
