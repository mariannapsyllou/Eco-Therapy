import customtkinter as ctk
from tkinter import PhotoImage


class Enrollment(ctk.CTk):
    #width = 1024
    #height = 900

    def __init__(self, **args):
        ctk.CTk.__init__(self, **args)

        self.title("Enrollment")
        #self.geometry(f"{self.width}x{self.height}")
        self.resizable(True, True)

        self.canvas = ctk.CTkCanvas(self, width=1024, height=900)
        self.bg_image = PhotoImage(file="nature2.png", width=1024, height=900)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.canvas.create_text(512, 140, text="Eco Therapy",
                                font=("Georgia", 90, "bold"),
                                fill="#165806")
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
        self.canvas.create_text(395, 280, text="First Name",
                                font=("Georgia", 20),
                                fill="white")
        first_name_entry = ctk.CTkEntry(self, width=170,
                                        height=50, font=("Helvetica", 20))
        self.canvas.create_window(330, 300, anchor="nw",
                                  window=first_name_entry)
        self.canvas.create_text(615, 280, text="Last Name",
                                font=("Georgia", 20),
                                fill="white")
        last_name_entry = ctk.CTkEntry(self, width=170,
                                       height=50, font=("Helvetica", 20))
        self.canvas.create_window(550, 300, anchor="nw",
                                  window=last_name_entry)
        self.canvas.create_text(470, 380, text="Phone Number",
                                font=("Georgia", 20),
                                fill="white")
        phone_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Helvetica", 20))
        self.canvas.create_window(380, 400, anchor="nw", window=phone_entry)
        self.canvas.create_text(415, 480, text="Email",
                                font=("Georgia", 20),
                                fill="white")
        email_entry = ctk.CTkEntry(self, width=300,
                                   height=50, font=("Helvetica", 20))
        self.canvas.create_window(380, 500, anchor="nw", window=email_entry)

        self.canvas.create_text(445, 580, text="Date of Birth",
                                font=("Georgia", 20),
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
                                         font=("Georgia", 15),
                                         dynamic_resizing=False)
        options_year.set("Year")
        self.canvas.create_window(370, 600, anchor="nw", window=options_year)

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
                                          font=("Georgia", 15),
                                          dynamic_resizing=False)
        options_month.set("Month")
        self.canvas.create_window(475, 600, anchor="nw", window=options_month)

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
                                        font=("Georgia", 15),
                                        dynamic_resizing=False)
        options_day.set("Day")
        self.canvas.create_window(590, 600, anchor="nw", window=options_day)

        def button_function():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            year = options_year.get()
            month = options_month.get()
            day = options_day.get()
            if (phone.isdigit()):
                print(f"{first_name} {last_name}\n{phone}\n{email}\n"
                      f"{year} {month} {day}")
            else:
                self.canvas.create_text(520, 460,
                                        text=("Please enter a "
                                              "correct phone number"),
                                        font=("Verdana", 13, "bold"),
                                        fill="red")

        enroll_button = ctk.CTkButton(self, width=100, height=50,
                                      text="Enroll", fg_color="#165806",
                                      bg_color="#165806",
                                      font=("Georgia", 50, "bold"),
                                      command=button_function)
        self.canvas.create_window(450, 700, anchor="nw", window=enroll_button)


if __name__ == "__main__":
    enroll = Enrollment()
    enroll.mainloop()
