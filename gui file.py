import tkinter as ttk
app= ttk.TK()
app.title('Solar Radiation Prediction')
app.geometry('600X400')
app.title('solar radiation prediction')
ttk.Label(app,text='Enter Date',font=('Arial',20)).place(x=140,y=50)
day=ttk.Variable(app)
ttk.Label(app,text='Select Date').place(x=60,y=100)
ttk.OptionMenu(app,day,*list(range(1,31))).place(x=60,y=130)
month=ttk.Variable(app)
name=[['January'],['Feburary'],['March'],['April'],['May'],['June'],['july'],['August'],['September'],['October'],['November'],['December']]
ttk.Label(app,text='Select Month').place(x=140,y=100)
ttk.OptionMenu(app,month,*name).place(x=140,y=130)
year=ttk.Variable(app)


def show():
  #  dayw=day.get()
   # monthw=month.get()
   # spl=str(df['date'].split('-'))
 #   print(spl)

  result = ttk.Variable(app)
  result.set('solar radiation')
  ttk.Label(app,textvariable=result).place(x=230,y=100)
  ttk.Button(app,text='Show',command=show).place(x=230,y=130)

app.mainloop()