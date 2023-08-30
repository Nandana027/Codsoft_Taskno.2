import tkinter as tk

class calculator:
    def __init__(self,root):
        self.root=root
        self.root.title("Calcultor")
        self.entry=tk.Entry(root,width=30,borderwidth=5)
        self.entry.grid(row=0,column=0,columnspan=4)
        self.calci_buttons()
        
        
    def calci_buttons(self):
       

        buttons_char=[
            
            '1','2','3','+',
            '4','5','6','-',
            '7','8','9','*',
            '0','=','%','/',
            
        ]

        r=1
        c=0 
        for text in buttons_char:
         tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.click(t)).grid(row=r, column=c)
         c += 1
         if c > 3:
             c= 0
             r+= 1
     
    def click(self,text):
     if text=='=':        
    
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")

     else:
         text_now=self.entry.get()
         self.entry.delete(0,tk.END)
         self.entry.insert(0,text_now+text)

if __name__ == "__main__":
    root = tk.Tk()
    calci = calculator(root)
    root.mainloop()



     
    



   
