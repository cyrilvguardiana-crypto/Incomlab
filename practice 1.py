student = {
    "ann": 78,
    "ben": 89,
    "clara": 94,
    "cent": 89,
}
print("Students Grade")
print("ann" , student["ann"])
print("ben" , student["ben"])
print("clara" , student["clara"])
print("cent" , student["cent"])
student["cy"] = 87
student["feng"] = 79
name1 = input("Enter student name:()")
grade1 = int(input("Enter student grade:()"))
student[name1]= grade1
print (student)
print("\nUpdate grade")
for name, grade in student.items():
    print(name , grade)
search = input("\nEnter student ")
if search in student:
    print(search ,"Has grade of", grade)
else:
    print("dont have student name")