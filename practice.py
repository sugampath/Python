# from datetime import date
# today  = date.today()
# year = int(today.year)
# birth_year = 1994
# age = year - birth_year
# print(f"Your  age is  {age}.")

##Second  Excercise
# name = input("Enter your  name")
# password  = input("Enter   your  password")
# len_password =  len(password)
# secret = "*" * len_password
# print(f"hey {name} your {secret} password   is  {len_password} character long.")

# ##List 
# matrix = [ 
# [1,2,[3,4,[5,6,7]]],
# [10,11,12,13,14,],
# [100,101,12,103]
# ]
# print(matrix[0][2][2][2])

# sage = [1,2,3,4,"Asdf","manoj"]

# ##Add  item  to   the  end 
# sage.append('Prakash')
# print(sage)
# ## Add  item to the  specific index 
# sage.insert(0,"Yash")
# print(sage)
# sage.extend([12,23,45,67,89])
# print(sage)
# sage.append([1,2,3])
# print(sage)
# #removing 
# sage.pop()
# print(sage)
# #remove  item at  specific  index
# sage.pop(0)
# print(sage)
# #remove  specific  value 
# sage.remove(2)
# print(sage)
# #clear the  all  item 
# new_list = sage.clear()
# print(new_list)
# #sort the  item in ascending order 
# aa = [1,7,3,4,5,6,2]
# aa.sort()
# print(aa)
# #sort the  item in ascending order 
# aa = [1,7,3,4,5,6,2]
# aa.sort(reverse = True )
# print(aa)

##checck magician  answer 

# is_magician = False
# is_expert = False

# if  is_magician  and is_expert :
# 	print("YOu are  a  magician master")
# elif (is_magician and  not(is_expert)):
# 	print("At least you are getting there")
# elif not is_magician:

# 	print("develop magic  power")

###dictionery 
# import json
# import ast
# user  = {
# 	'name':'Prakash',
# 	'age' :29,
# 	'can_swim': False }

# ##Convert to the  str  type 
# aa = json.dumps(user)
# print(aa)
# print(type(aa))

# ##  convert  str  type  to  dict 
# dd = json.loads(aa)
# print(dd)
# print(type(dd))

# ee = ast.literal_eval(aa)
# print(ee)
## WAy of  getting items 
##Get key value  in Tuple Form 
# for i in user.items():
# 	print(i)

##Get  key  and value 
# for  k,v in user.items():
# 	print(f'Key is {k} and  value is {v}')

## To get the  value  only 
# for  i in user.values():
# 	print(i)

## To get the  keys 
# for  i in user.keys():
# 	print(f'keys of  dictionery is {i}')

##copy the  dictionery
# user2 = user.copy()
# print(user)

# ##Updating  a  dictionery 
# user2["Adress"] = "Patan"
# print(user2)

# ## Accessing  element 
# print(user2["age"])
# print(user2.get("age"))

# ## clear   all   dictionery  item 
# user2.clear()
# print(user2)

# ## get  items  in dict  
# print(user.items())

# ##  remove  specific  key 
# user.pop("name")
# print(user)

# ##  update  with specific  key  value   pair 
# user.update({"FirstName" :"Prakash"})
# print(user)

# ##Display  lenghh of  dictionery 
# print(len(user))


# test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4, 'geeks' : 6}
# test_dict2 = {'for' : 3, 'geeks' : 5}

# test_dict1.update(test_dict2)
# print(test_dict1)

# reverse_dict = list(reversed(user.items()))
# print(reverse_dict)

# for  i , j in enumerate([1,2,3,4,5]):
# 	print(i,j)

##
# pic  = [[0,0,1,0,0,0],
# 		[0,1,1,1,0,0],
# 		[1,1,1,1,1,0]]


##Display  repeated  item in list 
# a = []
# for  i in pic :
# 	for  j in i:
# 		if (j == 1):
# 			print("*" , end  = "")
# 		else :
# 			print(" " , end = "")
# 	print (" ")

# ## Print duplicate  item in  a  list 
# c = []
# a = ["aa","bb" ,"cc" ,"aa" ,"bb", "ll"]
# for  value  in a:
# 	if a.count(value) > 1:
# 		if value  not in c:
# 			c.append(value)
# # print(c)

# for  items  in a:
# 	if items  not in c:
# 		c.append(items)
# 	else:
# 		print(items)

# from iteration_utilities import unique_everseen
# dup = list(unique_everseen(duplicates(a)))
# print(dup)

# import pandas as pd
a = [1,2,3,3,3,4,5,6,6,7]
# vc = pd.Series(a).value_counts()
# aa = vc[vc > 1].index.tolist()
# print(aa)

# from collections import Counter

# print((Counter(a)))
# print(Counter(set(a)))
# dup = (Counter(a) - (Counter(set(a))))
# print(dup)
# # print(list(dup.keys()))

##Function 
# def say_hello():
# 	print("Hello World")

# # say_hello()

# def calc(sign , a,b):
# 	''' 
# 	 This is a simple calculator 

# 	'''
# 	if sign == "+":
# 		sum = a+b
# 		return (sum)
# 	elif sign == "-":
# 		diff = a-b 
# 		return (diff)
# 	elif sign == "*":
# 		prod = a*b
# 		return (prod)
# 	elif sign == "/":
# 		return(a/b)
# 	elif sign == "%":
# 		return (a%b)
# 	elif  sign == "**":
# 		power = a**b
# 		return (power)
# 	else :
# 		return ("Wrong Entry")

# print(f'The  sum   is {calc("+", 2 ,3 )}.')
# print(f'The  difference  is {calc("-", 2 ,3 )}.')
# print(calc("+",2,3))
# print(help(calc))
# print(calc.__doc__)

###WARLUS  OPERATOR 
a = "helloooooo0000o"

# if  (len(a) > 10):
# 	print(f"Too  long {len(a)} elements ")

# if  ((n :=len(a)) > 10):
# 	print(f"Too  long {n} elements ")

# while ((n:=  len(a)) > 1):
# 	print(n)
# 	a = a[:-1]
# print(a)

##local  and  gloabl  scope  rules 
#1 >> start  with local 
#2  >> parent  local 
#3 >> Global 
#4 >> built  in python function  

###Global 
# total  = 0 
# def count():
# 	global total 
# 	total +=1
# 	return total 

# print(count())

# total = 0 
# def  count(total):
# 	total += 1
# 	return total

# print(count(count(count(total))))
