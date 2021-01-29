#python program which accepts the radius of a circle 
radius=float(input("Input the circle of radius :"))
area=((22/7)*radius*radius)
print("The area of the circle with radius",radius,"is:",area)
#file extension
filename = input("Input the Filename: ")
file_ext = filename.split(".")
print ("The extension of the file is : " + file_ext[-1])

