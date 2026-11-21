# Welcome the user to the text analysis tool
def WelcomeUser():
  print("Welcome to the Text Analysis Tool, I will mine and analyze a body of text from a file you provide.")

# Get Username
def get_username():
  # Print a message prompting the user to enter their username
  usernamefrominput=input("\nPlease enter your username: \n")
  return usernamefrominput

# greet the user and inform them about the text analysis process
def greet_user(username):
  print("Hello," + username)

WelcomeUser()
username = get_username()
greet_user(username)
