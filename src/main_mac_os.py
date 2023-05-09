"""
This module contains the graphical user interface (GUI)
for the Eco-Therapy application.

The GUI is built using the tkinter library, and consists of several classes
that each represent a different window or dialog
in the application.

Note that this module requires the tkinter library to be installed.

"""

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import webbrowser
import re
import customtkinter as ctk
import read_db



class App(tk.Tk):
    """The main application class that creates and manages the GUI.

    This class inherits from `tk.Tk` and is responsible for creating the main
    window of the application and managing its frames. It initializes the
    `title_font` font and sets the window geometry. It also creates instances
    of the different GUI classes (`MainMenuGui`, `EnrollGui`, `Articles`,
    `EnrollmentGui`, and `AboutUs`) and stores them in a dictionary, where each
    key is the name of the corresponding class. It provides a method,
    `show_frame`,
    that can be used to switch between frames.

    Attributes:
        title_font (tkFont.Font): The font used for the window title.

    Methods:
        __init__(self, **args): Initializes the main window and creates the
        frames.
        show_frame(self, page_name): Raises the frame corresponding to the
        given name.
    """

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

        for F in (MainMenuGui, EnrollGui, Articles, EnrollmentGui, AboutUs):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainMenuGui")

    def show_frame(self, page_name):
        """Raises frames"""
        frame = self.frames[page_name]
        frame.tkraise()


class FrameTemplate(tk.Frame):
    """
    A template for creating frames with a background image and buttons for
    navigating to other frames.

    Attributes:
    -----------
    parent: tk.Tk or tk.Frame
        The parent widget of this frame.
    controller: App
        The App instance that controls the overall flow of the program.
    image: tk.PhotoImage
        The image to be displayed as the background of this frame.
    canvas: tk.Canvas
        The canvas widget used to display the background image.
    font_style: tkFont.Font
        The font style used for the text on the buttons.
    homebutton: ctk.CTkButton
        The button for returning to the main menu.
    activity_button: ctk.CTkButton
        The button for navigating to the activities page.
    about_button: ctk.CTkButton
        The button for navigating to the about us page.
    """
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
        color = f'#{169:02x}{200:02x}{244:02x}'

        self.homebutton = ctk.CTkButton(self,
                                        text="Home",
                                        font=("Helvetica", 20, "bold"),
                                        bg_color=color,
                                        fg_color=color,
                                        command=lambda:
                                        controller.show_frame("MainMenuGui"))
        self.homebutton.place(relx=0.01, rely=0.02)

        self.activity_button = ctk.CTkButton(self,
                                             text="Activities",
                                             font=("Helvetica", 20, "bold"),
                                             bg_color="#aac4f5",
                                             fg_color="#aac4f5",
                                             command=lambda:
                                             controller.show_frame("EnrollGui")
                                             )
        self.activity_button.place(relx=0.40, rely=0.03, anchor='w')
        self.about_button = ctk.CTkButton(self,
                                          text="About us",
                                          font=("Helvetica", 20, "bold"),
                                          bg_color="#ced5f2",
                                          fg_color="#ced5f2",
                                          command=lambda:
                                          controller.show_frame("AboutUs"))
        self.about_button.place(relx=0.85, rely=0.03, anchor='w')


