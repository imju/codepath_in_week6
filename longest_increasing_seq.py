class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
	    ans = anchor = 0
	    for i in range(len(A)):
	        if i and A[i-1] >= A[i]: anchor = i
	        ans = max(ans, i - anchor +1)
	    return ans
