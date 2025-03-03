
file_var = open("ran.html","w")
# file_var.write("<html> ")

var = "Sheik"

file_var.writelines(f"""
                    <html><head></head><body><p>Hello Team! I am {var}</p>
                    <input type="text" name="name" value="Enter your name">
                    <br>
                    <input type="submit" value="Submit"></body></html>>""")
file_var.close()