class MainMenuGui(FrameTemplate, tk.Frame):
    """
    A class representing the main menu GUI of the Eco Therapy application.

    Inherits from FrameTemplate and tk.Frame. Displays information about the
    application and provides buttons to enroll in activities or learn more
    about
    environmental issues.

    Args:
        parent (Tk): The parent widget.
        controller (Tk): The controller widget.

    Attributes:
        canvas (tk.Canvas): A canvas widget on which to draw text and
        images.
        button1 (ctk.CTkButton): A custom button widget to enroll in
        activities.
        button2 (ctk.CTkButton): A custom button widget to learn more.
        font_style (tkFont.Font): A font object to use for text.
    """

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.canvas.create_text(750, 140,
                                text="Eco Therapy",
                                font=("Verdana", 100, "bold"),
                                fill='#317353')
        self.canvas.create_text(450, 405,
                                text="Join our activity sessions to improve "
                                "the\
                                \n           environment, with "
                                "others.\
                                \n\nMake a difference by planting trees, "
                                "recycling\
                                \n            and helping beekeepers.",
                                font=('Verdana', 20),
                                fill='#317353')

        self.button1 = ctk.CTkButton(self, text=" ENROLL",
                                     font=("Verdana", 22),
                                     fg_color="#317353",
                                     height=60,
                                     width=190,
                                     command=lambda:
                                     controller.show_frame("EnrollGui")
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
                                fill='#317353')
        self.button2 = ctk.CTkButton(self, text="LEARN MORE",
                                     font=('Verdana', 22),
                                     fg_color=('#317353'),
                                     height=60,
                                     width=190,
                                     command=lambda:
                                     controller.show_frame("Articles"))
        self.button2.place(relx=0.84, rely=0.59, anchor='e')

        self.canvas.create_text(750, 840,
                                text="-'I felt so much relief after joining "
                                     "a tree planting session. "
                                     "Being in the woods,"
                                     "\nbreathing fresh air, "
                                     "and helping the environment at the same "
                                     "time? Count me in!!'-",
                                font=self.font_style,
                                fill="white")
        self.canvas.create_text(900, 870,
                                text="Mathilde K.",
                                font=self.font_style,
                                fill="white")


class EnrollGui(FrameTemplate, tk.Frame):
    """A graphical user interface for enrolling in events.

    This class extends the `FrameTemplate` and `tk.Frame`
    classes. It allows the user to browse available events
    and enroll in one of them. The events are fetched from a
    database through an instance of the `read_db.DbInteraction`
    class.

    Attributes:
        read_db (read_db.DbInteraction): An instance of the
        `read_db.DbInteraction` class, used to read data from the
            database.
        controller (Tkinter.Tk): The main controller of the application.
        events (list): A list of available events, fetched from the database.

    Methods:
        set_eventid(controller, frame_name, seventid): Sets the `EVENTID`
        global variable to the id of the selected event
            and switches the current frame to `frame_name`.
    """

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.read_db = read_db.DbInteraction()
        self.controller = controller
        self.events = self.read_db.read_data()
        self.canvas.create_text(700, 140,
                                text="Activities",
                                font=("Verdana", 100, "bold"),
                                fill='#317353'
                                )

        self.canvas.create_text(850, 270,
                                text="Here you can find information on our next available events.\
                                    \nCheck the page frequently as they are updated daily.",

                                font=('Helvetica', 25,),
                                fill='#317353'
                                )

        button_1 = ctk.CTkButton(self,
                                 width=230,
                                 height=150,
                                 corner_radius=5,
                                 # the button text is derived from the
                                 # events table in the database
                                 text=f"\n{self.events[0][1]}\n\n"
                                      f"Location: {self.events[0][3]}\n"
                                      f"Date&Time: {self.events[0][2]}\n",
                                 anchor="center",
                                 font=("Verdana", 18),
                                 # command=lambda: controller.show_frame
                                 # ("EnrollmentGui"),
                                 fg_color="#317353",
                                 bg_color="#5D623F",
                                 border_width=1,
                                 border_color="#97C2AD",
                                 hover_color="#22533C",
                                 command=lambda:
                                 self.set_eventid(controller,
                                                  "EnrollmentGui",
                                                  self.events[0][0]
                                                  ))
        self.canvas.create_window(180, 600, anchor="nw", window=button_1)

        button_2 = ctk.CTkButton(self,
                                 width=230,
                                 height=150,
                                 corner_radius=5,
                                 # the button text is derived from the events table in the database
                                 text=f"\n{self.events[1][1]}\n\n"
                                 f"Location: {self.events[1][3]}\n"
                                 f"Date&Time: {self.events[1][2]}\n",
                                 anchor="center",
                                 font=("Verdana", 18),
                                 # command=lambda:
                                 # controller.show_frame("EnrollmentGui"),
                                 fg_color="#317353",
                                 bg_color="#9D7C85",
                                 border_width=1,
                                 border_color="#97C2AD",
                                 hover_color="#22533C",
                                 command=lambda:
                                 self.set_eventid(controller, "EnrollmentGui",
                                                  self.events[1][0])
                                 )
        self.canvas.create_window(580, 600, anchor="nw", window=button_2)

        button_3 = ctk.CTkButton(self,
                                 width=230,
                                 height=150,
                                 corner_radius=5,
                                 # the button text is derived from the events
                                 # table in the database
                                 text=f"\n{self.events[2][1]}\n\n"
                                 f"Location: {self.events[2][3]}\n"
                                 f"Date&Time: {self.events[2][2]}\n",
                                 anchor="center",
                                 font=("Verdana", 18),
                                 # command=lambda:
                                 # controller.show_frame("EnrollmentGui"),
                                 fg_color="#317353",
                                 bg_color="#CBA09A",
                                 border_width=1,
                                 border_color="#97C2AD",
                                 hover_color="#22533C",
                                 command=lambda:
                                 self.set_eventid(controller,
                                                  "EnrollmentGui",
                                                  self.events[2][0])
                                 )
        self.canvas.create_window(980, 600, anchor="nw", window=button_3)

    def set_eventid(self, controller, frame_name, seventid):
        """Sets the global EVENTID"""
        global EVENTID
        EVENTID = seventid
        controller.show_frame(frame_name)


