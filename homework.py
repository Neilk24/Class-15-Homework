def perimeter_rec(length,width):
    return 2*(length+width)
def area_rec(length,width):
    return length*width
def circum_cir(radius):
    return 2*radius*3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482
def area_cir(radius):
    return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482*(radius**2)

print("Enter the choice you want: ")
print("")
print("a. perimeter of a rectangle")
print("b. area of a rectangle")
print("c. circumference of a circle")
print("d. area of a circle")
print("")

choice=str(input("Please choose(a/b/c/d): "))

if choice=='a':
    length=float(input("Enter the number you want as the length of the rectangle: "))
    width=float(input("Enter the number you want as the width of the rectangle: "))
    print("The perimeter of your rectangle is",perimeter_rec(length,width))

elif choice=='b':
    length=float(input("Enter the number you want as the length of the rectangle: "))
    width=float(input("Enter the number you want as the width of the rectangle: "))
    print("The area of your rectangle is",area_rec(length,width))

elif choice=='c':
    radius=float(input("Enter the number you want as the radius: "))
    print("The circumference of your circle is: ",circum_cir(radius))

elif choice=='d':
    radius=float(int(input("Enter the number you want as the radius: ")))
    print("The area of your circle is: ",area_cir(radius))

else:
    print("This is not a valid input. PLease try again.")