class multifunctions():
    def areatriangle(height,bredth):
        height=32
        bredth=34
        print("height=32")
        print("bredth=34")
        print("area formula:(height*bredth)/2")
        area=(32*34)/2
        print("area of triangle:",area)
        return area
    def perimetertriangle(height1,height2,bredth):
        height1=2
        height2=4
        bredth=4
        print("height1=2")
        print("height2=4")
        print("bredth=4")
        print("perimeter of formula:height1+height2+bredth")
        perimeter=height1+height2+bredth
        print("perimeter of triangle: ", perimeter)
        return perimeter

    def subfieldsai():
        list=("Machine learning\nNeural Networks\nvision\nRobotics\nSpeech processing\nNatural language processing")
        print("sub-fields In AI are:")
        print(list)
  
    def percentage():
        a=int(input("subject 1="))
        b=int(input("subject 2="))
        c=int(input("subject 3="))
        d=int(input("subject 4="))
        e=int(input("subject 5="))
        total=a+b+c+d+e
        print("total:",total)
        per=(total/500)*100
        print(per)
        print("percentage:",per)          
    def elgibileformarriage():
        gender=input("Enter your Gender:")
        age=int(input("Enter your Age:"))
        if(gender in ("male")):
            if(age>=21):
                print("eligible")
            else:
                print("not elgible")
        if(gender in ("female")):
            if(age>=18):
                print("elgible")
            else:
                print("not elgible")
    def agecateagery():
        age=int(input("enter the age:"))
        if(age<18):
            print("children")
            cat="chlid"
        elif(age<35):
            print("adult")
            cate="adult"
        elif(age<59):
            print("citizen")
            cate="citizen"
        else:
            print("senier citizen")
            cate="senier citizen"
        return cate    
    
    def bmi():
        bmi=int(input("enter the bmi index:"))
        if(bmi<18.5):
            print("under weight")
            message=("under weight")
        elif(bmi<24.9):
            print("normal")
            message=("normal")
        elif(bmi<29.9):
            print("over weight")
            message("over weight")
        else:
            print("very over weight")
            message=("very over weight")
        return bmi   


      
    