class Articles(FrameTemplate, tk.Frame):
    """
    A class that creates a frame to display articles related to climate change
    and mental health.

    Args:
        parent (tkinter.Tk): The parent tkinter object.
        controller: An instance of the controller class that manages the GUI.

    Attributes:
        controller: An instance of the controller class that manages the GUI.
        frame_article1: A tkinter Frame object that displays the first article.
        tree_label: A tkinter Label object that is a placeholder in the first
        article frame.
        article_text: A tkinter Label object that displays the text of the
        first article.
        url1 (str): A string containing the URL of the first article.
        read_more_label: A tkinter Label object that, when clicked, opens the
        URL of the first article in a browser.
        frame_article2: A tkinter Frame object that displays the second
        article.
        tree_label2: A tkinter Label object that is a placeholder in the
        second article frame.
        article_text: A tkinter Label object that displays the text of the
        second article.
        url2 (str): A string containing the URL of the second article.
        read_more_label2: A tkinter Label object that, when clicked, opens the
        URL of the second article in a browser.
        frame_article3: A tkinter Frame object that displays the third article.
        tree_label3: A tkinter Label object that is a placeholder in the third
        article frame.
        article_text: A tkinter Label object that displays the text of the
        third article.
        url3 (str): A string containing the URL of the third article.
        read_more_label3: A tkinter Label object that, when clicked, opens the
        URL of the third article in a browser.
    """

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.23, rely=0.15, anchor="n")
        self.tree_label = ctk.CTkLabel(self.frame_article1, text="         ")
        self.tree_label.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="\n     HOW TO COPE WITH "
                                         "ECO ANXIETY\
                                         \n1. Don't try to deny or "
                                         "Suppress your emotions.\
                                         \n2. Take Action\
                                         \n3. Find the right "
                                         "professionall help\
                                         \n4. Connect with others and "
                                         "share your concerns\
                                         \n5. Spend time in nature\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=1000,
                                         fg_color="#E2EDF7",
                                         text_color="#317353",
                                         bg_color="transparent",
                                         )
        self.article_text.pack(side="left")
        self.url1 = "https://www.everydayhealth.com/eco-anxiety/how-to-cope-with-eco-anxiety/"
        self.read_more_label = ctk.CTkLabel(self,
                                            text="Read More",
                                            text_color="#317353",
                                            cursor="hand",
                                            fg_color="#E2EDF7",
                                            font=("Verdana", 14, "bold"))
        self.read_more_label.place(relx=0.20, rely=0.48, anchor="w")
        self.read_more_label.bind("<Button-1>",
                                  lambda event: webbrowser.open_new(self.url1))

        self.frame_article1 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article1.place(relx=0.25, rely=0.55, anchor="n")
        self.tree_label2 = ctk.CTkLabel(self.frame_article1, text="         ")
        self.tree_label2.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article1,
                                         text="\nADDRESSING CLIMATE "
                                         "CHANGE CONCERNS\
                                             \nIN PRACTISE\
                                             \nThe planet is undergoing "
                                              "rapid and\
                                             \nunprecedented climate "
                                              "change that is creating\
                                             \nstress and mental anguish "
                                              "for people around\
                                             \nthe world\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=1000,
                                         fg_color="#E2EDF7",
                                         text_color="#317353",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url2 = "https://www.apa.org/monitor/2021/03/ce-climate-change"
        self.read_more_label2 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#317353",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 14, "bold"))
        self.read_more_label2.place(relx=0.22, rely=0.85, anchor="w")
        self.read_more_label2.bind("<Button-1>",
                                   lambda event:
                                   webbrowser.open_new(self.url2))

        self.frame_article3 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article3.place(relx=0.55, rely=0.34, anchor="w")
        self.tree_label3 = ctk.CTkLabel(self.frame_article3, text="         ")
        self.tree_label3.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article3,
                                         text="\nCLIMATE ANXIETY: "
                                         "21 RESOURCES TO\
                                         \nENERGISE YOU INTO ACTION\
                                         \n\nFears about the climate crisis "
                                         "getting the better\
                                         \nof you? Greenpeace staff helps "
                                         "you navigate\
                                         \nyour worries about the enviromental\
                                         \nemergency\
                                         \nHere is what they recommended\n\n",
                                         justify="left",
                                         font=("Verdana", 18),
                                         wraplength=2000,
                                         fg_color="#E2EDF7",
                                         text_color="#317353",
                                         bg_color="transparent")
        self.article_text.pack(side="left")
        self.url3 = ("https://www.greenpeace.org.uk/news/climate-anxiety-"
                     "resources-to-energise-action/?gclid="
                     "CjwKCAjwo7iiBhAEEiwAsIxQEdl"
                     "lTZSd97f7yiVjbg1Ktpw3Jl9_R7h9kIYKfGpWW_RWRhhL-"
                     "bIMpRoC0lkQAvD_BwE")
        self.read_more_label3 = ctk.CTkLabel(self,
                                             text="Read More",
                                             text_color="#317353",
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 14, "bold"))
        self.read_more_label3.place(relx=0.67, rely=0.52, anchor="w")
        self.read_more_label3.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(self.url3))
        self.frame_article4 = ctk.CTkFrame(self, fg_color="#E2EDF7")
        self.frame_article4.place(relx=0.89, rely=0.74, anchor="e")
        self.tree_label4 = ctk.CTkLabel(self.frame_article4, text="         ")
        self.tree_label4.pack(side="left")
        self.article_text = ctk.CTkLabel(self.frame_article4,
                                         text="\n7 WAYS TO PREVENT ECO-ANXIETY\
                                         \n\nRead and learn ways to "
                                         "prevent Eco-Anxiety.\
                                         \nLearn about practices you can "
                                         "do at home\
                                         \nsuch as recycling and "
                                         "gardening.\n\n",
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
                                             cursor="hand",
                                             fg_color="#E2EDF7",
                                             font=("Verdana", 14, "bold"))
        self.read_more_label4.place(relx=0.77, rely=0.85, anchor="e")
        self.read_more_label4.bind("<Button-1>",
                                   lambda event: webbrowser.open_new(
                                                            self.url4))


