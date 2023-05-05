import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
import webbrowser
from read_db import format_data, read_data
import sqlite3
from tkinter import messagebox

con = sqlite3.connect("eco-therapy.db")

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
        for F in (MainMenuGui, EnrollGui, Articles, EnrollmentGui):
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
        self.events = format_data(read_data())
        self.font_style = tkFont.Font(family="Verdana",
                                      size=16,
                                      slant="italic")
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.create_text(700, 140,
                                text="Events",
                                font=("Verdana", 100, "bold"),
                                fill='#189AB4'
                                )
        color = '#%02x%02x%02x' % (169, 200, 244)
        self.homebutton = ctk.CTkButton(self,
                                text="Home",
                                font=("Helvetica", 20,),
                                bg_color=color,
                                fg_color=color,
                                command=lambda: controller.show_frame("MainMenuGui")
                                )
        self.homebutton.place(relx=0.01, rely=0.02)

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
        self.canvas.create_text(850, 270,
                                text="Here you can find information on our next available events.\
                                    \nCheck the page frequently as they are updated daily.",

                                font=('Helvetica', 25,),
                                fill='#189AB4'
                                )
        button_1 = ctk.CTkButton(
                                self, 
                                width=230, 
                                height=150,
                                corner_radius=5,
                                # the button text is derived from the events table in the database
                                text=f"\n{self.events[0][1]}\n\n" + f"Location: {self.events[0][3]}\n" + f"Date&Time: {self.events[0][2]}\n",
                                anchor="center",
                                font=("Verdana", 18),
                                #command=lambda: controller.show_frame("EnrollmentGui"),
                                fg_color="#317353",
                                bg_color="#5D623F",
                                border_width=1,
                                border_color="#97C2AD",
                                hover_color="#22533C",
                                command=lambda: self.set_eventid(controller, "EnrollmentGui", self.events[0][0])
                                )
        self.canvas.create_window(180, 600, anchor="nw", window=button_1)

        button_2 = ctk.CTkButton(
                                self, 
                                width=230, 
                                height=150,
                                corner_radius=5,
                                # the button text is derived from the events table in the database
                                text=f"\n{self.events[1][1]}\n\n" + f"Location: {self.events[1][3]}\n" + f"Date&Time: {self.events[1][2]}\n",
                                anchor="center",
                                font=("Verdana", 18),
                                #command=lambda: controller.show_frame("EnrollmentGui"),
                                fg_color="#317353",
                                bg_color="#9D7C85",
                                border_width=1,
                                border_color="#97C2AD",
                                hover_color="#22533C",
                                command=lambda: self.set_eventid(controller, "EnrollmentGui", self.events[1][0])
                                )
        self.canvas.create_window(580, 600, anchor="nw", window=button_2)

        button_3 = ctk.CTkButton(
                                self, 
                                width=230, 
                                height=150,
                                corner_radius=5,
                                # the button text is derived from the events table in the database
                                text=f"\n{self.events[2][1]}\n\n" + f"Location: {self.events[2][3]}\n" + f"Date&Time: {self.events[2][2]}\n",
                                anchor="center",
                                font=("Verdana", 18),
                                #command=lambda: controller.show_frame("EnrollmentGui"),
                                fg_color="#317353",
                                bg_color="#CBA09A",
                                border_width=1,
                                border_color="#97C2AD",
                                hover_color="#22533C",
                                command=lambda: self.set_eventid(controller, "EnrollmentGui", self.events[2][0])
                                )
        self.canvas.create_window(980, 600, anchor="nw", window=button_3)

    def set_eventid(self, controller, frame_name, seventid):
        global EVENTID
        EVENTID = seventid
        controller.show_frame(frame_name)




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
        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.23, rely=0.15, anchor="n")
        self.tree_label = ctk.CTkLabel(self.frame_article1)
        self.tree_label.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="\n     HOW TO COPE WITH ECO ANXIETY\
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
        self.article_text.pack(side="left")
        self.url1 = "https://www.everydayhealth.com/eco-anxiety/how-to-cope-with-eco-anxiety/"
        self.read_more_label = ctk.CTkLabel(self,
                                            text="Read More",
                                            text_color="#189AB4",
                                            cursor="hand",
                                            fg_color="#E2EDF7",
                                            font=("Verdana", 15))
        self.read_more_label.place(relx=0.20, rely=0.46, anchor="w")
        self.read_more_label.bind("<Button-1>",
                                  lambda event: webbrowser.open_new(self.url1))

        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.25, rely=0.55, anchor="n")
        self.tree_label2 = ctk.CTkLabel(self.frame_article1)
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
        self.article_text.pack(side="left")
        self.url2 = "https://www.apa.org/monitor/2021/03/ce-climate-change"
        self.read_more_label2 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#189AB4",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label2.place(relx=0.22, rely=0.85, anchor="w")
        self.read_more_label2.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url2))


        self.frame_article3 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article3.place(relx=0.55, rely=0.34, anchor="w")
        self.tree_label3 = ctk.CTkLabel(self.frame_article3)
        self.tree_label3.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article3,
                                         text="\nCLIMATE ANXIETY: 21 RESOURCES TO\
                                         \nENERGISE YOU INTO ACTION\
                                         \n\nFears about the climate crisis getting the better\
                                         \nof you? Greenpeace staff helps you navigate\
                                         \nyour worries about the enviromental\
                                         \nemergency\
                                         \nHere is what they recommended\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=2000,
                                         fg_color="#E2EDF7",
                                         text_color="#189AB4",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url3 = "https://www.greenpeace.org.uk/news/climate-anxiety-resources-to-energise-action/?gclid=CjwKCAjwo7iiBhAEEiwAsIxQEdllTZSd97f7yiVjbg1Ktpw3Jl9_R7h9kIYKfGpWW_RWRhhL-bIMpRoC0lkQAvD_BwE"
        self.read_more_label3 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#189AB4",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label3.place(relx=0.71, rely=0.52, anchor="w")
        self.read_more_label3.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url3))


        self.frame_article4 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article4.place(relx=0.89, rely=0.74, anchor="e")
        self.tree_label4 = ctk.CTkLabel(self.frame_article4)
        self.tree_label4.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article4,
                                         text="\n7 WAYS TO PREVENT ECO-ANXIETY\
                                         \n\nRead and learn ways to prevent Eco-Anxiety.\
                                         \nLearn about practices you can do home\
                                         \nsuch as recycling and gardening.\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=500,
                                         fg_color="#E2EDF7",
                                         text_color="#189AB4",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url4 = "https://www.projectplanetid.com/post/7-ways-to-prevent-eco-anxiety"
        self.read_more_label4 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#189AB4",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label4.place(relx=0.76, rely=0.85, anchor="e")
        self.read_more_label4.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url4))

