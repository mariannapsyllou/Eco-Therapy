import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
import webbrowser


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
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set window size and position
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, window_x, window_y))
        for F in (MainMenuGui, EnrollGui, Articles):
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
        self.button2 = ctk.CTkButton(self, text="LEARN MORE",
                                     font=('Verdana', 22),
                                     fg_color=('#189AB4'),
                                     height=60,
                                     width=190,
                                     command=lambda: controller.show_frame("Articles"))
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
        self.canvas2 = tk.Canvas(self, width=60, height=30, bg=('#70A6DA'), highlightthickness=0)
        self.canvas.update_idletasks()
        self.canvas.place(relx=0.02, rely=0.98, anchor='w')




class Articles(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.image = tk.PhotoImage(file="back2.png")
        self.canvas = tk.Canvas(self)
        self.font_style = tkFont.Font(family="Verdana",
                                      size=16,
                                      slant="italic")
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")

        color = '#%02x%02x%02x' % (4, 96, 167)
        self.home_button = ctk.CTkButton(self,
                                text="Home",
                                font=("Helvetica", 20,),
                                bg_color=color,
                                fg_color=color,
                                command=lambda: controller.show_frame("MainMenuGui")
                                )
        self.home_button.place(relx=0.01, rely=0.02)
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
        self.image1 = tk.PhotoImage(file="art_1.png")
        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.23, rely=0.15, anchor="n")
        self.tree_label = ctk.CTkLabel(self.frame_article1, image=self.image1 )
        self.tree_label.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="     HOW TO COPE WITH ECO ANXIETY\
                                         \n1. Don't try to deny or Suppress your emotions.\
                                         \n2. Take Action\
                                         \n3. Find the right professionall help\
                                         \n4. Connect with others and share your concerns\
                                         \n5. Spend time in nature\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=1000,
                                         fg_color="#E2EDF7",
                                         text_color="#189AB4",
                                         bg_color="transparent",
                                         )
        self.article_text.pack(side="left", padx=5)
        self.url1 = "https://www.everydayhealth.com/eco-anxiety/how-to-cope-with-eco-anxiety/"
        self.read_more_label = ctk.CTkLabel(self,
                                            text="Read More",
                                            text_color="#189AB4",
                                            cursor="hand",
                                            fg_color="#E2EDF7",
                                            font=("Verdana", 15))
        self.read_more_label.place(relx=0.24, rely=0.46, anchor="w")
        self.read_more_label.bind("<Button-1>",
                                  lambda event: webbrowser.open_new(self.url1))

        self.image2 = tk.PhotoImage(file="eco1.png")
        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.25, rely=0.55, anchor="n")
        self.tree_label2 = ctk.CTkLabel(self.frame_article1, image=self.image2)
        self.tree_label2.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="\nADDRESSING CLIMATE CHANGE CONCERNS\
                                             \nIN PRACTISE\
                                             \nThe planet is undergoing rapid and\
                                             \nunprecedented climate change that is creating\
                                             \nstress and mental anguish for people around\
                                             \nthe world\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=1000,
                                         fg_color="#E2EDF7",
                                         text_color="#189AB4",
                                         bg_color="transparent")
        self.article_text.pack(side="left", padx=10)
        self.url2 = "https://www.apa.org/monitor/2021/03/ce-climate-change"
        self.read_more_label2 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#189AB4",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label2.place(relx=0.26, rely=0.86, anchor="w")
        self.read_more_label2.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url2))

        self.image3 = tk.PhotoImage(file="art3.png")
        self.frame_article3 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article3.place(relx=0.50, rely=0.33, anchor="w")
        self.tree_label3 = ctk.CTkLabel(self.frame_article3, image=self.image3, text="")
        self.tree_label3.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article3,
                                         text="\nCLIMATE ANXIETY: 21 RESOURCES TO\
                                         \nENERGISE YOU INTO ACTION\
                                         \n\nFears about the climate crisis getting\
                                         \nthe better of you? Greenpeace staff\
                                         \nhelps you navigate your worries about\
                                         \nthe enviromental emergency\
                                         \nHere is what they recommended\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=2000,
                                         fg_color="#E2EDF7",
                                         text_color="#189AB4",
                                         bg_color="transparent")
        self.article_text.pack(side="left", padx=20)
        self.url3 = "https://www.greenpeace.org.uk/news/climate-anxiety-resources-to-energise-action/?gclid=CjwKCAjwo7iiBhAEEiwAsIxQEdllTZSd97f7yiVjbg1Ktpw3Jl9_R7h9kIYKfGpWW_RWRhhL-bIMpRoC0lkQAvD_BwE"
        self.read_more_label3 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#189AB4",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label3.place(relx=0.73, rely=0.51, anchor="w")
        self.read_more_label3.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url3))

        self.image4 = tk.PhotoImage(file="art4.png")
        self.frame_article4 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article4.place(relx=0.99, rely=0.74, anchor="e")
        self.tree_label4 = ctk.CTkLabel(self.frame_article4, image=self.image4)
        self.tree_label4.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article4,
                                         text="\n7 WAYS TO PREVENT ECO-ANXIETY\
                                         \n\nRead and learn ways to prevent\
                                         \nEco-Anxiety. Learn about practices\
                                         \nyou can do home such as\
                                         \nrecycling and gardening\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=500,
                                         fg_color="#E2EDF7",
                                         text_color="#189AB4",
                                         bg_color="transparent")
        self.article_text.pack(side="left", padx=20)
        self.url4 = "https://www.projectplanetid.com/post/7-ways-to-prevent-eco-anxiety"
        self.read_more_label4 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#189AB4",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label4.place(relx=0.87, rely=0.87, anchor="e")
        self.read_more_label4.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url4))


