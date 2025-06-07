password = input("enter your password: ")
if password == "Soham@123": 
    print("welcome soham, good to see you again on project")
else: 
     print("access denied,try correct password")   
     exit() 

print("="*50)
print("Mini Resume Formatter".center(50))
print("="*50)

# take the inputs 
name = input("enter your name: ").title()
degree = input("enter your degree (ex. Bsc in cs): ").upper()
college = input("enter your college name: ").title()
skills = input("enter your skills : ").capitalize()
email = input("enter your email: ").lower()

# formattings skills
format = (skills.replace(",","/"))

# display output
print("\n" + "-"*50)
print(name.center(50))
print(degree.center(50))
print(college.center(50))
print("-"*50)
print("email: ",email)
print("skills: ",format)