class Dog:
    def __init__(self, name, breed):
        self.name = name  # instance variable
        self.breed = breed  # instance variable

    def bark(self):  # instance method
        print(f"{self.name} is barking!")

if __name__ == "__main__":
    my_dog = Dog("Tommy", "Golden Retriever")
    # call the method
    my_dog.bark()
        
