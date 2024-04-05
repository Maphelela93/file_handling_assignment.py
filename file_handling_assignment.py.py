# handle file assisgnment

def write_to_file(filename):
    try:
        with open (filename, 'w') as f:
            f.write("This is a weekend special\n")
            f.write("my bree number is 064 7999/n")
            f.write("weekend special on me/n")
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
    except PermissionError:
         print(f"Error: Permission denied to write to '{filename}' .")
    except Exception as e:
        print(f"Error:{e}")
        
    else:
        print('file created and written successfully.')
        
def read_and_display(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print("contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print(f"error: file '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read from '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
        
        
def append_to_file(filename):
    try:
        with open(filename, 'a') as f:
            f.write("\n This is where i draw the line\n")
            f.write("064 7999 i i charge the number\n")
            f.write("yet Mnike Tyle ICU.")
    except FileNotFoundError:
        print(f"Error: file '{filename} not found.")
    except PermissionError:
        print(f"Error: Permission denied to append to '{filename}'.")
    except Exception as e:
        print (f"Error: {e}")
    else:
        print("file appended successfully")
        
if __name__ == "__name__":
    filename = "my_file.txt"
    
    # writing the file
    write_to_file(filename)
    
    # Reading and displaying the file
    read_and_display(filename)
    
    #Appending the file
    append_to_file(filename)
    
    # reading and displaying updated file
    read_and_display(filename)
    
    
        