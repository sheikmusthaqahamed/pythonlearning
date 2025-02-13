def test():
    while True:
        num = int(input("Enter the number - \n"))
        try:
            print(12/num)
            break
        except ZeroDivisionError as e:
            print(f"Error - {e}")
            continue
        except TypeError as e:
            print(f"Error - {e}")
            continue

test()