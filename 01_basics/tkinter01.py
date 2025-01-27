import tkinter as tk 

def on_submit():
    user_input = entry.get()
    print("You entered: ",user_input)

root = tk.Tk()

root.title("Entry widget Demo")

entry = tk.Entry(root,width = 30)
entry.pack(pady=0)

submit_button =  tk.Button(root,text="Submit",command=on_submit)
submit_button.pack()

root.mainloop()