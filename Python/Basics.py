##simple print stmnt ###
# print('hello world')



####variable#####
	#letter number underscore
	#cant start with number
	#cant use keywords as variable name
_message = 'Hi this is message'
# print(_message)
_message = 'message changed'
# print(_message)



#####String#######
	#anthing bw '' & ""
_message = 'Hi thi\'s is message'

#Captialize first char
print(_message.title())
#upper(),lower() - return new string not change the passed one
#strip(),rstrip(),lstrip() - remove spaces and return new string
#f- formatted string
print(f'Message with varible = {_message}')


#####Numbers####
x,y,z = 1,2,3
# print(x,y,z)

#/ - give float
#// - give integer
# x ** y - x to the pow of y
# print(10/3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

#import math  -  for getting math functions
#abs(),round()


#####String + math ####
# print(_message * 10)

#####Take input from user####
# name = input('Whats ur name ?')
# print(name)

# import sys
# print(sys.version)

#### Functions #####
# int()
# float()
#Len()
# print(len(_message))

#find() - return index of first char in string
# print(_message.find('h'))

#replace()
# print(_message.replace('H','Hello'))

#in, not in
# print('hello' in _message)






####char/substirng in String ####

# print(_message[0])

#get string from [a,b)
# print(_message[0:4])

#get char from end
# print(_message[-1])

#get substring from index to last
# print(_message[2:])

#get substring from start to index-1
# print(_message[:5])

#copy string
# newstring = _message[:]
# print(newstring)





