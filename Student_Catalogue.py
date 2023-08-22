class StudentCatalog:
    def __init__(self):
        self.students = []

    def add_student(self, records, last_index):
        student_id = input("Enter the student's ID: ")
        name = input("Enter the student's name: ")
        last_name = input("Enter the student's last name: ")
        middle_name = input("Enter the student's middle name: ")
        major = input("Enter the student's major: ")
        email = input("Enter the student's email: ")
        phone = input("Enter the student's phone number: ")

        student = {
            'student_id': student_id,
            'name': name,
            'last_name': last_name,
            'middle_name': middle_name,
            'major': major,
            'email': email,
            'phone': phone
        }
        records.append(student)

        last_index += 1
        return last_index

    def remove_student(self, student_id):
        student_found = None
        for student in self.students:
            if student['student_id'] == student_id:
                student_found = student
                self.students.remove(student)
                break
        return student_found

    def modify_student(self, student_id, new_name, new_last_name, new_middle_name, new_major, new_email, new_phone):
        for student in self.students:
            if student['student_id'] == student_id:
                student['name'] = new_name
                student['last_name'] = new_last_name
                student['middle_name'] = new_middle_name
                student['major'] = new_major
                student['email'] = new_email
                student['phone'] = new_phone
                break

    def find_student(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                return student
        return None

    def list_students(self):
        return self.students

# Function to display the menu and get the user's choice
def display_menu():
    print("\nMain Menu")
    print("1. Add Students")
    print("2. Remove Students")
    print("3. Modify Students")
    print("4. Show All")
    print("5. Search for Student")
    print("6. Exit")
    option = int(input("Enter your option: "))
    return option

# Function to display the confirmation menu for deletion
def display_delete_confirmation_menu():
    print("Are you sure you want to delete the student?")
    print("1. Yes")
    print("2. No")
    option = int(input("Enter your selection: "))
    return option

# Example Usage:
catalog = StudentCatalog()
last_index = -1

while True:
    option = display_menu()

    if option == 1:
        last_index = catalog.add_student(catalog.students, last_index)
    elif option == 2:
        student_id_to_remove = input("Enter the student ID to remove: ")
        student_found = catalog.remove_student(student_id_to_remove)
        if student_found:
            print("Student found, their details are:")
            print("Student ID:", student_found['student_id'])
            print("Name:", student_found['name'])
            print("Last Name:", student_found['last_name'])
            print("Middle Name:", student_found['middle_name'])
            print("Major:", student_found['major'])
            print("Email:", student_found['email'])
            print("Phone:", student_found['phone'])

            delete_confirmation = display_delete_confirmation_menu()
            if delete_confirmation == 1:
                if catalog.remove_student(student_id_to_remove):
                    print("Student removed successfully.")
                else:
                    print("Could not remove the student.")
            else:
                print("Deletion canceled.")
        else:
            print("Student not found.")
    elif option == 3:
        student_id_to_modify = input("Enter the student ID to modify: ")
        new_name = input("Enter the new name for the student: ")
        new_last_name = input("Enter the new last name for the student: ")
        new_middle_name = input("Enter the new middle name for the student: ")
        new_major = input("Enter the new major for the student: ")
        new_email = input("Enter the new email for the student: ")
        new_phone = input("Enter the new phone number for the student: ")
        catalog.modify_student(student_id_to_modify, new_name, new_last_name, new_middle_name, new_major, new_email, new_phone)
    elif option == 4:
        print("Registered Students:")
        print(catalog.list_students())
    elif option == 5:
        student_id_to_find = input("Enter the student ID to search for: ")
        student_found = catalog.find_student(student_id_to_find)
        if student_found:
            print("Student found, their details are:")
            print("Student ID:", student_found['student_id'])
            print("Name:", student_found['name'])
            print("Last Name:", student_found['last_name'])
            print("Middle Name:", student_found['middle_name'])
            print("Major:", student_found['major'])
            print("Email:", student_found['email'])
            print("Phone:", student_found['phone'])
        else:
            print("Student not found.")
    elif option == 6:
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.")

# Add students to the catalog
last_index = catalog.add_student(catalog.students, last_index)
last_index = catalog.add_student(catalog.students, last_index)

# List students after adding two students
print("Registered Students:")
print(catalog.list_students())

# Modify a student
student_id_to_modify = input("Enter the student ID to modify: ")
new_name = input("Enter the new name for the student: ")
new_last_name = input("Enter the new last name for the student: ")
new_middle_name = input("Enter the new middle name for the student: ")
new_major = input("Enter the new major for the student: ")
new_email = input("Enter the new email for the student: ")
new_phone = input("Enter the new phone number for the student: ")

catalog.modify_student(student_id_to_modify, new_name, new_last_name, new_middle_name, new_major, new_email, new_phone)

# List students after modification
print("Students after modification:")
print(catalog.list_students())

# Remove a student
catalog.remove_student('67890')

# List students after removal
print("Students after removal:")
print(catalog.list_students())
