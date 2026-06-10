# collection = single "variable" used to store multiple values
#List = [] ordered and changeable. Duplicates OK
#set= {} unordered and immutable, but Add/Remove OK. NO duplicates
#Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#LIsts: A List is an ordered, mutable (changeable) collection of elements in Python that can store multiple items of different data types within a single variable.

fruits = ["apple", "orange", "banana", "coconut"]
#print(dir(fruits))   #It shows all attributes and methods available for the object.
#print(help(fruits))   #It explains what each method does and how to use it.
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")

# fruits[0] = "pineapple"
# fruits.append("pineapple")  #To Add the Element in the List
# fruits.remove("apple")      #Remove the Eleemetn in the List 
# fruits.insert(0, "pineapple")  #To Insert the Element in the List at the specific index
# fruits.sort()                  #To Sort the List in Ascending order
# fruits.reverse()             #To Sort the List in Descending order
# fruits.clear()                 #To Clear the List
# print(fruits.index("apple"))
print(fruits.count("banana"))    #To Count the Occurrence of an Element in the List

print(fruits)



#Set :A Set is an unordered, mutable collection of unique elements in Python. It does not allow duplicate values.

fruits={"apple","guva","Coconut","Mango"}
print(type(fruits))

fruits={"apple","guva","Coconut","Mango"}
#print(type(fruits))        #<set>
#fruits.add("Banana")
#print(fruits)             #{'Coconut', 'Mango', 'Banana', 'guva', 'apple'}
fruits.remove("apple")
#print(fruits)
#print(fruits[0])  #its Get Error, because set is unordered collection of data and it does not support indexing.
print(fruits.pop()) #it will remove and return a random element from the set.
fruits.add("apple")
print(fruits)  #{'Coconut', 'Mango', 'Banana', 'guva', 'apple'} -> Because Set doesnt allow Duplicate values
print(len(fruits))

print(dir(fruits))

s1={12,2,3,1,12,3,4}
s2={1,2,3,4,5,6}
print(s1.union(s2))  #{1, 2, 3, 4, 5, 6, 12}
print(s1.intersection(s2))  #{1, 2, 3, 4}
print(s1.difference(s2))  #{12}
print(s1.symmetric_difference(s2))  #{5, 6, 12}  -> It will return the elements which are present in either of the sets but not in both.


#Tuple :A Tuple is an ordered, immutable collection of elements in Python that can store multiple values of different data types.

#tuple
fruits=("apple","banana","cherry","orange","kiwi","melon","mango")
print(dir(fruits))
print(fruits[0])
fruits.index("apple")
fruits.count("apple")


#



