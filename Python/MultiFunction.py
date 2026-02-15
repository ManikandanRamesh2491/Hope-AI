class MultiFunction():
    def Subfields():
        list1=("Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        for temp in list1:
            print(temp)

    def OddEven():
        num=int(input("Enter the number:"))
        if(num % 2 == 0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=="Female"):
            if(age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Invalid Input")

    def percentage():
        m1=float(input("Subject1="))
        m2=float(input("Subject2="))
        m3=float(input("Subject3="))
        m4=float(input("Subject4="))
        m5=float(input("Subject5="))
        total=m1+m2+m3+m4+m5
        percent=(total/500)*100
        print("Total : ",total)
        print("Percentage : ",percent)

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",(Height*Breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Height1+Height2+Breadth)