	#fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。

def  fact(n):
		if n==1:
			return 1
		return n * fact(n-1)

fact(2)