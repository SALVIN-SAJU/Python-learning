main_role: str=input("ENTER THE NAME OF MAIN CHARACTER: ")
gender_main: str=input("Gender of main role: ")
prof_name: str=input("Enter prof. name: ")
num_students: int=int(input("Enter the no. of students: "))
science_major: str=input("Name of science major: ")
if gender_main=="Male":
    gen="his"
    ge="he"
else:
    gen="her"
    ge="she"
# if  science_major=="Male":
#     je="he"
# else:
#     je="she"


print(f"""In {gen} college dorm, {main_role} decided to learn Python after hearing about its usefulness in data science. Eager to start, he attended  first class, where {gen} enthusiastic professor, {prof_name}, encouraged over {num_students} students to explore coding's power. However, Sarah quickly felt overwhelmed by terms like “variables” and “loops.”

Determined, {ge} spent the next three nights creating a program to track her homework, envisioning how it would revolutionize {gen} study habits. After typing away for five hours, {ge} hit Run and was met with a barrage of error messages. Frustrated, {ge} turned to {gen} roommate, {science_major}, a computer science major, who laughed and said, “Let’s take a look.”

After just a few minutes,  found that {ge} had misspelled print as pritn. Relieved but motivated, {main_role} jumped back in. After a week of trial and error, {ge} finally created a functioning homework tracker that could add, remove, and remind {gen} of assignments.""")