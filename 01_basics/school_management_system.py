class School:
    def __init__(self):
        self.students = {}
        self.student_id = 101
    def add(self,name,grade):
        student_id = self.next_id
        self.student[student_id] = {
          "name" : name,
         "grade" :grade,
        
          }
        self.next_id += 1
        print(f"student added succesfully with student_id : {student_id}")
      
    def view_students(self):
        if not self.students:
            print("There are no data of students in the database")
            return
        
        for student_id,details in self.students.items:
            print(f"ID:{student_id}, Name : {details['name']}, Grade : {details['grade']}") 



    def search_student(self,id):
        is_found = False
        for student_id,details in self.students.items:
            if str(student_id) == id or details["name "].lower() == id.lower():
                print(f"Student id = {student_id},Name = {details['name']},Grade = {details['grade']}")
                is_found = True
            if not is_found:
                print("There is no student with the id!")


        

    def remove_student(self,student_id):
        student_id = int(student_id)

        if student_id in self.students:
            del self.students[student_id]
            print(f"student with the id {student_id} succesfully removed.")
        

def main():
    school= School()
    print("welcome to our schools database")
    while True:
        print("""
            Make a choice!!
        1> Add a student in the database.
        2> view a student in the database.
        3> search the student information
        4> remove the student..
        """)

        choice = int(input("make a choice"))
        match choice:
            case 1:
                name = input("Enter the name of the student")
                grade = input("Enter the grade: ")
                school.add(name,grade)
            case 2:
                school.view_students()
            case 3:
                id = input("Enter the Name or student id of the student ")  
                school.search_student(id)
            case 4:
                id  = input("Enter the id of the student ")
                school.remove_student(id)

if __name__ == "__main__":
    main()
            
        