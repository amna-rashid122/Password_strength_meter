class TemperatureConverter():
    @staticmethod
    def celsius_to_fahrenheit(c):
        return(c*9/5) +32
    
if __name__ == "__main__":
    print("fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(0))    
    print("fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(100))    