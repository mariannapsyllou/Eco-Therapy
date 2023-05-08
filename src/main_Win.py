import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
import webbrowser
from read_db import format_data, read_data
import sqlite3
from tkinter import messagebox
from tkinter import PhotoImage

con = sqlite3.connect("eco-therapy.db")


class App(tk.Tk):

    def __init__(self, **args):
        tk.Tk.__init__(self, **args)
        self.title_font = tkFont.Font(family="Helvetica", size=40, weight="bold")
        container = tk.Frame(self, width=800, height=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MainMenuGui, EnrollGui, Articles, EnrollmentGui, AboutUs):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page_name] = frame

        self.attributes('-fullscreen', True)
        self.show_frame("MainMenuGui")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class FrameTemplate(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.controller = controller
        self.image = tk.PhotoImage(file="bb.png")
        self.canvas = tk.Canvas(self)
        self.font_style = tkFont.Font(family="Verdana",
                                      size=16,
                                      slant="italic")
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        color = '#%02x%02x%02x' % (169, 200, 244)
        self.homebutton = ctk.CTkButton(self,
                                        text="Home",
                                        font=("Helvetica", 20, "bold"),
                                        bg_color=color,
                                        fg_color=color,
                                        command=
                                        lambda:
                                        controller.show_frame("MainMenuGui"))
        self.homebutton.place(relx=0.01, rely=0.02)

        self.activity_button = ctk.CTkButton(self,
                                             text="Activities",
                                             font=("Helvetica", 20, "bold"),
                                             bg_color="#aac4f5",
                                             fg_color="#aac4f5",
                                             command=
                                             lambda:
                                             controller.show_frame("EnrollGui")
                                             )
        self.activity_button.place(relx=0.40, rely=0.03, anchor='w')
        self.about_button = ctk.CTkButton(self,
                                          text="About us",
                                          font=("Helvetica", 20, "bold"),
                                          bg_color="#ced5f2",
                                          fg_color="#ced5f2",
                                          command=
                                          lambda:
                                          controller.show_frame("AboutUs"))
        self.about_button.place(relx=0.85, rely=0.03, anchor='w')


class MainMenuGui(FrameTemplate, tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.canvas.create_text(650, 140,
                                text="Eco Therapy",
                                font=("Verdana", 70, "bold"),
                                fill='#317353')
        self.canvas.create_text(410, 330,
                                text="Join our activity sessions to improve the\
                                \n           environment, with others.\
                                \n\nMake a difference by planting trees, recycling\
                                \n            and helping beekeepers.",
                                font=('Verdana', 18),
                                fill='#317353')

        self.button1 = ctk.CTkButton(self, text=" ENROLL",
                                     font=("Verdana", 20),
                                     fg_color="#317353",
                                     height=60,
                                     width=190,
                                     command=lambda: controller.show_frame("EnrollGui")
                                     )
        self.button1.update_idletasks()
        self.button1.place(relx=0.14, rely=0.73, anchor='w')

        self.canvas.create_text(1100, 330,
                                text="Learn more ways to help the environment\
                                \n            in your daily acitivities.\
                                \n\nOur knowledge bank is updated continiously\
                                \n   to provide the latest information in the \
                                \n                          field.",
                                font=('Verdana', 16),
                                fill='#317353')
        self.button2 = ctk.CTkButton(self, text="LEARN MORE",
                                     font=('Verdana', 18),
                                     fg_color=('#317353'),
                                     height=60,
                                     width=190,
                                     command=lambda: controller.show_frame("Articles"))
        self.button2.place(relx=0.84, rely=0.73, anchor='e')

        self.canvas.create_text(750, 640,
                                text="-'I felt so much relief after joining a tree planting session.Beiing in the woods,\
                                    \nbreathing fresh air, and helping the environment at the same time? Count me in!!'-",
                                font=self.font_style,
                                fill="white")
        self.canvas.create_text(900, 670,
                                text="Mathilde K.",
                                font=self.font_style,
                                fill="white")


class EnrollGui(FrameTemplate, tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.events = format_data(read_data())
        self.canvas.create_text(680, 140,
                                text="Activities",
                                font=("Verdana", 70, "bold"),
                                fill='#317353'
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
        self.activity_button = ctk.CTkButton(self,
                                             text="Activities",
                                             font=("Helvetica", 20, "bold"),
                                             bg_color="#aac4f5",
                                             fg_color="#aac4f5",
                                             command=
                                             lambda:
                                             controller.show_frame("EnrollGui")
                                             )
        self.activity_button.place(relx=0.40, rely=0.03, anchor='w')
        self.about_button = ctk.CTkButton(self,
                                          text="About us",
                                          font=("Helvetica", 20, "bold"),
                                          bg_color="#ced5f2",
                                          fg_color="#ced5f2",
                                          command=
                                          lambda:
                                          controller.show_frame("AboutUs"))
        self.about_button.place(relx=0.85, rely=0.03, anchor='w')
        self.canvas.create_text(750, 270,
                                text="Here you can find information on our next available events.\
                                    \nCheck the page frequently as they are updated daily.",
                                font=('Helvetica', 15,),
                                fill="#317353"
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
        self.canvas.create_window(130, 400, anchor="nw", window=button_1)

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
        self.canvas.create_window(530, 400, anchor="nw", window=button_2)

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
        self.canvas.create_window(930, 400, anchor="nw", window=button_3)

    def set_eventid(self, controller, frame_name, seventid):
        global EVENTID
        EVENTID = seventid
        controller.show_frame(frame_name)


class Articles(FrameTemplate, tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.23, rely=0.15, anchor="n")
        self.tree_label = ctk.CTkLabel(self.frame_article1, text=" ")
        self.tree_label.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="\n     HOW TO COPE WITH ECO ANXIETY\
                                         \n1. Don't try to deny or Suppress your emotions.\
                                         \n2. Take Action\
                                         \n\n3. Find the right professionall help\
                                         \n4. Connect with others and share your concerns\
                                         \n5. Spend time in nature\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=550,
                                         fg_color="#E2EDF7",
                                         text_color="#317353",
                                         bg_color="transparent",
                                         )
        self.article_text.pack(side="left")
        self.url1 = "https://www.everydayhealth.com/eco-anxiety/how-to-cope-with-eco-anxiety/"
        self.read_more_label = ctk.CTkLabel(self,
                                            text="Read More",
                                            text_color="#317353",
                                            fg_color="#E2EDF7",
                                            font=("Verdana", 15))
        self.read_more_label.place(relx=0.20, rely=0.54, anchor="w")
        self.read_more_label.bind("<Button-1>",
                                  lambda event: webbrowser.open_new(self.url1))

        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.28, rely=0.60, anchor="n")
        self.tree_label2 = ctk.CTkLabel(self.frame_article1, text = " ")
        self.tree_label2.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="\nADDRESSING CLIMATE CHANGE CONCERNS\
                                             \nIN PRACTISE\
                                             \n\nThe planet is undergoing rapid and unprecedented\
                                             \nclimate change that is creating stress and\
                                             \nmental anguish for people around the world.\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=600,
                                         fg_color="#E2EDF7",
                                         text_color="#317353",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url2 = "https://www.apa.org/monitor/2021/03/ce-climate-change"
        self.read_more_label2 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#317353",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label2.place(relx=0.22, rely=0.93, anchor="w")
        self.read_more_label2.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url2))
        self.frame_article3 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article3.place(relx=0.45, rely=0.34, anchor="w")
        self.tree_label3 = ctk.CTkLabel(self.frame_article3, text=" ")
        self.tree_label3.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article3,
                                         text="\nCLIMATE ANXIETY: 21 RESOURCES TO\
                                         \nENERGISE YOU INTO ACTION\
                                         \n\nFears about the climate crisis getting the better\
                                         \nof you? Greenpeace staff helps you navigate\
                                         \nyour worries about the enviromental\
                                         \nemergency. Here is what they recommended\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=575,
                                         fg_color="#E2EDF7",
                                         text_color="#317353",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url3 = "https://www.greenpeace.org.uk/news/climate-anxiety-resources-to-energise-action/?gclid=CjwKCAjwo7iiBhAEEiwAsIxQEdllTZSd97f7yiVjbg1Ktpw3Jl9_R7h9kIYKfGpWW_RWRhhL-bIMpRoC0lkQAvD_BwE"
        self.read_more_label3 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#317353",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label3.place(relx=0.61, rely=0.52, anchor="w")
        self.read_more_label3.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url3))
        self.frame_article4 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article4.place(relx=0.89, rely=0.74, anchor="e")
        self.tree_label4 = ctk.CTkLabel(self.frame_article4, text= " ")
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
                                         text_color="#317353",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url4 = "https://www.projectplanetid.com/post/7-ways-to-prevent-eco-anxiety"
        self.read_more_label4 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#317353",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 15))
        self.read_more_label4.place(relx=0.76, rely=0.88, anchor="e")
        self.read_more_label4.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url4))


