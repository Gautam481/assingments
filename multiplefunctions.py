class multipleFunctions():
    def Subfields():
        print("Subfields in AI are :")
        topics=('Machine Learning','Neural Networks', 'Vision', 'Robotics' ,'Speech Processing' ,'Natural Language Processing')
        return topics
    def oddeven():
        i=(int(input("enter the value -")))
        if (i%2==1):
            print(i,"is a odd number")
            message="ODD NUMBER"
        else:
            print(i,"is a even number")
            message="EVEN NUMBER"
        return message
    def eligibleformen():
        print("Your gender is male")
        age=(int(input(" your age is :")))
        if(age>21):
            print("YOUR ELIGIBLE")
            message="YOUR ELIGIBLE"
        else:
            message="YOUR NOT ELIGIBLE"
            return message
    def eligibleforwomen():
        print("Your gender is female")
        age=(int(input(" your age is :")))
        if(age>18):
            print("YOUR ELIGIBLE")
            message="YOUR ELIGIBLE"
        else:
            message="YOUR NOT ELIGIBLE"
            return message
    def triangle():
        Height=3
        Breath=4
        area=(Height*Breath)/2

        print("area of triangle :",area)

        Height1=3
        Height2=4
        Breadth=45
        Perimeter =(Height1+Height2+Breadth)
        print("perimeter of triangle :" ,Perimeter)

        return (area,Perimeter)
    def percentage():
        subject1=98
        subject2=87
        subject3=95
        subject4=95
        subject5=93
        print("subject1=",subject1)
        print("subject2=",subject2)
        print("subject3=",subject3)
        print("subject4=",subject4)
        print("subject5=",subject5)
        Total=subject1+subject2+subject3+subject4+subject5
        print("Total :",Total)
        percentage=100*Total/500
        print("Percentage :", percentage)