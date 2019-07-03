import tkinter as Tk
root = Tk()
root.wm_title("Login Window")
root.config(background="#FFFFFF")
class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)#Set __init__ to the master class
        self.grid()
        self.create_main()#Creates function

    def create_main(self):
        print("testing")
        #Title
        self.title = Label(self, text=" Login Form ")
        self.title.grid(row=0, column=2)
        #Username Label
        self.user_entry_label = Label(self, text="Username: ")
        self.user_entry_label.grid(row=1, column=1)
        #Username Entry Box
        self.user_entry = Entry(self)                        
        self.user_entry.grid(row=1, column=2)
        #Password Label
        self.pass_entry_label = Label(self, text="Password: ")
        self.pass_entry_label.grid(row=2, column=1)
        #Password Entry Box
        self.pass_entry = Entry(self)                        
        self.pass_entry.grid(row=2, column=2)
        #Sign In Button
        self.sign_in_butt = Button(self, text="Sign In",command = self.logging_in)
        self.sign_in_butt.grid(row=5, column=2)

    def logging_in(self):
        print("Hi!")
        user_get = self.user_entry.get()#Retrieve Username
        pass_get = self.pass_entry.get()#Retrieve Password

        if user_get == 'Sammy':
            if pass_get == '123':
                print("Welcome!")