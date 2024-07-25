
from prettytable import PrettyTable

print("Welcome to the determinants calculator!")

matrix_type = int(input("What is the type of determinant? Type '2' for a 2x2 determinant and '3' for a 3x3 determinant --> "))

if matrix_type == 2:

    a1 = int(input("What is the number in 1st row, 1st column?"))
    a2 = int(input("What is the number in 1st row, 2nd column?"))
    b1 = int(input("What is the number in 2nd row, 1st column?"))
    b2 = int(input("What is the number in 2nd row, 2nd column?"))   

    table = PrettyTable()
    table.field_names = ["X", "C1", "C2"]
    table.add_row(["R1", a1, a2])
    table.add_row(["R2", b1, b2])

   
    det_2x2 = (a1 * b2 ) - (b1 * a2)

    print("Your matrix is --> ")
    print(table)
    print(f"The value of your determinant is {det_2x2}")

else:

    r1c1 = int(input("What is the number in 1st row, 1st column?"))  
    r1c2 = int(input("What is the number in 1st row, 2nd column?")) 
    r1c3 = int(input("What is the number in 1st row, 3rd column?"))
    r2c1 = int(input("What is the number in 2nd row, 1st column?")) 
    r2c2 = int(input("What is the number in 2nd row, 2nd column?"))
    r2c3 = int(input("What is the number in 2nd row, 3rd column?"))
    r3c1 = int(input("What is the number in 3rd row, 1st column?"))
    r3c2 = int(input("What is the number in 3rd row, 2nd column?"))
    r3c3 = int(input("What is the number in 3rd row, 3rd column?"))

    table = PrettyTable()
    table.field_names = ["X", "C1", "C2", "C3"]
    table.add_row(["R1", r1c1, r1c2, r1c3])
    table.add_row(["R2", r2c1, r2c2, r2c3])
    table.add_row(["R3", r3c1, r3c2, r3c3])

    det_3x3 = r1c1 * (r2c2 * r3c3 - r3c2 * r2c3) - r1c2 * (r2c1 * r3c3 - r3c1 * r2c3) + r1c3 * (r2c1 * r3c2 - r3c1 * r2c2)

    print("Your matrix is --> ")
    print(table)
    print(f"The value of your determinant is {det_3x3}")
