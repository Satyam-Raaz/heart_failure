class TemperatureConverter:
    @staticmethod
    def celsius_to_farenhiet(c):
        c=int(input("enter celsius degree"))
        return 9/5*c+32
    
c=int
print(TemperatureConverter.celsius_to_farenhiet(c))
