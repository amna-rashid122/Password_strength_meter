class Student:
    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks



    def display(self):
        print(f"name: {self.name}, Marks: {self.marks}")



if __name__ == "__main__":
    Student1 = Student("Amna" , 89.9)
    Student1.display()