import sys
from shape import *
from collections import Counter

database = []  # empty in-memory database
shape_dict = {"shape": 0, "ellipse": 0, "circle": 0, "rhombus": 0} #shape dictionary to keep count of occurrences

#Checking for errors in files and importing data into database
def validate_Shape(content, line):
    content = content.strip()
    list1 = content.split(" ")
    shape_name = ""

    # Checking for invalid shape names
    for key in shape_dict.keys():
        if (key == list1[0].lower()):
            shape_name = key

    if (shape_name == ""):
        print("Error: Invalid shape name on line " + str(line) + ": " + content)
        return False

    # Checking for invalid parameters
    for x in list1[1:]:
        if (int(x) <= 0):
            print("Error: Invalid " + shape_name + " on line " + str(line) + ": " + content)
            return False

    if (shape_name == "shape"):
        database.append(Shape())
    elif (shape_name == "ellipse"):
        database.append(Ellipse(int(list1[1]), int(list1[2])))
    elif (shape_name == "circle"):
        database.append(Circle(int(list1[1])))
    elif (shape_name == "rhombus"):
        database.append(Rhombus(int(list1[1]), int(list1[2])))

    if (shape_name != "shape"):
        shape_dict[shape_name] += 1
    shape_dict["shape"] += 1
    return True

#Load file input by user
def load_file():
    file_name = input("Enter the file name to load: ")
    row = 0
    shape_num = 0
    error_num = 0
    print("\nProcessing <<", file_name, ">>...\n")
    try:
        file = open(file_name, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            row += 1
            if (validate_Shape(line, row) == False):
                error_num += 1
            else:
                shape_num += 1
    except FileNotFoundError:
        print("Error: File not found")
        error_num += 1

    finally:
        print("\nProcessed " + str(row) + " row(s), " + str(shape_num) + " shapes(s) added, " + str(
            error_num) + " error(s)\n")
        file.close()







# -------------- OPERATIONS ----------------------------------------------
# Function to convert the multi-set to a set
def to_set():
    global database
    new_list1 = []
    new_list2 = []

    for i in range(len(database)):
        for j in range(i + 1, len(database)):
            if (database[i].equals(database[j])):
                new_list1.append(database[j])
                shape_name = database[j].__class__.__name__.lower()
                shape_dict[shape_name] -= 1
                if (shape_name != "shape"):
                    shape_dict[shape_name] -= 1
                shape_dict["shape"] -= 1

    for x in database:
        if x not in new_list1:
            new_list2.append(x)
    database = new_list2

    print("Converted Multi-set into a Set! All duplicates removed successfully.")



# Function to save the current database to a file
def save_file():
        file_name = input("Enter the file name to save: ")
        file = open(file_name, 'w')
        try:
            with open(file_name, 'w') as file:
                for x in database:
                    if (x.__class__.__name__.lower() == "shape"):
                        file.write("shape\n")
                    elif (x.__class__.__name__.lower() == "circle"):
                        file.write(f"circle {x.radius} \n")
                    elif (x.__class__.__name__.lower() == "rhombus"):
                        file.write(f"rhombus {x.p} {x.q}\n")
                    elif (x.__class__.__name__.lower() == "ellipse"):
                        file.write(f"ellipse {x.minor} {x.major}\n")
            print("File saved successfully!")
        except IOError:
          print("An error occurred while writing to the file.")
        finally:
            file.close()







# Function to print the current database
def print_database():
    print("Printing the database...")
    if (len(database) != 0):
        for x in database:
            x.print()


# Function to print the summary of the database
def print_summary():
    global database
    print("Printing the summary...")
    print(f"Circle(s): {shape_dict['circle']}")
    print(f"Ellipse(s): {shape_dict['ellipse']}")
    print(f"Rhombus(es): {shape_dict['rhombus']}")
    print(f"Shape(s): {shape_dict['shape']}")


# Function to print the detailed information of the database objects
def print_details():
    global database
    print("Printing the details...")
    database.sort(key=custom_sort_key)
    for x in database:
        class_name = x.__class__.__name__
        if (class_name == "Shape"):
         print(f"{class_name.lower()}")
        elif (class_name == "Circle"):
            print(f"{class_name.lower()} {x.radius}")
        elif (class_name == "Ellipse"):
            print(f"{class_name.lower()} {x.minor} {x.major}")
        elif (class_name == "Rhombus"):
            print(f"{class_name.lower()} {x.p} {x.q}")

#Sort by length of class name followed by sorting by first letter of class name
def custom_sort_key(obj):
    class_name = obj.__class__.__name__
    return (len(class_name), class_name[0])


# ------------------------------------------------------------------------------








#Menu to display choices available
def menu():
    print("\n===== MENU =====")
    print("1. LOAD <file>")
    print("2. TOSET")
    print("3. SAVE")
    print("4. PRINT")
    print("5. SUMMARY")
    print("6. DETAILS")
    print("0. QUIT")

    return input("Enter your choice (0-5): ")


if __name__ == "__main__":
    choice = "1"
    while (choice != "0"):
        choice = menu()
        if (choice == "1"):
            load_file()
        elif (choice != "0" and database == []):
            print("Error: No records found in database. Try loading a file.")
        else:
            #Other operations available to user only if database is not empty
            if (choice == "2"):
               to_set()
            elif (choice == "3"):
              save_file()
            elif (choice == "4"):
              print_database()
            elif (choice == "5"):
               print_summary()
            elif (choice == "6"):
               print_details()
            else:
                print("Invalid Choice. Try again!")

#Exit program
print("Thank you for using our program. Exiting...")
sys.exit(1)
