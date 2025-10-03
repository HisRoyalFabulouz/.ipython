# building user management and authentication system for web application
			# features: user registration, login, delete user, list users, update password
			# storing user data in a dictionary
			# each user has a unique id, name, username, password, email, is_admin status
			# functions for each feature
			# validating email and password during registration
			# checking for existing users during registration
			# error handling for invalid inputs

		

users = {100 : {"name" : "steve fabulouz", "username" : "fabulouz001", 
				"password" : "bossFab23@", "email" : "fabulouz@gmail.com","is_admin" : False
}, 

101 : {"name" : "soh chima", "username" : "sochima10", "password" : "sohsohchi2",
	    "email" : "sochibae22@gmail.com", "is_admin" : False

}, 
102 : {"name" : "victor emelie ", "username" : "ViktoR007", "password" : "victory1", 
	   "email" : "victoryes@yahoo.com", "is_admin" : False

}, 108 :{"name" : "okonjo joe", "username" : "joeboy10", "password" : "joejoe100",
		  "email" : "jeoboy@gmail.com", "is_admin" : False

},  118 :{"name" : "bdg nbbc", "username" : "ndhfee0", "password" : "jndvg73ds", "email" : "jebxvg@gmail.com", 
		 "is_admin" : False

}


}

import random
name = input("enter your full name: ").title()
username = input("enter your username: ")
password = str(input("enter your password: "))
email = input("enter your email: ").lower()


def register_users(name,email,username,password):
	try:
		# validating email and password
		if "@" not in email:
			print("invalid email, please input a valid email.")
			return False
		if len(password) < 8 and not any(char.isdigit()for char in password):
		
			print("password is too short, must be at least 8 characters.")
			return False
		if " " in password:
			print("password cannot contain spaces")
			return False
		
	except:
		return True
		# checking for existing users during registration 
	for user_id, user_data in users.items():
		u_email = user_data.get("email")
		u_username = user_data.get("email")
		u_password = user_data.get("password")
		if u_email == email and u_password == username:
			print("user already exists, please login")
		elif u_username == username and u_password == password:
			print("user already exists, please login")
			
			
			
		# generating unique user id for potential new user and adding to users to the system
	new_id = random.randint(100, 501)
	while new_id in users:
		new_id = random.randint(100, 501)
	users[new_id] = { "name" : name, "email" : email, "username" : username, "password" : password , "is_admin" : False
	
	}
	print("new user,", name, "registered successfully you can now login")
	return True


def login(username, password):
	# checking if user exists and password is correct 
	for user_id,user_data in users.items():
		u_username = user_data.get("username")
		u_password = user_data.get("password")
		u_email =user_data.get("email")
		if u_username == username  and u_password == password :
			print("welcome,", username, " you are logged in successfully")
			return True
		if u_email == username	and u_password == password:
			print("welcome,", username, " you are logged in successfully")
			return True
		
		if u_username == username and  u_password != password:
			print("incorrect password try again.")
			return False
			
		if u_email == username and u_password != password:
			print("incorrect password try again.")
			return False
			
		if u_email != username and u_password != password:
			print("sorry, you are not a registered yet, register first!!")
			return False
		if u_username != username and u_password != password:
			print("sorry, you are not a registered yet, register first!!")
			return False
	
		
		

														
def remove_user(user_id):
	# checking if user exists and deleting user from the system
	if user_id in users:
		
		del users[user_id]
		print("user with id:", user_id, "deleted successfully")
	else:
		print(f"No user with id: {user_id} found input a valid id ")




def get_users(users):
	# getting all users in the system but without their passwords
	# for security reasons 
	for user_id, user_data in users.items():
		
		get_users = {"user_id" : user_id, "name": user_data["name"], "username": user_data["username"],"email" : user_data["email"]}
		print(get_users)


       

			
def update_password(username, password, new):
	# checking if user exists and updating password
	# validating new password
	try:
		if len(new) < 8 and not any(char.isdigit() for char in new):
			print("error password input incorrect")
			return False
		if new == password:
			print("new password cannot be the same as old password")
			return False
		if " " in new:
			print("password cannot contain spaces")
			return False
	except:
		return True
	
	for id, info in users.items():
		if username == info.get("username") and password == info.get("password"):

			
			
			while True:
			
				users[id]["password"] = new
				
				print("password updated successfully")
				return True
		elif username == info.get("username") and password != info.get("password"):
			print("incorrect password, pls try again")	
			return False
		else :
			print(f"no user with {username} found,please register")
			return False
		

																														
			