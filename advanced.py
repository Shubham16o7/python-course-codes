
#list = ['car','bus','truck']            # this is known as functional arguments
 #   print(x*3)
                                         #one by one all items in list will be printed 3 times as mentioned in the code
#def map_simple(crazy,list):
#    for items in list:
 #       crazy(items)

#map_simple(loop,list)


#->2 for lists 
#lists are used for storing data

#below is the example of list
#list can be ordered,changeable and allow duplicates
#x = ['code','eat','repeat']
#print(x)

#print(len(x))    #for finding the length of the list
#print(type(x))   #for finding type of the list


#here is the tuple here the values are unchangeable,ordered and allow duplicates
#so a tuple will be having round brackets ()

#tuple=('car','bike',30,40,3.0,True,'bike')
#print(tuple)

#tuple=('car','bike',30,40,3.0,True,'bike')
#print(tuple[:5])

#and to check tuple len or type its the same process like list
 #so a tuple dont have one item 

#3 Dictionaries
#rules for the dictionaries are they are unordered , changeable and do not allow duplicated values
#example
#dictt={
 #   "name":"raj",
  #  "age":"26",
   # "vehicle":"bike"
#}
# print(type(dictt))

#3 List comprehension : List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example 3
#fruits=["apples","bananas","kiwi"]
#newfruit=[]
#for x in fruits:
 #   if 'a' in x:
 #      newfruit.append(x)
#print(newfruit)

#Example 2
#fruits=["apples","bananas","kiwi"]
#newfruit=[x for x in fruits if "i" in x]
#print(newfruit)

#file handling it means how to read write data 
# So r = read 
# a = append 
# w=write
#x = to creaye new file
#so here will make a file in this folder only with f.txt format and write how much we want to

#f=open("f.txt","r")
#print(f.read())

#f=open("f.txt","r") #to read characters
#print(f.read(5))

#f=open("f.txt","r") ---to read line one by one so the no. of line you use the  line will be prointed
#print(f.readline())


#f=open("f.txt","a")
#f.write("A new line now")    ------to add line
#f.close()
#f=open("f.txt","r")
#print(f.read())

#f=open("f.txt","w")
#f.write("A new line now")   -----to write the file
#f.close()
#f=open("f.txt","r")
#print(f.read())

#f=open("new.txt","x")   -------to create new file

#import os
#os.remove("new.txt")   ------- to remove file from folder

#import os
#if os.exists("newfile.txt"):
#   os.remove("newfile.txt")  ------condition if not present then show file notfound
#else:
#   print("file not found")   