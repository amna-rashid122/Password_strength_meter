class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start_car(self):  # Correct indentation
        self.engine.start()

if __name__ == "__main__":
    my_car = Car()
    my_car.start_car()  # Call the method

