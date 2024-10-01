name: str = "Salvin is is ready"
user_input: str = input("Enter a String to count : ")

print(f"normal string= {name}")
print(f"lower string= {name.lower()}")
print(f"upper string= {name.upper()}")
print(f" captitalize a string {name.capitalize()}")
print(f" title string {name.title()}")
print(f" count s in the string = {name.count("S")}")

print(f"  string {name.endswith("ready")}")
print(f"  string {name.startswith("ready")}")
print(f"  string {name.startswith("ready")}, count i in the string = {name.count("i")}")

print(f" user_input in the string is = {name.count(user_input)}")