class EnrollmentGui(FrameTemplate, tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.canvas.create_text(620, 140, text="Enrollment Form",
                                font=("Verdana", 70, "bold"),
                                fill="#317353")
        polygon=self.canvas.create_polygon(5, 15, 15, 5, 15, 10, 25, 10, 25, 20, 15,
                                   20, 15, 25, 5, 15, fill="#317353")
        x0, y0, x1, y1 = self.canvas.bbox(polygon)
        button = self.canvas.create_rectangle(x0, y0, x1, y1, fill="", outline="")
        self.canvas.tag_bind(button,'<Button-1>', lambda event: controller.show_frame("EnrollGui"))
        self.canvas.create_text(440, 280, text="First Name",
                                font=("Verdana", 20, "bold"),
                                fill="#317353")
        first_name_entry = ctk.CTkEntry(self, width=170,
                                        height=50, font=("Verdana", 20),
                                        bg_color="white", 
                                        fg_color="white", 
                                        border_width=0)
        self.canvas.create_window(375, 300, anchor="nw",
                                  window=first_name_entry)
        self.canvas.create_text(750, 280, text="Last Name",
                                font=("Verdana", 20, "bold"),
                                fill="#317353")
        last_name_entry = ctk.CTkEntry(self, width=170,
                                       height=50, font=("Verdana", 20), 
                                       bg_color="#317353", 
                                       fg_color="white", 
                                       border_width=0)
        self.canvas.create_window(685, 300, anchor="nw",
                                  window=last_name_entry)


        """ self.canvas.create_text(675, 380, text="Phone Number",
                                font=("Verdana", 25, "bold"),
                                fill="white")
        phone_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Verdana", 20))
        self.canvas.create_window(580, 400, anchor="nw", window=phone_entry)"""
        self.canvas.create_text(620, 380, text="Email",
                                font=("Verdana", 20, "bold"),
                                fill="#317353")
        email_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Verdana", 20),
                                   bg_color="white", 
                                   fg_color="white", 
                                   border_width=0)
        self.canvas.create_window(500, 400, anchor="nw", 
                                  window=email_entry)

        self.canvas.create_text(620, 490, text="Date of Birth",
                                font=("Verdana", 20, "bold"),
                                fill="#317353")

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
        self.canvas.create_window(480, 510, anchor="nw", window=options_year)

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
        self.canvas.create_window(595, 510, anchor="nw", window=options_month)

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
        self.canvas.create_window(710, 510, anchor="nw", window=options_day)

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
                                      text="Enroll", fg_color="#317353",
                                      bg_color="#317353",
                                      font=("Verdana", 50),
                                      command=lambda: (button_function(),
                                                       save_data_success())
                                      )
        self.canvas.create_window(570, 600, anchor="nw", window=enroll_button)

        def save_data_success():
            messagebox.showinfo(title="Success", message="Data saved successfully!")


