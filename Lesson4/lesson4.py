#Create a set using curly breaskets

#my_stet = {1,2,3}

#print(my_set)

#Creating a set from a list using the set() function
#my_set = ([4,5,6])
#print(my_set)

#Creating an empty set using the set() function
my_set = set()
print(my_set)

my_set ={1,1,2,3,3,4,5,3,2,3}
print(my_set) #Set will automaticlly remove duplicates


#################

set1 = {1,2,3}
set2 = {2,4,5}


#Union between set1 and set2 using the union() method

union_method = set1.union(set2)

#compute union between set1 and set2 using the | operator

union_operator = set1 | set2

print("Union of set1 and set2 using method: ", union_method)
print("Union of set1 and set2 using operator", union_operator)

#Compute intersection between set1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#Computing intersection between set1 and set2 using & operator

intersection_operator= set1 & set2

print("Intersection of set1 and set2 using the intersection method ", intersection_method)
print("intersection of set1 and set2 using the intersection operator", intersection_operator)

#computing the elements that are unique to set1 using the fiffrence method
difference_methode = set1 - set2

#Computing elements that are unique to set1 using the - operator
diffrence_operator = set1 - set2

print("Difference of set1 and set2 using the difference method: ", difference_method)
print("Difference of set1 and set2 using the - operator: ", difference_operator)

#Computing the elementes that are in set1 and in set2 but not in their intersection
symmetric_difference_method = set1.symmetric_difference(set2)

