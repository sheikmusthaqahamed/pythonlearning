def test():
    while True:
        num = int(input("Enter the number - \n"))
        try:
            print(12/num)
            False
        except ZeroDivisionError as e:
            print(f"Error - {e}")
            
        except TypeError as e:
            print(f"Error - {e}")
        finally:
            "Do you want to Exit?"
            

test()