#!/usr/bin/python3

if __name__ == '__main__':
	r = list(map(int, input().split()))
	x1, v1, x2, v2 = r

	diff_x = (x1 - x2)
	diff_v = (v2 - v1)
	div = diff_x / diff_v
	floor_div = diff_x // diff_v
	if div > 0:
		if floor_div == div:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")