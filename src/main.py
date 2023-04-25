import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont


class App(tk.Tk):

    def __init__(self, **args):
        tk.Tk.__init__(self, **args)
        self.title_font = tkFont.Font(family="Helvetica",
                                      size=100,
                                      weight="bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainMenuGui, EnrollGui):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainMenuGui")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenuGui(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.image = tk.PhotoImage(file="bb.png")
        self.canvas = tk.Canvas(self)
        self.font_style = tkFont.Font(family="Verdana",
                                      size=16,
                                      slant="italic")
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.create_text(750, 140,
                                text="Eco Therapy",
                                font=("Verdana", 100, "bold"),
                                fill='#189AB4')
        self.canvas.create_text(150, 30,
                                text="Home",
                                font=("Helvetica", 20,),
                                fill='white'
                                )
        self.canvas.create_text(500, 30,
                                text="About us",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(850, 30,
                                text="Volunteer",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(1150, 30,
                                text="Blog",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(450, 405,
                                text="Join our activity sessions to improve the\
                                \n           environment, with others.\
                                \n\nMake a difference by planting trees, recycling\
                                \n            and helping beekeepers.",
                                font=('Verdana', 20),
                                fill='#189AB4')

        self.button1 = ctk.CTkButton(self, text=" ENROLL",
                                     font=("Verdana", 22),
                                     fg_color="#189AB4",
                                     height=60,
                                     width=190,
                                     command=lambda: controller.show_frame("EnrollGui")
                                     )
        self.button1.update_idletasks()
        self.button1.place(relx=0.14, rely=0.59, anchor='w')

        self.canvas.create_text(1250, 410,
                                text="Learn more ways to help the environment\
                                \n            in your daily acitivities.\
                                \n\nOur knowledge bank is updated continiously\
                                \n   to provide the latest information in the \
                                \n                          field.",
                                font=('Verdana', 20),
                                fill='#189AB4')
        self.button2 = ctk.CTkButton(self, text="ARTICLES",
                                     font=('Verdana', 22),
                                     fg_color=('#189AB4'),
                                     height=60,
                                     width=190)
        self.button2.place(relx=0.84, rely=0.59, anchor='e')

        self.canvas.create_text(750, 840,
                                text="-'I felt so much relief after joining a tree planting session.Beiing in the woods,\
                                    \nbreathing fresh air, and helping the environment at the same time? Count me in!!'-",
                                font=self.font_style,
                                fill="white")
        self.canvas.create_text(900, 870,
                                text="Mathilde K.",
                                font=self.font_style,
                                fill="white")


class EnrollGui(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.image = tk.PhotoImage(file='bb.png')
        self.canvas = tk.Canvas(self)
        self.font_style = tkFont.Font(family="Verdana",
                                      size=16,
                                      slant="italic")
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.create_text(700, 140,
                                text="Locations",
                                font=("Verdana", 100, "bold"),
                                fill='#189AB4'
                                )
        self.canvas.create_text(150, 30,
                                text="Home",
                                font=("Helvetica", 20,),
                                fill='white'
                                )
        self.canvas.create_text(500, 30,
                                text="About us",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(850, 30,
                                text="Volunteer",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(1150, 30,
                                text="Blog",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas = tk.Canvas(self, width=60, height=30, bg=('#1C4508'))
        self.canvas.create_polygon(5, 15, 15, 5, 15, 10, 25, 10, 25, 20, 15,
                                   20, 15, 25, 5, 15, fill="#189AB4")
        self.canvas.bind('<Button-1>', lambda event: controller.show_frame("MainMenuGui"))

        self.canvas.update_idletasks()
        self.canvas.place(relx=0.02, rely=0.98, anchor='w')


if __name__ == "__main__":
    appl = App()
    appl.mainloop()