""" class EnrollmentGui(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = ctk.CTkCanvas(self, width=1024, height=900)
        self.bg_image = tk.PhotoImage(file="nature.png")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.canvas.create_text(750, 140, text="Eco Therapy",
                                font=("Georgia", 100, "bold"),
                                fill="#189AB4")
        self.canvas.create_text(74, 30,
                                text="Home",
                                font=("Helvetica", 20,),
                                fill='white'
                                )
        self.canvas.create_text(366, 30,
                                text="About us",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(658, 30,
                                text="Volunteer",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_text(950, 30,
                                text="Blog",
                                font=('Helvetica', 20,),
                                fill='white'
                                )
        self.canvas.create_polygon(5, 15, 15, 5, 15, 10, 25, 10, 25, 20, 15,
                                   20, 15, 25, 5, 15, fill="#189AB4")
        self.canvas.bind('<Button-1>', lambda event: controller.show_frame("EnrollGui"))
        self.canvas.create_text(595, 280, text="First Name",
                                font=("Verdana", 25, "bold"),
                                fill="white")

        first_name_entry = ctk.CTkEntry(self, width=170,
                                        height=50, font=("Verdana", 20))
        self.canvas.create_window(530, 300, anchor="nw",
                                  window=first_name_entry)
        self.canvas.create_text(915, 280, text="Last Name",
                                font=("Verdana", 25, "bold"),
                                fill="white")
        last_name_entry = ctk.CTkEntry(self, width=170,
                                       height=50, font=("Verdana", 20))
        self.canvas.create_window(850, 300, anchor="nw",
                                  window=last_name_entry)


        self.canvas.create_text(675, 380, text="Phone Number",
                                font=("Verdana", 25, "bold"),
                                fill="white")
        phone_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Verdana", 20))
        self.canvas.create_window(580, 400, anchor="nw", window=phone_entry)
        self.canvas.create_text(615, 480, text="Email",
                                font=("Verdana", 25, "bold"),
                                fill="white")
        email_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Verdana", 20))
        self.canvas.create_window(580, 500, anchor="nw", window=email_entry)

        self.canvas.create_text(665, 580, text="Date of Birth",
                                font=("Verdana", 25, "bold"),
                                fill="white")

        file_year = open(file='year.txt')
        read_year = file_year.readlines()
        year = []

        for line in read_year:
            year.append(line.strip())

        options_year = ctk.CTkOptionMenu(self, values=year,
                                         width=100,
                                         height=30,
                                         bg_color="#165806",
                                         fg_color="#165806",
                                         button_color="#165806",
                                         font=("Verdana", 15),
                                         dynamic_resizing=False)
        options_year.set("Year")
        self.canvas.create_window(570, 600, anchor="nw", window=options_year)

        file_month = open(file='month.txt')
        read_month = file_month.readlines()
        month = []

        for line in read_month:
            month.append(line.strip())

        options_month = ctk.CTkOptionMenu(self, values=month,
                                          width=110,
                                          height=30,
                                          bg_color="#165806",
                                          fg_color="#165806",
                                          button_color="#165806",
                                          font=("Verdana", 15),
                                          dynamic_resizing=False)
        options_month.set("Month")
        self.canvas.create_window(675, 600, anchor="nw", window=options_month)

        file_day = open(file='day.txt')
        read_day = file_day.readlines()
        days = []

        for line in read_day:
            days.append(line.strip())

        options_day = ctk.CTkOptionMenu(self, values=days,
                                        width=100,
                                        height=30,
                                        bg_color="#165806",
                                        fg_color="#165806",
                                        button_color="#165806",
                                        font=("Verdana", 15),
                                        dynamic_resizing=False)
        options_day.set("Day")
        self.canvas.create_window(790, 600, anchor="nw", window=options_day)

        def button_function():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            year = options_year.get()
            month = options_month.get()
            day = options_day.get()
            birthday = f"{year}-{month}-{day}"
            if (phone.isdigit()):
                print(f"{first_name} {last_name}\n{phone}\n{email}\n"
                      f"{year} {month} {day}")
            else:
                self.canvas.create_text(720, 460,
                                        text=("Please enter a "
                                              "correct phone number"),
                                        font=("Verdana", 13, "bold"),
                                        fill="red")

        enroll_button = ctk.CTkButton(self, width=100, height=50,
                                      text="Enroll", fg_color="#165806",
                                      bg_color="#165806",
                                      font=("Verdana", 50, "bold"),
                                      command=button_function)
        self.canvas.create_window(650, 700, anchor="nw", window=enroll_button)

 """
if __name__ == "__main__":
    appl = App()
    appl.mainloop()
