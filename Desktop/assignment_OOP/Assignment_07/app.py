class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public variable
        self._salary = salary      # protected variable
        self.__ssn = ssn           # private variable

if __name__ == "__main__":
    emp = Employee("Amna", 1,4500, "9876674-87-123")

    # Access public variable
    print("Public Variable:", emp.name)

    # Access protected variable
    print("Protected Variable:", emp._salary)

    # Try accessing private variable
    try:
        print("Private Variable:", emp.__ssn)
    except AttributeError:
        print("Cannot access private variable directly: __ssn")




