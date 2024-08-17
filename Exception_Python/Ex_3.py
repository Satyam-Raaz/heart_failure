def operate(num):
    try:
        result=5/num
    except:
        print("cannot divide a number by zero")
    finally:
        print("this part of the code always executed")

operate(2)
operate(0)        