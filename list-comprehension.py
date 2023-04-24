import random

import numpy as np
import mudule as mp
list = [True,False,False]

new_list = [1 if val == True else 0 for val in list];

print(new_list)

string = "AbhiIsTheRichPerson"

newString = "".join([" "+i if i>="A" and  i<="Z" else i.upper() if i in ["a","s"] else i for i in string])

print(newString[1:])


key = ["Abhi","Abhi2","Abhi3"]
value = ["val1","val2","val3"]

dict = {}

# for (key,val) in zip(key,value):
#     dict[key]=val

# print(dict)

newDcit = {k:val for (k,val) in zip(key,value)}
print(newDcit)


dict2 = {key[i]:value[i] for i in range(len(key))}


name={

    "Abhi":"good",
    "Baa":"good",
    "Daddy":"goodw"
}

newName ={(key2+"family" if key2!="Abhi" else key2):(val2 if val2!="good" else "geeee") for (key2,val2) in name.items() }

print(newName)


A = ["A", "T","C","G"]
strand = random.choices(A,k=10)
print(strand)


#dictorny of list
dns = {index:
      [val,
       ("T" if val=="A" else "A" if val=="T"
       else "C" if val=="G" else "G")
      ] for index,val in enumerate(strand)}

print(dns)


#list of dictonary
# ans=[{k:v} for i in range(len(value))]
# print(ans)


nn = [10,1,2,3,4,5,6,7,8];

# newN = [n for n in nn if n]%2==0;

# print(newN);


list_new = sorted(nn,key=lambda n:-n)
print(list_new)



class Emp():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __repr__(self):
        return '({},{})'.format(self.name,self.age)


e1 = Emp('Caral',24)
e2 = Emp('Aaral2',23)

emp = [e1,e2]

emp2 = sorted(emp,key=lambda n:n.age)
print(emp2)

str = "Abhi x"
str =str.replace("Abhi","AAbhi")
print(str)


val = int(input("deneter data"))
print(val) 


data = [
    [1,2,3],
    [2,3,4],
    [2,3]
]

print(data[2][1])

mp.heloo("abhu")