class EnrollmentGui(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.canvas = ctk.CTkCanvas(self, width=1024, height=900)
        self.bg_image = tk.PhotoImage(file="bb.png")
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.canvas.create_text(750, 140, text="Eco Therapy",
                                font=("Verdana", 100, "bold"),
                                fill="#189AB4")

        self.canvas.create_text(720, 240, text="Enrollment Form",
                                font=("Verdana", 40, "bold"),
                                fill="#189AB4")
        color = '#%02x%02x%02x' % (185, 200, 244)
        self.homebutton = ctk.CTkButton(self,
                                text="Home",
                                font=("Helvetica", 20,),
                                bg_color=color,
                                fg_color=color,
                                command=lambda: controller.show_frame("MainMenuGui")
                                )
        self.homebutton.place(relx=0.01, rely=0.02)
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
        polygon=self.canvas.create_polygon(5, 15, 15, 5, 15, 10, 25, 10, 25, 20, 15,
                                   20, 15, 25, 5, 15, fill="#189AB4")
        x0, y0, x1, y1 = self.canvas.bbox(polygon)
        button = self.canvas.create_rectangle(x0, y0, x1, y1, fill="", outline="")
        self.canvas.tag_bind(button,'<Button-1>', lambda event: controller.show_frame("EnrollGui"))
        self.canvas.create_text(540, 330, text="First Name",
                                font=("Verdana", 25, "bold"),
                                fill="#189AB4")

        first_name_entry = ctk.CTkEntry(self, width=170,
                                        height=50, font=("Verdana", 20),bg_color="white", fg_color="white", border_width=0)
        self.canvas.create_window(475, 350, anchor="nw",
                                  window=first_name_entry)
        self.canvas.create_text(815, 330, text="Last Name",
                                font=("Verdana", 25, "bold"),
                                fill="#189AB4")
        last_name_entry = ctk.CTkEntry(self, width=170,
                                       height=50, font=("Verdana", 20), bg_color="#189AB4", fg_color="white", border_width=0)
        self.canvas.create_window(750, 350, anchor="nw",
                                  window=last_name_entry)


        """ self.canvas.create_text(675, 380, text="Phone Number",
                                font=("Verdana", 25, "bold"),
                                fill="white")
        phone_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Verdana", 20))
        self.canvas.create_window(580, 400, anchor="nw", window=phone_entry)"""
        self.canvas.create_text(720, 460, text="Email",
                                font=("Verdana", 25, "bold"),
                                fill="#189AB4")
        email_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Verdana", 20),bg_color="white", fg_color="white", border_width=0)
        self.canvas.create_window(580, 480, anchor="nw", window=email_entry)

        self.canvas.create_text(720, 580, text="Date of Birth",
                                font=("Verdana", 25, "bold"),
                                fill="#189AB4")

        file_year = open(file='year.txt')
        read_year = file_year.readlines()
        year = []

        for line in read_year:
            year.append(line.strip())

        options_year = ctk.CTkOptionMenu(self, values=year,
                                         width=100,
                                         height=30,
                                         bg_color="white",
                                         fg_color="white",
                                         button_color="white",
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
                                          bg_color="white",
                                          fg_color="white",
                                          button_color="white",
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
                                        bg_color="white",
                                        fg_color="white",
                                        button_color="white",
                                        font=("Verdana", 15),
                                        dynamic_resizing=False)
        options_day.set("Day")
        self.canvas.create_window(790, 600, anchor="nw", window=options_day)

        def button_function():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            email = email_entry.get()
            year = options_year.get()
            month = options_month.get()
            day = options_day.get()
            birthday = f"{year}-{month}-{day}"

            c = con.cursor()

            # Insert user into users table
            c.execute("INSERT INTO users (firstname, lastname, email, birthdate) VALUES (?, ?, ?, ?)",
                    (first_name, last_name, email, birthday))
            user_id = c.lastrowid

            c.execute("INSERT INTO enrolled (user_id, event_id) VALUES (?, ?)", (user_id, EVENTID))

            con.commit()
            con.close()

        enroll_button = ctk.CTkButton(self, width=100, height=50,
                                      text="Enroll", fg_color="#189AB4",
                                      bg_color="#189AB4",
                                      font=("Verdana", 50),
                                      command=lambda: (button_function(),
                                                       save_data_success())
                                      )
        self.canvas.create_window(650, 700, anchor="nw", window=enroll_button)

        def save_data_success():
            messagebox.showinfo(title="Success", message="Data saved successfully!")



if __name__ == "__main__":
    appl = App()
    appl.mainloop()
