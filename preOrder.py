#!/usr/bin/python3

if __name__ == '__main__':

	def preOrder(root):
		if root is None:
			return ""
		else:
			r = str(root.data)
			return r + preOrder(root.left) + preOrder(root.right)