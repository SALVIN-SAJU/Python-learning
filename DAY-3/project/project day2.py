main_role: str=input("ENTER THE NAME OF MAIN CHARACTER: ")
main_gender:str = input("gender :")

prof_name: str=input("Enter prof. name: ")
prof_gender: str=input("gender :")

num_students: int=int(input("Enter the no. of students: "))

science_major: str=input("Name of science major: ")
major_gender: str=input("gender : ")


# main info
if main_gender.lower() == "male":
    main_1="his"
    main_2="he"
else:
    main_1="her"
    main_2="she"


# prof info
if prof_gender.lower()=="male":
    prof_1="his"
    prof_2="he"
else:
    prof_1="her"
    prof_2="she"


#major info
if major_gender.lower()=="male":
    major_1="his"
    major_2="he"
else:
    major_1="her"
    major_2="she"


print(f"""In {main_1} college dorm, {main_role} decided to learn Python after hearing about its usefulness in data science. Eager to start, {main_2} attended  first class, where enthusiastic professor, {prof_name}, encouraged over {num_students} students to explore coding's power. However, {main_role} quickly felt overwhelmed by terms like “variables” and “loops.”

Determined, spent the next three nights creating a program to track her homework, envisioning how it would revolutionizestudy habits. After typing away for five hours, hit Run and was met with a barrage of error messages. Frustrated,  turned to  roommate, {science_major}, a computer science major, who laughed and said, “Let’s take a look.”

After just a few minutes,  found that  had misspelled print as pritn. Relieved but motivated, {main_role} jumped back in. After a week of trial and error,{main_2}  finally created a functioning homework tracker that could add, remove, and remind  of assignments.""")