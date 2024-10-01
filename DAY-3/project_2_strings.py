name: str = "Coders are ready ready"
lower_name: str= name.lower()
user_input: str = input("Enter a String to count : ")
print(f" user_input in the string is = {lower_name.count(user_input.lower())}")
