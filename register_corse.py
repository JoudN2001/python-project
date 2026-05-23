# Data Structure
students = {
    "S001": {"name": "Ahmad Ali", "courses": {"CS101", "MATH201"}},
    "S002": {"name": "Sara Mahmoud", "courses": {"ENG150"}},
    "S003": {"name": "Omar Hussein", "courses": {"CS101", "ENG150", "PHYS110"}},
    "S004": {"name": "Lina Khaled", "courses": set()},
    "S005": {"name": "Yousef Nasser", "courses": {"CS101"}}
}

courses = {
    "CS101": {
        "name": "Introduction to Programming",
        "capacity": 3,
        "students": ["S001", "S003", "S005"]
    },
    "MATH201": {
        "name": "Calculus II",
        "capacity": 2,
        "students": ["S001"]
    },
    "ENG150": {
        "name": "Academic Writing",
        "capacity": 4,
        "students": ["S002", "S003"]
    },
    "PHYS110": {
        "name": "General Physics",
        "capacity": 2,
        "students": ["S003"]
    }
}


# Handle User Events
def add_student():
    student_id = input("Enter student ID (e.g., S006): ")
    name = input("Enter student name: ")
    
    students[student_id] = {"name": name, "courses": set()}
    print("Student was added successfully!")

def add_course():
    course_code = input("Enter course code (e.g., CS102): ")
    name = input("Enter course name: ")
    capacity = int(input("Enter course capacity: "))
    
    courses[course_code] = {"name": name, "capacity": capacity, "students": []}
    print("Course was added successfully!")

def register_course():
    # Check if student exists
    student_id = input("Enter student ID (e.g., S001): ")
    if student_id not in students:
        print("Error: Student ID not found. Please try again.")
        return 

    display_all_courses()
    
    # Check if course exists
    course_code = input("Enter course code (e.g., CS101) to register: ")
    if course_code not in courses:
        print("Error: Course code not found. Please try again.")
        return

    # Check for duplicate registration (Prevent duplicates)
    if course_code in students[student_id]["courses"]:
        print("Error: Student is already registered in this course!")
        return

    # Check course capacity
    current_students_count = len(courses[course_code]["students"])
    max_capacity = courses[course_code]["capacity"]
    
    if current_students_count >= max_capacity:
        print("Error: Course is full! Cannot register more students.")
        return

    # Register the course
    students[student_id]["courses"].add(course_code)
    
    courses[course_code]["students"].append(student_id)
    
    print(f"Success: Student {student_id} has been registered in {course_code}!")

def drop_course():
    student_id = input("Enter student ID (e.g., S001): ")
    if student_id not in students:
        print("Error: Student ID not found. Please try again.")
        return

    course_code = input("Enter course code (e.g., CS101) to drop: ")
    if course_code not in courses:
        print("Error: Course code not found. Please try again.")
        return
    
    if course_code not in students[student_id]["courses"]:
        print("Error: Student is not enrolled in this course!")
        return

    students[student_id]["courses"].remove(course_code)
    courses[course_code]["students"].remove(student_id)
    
    print(f"Success: Course {course_code} has been dropped for student {student_id}!")


def show_student_courses():
    student_id = input("Enter student ID (e.g., S001): ")
    if student_id not in students:
        print("Error: Student ID not found. Please try again.")
        return 
    
    details = students[student_id]
    
    print(f"\n--- {details['name']}'s Courses ---")
    print(f"{'ID':<10} | {'Name':<20} | {'Courses List'}")
    print("-" * 60)
    
    courses_list = ", ".join(details["courses"]) if details["courses"] else "None"
    print(f"{student_id:<10} | {details['name']:<20} | {courses_list}")
    print("-" * 60)


def show_course_students():
    course_code = input("Enter course code (e.g., CS101) to view: ")
    if course_code not in courses:
        print("Error: Course code not found. Please try again.")
        return
    
    details = courses[course_code]
    
    print(f"\n--- Students enrolled in: {details['name']} ---")
    print(f"{'Code':<10} | {'Course Name':<30} | {'Capacity':<10} | {'Students List'}")
    print("-" * 80)
    
    students_list = ", ".join(details["students"]) if details["students"] else "None"
    print(f"{course_code:<10} | {details['name']:<30} | {details['capacity']:<10} | {students_list}")
    print("-" * 80)

def display_all_students():
    print("\n--- All Students ---")
    # Formatted as a neat table using f-string spacing
    print(f"{'ID':<10} | {'Name':<20} | {'Courses List'}")
    print("-" * 60)
    for student_id, details in students.items():
        courses_list = ", ".join(details["courses"]) if details["courses"] else "None"
        print(f"{student_id:<10} | {details['name']:<20} | {courses_list}")
    print("-" * 60)

def display_all_courses():
    print("\n--- All Courses ---")
    # Formatted as a neat table using f-string spacing
    print(f"{'Code':<10} | {'Course Name':<30} | {'Capacity':<10} | {'Students List'}")
    print("-" * 80)
    for course_code, details in courses.items():
        students_list = ", ".join(details["students"]) if details["students"] else "None"
        print(f"{course_code:<10} | {details['name']:<30} | {details['capacity']:<10} | {students_list}")
    print("-" * 80)


# Program running until exit
is_running = True
while is_running:
    print("\n=====================================")
    print("University Course Registration System")
    print("=====================================")
    print("Please Select an Option:")
    print("[1] Add Student")
    print("[2] Add Course")
    print("[3] Register Course")
    print("[4] Drop Course")
    print("[5] Show Student Courses")
    print("[6] Show Course Students")
    print("[7] Display All Students")
    print("[8] Display All Courses")
    print("[9] Exit")
    print("=====================================")
    
    selected_action = input("Enter your choice: ")    
    
    match selected_action:
        case "1":
            add_student()
        case "2":
            add_course()
        case "3":
            register_course()
        case "4":
            drop_course()
        case "5":
            show_student_courses()
        case "6":
            show_course_students()
        case "7":
            display_all_students()
        case "8":
            display_all_courses()
        case "9":
            print("Exiting the system. Goodbye!")
            is_running = False
        case _:
            print("Invalid option. Please try again.")