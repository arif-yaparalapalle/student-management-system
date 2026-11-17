import json
with open("student management system/students.json","r") as file:
    students=json.load(file)

def save_students():
    with open("student management system/students.json","w") as file:
        json.dump(students,file,indent=4)

def add_student():
    try:
        student_id=int(input("enter student id:"))

    except ValueError:
        print("Please Enter Numbers Only")
        return
    
    if student_id <= 0:
        print("Invalid Student ID")
        return

    for student in students:
        if student["id"]==student_id:
            print("Student ID Already Exists")
            return
    name=input('enter student name:')
    if not name.strip():
        print("Student Name Cannot Be Empty")
        return
    
    try:
        age=int(input("enter student age:"))

    except ValueError:
        print("Please Enter numbers Only")
        return
    
    if age <= 0:
        print("Invalid Age")
        return
    course=input("enter course name:")
    if not course.strip():
        print("Course Name Cannot Be Empty")
        return
    student={
        "id":student_id,
        "name":name,
        "age":age,
        "course":course
    }
    students.append(student)
    save_students()
    print("Student Added Successfully!")
    print("--------------------------------------")

def view_students():
        if not students:
            print("No students Found")
        else:
            print("Total Students:", len(students))
            print("-" * 65)

            print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Course':<20}")

            print("-" * 65)

            for student in students:
                print(f"{student['id']:<10}{student['name']:<20}{student['age']:<10}{student['course']:<20}")

            print("-" * 65)

def search_student():
    try:
        search_id = int(input("Enter Student ID to search: "))

    except ValueError:
        print("Please Enter numbers Only")
        return

    if search_id <=0:
        print("Invalid Student ID")
        return

    for student in students:
        if student["id"] == search_id:
            print("Student Found Successfully!")
            print("Student ID:", student["id"])
            print("Student Name:", student["name"])
            print("Student Age:", student["age"])
            print("Course Name:", student["course"])
            print("-------------------------------")
            break
    else:
        print("Student Not Found")

def update_student():
    try:
        update_id = int(input("Enter Student ID to update: "))

    except ValueError:
        print("Please Enter numbers Only")
        return

    if update_id <=0:
        print("Invalid Student ID")
        return
    
    for student in students:
        if student["id"] == update_id:
            name = input("Enter New Student Name: ")
            if not name.strip():
                print("Student Name Cannot Be Empty")
                return
            try:
                age = int(input("Enter New Student Age: "))

            except ValueError:
                print("Please Enter numbers Only")
                return
            
            if age <= 0:
                    print("Invalid Age")
                    return
            course = input("Enter New Course Name: ")
            if not course.strip():
                print("Course Name Cannot Be Empty")
                return

            student["name"] = name
            student["age"] = age
            student["course"] = course
            save_students()

            print("Student Updated Successfully!")
            print("-----------------------------------------")
            break
    else:
        print("Student Not Found")

def delete_student():
    try:
        delete_id = int(input("Enter Student ID to delete: "))

    except ValueError:
        print("Please Enter numbers Only")
        return

    if delete_id <= 0:
        print("Invalid Student ID")
        return

    for student in students:
        if student["id"] == delete_id:
            confirm = input("Are you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":
                students.remove(student)
                save_students()
                print("Student Deleted Successfully!")
                print("-----------------------------------------")
            else:
                print("Deletion Cancelled")

            break
    else:
        print("Student Not Found")

def main_menu():
    while True:
        print("\nStudent Management System")
        print("-----------------------------------------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice=input("enter your choice:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice =="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            print("-----------------------------------------")
            print("Thank You")
            break
        else:
            print("Invalid Choice! Please Select 1 to 6")

main_menu()