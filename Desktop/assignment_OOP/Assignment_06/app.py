class Logger:
    def __init__(self):
        print("Object created") # Construtor

    def __del__(self):
        print("Object destroyed") # Destructor

if __name__ == "__main__" :
    log= Logger()
    del log            