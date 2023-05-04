import customtkinter as ctk
from tkinter import PhotoImage


class Activities(ctk.CTk):

    def __init__(self, **args):
        ctk.CTk.__init__(self, **args)

        # window title top left corner
        self.title("Activities")

        # window and background image
        self.canvas = ctk.CTkCanvas(self)
        self.resizable(True, True)
        self.bg_image = PhotoImage(file="bb.png")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Page header
        self.canvas.create_text(
                                750, 200,
                                text="ACTIVITIES",
                                font=("Verdana", 70, "bold"),
                                fill='#11BC90',
                                anchor="center"
                                )
        
        # NavBar labels (350 between each label)
        self.canvas.create_text(
                                200, 30,
                                text="Home",
                                font=("Helvetica", 16),
                                fill='white'
                                )
        self.canvas.create_text(
                                550, 30,
                                text="About us",
                                font=('Helvetica', 16),
                                fill='white'
                                )
        self.canvas.create_text(
                                900, 30,
                                text="Volunteer",
                                font=('Helvetica', 16),
                                fill='white'
                                )
        self.canvas.create_text(
                                1250, 30,
                                text="Blog",
                                font=('Helvetica', 16),
                                fill='white'
                                )


        # Buttons for each activity. 
        # There could be a create button mehtod, so less code is repeated.
        # The text could be stored as a string variable and passed to a button.
        button_1 = ctk.CTkButton(
                                self, 
                                width=230, 
                                height=150,
                                corner_radius=5,
                                # the button text is derived from the events table in the database
                                text="WASTE COLLECTION\n\nKristianstad",
                                anchor="center",
                                font=("Verdana", 18),
                                #command=lambda: controller.show_frame("EnrollmentGui"),
                                fg_color="#317353",
                                bg_color="#5D623F",
                                border_width=1,
                                border_color="#97C2AD",
                                hover_color="#22533C"
                                )
        self.canvas.create_window(180, 600, anchor="nw", window=button_1)

        button_2 = ctk.CTkButton(
                                self, 
                                width=230, 
                                height=150,
                                corner_radius=5,
                                # the button text is derived from the events table in the database
                                text="PLANT TREES\n\nHelsingborg",
                                anchor="center",
                                font=("Verdana", 18),
                                #command=lambda: controller.show_frame("EnrollmentGui"),
                                fg_color="#317353",
                                bg_color="#9D7C85",
                                border_width=1,
                                border_color="#97C2AD",
                                hover_color="#22533C"
                                )
        self.canvas.create_window(580, 600, anchor="nw", window=button_2)

        button_3 = ctk.CTkButton(
                                self, 
                                width=230, 
                                height=150,
                                corner_radius=5,
                                # the button text is derived from the events table in the database
                                text="FOREST HIKE\n\nMalmö",
                                anchor="center",
                                font=("Verdana", 18),
                                #command=lambda: controller.show_frame("EnrollmentGui"),
                                fg_color="#317353",
                                bg_color="#CBA09A",
                                border_width=1,
                                border_color="#97C2AD",
                                hover_color="#22533C"
                                )
        self.canvas.create_window(980, 600, anchor="nw", window=button_3)


if __name__ == "__main__":
    activities = Activities()
    activities.mainloop()
