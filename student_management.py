# ============================================
# STUDENT MANAGEMENT SYSTEM
# ============================================

students = []

while True:
    print("\n===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. View All Students")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # -----------------------------
    # Add Student
    # -----------------------------
    if choice == "1":
        student_id = input("Enter Student ID: ")

        # Check if ID already exists
        exists = False
        for student in students:
            if student["ID"] == student_id:
                exists = True
                break

        if exists:
            print("Student ID already exists!")
        else:
            name = input("Enter Student Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")

            student = {
                "ID": student_id,
                "Name": name,
                "Age": age,
                "Department": department
            }

            students.append(student)
            print("\nStudent added successfully!")

    # -----------------------------
    # Update Student
    # -----------------------------
    elif choice == "2":
        student_id = input("Enter Student ID to update: ")

        found = False

        for student in students:
            if student["ID"] == student_id:
                print("\nCurrent Details")
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Department:", student["Department"])

                student["Name"] = input("Enter New Name: ")
                student["Age"] = input("Enter New Age: ")
                student["Department"] = input("Enter New Department: ")

                print("\nStudent updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # -----------------------------
    # Delete Student
    # -----------------------------
    elif choice == "3":
        student_id = input("Enter Student ID to delete: ")

        found = False

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # -----------------------------
    # Search Student
    # -----------------------------
    elif choice == "4":
        search = input("Enter Student ID or Name: ")

        found = False

        for student in students:
            if student["ID"] == search or student["Name"].lower() == search.lower():
                print("\n========== Student Details ==========")
                print("Student ID :", student["ID"])
                print("Name       :", student["Name"])
                print("Age        :", student["Age"])
                print("Department :", student["Department"])
                print("=====================================")
                found = True

        if not found:
            print("Student not found.")

    # -----------------------------
    # View All Students
    # -----------------------------
    elif choice == "5":

        if len(students) == 0:
            print("\nNo student records available.")

        else:
            print("\n=========== ALL STUDENTS ===========")

            count = 1

            for student in students:
                print(f"\nStudent {count}")
                print("------------------------------")
                print("Student ID :", student["ID"])
                print("Name       :", student["Name"])
                print("Age        :", student["Age"])
                print("Department :", student["Department"])
                count += 1

            print("\nTotal Students:", len(students))

    # -----------------------------
    # Exit
    # -----------------------------
    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")