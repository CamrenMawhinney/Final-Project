#Camren Mawhinney
#Final Project
#Sept 2021

from tkinter import *
root = Tk()
root.title("Camren's Pizza") #Window title Camren's Pizza
v = DoubleVar()
menubar = Menu(root)
label_1 = Label(root, text="Name") #input name and address
label_2 = Label(root, text="Address")
x=StringVar()
y=StringVar()
entry_1 = Entry(root,textvariable=x)
entry_2 = Entry(root,textvariable=y)
label_1.pack(anchor=N, side=LEFT, fill=X, expand=YES)
entry_1.pack(side=TOP, anchor=W, fill=X, expand=YES)
label_2.pack(side=LEFT,anchor=N, fill=X, expand=YES)
entry_2.pack(side=TOP, anchor=W, fill=X, expand=YES)
c = Checkbutton(root, text = "Save my order for future use")
c.pack(side=BOTTOM)
sz = Label(root, text="Select the pizza size", bg="black", fg="white")
sz.pack(side=TOP, anchor=W, expand=YES)
small = Radiobutton(root, text="Small ($7.95)", variable=v, value=7.95).pack(anchor=W)
medium = Radiobutton(root, text="Medium ($9.95)", variable=v, value=9.95).pack(anchor=W)
large = Radiobutton(root, text="Large ($13.99)", variable=v, value=13.99).pack(anchor=W)
tp = Label(root, text="Select toppings. ($0.75 each)", bg="black", fg="white")
tp.pack(anchor=W)
Toppings = {"Pepperoni":1, "Extra Cheese":2, "Olives":3, "Tomatoes":4, "Grilled chicken":5,"Bacon":6}
s = StringVar()
s.set("Toppings")
c=IntVar()
ar=[]
for i in range (6):
    ar.append(DoubleVar()) # creating an array of DoubleVar to store radiobtn values
i=0
for te in Toppings:
    b = Radiobutton(root, text=te, variable=ar[i],value=0.75) # setting the radio btns
    b.pack()
    i+=1
    #var1 = te+ str(int)
    #var1 = IntVar()

    #Checkbutton(root, text=te, variable=var1).pack()
   
   
a=StringVar()
tip = Label(root, text="Tip amount").pack()
Entry(root,textvariable=a).pack()
def display():
    name=x.get()
    adress=y.get()
    p_cost=v.get()
    s=0
    for i in ar: # calculating topping bill
        s+=i.get()
    tip=int(a.get())
    total=s+p_cost+tip
    Label(root,text="...bill...", bg="black", fg="white").pack()
    Label(root, text="Name - "+name).pack()
    Label(root, text="Address - "+adress).pack()
    Label(root, text="Pizza cost - "+str(p_cost)).pack()
    Label(root, text="Topping cost - "+str(s)).pack()
    Label(root, text="Tip - "+str(tip)).pack()
    Label(root, text="Total - "+str(total)).pack()
button1=Button(root,text="submit",command=display,width=10).pack()
root.mainloop()