class EnrollmentGui(FrameTemplate, tk.Frame):
    """
    A class that inherits from FrameTemplate and tk.Frame and represents the
    enrollment form for the Eco Therapy application. The class provides various
    fields to input the personal details of the user, like first name,
    last name,email, and date of birth, which are then written to a database
    by clicking the enroll button.
    The class also contains functions to display a message-box if the
    data is saved successfully and to execute the writing process.

    Args:
    parent: The parent frame/widget of the current frame.
    controller: The main controller of the Eco Therapy application.

    Attributes:
    - parent (tk.Tk): The parent widget.
    - controller (tk.Tk): The main widget.
    - database (read_db.DbInteraction): An instance of the DbInteraction class,
      used for reading from and writing to the database.

    Methods:
    - save_data_success(self): Displays a message-box if the data is saved
      successfully.
    - execute_db(self): Writes the data to the database and executes the
      confirmation message.
    """

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.database = read_db.DbInteraction()
        self.canvas.create_text(720, 240, text="Enrollment Form",
                                font=("Verdana", 40, "bold"),
                                fill="#317353")
        polygon = self.canvas.create_polygon(
            5, 15, 15, 5, 15, 10, 25, 10, 25, 20, 15,
            20, 15, 25, 5, 15, fill="#317353")
        x_0, y_0, x_1, y_1 = self.canvas.bbox(polygon)
        button = self.canvas.create_rectangle(x_0, y_0, x_1, y_1, fill="",
                                              outline="")
        self.canvas.tag_bind(button, '<Button-1>', lambda event:
                             controller.show_frame("EnrollGui"))
        self.canvas.create_text(540, 330, text="First Name",
                                font=("Verdana", 25, "bold"),
                                fill="#317353")

        self.first_name_entry = ctk.CTkEntry(self, width=170,
                                             height=50, font=("Verdana", 20),
                                             bg_color="white",
                                             fg_color="white",
                                             border_width=0,
                                             text_color="#317353")
        self.canvas.create_window(475, 350, anchor="nw",
                                  window=self.first_name_entry)
        self.canvas.create_text(815, 330, text="Last Name",
                                font=("Verdana", 25, "bold"),
                                fill="#317353")
        self.last_name_entry = ctk.CTkEntry(self, width=170,
                                            height=50, font=("Verdana", 20),
                                            bg_color="black",
                                            fg_color="white",
                                            border_width=0,
                                            text_color="#317353")
        self.canvas.create_window(750, 350, anchor="nw",
                                  window=self.last_name_entry)

        self.canvas.create_text(720, 460, text="Email",
                                font=("Verdana", 25, "bold"),
                                fill="#317353")
        self.email_entry = ctk.CTkEntry(self, width=300,
                                        height=50, font=("Verdana", 20),
                                        bg_color="white",
                                        fg_color="white",
                                        border_width=0,
                                        text_color="#317353")
        self.canvas.create_window(580, 480, anchor="nw",
                                  window=self.email_entry)

        self.canvas.create_text(720, 580, text="Date of Birth",
                                font=("Verdana", 25, "bold"),
                                fill="#317353")

        with open(file='year.txt', encoding="UTF-8") as file_year:
            year = [line.strip() for line in file_year.readlines()]

        self.options_year = ctk.CTkOptionMenu(self, values=year,
                                              width=100,
                                              height=30,
                                              bg_color="white",
                                              fg_color="white",
                                              button_color="white",
                                              font=("Verdana", 15),
                                              text_color="#317353",
                                              dynamic_resizing=False)
        self.options_year.set("Year")
        self.canvas.create_window(570, 600, anchor="nw",
                                  window=self.options_year)

        with open(file='month.txt', encoding="UTF-8") as file_month:
            month = [line.strip() for line in file_month.readlines()]

        self.options_month = ctk.CTkOptionMenu(self, values=month,
                                               width=110,
                                               height=30,
                                               bg_color="white",
                                               fg_color="white",
                                               button_color="white",
                                               font=("Verdana", 15),
                                               text_color="#317353",
                                               dynamic_resizing=False)
        self.options_month.set("Month")
        self.canvas.create_window(675, 600, anchor="nw",
                                  window=self.options_month)

        with open(file='day.txt', encoding="UTF-8") as file_day:
            read_day = [line.strip() for line in file_day.readlines()]

        self.options_day = ctk.CTkOptionMenu(self, values=read_day,
                                             width=100,
                                             height=30,
                                             bg_color="white",
                                             fg_color="white",
                                             button_color="white",
                                             font=("Verdana", 15),
                                             text_color="#317353",
                                             dynamic_resizing=False)
        self.options_day.set("Day")
        self.canvas.create_window(790, 600, anchor="nw",
                                  window=self.options_day)

        enroll_button = ctk.CTkButton(self, width=100, height=50,
                                      text="Enroll", fg_color="#317353",
                                      bg_color="#317353",
                                      font=("Verdana", 50),
                                      command=lambda: self.execute_db())

        self.canvas.create_window(650, 700, anchor="nw", window=enroll_button)

    def save_data_success(self):
        """Displays message-box if data is saved correctly"""
        messagebox.showinfo(title="Success",
                            message="Data saved successfully!")

    def execute_db(self):
        """Writes data to db and executes confirmation message"""
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.birthday = (f"{self.options_year.get()}-"
                         f"{self.options_month.get()}-{self.options_day.get()}"
                         )
        if not re.match(email_regex, self.email_entry.get()):
            messagebox.showerror(title="Error", message="Invalid email adress")
            return
        self.database.write_db(self.first_name_entry.get(),
                               self.last_name_entry.get(),
                               self.email_entry.get(),
                               self.birthday, EVENTID)

        self.save_data_success()


