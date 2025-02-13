def test(num):
    try:
        print(12/num)
        
    except ZeroDivisionError as e:
        print(f"Error - {e}")
    except TypeError as e:
        print(f"Error - {e}")
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error2 - {e}")
    finally:
        print("Thank you")

test("d")