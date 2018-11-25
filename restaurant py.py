from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="SATYA RESTAURENT ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
CostofFries=0
CostofDrinks=0
CostofNoodles=0
CostofSoup=0
CostBurger=0
CostSandwitch=0
CostofMeal=0
def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())



    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())


    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())


    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())


    CostofFries =CoFries * 140
    CostofDrinks=CoD * 65
    CostofNoodles = CoNoodles* 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger* 260
    CostSandwich=CoSandwich * 300
    cm=(CostofFries+CostofDrinks+CostofNoodles+CostBurger+CostofSoup+CostSandwitch)
    st=cm/99
    pt=cm*0.2
    t=st+pt+cm

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.2)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)

    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    cd=("Cost of Drinks= "+str(CostofDrinks))
    cf=("Cost of Fries= "+str(CostofFries))
    cn=("Cost of Noodles= "+str(CostofNoodles))
    cs=("Cost of Soup= "+str(CostofSoup))
    cb=("Cost of Burger= "+str(CostBurger))
    css=("Cost of Sandwitch= "+str(CostSandwich))
    cm1=("Cost of Meal= "+str(cm))
    st1=("Sevice Tax= "+str(st))
    pt1=("Pay Tax= "+str(pt))
    t1=("Total= "+str(t))





    fobj=open("Billll.txt","w")
    fobj.write(cd)
    fobj.write("\n")
    fobj.write(cf)
    fobj.write("\n")
    fobj.write(cn)
    fobj.write("\n")
    fobj.write(cs)
    fobj.write("\n")
    fobj.write(cb)
    fobj.write("\n")
    fobj.write(css)
    fobj.write("\n")
    fobj.write(cm1)
    fobj.write("\n")
    fobj.write(st1)
    fobj.write("\n")
    fobj.write(pt1)
    fobj.write("\n")
    fobj.write(t1)
    fobj.close()

    fobj1=open("Bill List.txt","a")
    fobj1.write(cd)
    fobj1.write("\n")
    fobj1.write(cf)
    fobj1.write("\n")
    fobj1.write(cn)
    fobj1.write("\n")
    fobj1.write(cs)
    fobj1.write("\n")
    fobj1.write(cb)
    fobj1.write("\n")
    fobj1.write(css)
    fobj1.write("\n")
    fobj1.write(cm1)
    fobj1.write("\n")
    fobj1.write(st1)
    fobj1.write("\n")
    fobj1.write(pt1)
    fobj1.write("\n")
    fobj1.write(t1)
    fobj1.write("\n")
    fobj1.write("\n")
    fobj1.write("\n")
    fobj1.write("\n")
    fobj1.close()




def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
def Save():
    fobj=open("example1.txt","w")
    fobj.write("Just for experiment")

def Saveall():
    Soup.set("")
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="Fries",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)
btnSave=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Save",bg="powder blue",command=Save()).grid(row=7,column=4)
btnSaveall=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Bill List",bg="powder blue",command=Save()).grid(row=8,column=3)

root.mainloop()