class AboutUs(FrameTemplate, tk.Frame):
    """
    AboutUs - A class that inherits from FrameTemplate and tk.Frame,
    which displays the about us page of the Eco Therapy application.

    Args:
    parent: The parent frame/widget of the current frame.
    controller: The main controller of the Eco Therapy application.

    Attributes:
    canvas: The canvas object where the contents of the frame are displayed.

    Methods:
    init(self, parent, controller): Initializes the AboutUs frame and
    its contents.
    """
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        FrameTemplate.__init__(self, parent, controller)
        self.controller = controller
        self.canvas.create_text(750, 140,
                                text="About us",
                                font=("Verdana", 100, "bold"),
                                fill='#317353')
        self.canvas.create_text(350, 250,
                                text="Eco Therapy is an"
                                     " application that targets the"
                                     " \nsymptoms of eco anxiety.",
                                font=('Verdana', 22),
                                fill='#317353')
        self.canvas.create_text(550, 450,
                                text="Eco anxiety is a globally growing"
                                     " phenomenon among all ages."
                                     "\nIt includes strong feelings of worry"
                                     " and fear about the decline"
                                     " in the environment."
                                     "\nWays in which eco anxiety can"
                                     " be relieves are:"
                                     "\n\n1. Taking action to help the"
                                     "climate, no matter how small"
                                     "\n2. Recognizing and understanding"
                                     " eco anxiety"
                                     "\n3. Discussions about eco anxiety"
                                     "in groups"
                                     "\n4. Connecting with nature in"
                                     " positive ways",

                                font=('Verdana', 22),
                                fill='#317353')
        self.canvas.create_text(1300, 350,
                                text="Contributors:\
                                    \n\nAxel Friberg\
                                    \nMiina Mäkinen\
                                    \nMarianna Psyllou\
                                    \nCourage Räsänen\
                                    \nKim Zugic",
                                font=("Verdana", 22),
                                fill='#317353')


if __name__ == "__main__":
    appl = App()
    appl.mainloop()
