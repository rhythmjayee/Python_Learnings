#user defined functions

# def some_function():
# 	print('Hiii, I m fun')
# 	print('Random data')

# some_function()

# def some_function_with_Parameter(x,y):
# 	print(f'Hiii x={x}, I m fun')
# 	print(f'{y} Random data')

# some_function_with_Parameter(1,2)

# def some_function_return(): - on default function return None
# 	x = 3;
# 	y = x**2
# 	return y
# res = some_function_return()
# print(res)


#Classes
class Parent:
	def some_repeat_method(self):
		print("I do single stuff")



class Some(Parent):#Inheritance
	def __init__(self,x,y):#constructor
		self.x = x
		self.y = y

	def method1(self):
		self.x += 1
		print('Hi from method 1')

	def method2(self):
		print("hi form method 2")


objectS = Some(1,2)

objectS.method1();
print(objectS.x)
objectS.some_repeat_method()








