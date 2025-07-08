from tkinter import *
import math

import tkinter.messagebox
import cmath

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568")

calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self,num):
        self.result = False
        firstNum = textDisplay.get()
        secondNum = str(num)
        if self.input_value:
            self.current = secondNum
            self.input_value = False
        else:
            if secondNum == '.':
                if secondNum in firstNum:
                    return
            self.current = firstNum + secondNum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(textDisplay.get())
            

    def display(self,value):
        textDisplay.delete(0,END)
        textDisplay.insert(0,value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        if self.op == "pow":
            self.total = pow(self.total,self.current)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def sqroot(self):
        self.result = False
        self.current = math.sqrt(float(textDisplay.get()))
        self.display(self.current)

    def mathsPM(self):
        self.result = False
        self.current = -(float(textDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current =  math.cosh(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current =  math.tan(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current =  math.tanh(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current =  math.sin(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current =  math.sinh(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current =  math.log(float(textDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current =  math.exp(float(textDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current =  math.acosh(float(textDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current =  math.asinh(float(textDisplay.get()))
        self.display(self.current)

    def fact(self):
        self.result = False
        self.current =  math.factorial(float(textDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current =  math.expm1(float(textDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current =  math.lgamma(float(textDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current =  math.degrees(float(textDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current =  math.log2(float(textDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current =  math.log10(float(textDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current =  math.log1p(float(textDisplay.get()))
        self.display(self.current)

    def Clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_entry()
        self.total = 0
        

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
        
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

        
addedValue = Calc()

textDisplay = Entry(calc, font=('arial',20,'bold'),bg="powder blue",bd=30,width="28", justify = RIGHT)
textDisplay.grid(row=0,column=0,columnspan=4,pady=1)
textDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row = j,column = k, pady = 1)

        btn[i]["command"] = lambda x = numberpad[i]: addedValue.numberEnter(x)

        i+=1

#___________________________________
#Standard keys

buttonClear = Button(calc, text="C",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=addedValue.Clear_entry)
buttonClear.grid(row=1,column=0, pady=1)
        
buttonClearAll = Button(calc, text="CE",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=addedValue.all_Clear_Entry)
buttonClearAll.grid(row=1,column=1, pady=1)

buttonSqroot = Button(calc, text="√",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=addedValue.sqroot)
buttonSqroot.grid(row=1,column=2, pady=1)
        
buttonAdd = Button(calc, text="+",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.operation("add"))
buttonAdd.grid(row=1,column=3, pady=1)

buttonSub = Button(calc, text="-",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.operation("sub"))
buttonSub.grid(row=2,column=3, pady=1)

buttonMul = Button(calc, text="*",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.operation("multi"))
buttonMul.grid(row=3,column=3, pady=1)

buttonDiv = Button(calc, text="÷",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.operation("divide"))
buttonDiv.grid(row=4,column=3, pady=1)


buttonZero = Button(calc, text="0",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.numberEnter(0))
buttonZero.grid(row=5,column=0, pady=1)

buttonDot = Button(calc, text=".",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.numberEnter("."))
buttonDot.grid(row=5,column=1, pady=1)

buttonPM = Button(calc, text="±",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=addedValue.mathsPM)
buttonPM.grid(row=5,column=2, pady=1)

buttonEquals = Button(calc, text="=",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.sum_of_total)
buttonEquals.grid(row=5,column=3, pady=1)

#Scientific keys

buttonPi = Button(calc, text="π",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.pi)
buttonPi.grid(row=1,column=4, pady=1)
        
buttonCos = Button(calc, text="cos",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.cos)
buttonCos.grid(row=1,column=5, pady=1)

buttonTan = Button(calc, text="tan",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.tan)
buttonTan.grid(row=1,column=6, pady=1)
        
buttonSin = Button(calc, text="sin",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.sin)
buttonSin.grid(row=1,column=7, pady=1)


button2Pi = Button(calc, text="2π",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.tau)
button2Pi.grid(row=2,column=4, pady=1)

buttonCosh = Button(calc, text="cosh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.cosh)
buttonCosh.grid(row=2,column=5, pady=1)

buttonTanh = Button(calc, text="tanh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.tanh)
buttonTanh.grid(row=2,column=6, pady=1)

buttonSinh = Button(calc, text="sinh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.sinh)
buttonSinh.grid(row=2,column=7, pady=1)


buttonLn = Button(calc, text="ln",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.log)
buttonLn.grid(row=3,column=4, pady=1)

buttonExp = Button(calc, text="Exp",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.exp)
buttonExp.grid(row=3,column=5, pady=1)

buttonMod = Button(calc, text="Mod",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.operation("mod"))
buttonMod.grid(row=3,column=6, pady=1)

buttonE = Button(calc, text="e",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.e)
buttonE.grid(row=3,column=7, pady=1)


buttonLog2 = Button(calc, text="log2",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.log2)
buttonLog2.grid(row=4,column=4, pady=1)

buttonDeg = Button(calc, text="deg",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.degrees)
buttonDeg.grid(row=4,column=5, pady=1)

buttonAcosh = Button(calc, text="acosh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.acosh)
buttonAcosh.grid(row=4,column=6, pady=1)

buttonAsinh = Button(calc, text="asinh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.asinh)
buttonAsinh.grid(row=4,column=7, pady=1)


buttonLog10 = Button(calc, text="log10",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.log10)
buttonLog10.grid(row=5,column=4, pady=1)

buttonLog1p = Button(calc, text="log1p",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.log1p)
buttonLog1p.grid(row=5,column=5, pady=1)

buttonFact = Button(calc, text="x!",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = addedValue.fact)
buttonFact.grid(row=5,column=6, pady=1)

buttonPow = Button(calc, text="pow",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command = lambda: addedValue.operation("pow"))
buttonPow.grid(row=5,column=7, pady=1)



#______________________________

labelDisplay =  Label(calc, text="Scientific Calculator",font=('arial',30,'bold'),justify=CENTER)
labelDisplay.grid(row=0,column=4,columnspan=4)

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Caluclator","Are you sure you want to exit ?")
    if iExit > 0:
        root.destroy()
        return
def Scientific():
    
    root.resizable(width=False, height=False)
    root.geometry("944x568")

def Standard():

    root.resizable(width=False, height=False)
    root.geometry("480x568")

def Quadratic():

    def quad():
        global lab4,lab5
        a = float(e1.get())
        b = float(e2.get())
        c = float(e3.get())

        D = float((b*b)-(4*a*c))

        if D >= 0:
            x1 = float((-b + math.sqrt(D))/(2*a))
            x2 = float((-b - math.sqrt(D))/(2*a))
            lab4 = Label(root2,text="root 1: "+str(x1)+"\nroot 2: "+str(x2),font=('arial',20,'bold'),bg="powder blue",width=27)
        elif D < 0:
            lab4 = Label(root2,text="Roots are imaginary",font=('arial',20,'bold'),bg="powder blue",width=27,height=2)
            
            

        def displayQuad(lab4):
            if D >= 0:
                
                
                lab4.place_forget()
                lab4.place(x=10,y=450)
            elif D < 0:
                
                lab4.place_forget()                  
                
                
                lab4.place(x=10,y=450)
        displayQuad(lab4)
            
            

    
            
    
    root2 = Tk()
    root2.title("Quadratic")
    root2.configure(background="powder blue")
    root2.resizable(width=False, height=False)
    root2.geometry("480x568")

    textQuad1 = Label(root2,text="Quadratic Equation Solver",font=('arial',20,'bold'),bg="powder blue").place(x=60,y=0)
    
    eq = Label(root2,text="ax²+bx+c = 0 (a ≠ 0)",font=('arial',20,'bold'),bg="powder blue").place(x=110,y=50)
    
    lab1 = Label(root2,text="a :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=110)
    e1 = Entry(root2,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e1.place(x=100,y=100)

    lab2 = Label(root2,text="b :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=210)
    e2 = Entry(root2,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e2.place(x=100,y=200)

    lab3 = Label(root2,text="c :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=310)
    e3 = Entry(root2,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e3.place(x=100,y=300)

    submit = Button(root2, text="SUBMIT",font=('arial',20,'bold'),command=quad).place(x=180,y=380)
    
    root2.mainloop()


def Cubic():
    
    def cub():
        global lab5
        
        a = float(e1.get())
        b = float(e2.get())
        c = float(e3.get())
        d = float(e4.get())
        
        e = 2.7182818284590
        f = float(((3*c/a)-(b*b/(a*a)))/3)
        g = float(((2*b*b*b/(a*a*a))-(9*b*c/(a*a))+(27*d/a))/27)
        h = float((g*g/4)+(f*f*f/27))
        i = complex(cmath.sqrt((g*g/4)- h))
        j = complex(cmath.exp(cmath.log10(i)/cmath.log10(e)/3))
        k = complex(cmath.acos((-1)*(g/(2*i))))
        l = complex(j*(-1))
        m = complex(cmath.cos(k/3))
        n = complex(cmath.sqrt(3)*cmath.sin(k/3))
        p = complex((b/3*a)*(-1))
        r = complex((-1)*(g/2)+cmath.sqrt(h))
        s = complex(cmath.exp(cmath.log10(r)/cmath.log10(e)/3))
        t = complex((-1)*(g/2)-cmath.sqrt(h))
        u = complex(cmath.exp(cmath.log10(t)/cmath.log10(e)/3))
        

        if h > 0:
            w = 1
        if h <= 0:
            w = 3
        if ((f==0) and (g==0) and (h==0)):
            w = 2

        if w == 1:
            x1 = complex((s+u)-(b/3*a))
            x2 = complex((-1)*(s+u)/2-(b/3*a))
            x3 = complex((s-u)*cmath.sqrt(3)/2)

            r1 = complex(x1)
            r2 = complex(x2 + i*x3)
            r3 = complex(x2 - i*x3)

            lab5 = Label(root3,text="root 1: "+str(r1)+"\nroot 2: "+str(r2)+"\nroot 3: "+str(r3),font=('arial',15,'bold'),bg="powder blue",width=42)

        if w == 2:
            
            x1 = complex(cmath.exp(cmath.log10(d/a)/cmath.log10(e)/3)*(-1))
            lab5 = Label(root3,text="root is: "+str(r1),font=('arial',15,'bold'),bg="powder blue",width=42, height=2)

        if w == 3:

            x1 = complex(2*j*cmath.cos(k/3)-(b/3*a))
            x2 = complex(l*(m+n)+p)
            x3 = complex(l*(m-n)+p)
            lab5 = Label(root3,text="root 1: "+str(x1)+"\nroot 2: "+str(x2)+"\nroot 3: "+str(x3),font=('arial',15,'bold'),bg="powder blue",width=42)

        def displayCub(lab5):
                
                lab5.place_forget()
                lab5.place(x=10,y=550)

        displayCub(lab5)


    
   
    root3 = Tk()
    root3.title("Cubic")
    root3.configure(background="powder blue")
    root3.resizable(width=False, height=False)
    root3.geometry("520x668")

    textCub1 = Label(root3,text="Cubic Equation Solver",font=('arial',20,'bold'),bg="powder blue").place(x=100,y=0)
    
    eq = Label(root3,text="ax³+bx²+cx+d = 0 (a ≠ 0)",font=('arial',20,'bold'),bg="powder blue").place(x=95,y=50)
    
    lab1 = Label(root3,text="a :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=110)
    e1 = Entry(root3,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e1.place(x=100,y=100)

    lab2 = Label(root3,text="b :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=210)
    e2 = Entry(root3,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e2.place(x=100,y=200)

    lab3 = Label(root3,text="c :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=310)
    e3 = Entry(root3,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e3.place(x=100,y=300)

    lab4 = Label(root3,text="d :",font=('arial',20,'bold'),bg="powder blue").place(x=50,y=410)
    e4 = Entry(root3,font=('arial',20,'bold'),bg="white",bd=10,width="20", justify = RIGHT)
    e4.place(x=100,y=400)
    
    submit = Button(root3, text="SUBMIT",font=('arial',20,'bold'),command=cub).place(x=180,y=470)
    
    root3.mainloop()


def MatrixAdd():
    
    root4 = Tk()
    root4.title("Matrix Addition")
    root4.configure(background="powder blue")
    root4.resizable(width=False, height=False)
    root4.geometry("300x200")

    def matrix2by2():
        root5 = Tk()
        root5.title("2x2 Matrix Addition")
        root5.configure(background="powder blue")
        root5.resizable(width=False, height=False)
        root5.geometry("900x600")
        
        
        textMat2by2 = Label(root5,text="2x2 Matrix Addition",font=('arial',20,'bold'),bg="powder blue").place(x=320,y=10)
        
        laba = Label(root5,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=150,y=50)
        
        pic1 = PhotoImage(master = root5,file="Capture2by2_left.png")
        w1 = Label(root5,image = pic1,bg="powder blue").place(x=10,y=100)

        pic2 = PhotoImage(master = root5,file="Capture2by2_right.png")
        w2 = Label(root5,image = pic2,bg="powder blue").place(x=390,y=100)

        e1 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=112)

        e2 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=112)

        e3 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=40,y=162)

        e4 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=240,y=162)
        
        labPlus = Label(root5,text="+",font=('arial',20,'bold'),bg="powder blue",).place(x=435,y=135)
        labb = Label(root5,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=600,y=50)
        
        pic3 = PhotoImage(master = root5,file="Capture2by2_left.png")
        w3 = Label(root5,image = pic3,bg="powder blue").place(x=460,y=100)

        pic4 = PhotoImage(master = root5,file="Capture2by2_right.png")
        w4 = Label(root5,image = pic4,bg="powder blue").place(x=840,y=100)

        e5 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=490,y=112)

        e6 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=690,y=112)

        e7 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e7.place(x=490,y=162)

        e8 = Entry(root5,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e8.place(x=690,y=162)

        def calculate2by2():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            a4 = float(e4.get())
            b1 = float(e5.get())
            b2 = float(e6.get())
            b3 = float(e7.get())
            b4 = float(e8.get())

            A = [[a1,a2],
                 [a3,a4]]

            B = [[b1,b2],
                 [b3,b4]]

            result = [[0,0],
                      [0,0]]
            for i in range(len(A)):
                for j in range(len(A[0])):
                               result[i][j] = A[i][j] + B[i][j]
                               
            labResult = Label(root5,text="Result: ",font=('arial',20,'bold'),bg="powder blue",).place(x=100,y=375)

            respic1 = PhotoImage(master = root5,file="Capture2by2_left.png")
            resw1 = Label(root5,image = pic3,bg="powder blue").place(x=200,y=340)

            respic2 = PhotoImage(master = root5,file="Capture2by2_right.png")
            resw2 = Label(root5,image = pic4,bg="powder blue").place(x=600,y=340)
            
            r1 = Label(root5,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=230,y=350)

            r2 = Label(root5,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=430,y=350)

            r3 = Label(root5,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=230,y=400)

            r4 = Label(root5,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=430,y=400)
            
            
        submit = Button(root5,text="SUBMIT",font=('arial',20,'bold'),command=calculate2by2).place(x=380,y=250)
        
        
        root5.mainloop()

    


    


    def matrix3by3():
        root6 = Tk()
        root6.title("3x3 Matrix Addition")
        root6.configure(background="powder blue")
        root6.resizable(width=False, height=False)
        root6.geometry("650x800")
        
        
        textMat2by2 = Label(root6,text="3x3 Matrix Addition",font=('arial',20,'bold'),bg="powder blue").place(x=200,y=10)
        
        laba = Label(root6,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=60)
        
        pic1 = PhotoImage(master = root6,file="Capture3by3_left.png")
        w1 = Label(root6,image = pic1,bg="powder blue").place(x=10,y=100)

        pic2 = PhotoImage(master = root6,file="Capture3by3_right.png")
        w2 = Label(root6,image = pic2,bg="powder blue").place(x=590,y=100)

        e1 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=112)

        e2 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=112)

        e3 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=440,y=112)
        
        e4 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=40,y=162)

        e5 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=240,y=162)

        e6 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=440,y=162)

        e7 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e7.place(x=40,y=212)

        e8 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e8.place(x=240,y=212)

        e9 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e9.place(x=440,y=212)
        
        labPlus = Label(root6,text="+",font=('arial',20,'bold'),bg="powder blue").place(x=310,y=270)
        labb = Label(root6,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=300)
        
        pic3 = PhotoImage(master = root6,file="Capture3by3_left.png")
        w3 = Label(root6,image = pic3,bg="powder blue").place(x=10,y=337)

        pic4 = PhotoImage(master = root6,file="Capture3by3_right.png")
        w4 = Label(root6,image = pic4,bg="powder blue").place(x=590,y=337)

        e10 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e10.place(x=40,y=350)

        e11 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e11.place(x=240,y=350)

        e12 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e12.place(x=440,y=350)
        
        e13 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e13.place(x=40,y=400)

        e14 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e14.place(x=240,y=400)

        e15 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e15.place(x=440,y=400)

        e16 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e16.place(x=40,y=450)

        e17 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e17.place(x=240,y=450)

        e18 = Entry(root6,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e18.place(x=440,y=450)

        def calculate3by3():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            a4 = float(e4.get())
            a5 = float(e5.get())
            a6 = float(e6.get())
            a7 = float(e7.get())
            a8 = float(e8.get())
            a9 = float(e9.get())
            
            b1 = float(e10.get())
            b2 = float(e11.get())
            b3 = float(e12.get())
            b4 = float(e13.get())
            b5 = float(e14.get())
            b6 = float(e15.get())
            b7 = float(e16.get())
            b8 = float(e17.get())
            b9 = float(e18.get())

            A = [[a1,a2,a3],
                 [a4,a5,a6],
                 [a7,a8,a9]]

            B = [[b1,b2,b3],
                 [b4,b5,b6],
                 [b7,b8,b9]]

            result = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
            for i in range(len(A)):
                for j in range(len(A[0])):
                               result[i][j] = A[i][j] + B[i][j]
                               
            labResult = Label(root6,text="Result :-",font=('arial',20,'bold'),bg="powder blue").place(x=260,y=566)

            respic1 = PhotoImage(master = root6,file="Capture3by3_left.png")
            resw1 = Label(root6,image = pic3,bg="powder blue").place(x=10,y=597)

            respic2 = PhotoImage(master = root6,file="Capture3by3_right.png")
            resw2 = Label(root6,image = pic4,bg="powder blue").place(x=592,y=597)
            
            r1 = Label(root6,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=40,y=610)

            r2 = Label(root6,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=240,y=610)

            r3 = Label(root6,text=str(result[0][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=440,y=610)

            r4 = Label(root6,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=40,y=660)

            r5 = Label(root6,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r5.place(x=240,y=660)

            r6 = Label(root6,text=str(result[1][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r6.place(x=440,y=660)

            r7 = Label(root6,text=str(result[2][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r7.place(x=40,y=710)

            r8 = Label(root6,text=str(result[2][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r8.place(x=240,y=710)

            r9 = Label(root6,text=str(result[2][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r9.place(x=440,y=710)
            
        submit = Button(root6,text="SUBMIT",font=('arial',20,'bold'),command=calculate3by3).place(x=255,y=510)
        
        
        root6.mainloop()

    textMA = Label(root4,text="Matrix Addition",font=('arial',20,'bold'),bg="powder blue").place(x=55,y=10)
    
    Button1 = Button(root4,text="2x2",font=('arial',20,'bold'),width=5,height=2,command=matrix2by2).place(x=50,y=60)

    Button2 = Button(root4,text="3x3",font=('arial',20,'bold'),width=5,height=2,command=matrix3by3).place(x=170,y=60)


    root4.mainloop()

        
def MatrixMul():
    
    root7 = Tk()
    root7.title("Matrix Multiplication")
    root7.configure(background="powder blue")
    root7.resizable(width=False, height=False)
    root7.geometry("500x500")




    def MM2x1by1x2():
        
        root8 = Tk()
        root8.title("2x1 by 1x2 Matrix Multiplication")
        root8.configure(background="powder blue")
        root8.resizable(width=False, height=False)
        root8.geometry("660x500")
        
        
        textMat2by2 = Label(root8,text="2x1 by 1x2 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=125,y=10)
        
        laba = Label(root8,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=80,y=50)
        
        pic1 = PhotoImage(master = root8,file="Capture2by2_left.png")
        w1 = Label(root8,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=10,y=100)

        pic2 = PhotoImage(master = root8,file="Capture2by2_right.png")
        w2 = Label(root8,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=190,y=100)
        
        e1 = Entry(root8,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=112)

        e2 = Entry(root8,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=40,y=162)

        labMul = Label(root8,text="x",font=('arial',20,'bold'),bg="powder blue",).place(x=240,y=130)
        labb = Label(root8,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=410,y=50)
        
        pic3 = PhotoImage(master = root8,file="Capture2by2_left.png")
        w3 = Label(root8,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=270,y=100)

        pic4 = PhotoImage(master = root8,file="Capture2by2_right.png")
        w4 = Label(root8,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=612,y=100)

        e3 = Entry(root8,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=280,y=132)

        e4 = Entry(root8,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=480,y=132)

        def MMcalculate2x1by1x2():

            a1 = float(e1.get())
            a2 = float(e2.get())
            b1 = float(e3.get())
            b2 = float(e4.get())
            

            A = [[a1],
                 [a2]]

            B = [[b1,b2]]
                 

            result = [[0,0],
                      [0,0]]
                      
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root8,text="Result: ",font=('arial',20,'bold'),bg="powder blue",).place(x=10,y=375)

            respic1 = PhotoImage(master = root8,file="Capture2by2_left.png")
            resw1 = Label(root8,image = pic3,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=110,y=340)

            respic2 = PhotoImage(master = root8,file="Capture2by2_right.png")
            resw2 = Label(root8,image = pic4,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=510,y=340)
            
            r1 = Label(root8,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=140,y=350)

            r2 = Label(root8,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=340,y=350)

            r3 = Label(root8,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=140,y=400)

            r4 = Label(root8,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=340,y=400)

            

            
            
        submit = Button(root8,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate2x1by1x2).place(x=260,y=250)
#--------------------------------------------
    def MM1x2by2x1():
        
        root9 = Tk()
        root9.title("1x2 by 2x1 Matrix Multiplication")
        root9.configure(background="powder blue")
        root9.resizable(width=False, height=False)
        root9.geometry("640x500")
        
        
        textMat2by2 = Label(root9,text="1x2 by 2x1 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=125,y=10)
        
        laba = Label(root9,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=160,y=50)
        
        pic1 = PhotoImage(master = root9,file="Capture2by2_left.png")
        w1 = Label(root9,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=10,y=100)

        pic2 = PhotoImage(master = root9,file="Capture2by2_right.png")
        w2 = Label(root9,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=352,y=100)
        
        e1 = Entry(root9,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=20,y=137)

        e2 = Entry(root9,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=220,y=137)

        labMul = Label(root9,text="x",font=('arial',20,'bold'),bg="powder blue",).place(x=400,y=130)
        labb = Label(root9,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=480,y=50)
        
        pic3 = PhotoImage(master = root9,file="Capture2by2_left.png")
        w3 = Label(root9,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=430,y=100)

        pic4 = PhotoImage(master = root9,file="Capture2by2_right.png")
        w4 = Label(root9,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=580,y=100)

        e3 = Entry(root9,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=444,y=112)

        e4 = Entry(root9,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=444,y=162)

        def MMcalculate1x2by2x1():

            a1 = float(e1.get())
            a2 = float(e2.get())
            b1 = float(e3.get())
            b2 = float(e4.get())
            

            A = [[a1,a2]]
                 

            B = [[b1],
                 [b2]]
                 

            result = [[0]]
                      
                      
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root9,text="Result: ",font=('arial',20,'bold'),bg="powder blue",).place(x=110,y=375)

            respic1 = PhotoImage(master = root9,file="Capture2by2_left.png")
            resw1 = Label(root9,image = pic3,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=220,y=340)

            respic2 = PhotoImage(master = root9,file="Capture2by2_right.png")
            resw2 = Label(root9,image = pic4,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=390,y=340)
            
            r1 = Label(root9,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=230,y=370)

            
        submit = Button(root9,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate1x2by2x1).place(x=260,y=250)
        
#----------------------------------------------    
    def MM2x2by2x2():
            
        
        root10 = Tk()
        root10.title("2x2 by 2x2 Matrix Multiplication")
        root10.configure(background="powder blue")
        root10.resizable(width=False, height=False)
        root10.geometry("900x600")
        
        
        textMat2by2 = Label(root10,text="2x2 by 2x2 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=220,y=10)
        
        laba = Label(root10,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=150,y=50)
        
        pic1 = PhotoImage(master = root10,file="Capture2by2_left.png")
        w1 = Label(root10,image = pic1,bg="powder blue")
        w1.image = pic1 
        w1.place(x=10,y=100)

        pic2 = PhotoImage(master = root10,file="Capture2by2_right.png")
        w2 = Label(root10,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=390,y=100)

        e1 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=112)

        e2 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=112)

        e3 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=40,y=162)

        e4 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=240,y=162)
        
        labMul = Label(root10,text="x",font=('arial',20,'bold'),bg="powder blue",).place(x=435,y=135)
        labb = Label(root10,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=600,y=50)
        
        pic3 = PhotoImage(master = root10,file="Capture2by2_left.png")
        w3 = Label(root10,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=460,y=100)

        pic4 = PhotoImage(master = root10,file="Capture2by2_right.png")
        w4 = Label(root10,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=840,y=100)

        e5 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=490,y=112)

        e6 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=690,y=112)

        e7 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e7.place(x=490,y=162)

        e8 = Entry(root10,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e8.place(x=690,y=162)

        def MMcalculate2x2by2x2():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            a4 = float(e4.get())
            b1 = float(e5.get())
            b2 = float(e6.get())
            b3 = float(e7.get())
            b4 = float(e8.get())

            A = [[a1,a2],
                 [a3,a4]]

            B = [[b1,b2],
                 [b3,b4]]

            result = [[0,0],
                      [0,0]]
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root10,text="Result: ",font=('arial',20,'bold'),bg="powder blue",).place(x=100,y=375)

            respic1 = PhotoImage(master = root10,file="Capture2by2_left.png")
            resw1 = Label(root10,image = pic3,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=200,y=340)

            respic2 = PhotoImage(master = root10,file="Capture2by2_right.png")
            resw2 = Label(root10,image = pic4,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=600,y=340)
            
            r1 = Label(root10,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=230,y=350)

            r2 = Label(root10,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=430,y=350)

            r3 = Label(root10,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=230,y=400)

            r4 = Label(root10,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=430,y=400)
                
        submit = Button(root10,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate2x2by2x2).place(x=380,y=250)


#------------------------------------------------

    def MM3x1by1x3():
        root11 = Tk()
        root11.title("3x1 by 1x3 Matrix Multiplication")
        root11.configure(background="powder blue")
        root11.resizable(width=False, height=False)
        root11.geometry("650x800")
        
        
        textMat2by2 = Label(root11,text="3x1 by 1x3 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=110,y=10)
        
        laba = Label(root11,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=60)
        
        pic1 = PhotoImage(master = root11,file="Capture3by3_left.png")
        w1 = Label(root11,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=220,y=100)

        pic2 = PhotoImage(master = root11,file="Capture3by3_right.png")
        w2 = Label(root11,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=380,y=100)

        e1 = Entry(root11,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=240,y=112)
        
        e2 = Entry(root11,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=162)

        e3 = Entry(root11,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=240,y=212)
        
        labPlus = Label(root11,text="x",font=('arial',20,'bold'),bg="powder blue").place(x=310,y=270)
        labb = Label(root11,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=300)
        
        pic3 = PhotoImage(master = root11,file="Capture3by3_left.png")
        w3 = Label(root11,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=10,y=337)

        pic4 = PhotoImage(master = root11,file="Capture3by3_right.png")
        w4 = Label(root11,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=590,y=337)

        e4 = Entry(root11,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=40,y=400)

        e5 = Entry(root11,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=240,y=400)

        e6 = Entry(root11,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=440,y=400)
        
        

        def MMcalculate3x1by1x3():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            
            b1 = float(e4.get())
            b2 = float(e5.get())
            b3 = float(e6.get())

            A = [[a1],
                 [a2],
                 [a3]]

            B = [[b1,b2,b3]]

            result = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root11,text="Result :-",font=('arial',20,'bold'),bg="powder blue").place(x=260,y=566)

            respic1 = PhotoImage(master = root11,file="Capture3by3_left.png")
            resw1 = Label(root11,image = pic3,bg="powder blue").place(x=10,y=597)

            respic2 = PhotoImage(master = root11,file="Capture3by3_right.png")
            resw2 = Label(root11,image = pic4,bg="powder blue").place(x=592,y=597)
            
            r1 = Label(root11,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=40,y=610)

            r2 = Label(root11,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=240,y=610)

            r3 = Label(root11,text=str(result[0][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=440,y=610)

            r4 = Label(root11,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=40,y=660)

            r5 = Label(root11,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r5.place(x=240,y=660)

            r6 = Label(root11,text=str(result[1][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r6.place(x=440,y=660)

            r7 = Label(root11,text=str(result[2][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r7.place(x=40,y=710)

            r8 = Label(root11,text=str(result[2][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r8.place(x=240,y=710)

            r9 = Label(root11,text=str(result[2][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r9.place(x=440,y=710)
            
        submit = Button(root11,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate3x1by1x3).place(x=255,y=510)
        
        
        root11.mainloop()
#----------------------
    def MM1x3by3x1():
        root12 = Tk()
        root12.title("1x3 by 3x1 Matrix Multiplication")
        root12.configure(background="powder blue")
        root12.resizable(width=False, height=False)
        root12.geometry("650x800")
        
        
        textMat2by2 = Label(root12,text="1x3 by 3x1 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=100,y=10)
        
        laba = Label(root12,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=60)
        
        pic1 = PhotoImage(master = root12,file="Capture3by3_left.png")
        w1 = Label(root12,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=10,y=100)

        pic2 = PhotoImage(master = root12,file="Capture3by3_right.png")
        w2 = Label(root12,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=590,y=100)

        e1 = Entry(root12,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=162)

        e2 = Entry(root12,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=162)

        e3 = Entry(root12,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=440,y=162)
        
        
        labPlus = Label(root12,text="x",font=('arial',20,'bold'),bg="powder blue").place(x=310,y=270)
        labb = Label(root12,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=300)
        
        pic3 = PhotoImage(master = root12,file="Capture3by3_left.png")
        w3 = Label(root12,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=220,y=337)

        pic4 = PhotoImage(master = root12,file="Capture3by3_right.png")
        w4 = Label(root12,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=385,y=337)

        e4 = Entry(root12,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=240,y=350)

        e5 = Entry(root12,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=240,y=400)

        e6 = Entry(root12,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=240,y=450)

        

        def MMcalculate1x3by3x1():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            
            b1 = float(e4.get())
            b2 = float(e5.get())
            b3 = float(e6.get())


            A = [[a1,a2,a3]]
                 

            B = [[b1],
                 [b2],
                 [b3]]

            result = [[0]]
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root12,text="Result :-",font=('arial',20,'bold'),bg="powder blue").place(x=260,y=566)

            respic1 = PhotoImage(master = root12,file="Capture3by3_left.png")
            resw1 = Label(root12,image = pic3,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=210,y=597)
            
            respic2 = PhotoImage(master = root12,file="Capture3by3_right.png")
            resw2 = Label(root12,image = pic4,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=392,y=597)
            
            r1 = Label(root12,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=230,y=655)
            
        submit = Button(root12,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate1x3by3x1).place(x=255,y=510)
        
        
        root12.mainloop()

    def MM3x2by2x3():
        
        root13 = Tk()
        root13.title("3x2 by 2x3 Matrix Multiplication")
        root13.configure(background="powder blue")
        root13.resizable(width=False, height=False)
        root13.geometry("650x800")
        
        
        textMat2by2 = Label(root13,text="3x2 by 2x3 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=100,y=10)
        
        laba = Label(root13,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=60)
        
        pic1 = PhotoImage(master = root13,file="Capture3by3_left.png")
        w1 = Label(root13,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=110,y=100)

        pic2 = PhotoImage(master = root13,file="Capture3by3_right.png")
        w2 = Label(root13,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=490,y=100)

        e1 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=140,y=112)

        e2 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=340,y=112)

        e3 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=140,y=162)

        e4 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=340,y=162)

        e5 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=140,y=212)

        e6 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=340,y=212)

        
        labMul = Label(root13,text="x",font=('arial',20,'bold'),bg="powder blue").place(x=310,y=270)
        labb = Label(root13,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=300)
        
        pic3 = PhotoImage(master = root13,file="Capture3by3_left.png")
        w3 = Label(root13,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=10,y=337)

        pic4 = PhotoImage(master = root13,file="Capture3by3_right.png")
        w4 = Label(root13,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=590,y=337)

        e7 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e7.place(x=40,y=375)

        e8 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e8.place(x=240,y=375)

        e9 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e9.place(x=440,y=375)
        
        e10 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e10.place(x=40,y=425)

        e11 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e11.place(x=240,y=425)

        e12 = Entry(root13,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e12.place(x=440,y=425)


        def MMcalculate3x2by2x3():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            a4 = float(e4.get())
            a5 = float(e5.get())
            a6 = float(e6.get())
                        
            b1 = float(e7.get())
            b2 = float(e8.get())
            b3 = float(e9.get())
            b4 = float(e10.get())
            b5 = float(e11.get())
            b6 = float(e12.get())
            

            A = [[a1,a2],
                 [a3,a4],
                 [a5,a6]]

            B = [[b1,b2,b3],
                 [b4,b5,b6]]

            result = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root13,text="Result :-",font=('arial',20,'bold'),bg="powder blue").place(x=260,y=566)

            respic1 = PhotoImage(master = root13,file="Capture3by3_left.png")
            resw1 = Label(root13,image = respic1,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=10,y=597)

            respic2 = PhotoImage(master = root13,file="Capture3by3_right.png")
            resw2 = Label(root13,image = respic2,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=592,y=597)
            
            r1 = Label(root13,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=40,y=610)

            r2 = Label(root13,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=240,y=610)

            r3 = Label(root13,text=str(result[0][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=440,y=610)

            r4 = Label(root13,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=40,y=660)

            r5 = Label(root13,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r5.place(x=240,y=660)

            r6 = Label(root13,text=str(result[1][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r6.place(x=440,y=660)

            r7 = Label(root13,text=str(result[2][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r7.place(x=40,y=710)

            r8 = Label(root13,text=str(result[2][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r8.place(x=240,y=710)

            r9 = Label(root13,text=str(result[2][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r9.place(x=440,y=710)
            
        submit = Button(root13,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate3x2by2x3).place(x=255,y=510)

        root13.mainloop()
#------------------------------------------------
    def MM2x3by3x2():
        
        root14 = Tk()
        root14.title("2x3 by 3x2 Matrix Multiplication")
        root14.configure(background="powder blue")
        root14.resizable(width=False, height=False)
        root14.geometry("650x800")
        
        
        textMat2by2 = Label(root14,text="2x3 by 3x2 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=125,y=10)
        
        laba = Label(root14,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=60)
        
        pic1 = PhotoImage(master = root14,file="Capture3by3_left.png")
        w1 = Label(root14,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=10,y=100)

        pic2 = PhotoImage(master = root14,file="Capture3by3_right.png")
        w2 = Label(root14,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=590,y=100)

        e1 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=137)

        e2 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=137)

        e3 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=440,y=137)
        
        e4 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=40,y=187)

        e5 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=240,y=187)

        e6 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=440,y=187)
        
        labMul = Label(root14,text="x",font=('arial',20,'bold'),bg="powder blue").place(x=310,y=270)
        labb = Label(root14,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=300)
        
        pic3 = PhotoImage(master = root14,file="Capture3by3_left.png")
        w3 = Label(root14,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=110,y=337)

        pic4 = PhotoImage(master = root14,file="Capture3by3_right.png")
        w4 = Label(root14,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=490,y=337)

        e7 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e7.place(x=140,y=350)

        e8 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e8.place(x=340,y=350)
     
        e9 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e9.place(x=140,y=400)

        e10 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e10.place(x=340,y=400)

        e11 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e11.place(x=140,y=450)

        e12 = Entry(root14,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e12.place(x=340,y=450)

        def MMcalculate2x3by3x2():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            a4 = float(e4.get())
            a5 = float(e5.get())
            a6 = float(e6.get())
                        
            b1 = float(e7.get())
            b2 = float(e8.get())
            b3 = float(e9.get())
            b4 = float(e10.get())
            b5 = float(e11.get())
            b6 = float(e12.get())
            

            A = [[a1,a2,a3],
                 [a4,a5,a6]]

            B = [[b1,b2],
                 [b3,b4],
                 [b5,b6]]

            result = [[0,0],
                      [0,0]]
                      
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root14,text="Result :-",font=('arial',20,'bold'),bg="powder blue").place(x=260,y=566)

            respic1 = PhotoImage(master = root14,file="Capture3by3_left.png")
            resw1 = Label(root14,image = respic1,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=110,y=597)

            respic2 = PhotoImage(master = root14,file="Capture3by3_right.png")
            resw2 = Label(root14,image = respic2,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=492,y=597)
            
            r1 = Label(root14,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=140,y=635)

            r2 = Label(root14,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=340,y=635)

            r3 = Label(root14,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=140,y=685)

            r4 = Label(root14,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=340,y=685)

        submit = Button(root14,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate2x3by3x2).place(x=255,y=510)

        root14.mainloop()
#------------------------------------------------

    def MM3x3by3x3():
        
        root15 = Tk()
        root15.title("3x3 by 3x3 Matrix Multiplication")
        root15.configure(background="powder blue")
        root15.resizable(width=False, height=False)
        root15.geometry("650x800")
        
        
        textMat2by2 = Label(root15,text="3x3 by 3x3 Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=100,y=10)
        
        laba = Label(root15,text="Matrix A",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=60)
        
        pic1 = PhotoImage(master = root15,file="Capture3by3_left.png")
        w1 = Label(root15,image = pic1,bg="powder blue")
        w1.image = pic1
        w1.place(x=10,y=100)

        pic2 = PhotoImage(master = root15,file="Capture3by3_right.png")
        w2 = Label(root15,image = pic2,bg="powder blue")
        w2.image = pic2
        w2.place(x=590,y=100)

        e1 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e1.place(x=40,y=112)

        e2 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e2.place(x=240,y=112)

        e3 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e3.place(x=440,y=112)
        
        e4 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e4.place(x=40,y=162)

        e5 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e5.place(x=240,y=162)

        e6 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e6.place(x=440,y=162)

        e7 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e7.place(x=40,y=212)

        e8 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e8.place(x=240,y=212)

        e9 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e9.place(x=440,y=212)

        
        labMul = Label(root15,text="x",font=('arial',20,'bold'),bg="powder blue").place(x=310,y=270)
        labb = Label(root15,text="Matrix B",font=('arial',15,'bold'),bg="powder blue").place(x=280,y=300)
        
        pic3 = PhotoImage(master = root15,file="Capture3by3_left.png")
        w3 = Label(root15,image = pic3,bg="powder blue")
        w3.image = pic3
        w3.place(x=10,y=337)

        pic4 = PhotoImage(master = root15,file="Capture3by3_right.png")
        w4 = Label(root15,image = pic4,bg="powder blue")
        w4.image = pic4
        w4.place(x=590,y=337)

        e10 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e10.place(x=40,y=350)

        e11 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e11.place(x=240,y=350)

        e12 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e12.place(x=440,y=350)
        
        e13 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e13.place(x=40,y=400)

        e14 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e14.place(x=240,y=400)

        e15 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e15.place(x=440,y=400)

        e16 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e16.place(x=40,y=450)

        e17 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e17.place(x=240,y=450)

        e18 = Entry(root15,font=('arial',20,'bold'),bg="white",bd=5,width="10", justify = RIGHT)
        e18.place(x=440,y=450)


        def MMcalculate3x3by3x3():
            
            a1 = float(e1.get())
            a2 = float(e2.get())
            a3 = float(e3.get())
            a4 = float(e4.get())
            a5 = float(e5.get())
            a6 = float(e6.get())
            a7 = float(e7.get())
            a8 = float(e8.get())
            a9 = float(e9.get())
            
            b1 = float(e10.get())
            b2 = float(e11.get())
            b3 = float(e12.get())
            b4 = float(e13.get())
            b5 = float(e14.get())
            b6 = float(e15.get())
            b7 = float(e16.get())
            b8 = float(e17.get())
            b9 = float(e18.get())

            A = [[a1,a2,a3],
                 [a4,a5,a6],
                 [a7,a8,a9]]

            B = [[b1,b2,b3],
                 [b4,b5,b6],
                 [b7,b8,b9]]

            result = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
                               
            labResult = Label(root15,text="Result :-",font=('arial',20,'bold'),bg="powder blue").place(x=260,y=566)

            respic1 = PhotoImage(master = root15,file="Capture3by3_left.png")
            resw1 = Label(root15,image = respic1,bg="powder blue")
            resw1.image = respic1
            resw1.place(x=10,y=597)

            respic2 = PhotoImage(master = root15,file="Capture3by3_right.png")
            resw2 = Label(root15,image = respic2,bg="powder blue")
            resw2.image = respic2
            resw2.place(x=592,y=597)
            
            r1 = Label(root15,text=str(result[0][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r1.place(x=40,y=610)

            r2 = Label(root15,text=str(result[0][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r2.place(x=240,y=610)

            r3 = Label(root15,text=str(result[0][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r3.place(x=440,y=610)

            r4 = Label(root15,text=str(result[1][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r4.place(x=40,y=660)

            r5 = Label(root15,text=str(result[1][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r5.place(x=240,y=660)

            r6 = Label(root15,text=str(result[1][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r6.place(x=440,y=660)

            r7 = Label(root15,text=str(result[2][0]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r7.place(x=40,y=710)

            r8 = Label(root15,text=str(result[2][1]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r8.place(x=240,y=710)

            r9 = Label(root15,text=str(result[2][2]),font=('arial',20,'bold'),bg="powder blue",bd=5,width="10", justify = RIGHT)
            r9.place(x=440,y=710)
            
        submit = Button(root15,text="SUBMIT",font=('arial',20,'bold'),command=MMcalculate3x3by3x3).place(x=255,y=510)

        root15.mainloop()

    
        

#------------------------------------------------
    textMA = Label(root7,text="Matrix Multiplication",font=('arial',20,'bold'),bg="powder blue").place(x=120,y=10)
    
    Button1 = Button(root7,text="2x1 by 1x2",font=('arial',20,'bold'),width=10,height=2,command=MM2x1by1x2).place(x=50,y=60)

    Button2 = Button(root7,text="1x2 by 2x1",font=('arial',20,'bold'),width=10,height=2,command=MM1x2by2x1).place(x=270,y=60)

    Button3 = Button(root7,text="2x2 by 2x2",font=('arial',20,'bold'),width=10,height=2,command=MM2x2by2x2).place(x=50,y=160)

    Button4 = Button(root7,text="3x1 by 1x3",font=('arial',20,'bold'),width=10,height=2,command=MM3x1by1x3).place(x=270,y=160)

    Button5 = Button(root7,text="1x3 by 3x1",font=('arial',20,'bold'),width=10,height=2,command=MM1x3by3x1).place(x=50,y=260)

    Button6 = Button(root7,text="3x2 by 2x3",font=('arial',20,'bold'),width=10,height=2,command=MM3x2by2x3).place(x=270,y=260)

    Button7 = Button(root7,text="2x3 by 3x2",font=('arial',20,'bold'),width=10,height=2,command=MM2x3by3x2).place(x=50,y=360)

    Button8 = Button(root7,text="3x3 by 3x3",font=('arial',20,'bold'),width=10,height=2,command=MM3x3by3x3).place(x=270,y=360)

    root7.mainloop()
#---------------------------


def Permutations():
    
    root16 = Tk()
    root16.title("Permutations")
    root16.configure(background="powder blue")
    root16.resizable(width=False, height=False)
    root16.geometry("400x300")

    textProb = Label(root16,text="Permutations",font=('arial',20,'bold'),bg="powder blue").place(x=110,y=10)
    textnpr = Label(root16,text="ⁿPᵣ (n >= r)",font=('arial',20,'bold'),bg="powder blue").place(x=130,y=40)
        
    laba = Label(root16,text="n:",font=('arial',20,'bold'),bg="powder blue").place(x=10,y=80)
    labb = Label(root16,text="r:",font=('arial',20,'bold'),bg="powder blue").place(x=10,y=130)

    e1 = Entry(root16,font=('arial',20,'bold'),bg="white",bd=5,width="22", justify = RIGHT)
    e1.place(x=40,y=80)

    e2 = Entry(root16,font=('arial',20,'bold'),bg="white",bd=5,width="22", justify = RIGHT)
    e2.place(x=40,y=130)

    def calculateNPR():
        
        n = float(e1.get())
        r = float(e2.get())
        npr = math.factorial(int(n))/math.factorial(int(n-r))
        labres = Label(root16,text="Result: "+str(npr),font=('arial',15,'bold'),bg="powder blue").place(x=10,y=250)

    submit = Button(root16,text="SUBMIT",font=('arial',20,'bold'),command=calculateNPR).place(x=135,y=180)

def Combinations():
    
    root17 = Tk()
    root17.title("Combinations")
    root17.configure(background="powder blue")
    root17.resizable(width=False, height=False)
    root17.geometry("400x300")

    textProb = Label(root17,text="Combinations",font=('arial',20,'bold'),bg="powder blue").place(x=110,y=10)
    textnpr = Label(root17,text="ⁿCᵣ (n >= r)",font=('arial',20,'bold'),bg="powder blue").place(x=130,y=40)
        
    laba = Label(root17,text="n:",font=('arial',20,'bold'),bg="powder blue").place(x=10,y=80)
    labb = Label(root17,text="r:",font=('arial',20,'bold'),bg="powder blue").place(x=10,y=130)

    e1 = Entry(root17,font=('arial',20,'bold'),bg="white",bd=5,width="22", justify = RIGHT)
    e1.place(x=40,y=80)

    e2 = Entry(root17,font=('arial',20,'bold'),bg="white",bd=5,width="22", justify = RIGHT)
    e2.place(x=40,y=130)

    def calculateNCR():
        
        n = float(e1.get())
        r = float(e2.get())
        npr = math.factorial(int(n))/math.factorial(int(n-r))
        ncr = int(npr)/math.factorial(int(r))
        labres = Label(root17,text="Result: "+str(ncr),font=('arial',15,'bold'),bg="powder blue").place(x=10,y=250)

    submit = Button(root17,text="SUBMIT",font=('arial',20,'bold'),command=calculateNCR).place(x=135,y=180)        
    

menubar = Menu(calc)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label="Standard",command=Standard)
filemenu.add_command(label="Scientific",command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)


polymenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Polynomails", menu=polymenu)
polymenu.add_command(label="Quadratic",command=Quadratic)
polymenu.add_command(label="Cubic",command=Cubic)

matrixmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Matrix", menu=matrixmenu)
matrixmenu.add_command(label="Addition",command=MatrixAdd)
matrixmenu.add_command(label="Multiplication",command=MatrixMul)

Probmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Probability", menu=Probmenu)
Probmenu.add_command(label="Permutations",command=Permutations)
Probmenu.add_command(label="Combinations",command=Combinations)



root.config(menu=menubar)
root.mainloop()
