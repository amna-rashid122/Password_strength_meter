# Step 1: Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Step 2: Child class
class Teacher(Person):  # Inheriting from Person
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    # Step 3: Display method
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Step 4: Main block
if __name__ == "__main__":
    # Creating object
    teacher = Teacher(" Amna", "Computer")
    teacher.display()

            
