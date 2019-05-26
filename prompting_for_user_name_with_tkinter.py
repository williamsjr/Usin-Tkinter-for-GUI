from tkinter import *

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("300x200")
       self.master.title("My GUI")
       self.grid()

       self.prompt = Label(self, text = "What's your name? ")
       self.prompt.grid(row = 0, column = 0)

       self.input = Entry(self)
       self.input.grid(row = 0, column = 1, padx = 10)

       self.button_submit = Button( self, text = "Submit",
           command = self.submit)
       self.button_submit.grid(columnspan = 2, pady = 10)

       self.my_text = StringVar()
       
       self.message = Label(self, textvariable = self.my_text)
       self.message.grid(row = 3, column = 0)

   def submit(self):
       output = "Hi " + self.input.get()
       self.my_text.set(output)
                    
       

frame02 = MyFrame()
frame02.mainloop()
