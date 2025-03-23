class Student_Management_System:

    def __init__(self):
        self.student_details = []

    def add_students(self, student_name, student_age, student_ID):
        self.name = student_name
        self.age = student_age
        self.ID = student_ID

        self.student_details.append({"Name": self.name, "Age": self.age, "Student ID": self.ID})

    def edit_student_details(self, old_student_name, old_student_ID, old_student_age, student_name, student_ID, student_age):
        for details in self.student_details:
            if details["Name"] == old_student_name and details["Student ID"] == old_student_ID and details["Age"] == old_student_age:
                details["Name"] = student_name
                details["Student ID"] = student_ID
                details["Age"] = student_age
                print(f"Student Name '{old_student_name}' has been updated to '{student_name}'\n"
                      f"Student Age '{old_student_age}' has been updated to '{student_age}'\n"
                      f"Student ID '{old_student_ID}' has been updated to '{student_ID}'")
                return
        print("Student details not found!")

    def remove_student_details(self, student_ID):
        for details in self.student_details:
            if details["Student ID"] == student_ID:
                self.student_details.remove(details)
                return f"Student with ID '{student_ID}' has been removed."
        return f"Student with ID '{student_ID}' not found!"

    def view_all_student_details(self):
        if not self.student_details:
            return "No student found!"
        return self.student_details
    
    def find_student_ID(self, student_ID):
        for details in self.student_details:
            if details["Student ID"] == student_ID:
                return details
        return f"Student with ID: {student_ID} not found!"