class AboutUs(FrameTemplate, tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.canvas.create_text(650, 140,
                                text="About us",
                                font=("Verdana", 70, "bold"),
                                fill='#317353')
        self.canvas.create_text(500, 250,
                                text="Eco Therapy is an application that targets the\
                                    \nsymptoms of eco anxiety.",
                                font=('Verdana', 18),
                                fill='#317353')
        self.canvas.create_text(600, 450,
                                text="Eco anxiety is a globally growing phenomenon among all ages.\
                                    \nIt includes strong feelings of worry and fear about the decline\
                                    \nin the environment.\
                                    \nWays in which eco anxiety can be relieves are:\
                                    \n\n1. Taking action to help the climate, no matter how small\
                                    \n2.Recognizing and understanding eco anxiety\
                                    \n3.Discussions about eco anxiety in groups\
                                    \n4.Connecting with nature in positive ways",

                                font=('Verdana', 18),
                                fill='#317353')
        self.canvas.create_text(1280, 350,
                                text="Contributors:\
                                    \n\nAxel Friberg\
                                    \nMiina Mäkinen\
                                    \nMarianna Psyllou\
                                    \nCourage Räsänen\
                                    \nKim Zugic",
                                font=("Verdana",18),
                                fill='#317353')


if __name__ == "__main__":
    appl = App()
    appl.mainloop()
