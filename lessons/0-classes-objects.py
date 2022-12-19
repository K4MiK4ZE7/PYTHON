class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name +" "+ self.age

user_name = input("Name :\t")
user_age = input("Age :\t")

u1 = User(user_name, user_age)

print(u1)