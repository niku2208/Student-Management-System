
class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password


class Admin(User):

    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)


class Student(User):

    def __init__(self, user_id, name, password, age, course,
                 subjects, marks, attendance):

        super().__init__(user_id, name, password)

        self.age = age
        self.course = course
        self.subjects = set(subjects)
        self.marks = marks
        self.attendance = attendance

    def calculate_percentage(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)

    def display_profile(self):
        print("\n------ MY PROFILE ------")
        print("Student ID:", self.user_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Subjects:", self.subjects)
        print("Attendance:", self.attendance, "%")

    def display_result(self):
        print("\n------ MY RESULT ------")

        if len(self.marks) == 0:
            print("No marks available.")
            return

        for i in range(len(self.marks)):
            subject = list(self.subjects)[i] if i < len(self.subjects) else "Subject " + str(i + 1)
            print(subject, ":", self.marks[i])

        percentage = self.calculate_percentage()

        print("Percentage:", round(percentage, 2), "%")

        if percentage >= 90:
            print("Grade: A+")
        elif percentage >= 80:
            print("Grade: A")
        elif percentage >= 70:
            print("Grade: B")
        elif percentage >= 60:
            print("Grade: C")
        elif percentage >= 40:
            print("Grade: D")
        else:
            print("Grade: F")


class StudentManagementSystem:

    def __init__(self):

        self.admin = Admin("admin", "Administrator", "admin123")

        self.students = {}

        self.add_sample_students()

    def add_sample_students(self):

        self.students["101"] = Student(
            "101", "Rahul", "rahul123", 19,
            "B.Tech CSE",
            ["Python", "Maths", "Physics"],
            [85, 90, 78],
            85
        )

        self.students["102"] = Student(
            "102", "Aman", "aman123", 20,
            "B.Tech CSE",
            ["Python", "Maths", "Physics"],
            [75, 80, 88],
            90
        )

        self.students["103"] = Student(
            "103", "Priya", "priya123", 19,
            "B.Tech IT",
            ["Python", "Maths", "Physics"],
            [92, 95, 89],
            95
        )

    # ---------------- LOGIN SYSTEM ----------------

    def login(self):

        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")

        while True:

            print("\n1. Admin Login")
            print("2. Student Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.admin_login()

            elif choice == "2":
                self.student_login()

            elif choice == "3":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice!")

    # ---------------- ADMIN LOGIN ----------------

    def admin_login(self):

        print("\n------ ADMIN LOGIN ------")

        user_id = input("Enter Admin ID: ")
        password = input("Enter Password: ")

        if (user_id == self.admin.user_id and
                password == self.admin.password):

            print("\nAdmin login successful!")
            self.admin_menu()

        else:
            print("Invalid Admin ID or Password!")

    # ---------------- STUDENT LOGIN ----------------

    def student_login(self):

        print("\n------ STUDENT LOGIN ------")

        user_id = input("Enter Student ID: ")
        password = input("Enter Password: ")

        student = self.students.get(user_id)

        if student and student.password == password:

            print("\nWelcome,", student.name)
            self.student_menu(student)

        else:
            print("Invalid Student ID or Password!")

    # ---------------- ADMIN MENU ----------------

    def admin_menu(self):

        while True:

            print("\n========== ADMIN DASHBOARD ==========")

            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student Details")
            print("5. Update Student Marks")
            print("6. Update Attendance")
            print("7. Delete Student")
            print("8. View Class Statistics")
            print("9. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_all_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.update_marks()

            elif choice == "6":
                self.update_attendance()

            elif choice == "7":
                self.delete_student()

            elif choice == "8":
                self.class_statistics()

            elif choice == "9":
                print("Admin logged out successfully!")
                break

            else:
                print("Invalid choice!")

    # ---------------- ADD STUDENT ----------------

    def add_student(self):

        print("\n------ ADD STUDENT ------")

        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("Student ID already exists!")
            return

        name = input("Enter Name: ")
        password = input("Create Password: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        subjects = input(
            "Enter subjects separated by commas: "
        ).split(",")

        subjects = [s.strip() for s in subjects if s.strip()]

        marks = []

        for subject in subjects:

            mark = float(input("Enter marks in " + subject + ": "))

            if mark < 0 or mark > 100:
                print("Invalid marks! Enter marks between 0 and 100.")
                return

            marks.append(mark)

        attendance = float(input("Enter Attendance Percentage: "))

        if not 0 <= attendance <= 100:
            print("Invalid attendance!")
            return

        self.students[student_id] = Student(
            student_id,
            name,
            password,
            age,
            course,
            subjects,
            marks,
            attendance
        )

        print("Student added successfully!")

    # ---------------- VIEW ALL STUDENTS ----------------

    def view_all_students(self):

        print("\n------ ALL STUDENTS ------")

        if not self.students:
            print("No student records found!")
            return

        for student_id, student in self.students.items():

            print("\nStudent ID:", student_id)
            print("Name:", student.name)
            print("Course:", student.course)
            print("Percentage:", round(
                student.calculate_percentage(), 2
            ), "%")

    # ---------------- SEARCH STUDENT ----------------

    def search_student(self):

        student_id = input("Enter Student ID to search: ")

        student = self.students.get(student_id)

        if student:

            print("\nStudent Found!")
            student.display_profile()
            student.display_result()

        else:
            print("Student not found!")

    # ---------------- UPDATE STUDENT ----------------

    def update_student(self):

        student_id = input("Enter Student ID: ")

        student = self.students.get(student_id)

        if not student:
            print("Student not found!")
            return

        print("\n1. Update Name")
        print("2. Update Age")
        print("3. Update Course")
        print("4. Update Password")

        choice = input("Enter choice: ")

        if choice == "1":
            student.name = input("Enter New Name: ")

        elif choice == "2":
            student.age = int(input("Enter New Age: "))

        elif choice == "3":
            student.course = input("Enter New Course: ")

        elif choice == "4":
            student.password = input("Enter New Password: ")

        else:
            print("Invalid choice!")
            return

        print("Student details updated successfully!")

    # ---------------- UPDATE MARKS ----------------

    def update_marks(self):

        student_id = input("Enter Student ID: ")

        student = self.students.get(student_id)

        if not student:
            print("Student not found!")
            return

        print("\nSubjects:", student.subjects)

        subjects = list(student.subjects)

        for i in range(len(subjects)):

            print(i + 1, ".", subjects[i])

        try:
            index = int(input("Select subject number: ")) - 1

            if index < 0 or index >= len(subjects):
                print("Invalid subject!")
                return

            marks = float(input("Enter new marks: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
                return

            student.marks[index] = marks

            print("Marks updated successfully!")

        except ValueError:
            print("Please enter a valid number!")

    # ---------------- UPDATE ATTENDANCE ----------------

    def update_attendance(self):

        student_id = input("Enter Student ID: ")

        student = self.students.get(student_id)

        if not student:
            print("Student not found!")
            return

        attendance = float(input("Enter new attendance: "))

        if not 0 <= attendance <= 100:
            print("Invalid attendance!")
            return

        student.attendance = attendance

        print("Attendance updated successfully!")

    # ---------------- DELETE STUDENT ----------------

    def delete_student(self):

        student_id = input("Enter Student ID to delete: ")

        if student_id in self.students:

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            )

            if confirm.lower() == "yes":

                del self.students[student_id]

                print("Student deleted successfully!")

            else:
                print("Deletion cancelled!")

        else:
            print("Student not found!")

    # ---------------- CLASS STATISTICS ----------------

    def class_statistics(self):

        if not self.students:
            print("No student records available!")
            return

        total_students = len(self.students)
        total_percentage = 0

        highest = -1
        lowest = 101

        topper = ""
        lowest_student = ""

        for student in self.students.values():

            percentage = student.calculate_percentage()

            total_percentage += percentage

            if percentage > highest:
                highest = percentage
                topper = student.name

            if percentage < lowest:
                lowest = percentage
                lowest_student = student.name

        average = total_percentage / total_students

        print("\n------ CLASS STATISTICS ------")
        print("Total Students:", total_students)
        print("Class Average:", round(average, 2), "%")
        print("Topper:", topper)
        print("Highest Percentage:", round(highest, 2), "%")
        print("Lowest Percentage:", round(lowest, 2), "%")
        print("Lowest Scorer:", lowest_student)

    # ---------------- STUDENT MENU ----------------

    def student_menu(self, student):

        while True:

            print("\n========== STUDENT DASHBOARD ==========")

            print("1. View My Profile")
            print("2. View My Marks")
            print("3. View My Percentage")
            print("4. View My Attendance")
            print("5. View My Result")
            print("6. Change My Password")
            print("7. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":

                student.display_profile()

            elif choice == "2":

                student.display_result()

            elif choice == "3":

                print(
                    "My Percentage:",
                    round(student.calculate_percentage(), 2),
                    "%"
                )

            elif choice == "4":

                print("My Attendance:", student.attendance, "%")

            elif choice == "5":

                student.display_result()

            elif choice == "6":

                new_password = input("Enter New Password: ")

                student.password = new_password

                print("Password changed successfully!")

            elif choice == "7":

                print("Student logged out successfully!")
                break

            else:
                print("Invalid choice!")


# ---------------- MAIN PROGRAM ----------------

system = StudentManagementSystem()

system.login()
