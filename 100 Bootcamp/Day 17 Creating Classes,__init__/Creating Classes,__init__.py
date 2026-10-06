# UserCar Pascal

# userCar camel case

# uer_car snake case


class User: #PascalCase

    def __init__(self, user_id, user_name):#inside this funtion we initialize or create starting values for our attributes
        self.id = user_id #id - > attributes (variables), user_id -> name of the parameter
        self.username = user_name
        self.followers = 0
        self.following = 0
        print("new user being created...")
    
    def follow(self,user): #creating method,which uses already existing objects to affiiate
        user.followers +=1
        self.following +=1 #attribute
    #pass


user_1 = User("001","angela") #creating object
user_1.id = "002" # the same effect as in the function
user_1.username = "angela"

user_2 = User("003","jack")

print(user_1.id) #we call name of the attribute. NOT THE PARAMETER which is user_id
print(user_1.followers) #we call name of the attribute. NOT THE PARAMETER which is user_id


user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


