
import json
dict ={"name":"Abhi","salary":None,"hobbidsdes":["A","V","B"]}

def deserialize(personJSON):
    person = json.loads(personJSON);
    print(person) 

personJSON = json.dumps(dict,indent=4)
print(personJSON)



deserialize(personJSON)

with open("data.json","w") as f:
    json.dump(dict,f,indent=4)

f.close()




class User:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

    def __repr__(self):
        return {"Abi":"Abhi"}


def encode_user(o):

    if isinstance(o,User):
        return {"name":o.name,"age":o.age};
    else:
        raise TypeError("Of wrong type shold be of user")

user1 = User("Abhi",23)
user2  =User("Ba",60)

from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self,o):
        if isinstance(o,User):
            return {"name":o.name,"age":o.age};
        else:
            raise TypeError("Of wrong type shold be of user")

# print(json.dumps(user1,default=encode_user))
print(json.dumps(user1,cls=UserEncoder))



def decotr(func):

    def wrapper(*args,**kwargs):
        print("hhh");
        func(*args,**kwargs);

    return wrapper;


@decotr
def printer(x):
    print("Abhi"+x)

printer("Abhi");    