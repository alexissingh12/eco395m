# print("Hello World")

# def hello():
# 	print("hello")

# def hello2():
# 	return "hello"

# hello()
# hello()
# hello()

# hello2()


# print(hello2() + " how are you")
# print(f"{hello2()} how are you")

###################

# def add(a, b):
# 	return a + b

# # print(add(1, 2))
# # print(add("1", "2"))

# a = 1000
# add(1, 2)
# print(a)

#######################

# don't do this

# c = 6

# def add_with_c(a, b):
# 	return a + b + c

# print(add_with_c(1, 2))

#######################


# def print_is_even_or_odd(num):
# 	if num % 2 == 0:
# 		print("even")
# 	else:
# 		print("odd")

# print_is_even_or_odd(888)

#######################

def grade(n):

	if n >= 90:
		return "A"
	elif n >= 80:
		return "B"
	elif n >= 70:
		return "C"
	elif n >= 60:
		return "D"
	else:
		return "F"

def grade2(n):

	if n >= 90:
		return "A"
	if n >= 80:
		return "B"
	if n >= 70:
		return "C"
	if n >= 60:
		return "D"
	
	return "F"

def grade3(n):

	if n >= 90:
		return "A"
	if 90 > n >= 80:
		return "B"
	if 80 > n >= 70:
		return "C"
	if 70 > n >= 60:
		return "D"
	
	return "F"

print(grade(88))
print(grade(101))
print(grade(-101))

print(grade2(88))
print(grade2(101))
print(grade2(-101))

print(grade3(88))
print(grade3(101))
print(grade3(-101))





