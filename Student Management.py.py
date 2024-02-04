print("---------1----------------------------------------------------------------------")
print("````````````````````````````SEVENTEEN PUBLIC SCHOOL````````````````````````````")
print("-------------------------------------------------------------------------------")
def check():
    a=int(input("Enter your ad.no:"))
    print("Name         :",l1[a])
    print("Age          :",l2[a])
    print("Blood Group  :",l3[a])
    print("\n")
def add():
    d=input("Enter Name:")
    l1.append(d)
    e=int(input("Enter AGE:"))
    l2.append(e)
    y=input("Enter Blood group:")
    l3.append(y)
    print("\n")
    for n in rang1e(len(l1)):
        print("Name:",l1[n])
        print("Age:",l2[n])
        print("Blood group:",l3[n])
        print("\n")
def delete():
    g=int(input("Enter your admission number:"))
    del l1[g]
    del l2[g]
    del l3[g]
    for m in range(len(l1)):
        print("Name:",l1[m])
        print("Age:",l2[m])
        print("Blood group:",l3[m])
        print("\n")
def exit_details():
    print("thank you")
print("If want to check the your detalis (enter 1)")
print("If you want to add your details (enter 2)")
print("If you want to remove the details(enter 3)")
print("If u want to exit (enter 4)")
l1 = ["Xu Minghao" ,"Wonwoo","Kim Mingyu","Wen Junhui","Joshua","Jeonghan","DK","Scoups","Vernon","Woozi","Hoshi","Seungkwan","Dino"]
l2 = [16,17 ,16,17,16,17,18,17,16,17,18,17,16]
l3 = ["A","B","AB","A","B","O","O","A","AB","O","A","B","A"]
print("\n")
while True:
    f=int(input("Enter the number you want to check: "))
    if f==1:
       check()
    elif f==2:
         add()
    elif f==3:
         delete()
    elif f==4:
        exit()
    u = input("Let's next? (yes/no): ")
    if u == "no":
     exit()
        
    else:
        print("continue")

    








