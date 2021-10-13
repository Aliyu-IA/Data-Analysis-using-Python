import tkinter as tk
from tkinter import Canvas, DoubleVar, Frame, StringVar, ttk
import tkinter
from tkinter.constants import ANCHOR, BOTH, HORIZONTAL, LEFT, RIGHT, VERTICAL, Y
from tkinter import messagebox
from tkinter import *


root = tk.Tk()
console = tk.Text(root)
console.grid(row=0, column=0)
root.title("Decision Support System")

root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

my_canvas = Canvas(root)
my_canvas.grid(row = 0, column = 0, sticky = "news")

#Scrollbar Vertical
v_scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = my_canvas.yview)
v_scrollbar.grid(row = 0, column = 1, sticky="ns")
my_canvas.configure(yscrollcommand = v_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#Scrollbar Horizontal
h_scrollbar = ttk.Scrollbar(root, orient = HORIZONTAL, command = my_canvas.xview)
h_scrollbar.grid(row = 1, column = 0, sticky="ew")
my_canvas.configure(xscrollcommand = h_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#create a Main Frame
main_frame = tk.Frame(my_canvas)
main_frame.grid(row = 0, column = 0, sticky = "nsew")


# Labels
tk.Label(main_frame, text="Decision Support System", font="helvetica 18 bold").grid(
    column=0, row=0, sticky="w", padx=500)
tk.Label(main_frame, text="""This is a simple application that will help in decision making on whether to adopt a technology based on criteria listed below, you are rate each criteria 1-5
1- Strongly disagree, 2- Disagree, 3- Neutral, 4-Agree, 5- Strongly agree""", font="Arial 10").grid(column=0, row=1, sticky="w", padx=250)
tk.Label(main_frame, text="What type of technology are you trying to invest in?").grid(
    column=0, row=2, sticky="w", pady=20, padx=10)
tk.Label(main_frame, text="CA1- Technological Predictors, Group score[35], Coefficient = 0.200",font="helvetica 11 bold").grid(
    column=0, row=3, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="Ca1.1- Level of training required : is training of staff going to be thorough?").grid(
    column=0, row=4, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca1.2- Proven technology effectiveness : is there documented evidence showing the technology is effective?").grid(
    column=0, row=5, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca1.3- Having the required features : does the technology have the essential feature(s) to perform specified task?").grid(
    column=0, row=6, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca1.4- Client demand to use a technology : will the technology meet client’s demands?").grid(
    column=0, row=7, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca1.5- Technology reliability : is there evidence that the technology will consistently meets performance requirements?").grid(
    column=0, row=8, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca1.6- Technology durability : is there available evidence indicating that this technology has a long shelf life?").grid(
    column=0, row=9, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca1.7- Government policy and regulation : will the technology help meet stipulated regulatory requirements?").grid(
    column=0, row=10, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="CA2- Managerial Predictors, Group score[20], Coefficient = 0.197",font="helvetica 11 bold").grid(
    column=0, row=11, sticky="w", pady=20, padx=10)
tk.Label(main_frame, text="ca2.1- Top management degree of involvement : will the management support the use of this technology?").grid(
    column=0, row=12, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca2.2- Versatility : will the technology features improve other performance indicators (e.g. work quality)?").grid(
    column=0, row=13, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca2.3- Organizations technology budget : is the technology within the organization's budget?").grid(
    column=0, row=14, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="""ca2.4- Level of compatibility with current processes : will the technology be interoperable with existing technologies and 
would it should fit in seamlessly into our current operations?""").grid(
    column=0, row=15, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca2.5- Potential cost savings : will the technology have the potential to reduce project cost?").grid(
    column=0, row=16, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca2.6- Competitive advantage : will the technology have a positive impact on the company’s core competency?").grid(
    column=0, row=17, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="CA3- Organizational Predictors, Group score[15], Coefficient = 0.195",font="helvetica 11 bold").grid(
    column=0, row=18, sticky="w", pady=20, padx=10)
tk.Label(main_frame, text="ca3.1- Technology adoption?").grid(
    column=0, row=19, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca3.2- Organization culture : is the company's employees open to trying new technologies?").grid(
    column=0, row=20, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca3.3- Industry-level change requires?").grid(
    column=0, row=21, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="CA4- Cost Predictors, Group score[10], Coefficient = 0.202",font="helvetica 11 bold").grid(
    column=0, row=22, sticky="w", pady=20, padx=10)
tk.Label(main_frame, text="ca4.1- Capital cost of technology").grid(
    column=0, row=23, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca4.2- Level of technical support available : If required, will there be technical support readily available?").grid(
    column=0, row=24, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="CA5- Technical Predictors, Group score[10], Coefficient = 0.205",font="helvetica 11 bold").grid(
    column=0, row=25, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca5.1- Level of complexity : is the technology easy to use?").grid(
    column=0, row=26, sticky="w", pady=10, padx=10)
tk.Label(main_frame, text="ca5.2- Observability : have the performance of this technology be observed before investing?").grid(
    column=0, row=27, sticky="w", pady=10, padx=10)

e1=StringVar()
e2=IntVar()
e3=IntVar()
e4=IntVar()
e5=IntVar()
e6=IntVar()
e7=IntVar()
e8=IntVar()
e9=IntVar()
e10=IntVar()
e11=IntVar()
e12=IntVar()
e13=IntVar()
e14=IntVar()
e15=IntVar()
e16=IntVar()
e17=IntVar()
e18=IntVar()
e19=IntVar()
e20=IntVar()
e21=IntVar()

#Text Input
my_entry1= tk.Entry(main_frame, textvariable=e1, width=20, borderwidth=2)
my_entry1.grid(column=0, row=2, padx=800)
my_entry2= tk.Entry(main_frame, textvariable=e2, width=20, borderwidth=2)
my_entry2.grid(column=0, row=4)
my_entry3=tk.Entry(main_frame, textvariable=e3, width=20, borderwidth=2)
my_entry3.grid(column=0, row=5)
my_entry4=tk.Entry(main_frame, textvariable=e4, width=20, borderwidth=2)
my_entry4.grid(column=0, row=6)
my_entry5=tk.Entry(main_frame, textvariable=e5, width=20, borderwidth=2)
my_entry5.grid(column=0, row=7)
my_entry6=tk.Entry(main_frame, textvariable=e6, width=20, borderwidth=2)
my_entry6.grid(column=0, row=8)
my_entry7=tk.Entry(main_frame, textvariable=e7, width=20, borderwidth=2)
my_entry7.grid(column=0, row=9)
my_entry8=tk.Entry(main_frame, textvariable=e8, width=20, borderwidth=2)
my_entry8.grid(column=0, row=10)
my_entry9=tk.Entry(main_frame, textvariable=e9, width=20, borderwidth=2)
my_entry9.grid(column=0, row=12)
my_entry10=tk.Entry(main_frame, textvariable=e10, width=20, borderwidth=2)
my_entry10.grid(column=0, row=13)
my_entry11=tk.Entry(main_frame, textvariable=e11, width=20, borderwidth=2)
my_entry11.grid(column=0, row=14)
my_entry12=tk.Entry(main_frame, textvariable=e12, width=20, borderwidth=2)
my_entry12.grid(column=0, row=15)
my_entry13=tk.Entry(main_frame, textvariable=e13, width=20, borderwidth=2)
my_entry13.grid(column=0, row=16)
my_entry14=tk.Entry(main_frame, textvariable=e14, width=20, borderwidth=2)
my_entry14.grid(column=0, row=17)
my_entry15=tk.Entry(main_frame, textvariable=e15, width=20, borderwidth=2)
my_entry15.grid(column=0, row=19)
my_entry16=tk.Entry(main_frame, textvariable=e16, width=20, borderwidth=2)
my_entry16.grid(column=0, row=20)
my_entry17=tk.Entry(main_frame, textvariable=e17, width=20, borderwidth=2)
my_entry17.grid(column=0, row=21)
my_entry18=tk.Entry(main_frame, textvariable=e18, width=20, borderwidth=2)
my_entry18.grid(column=0, row=23)
my_entry19=tk.Entry(main_frame,  textvariable=e19,width=20, borderwidth=2)
my_entry19.grid(column=0, row=24)
my_entry20=tk.Entry(main_frame, textvariable=e20, width=20, borderwidth=2)
my_entry20.grid(column=0, row=26)
my_entry21=tk.Entry(main_frame, textvariable=e21, width=20, borderwidth=2)
my_entry21.grid(column=0, row=27)

def click():
    CA1 = e2.get()+e3.get()+e4.get()+e5.get()+e6.get()+e7.get()+e8.get()
    CA2 = e9.get()+e10.get()+e11.get()+e12.get()+e13.get()+e14.get()
    CA3 = e15.get()+e16.get()+e17.get()
    CA4 = e18.get()+e19.get()
    CA5 = e20.get()+e21.get()
    ictai = 19.91
    coefCa1 = 0.200
    coefCa2 = 0.197
    coefCa3 = 0.195
    coefCa4 = 0.202
    coefCa5 = 0.205
    APS = CA1*coefCa1 + CA2*coefCa2 + CA3*coefCa3 + CA4*coefCa4 + CA5*coefCa5
    apsrd = round(APS, 2)
    perScore = APS/ictai*100
    rdscore = round(perScore, 2)
    if perScore > 65:
        outputLb1.config(text=f"{e1.get()} will be successful when adopted, \n An accumulated score of at least 65% indicates that the evaluated technology would likely be successful if adopted (Goodrum et al. 2011)")
        outputLb2.config(text= f"Adoption Prediction score(ICTAI): {apsrd}")
        outputLb3.config(text=f" % Relative to maximun score: {rdscore} %" )
    else:
        outputLb1.config(text=f"Sorry, {e1.get()} would not fit the organization's processes. \n An accumulated score of at least 65% must be obtained, this will indicate that the evaluated technology would likely be successful if adopted (Goodrum et al. 2011)")
        outputLb2.config(text= f"Adoption Prediction score(ICTAI): {apsrd}")
        outputLb3.config(text=f" % Relative to maximun score: {rdscore} %" )


outputLb1=tk.Label(main_frame, fg="green", font="Arial 10")
outputLb1.grid(row=32, column=0, sticky="w")
outputLb2 = tk.Label(main_frame,fg="green", font="Arial 10")
outputLb2.grid(row=33, column=0, sticky="w")
outputLb3 = tk.Label(main_frame,fg="green", font="Arial 10")
outputLb3.grid(row=34, column=0, sticky="w")


#Button
my_button = tk.Button(main_frame,text="Decide!", command=click, width=20, borderwidth=5, bg="yellow")
my_button.grid(column=0, row=30)

my_canvas.create_window((0,0), window = main_frame, anchor = "nw")


# #GUI window
root.geometry("1024x500")
root.mainloop()
