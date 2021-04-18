def get_square(n):
	return n*n

print(f"__name__:{__name__}")
if __name__ == '__main__':
	print("square.py is executed as main program")
	print(get_square(5))

else:
	print("square.py is being imported as a module")
