def test():
    
   
    try:
        return (12/0)
    except Exception as e:
        print("e1")
        return e
    finally:
        print("rgvfb")
        #return ("Finally Block")

#ONLY ONE RETURN IS RETURNED
print(test())