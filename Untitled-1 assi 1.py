def add_student(students):
  name = input("Enter the student's name: ")
  students.append(name)
  print(f"{name} added to the list.")

def remove_student(students):
  name = input("Enter the student's name to remove: ")
  if name in students:
    students.remove(name)
    print(f"{name} removed from the list.")
  else:
    print(f"{name} is not in the list.")

def display_students(students):
  if not students:
    print("The list is empty.")
  else:
    print("Student List:")
    for student in students:
      print(student)

def main():
  students = []
  while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Display students")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
      add_student(students)
    elif choice == 2:
      remove_student(students)
    elif choice == 3:
      display_students(students)
    elif choice == 4:
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()