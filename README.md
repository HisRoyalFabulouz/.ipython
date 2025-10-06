# building user management and authentication system for web application
			# features: user registration, login, delete user, list users, update password
			# storing user data in a dictionary
			# each user has a unique id, name, username, password, email, is_admin status
			# functions for each feature
			# validating email and password during registration
			# checking for existing users during registration
			# error handling for invalid inputs



functions 

register_users():

login(username, password):
	# checking if user exists and password is correct 

remove_user(user_id):
	# checking if user exists and deleting user from the system
  
get_users(users):
	# getting all users in the system but without their passwords
	# for security reasons

  update_password(username, password, new):
	# checking if user exists and updating password
	# validating new password
