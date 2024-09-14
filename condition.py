#  what are condtional statement

# if and else statement

# age = 15

# if(age < 18):
#     print ("you are not an adult")
# else:
#     print("you are an adult")

# name = "Chuks"
# country = "Togo"

# if(country == "Nigeria"):
#     print(f"Welcome {name} from {country}")
# else:
#     print("You are not a Nigerian")


# username = "Johnny"
# password = " 12345"

# # if(username == "John"):
# #     print(F"You are loggen in as {username}")
# # else:
# #     print(f"{username} is not registerd")

# if(username == "John" and password == "12345"):
#     print("You are logged in")
# else:
#     print(f"{username} is not a registered user")



# server_username = "Johnny"
# server_password = "John123**"

# username = input("Welcome kindly enter your username")
# password = input("Kindly enter your secured password")

# if(username == server_username and password == server_password):
#     print(f"You are logged in as {username}")
# else:
#     print(f"{username} is not registeed user")


server_username = "Johnny"
server_password = "John123**"

username = input("Please enter your username ")

password = input("Please enter your password ")

if(username != server_username and password != server_password ):
    print("Both username and password credentials are invalid")

elif(username == server_username and password != server_password):
    print("Invalid password credentials")

elif(username != server_username and password == server_password):
    print("Invalid Username")

elif(username == server_username and password == server_password):
    print(f"You are succesfully logged in as {username}")
    

#age = 50
# check if the person is an youhg adult (18 to 25)

# check if the password is a teenager

# check if the person is a kid

# if(age >= 18 and age < 26):
#     print("You are a young adult")

# elif(age > 12 and age < 18):
#     print("You are a teenager")

# elif( age <= 12):
#     print("You are a kid")

# else:
#     print("You are an elderly adult")


