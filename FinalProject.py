import tkinter
import customtkinter
import webview
import mysql.connector
from PIL import ImageTk, Image

# Establish MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rental_system"
)
cursor = connection.cursor()

# CustomTkinter setup
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# Main application window
app = customtkinter.CTk()
app.geometry("600x400")
app.title("Login")


# Function to open web browser for Facebook
def open_facebook():
    webview.create_window("Facebook", 'https://www.facebook.com/')
    webview.start()


# Function to open web browser for Google
def open_google():
    webview.create_window("Google", 'https://myaccount.google.com/?pli=1')
    webview.start()


class Login:
    def __init__(self, master):
        self.master = master

        # Load background image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Login frame
        self.frameLogin = customtkinter.CTkFrame(master=self.lL, width=320, height=360, corner_radius=15)
        self.frameLogin.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Labels and input fields for login
        self.lLT = customtkinter.CTkLabel(master=self.frameLogin, text="Log in to your Account", font=("Century Gothic", 20))
        self.lLT.place(x=10, y=45)

        self.eEmail = customtkinter.CTkEntry(master=self.frameLogin, width=220, placeholder_text="Email")
        self.eEmail.place(x=50, y=110)

        self.ePassword = customtkinter.CTkEntry(master=self.frameLogin, width=220, placeholder_text="Password", show="*")
        self.ePassword.place(x=50, y=165)

        # Show/Hide password checkbox
        self.show_password_checkbox = customtkinter.CTkCheckBox(master=self.frameLogin,text='', checkbox_width=10, checkbox_height=10, command=self.toggle_password)
        self.show_password_checkbox.place(x=275, y=167)

        # Forget password button
        self.lTFP = customtkinter.CTkButton(master=self.frameLogin, fg_color='transparent',text="Forgot Password?", hover_color="#A4A4A4", command=self.forget_password, font=("Century Gothic", 12))
        self.lTFP.place(x=165, y=195)

        # Login and Create Account buttons
        self.bLogin = customtkinter.CTkButton(master=self.frameLogin, text='Login', corner_radius=6, command=self.login)
        self.bLogin.place(x=100, y=225)

        self.bCreate = customtkinter.CTkButton(master=self.frameLogin, text='Create Account', corner_radius=6, command=self.open_create)
        self.bCreate.place(x=100, y=260)

        # Social login buttons
        self.imgGoogle = customtkinter.CTkImage(Image.open("Misc/Google logo.png").resize((20, 20)))
        self.imgFacebook = customtkinter.CTkImage(Image.open("Misc/Facebook.png").resize((20, 20)))

        self.button_google = customtkinter.CTkButton(master=self.frameLogin,width=100,height=20, image=self.imgGoogle, text="Google", compound="left", fg_color="white", hover_color="#A4A4A4", command=open_google)
        self.button_google.place(x=65, y=295)

        self.button_facebook = customtkinter.CTkButton(master=self.frameLogin,width=100,height=20, image=self.imgFacebook, text="Facebook", compound="left", fg_color="white", hover_color="#A4A4A4", command=open_facebook)
        self.button_facebook.place(x=175, y=295)

    # Toggle password visibility
    def toggle_password(self):
        if self.ePassword.cget("show") == "*":
            self.ePassword.configure(show="")
        else:
            self.ePassword.configure(show="*")

    # Handle login functionality
    def login(self):
        email = self.eEmail.get()
        password = self.ePassword.get()

        if not email or not password:
            self.show_message("All fields are required", "red")
            return

        query = "SELECT * FROM customer WHERE email = %s AND password = %s"
        values = (email, password)

        try:
            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                self.master.destroy()
                menu_window = customtkinter.CTk()
                menu_window.geometry("1280x720")
                menu_window.title("Menu")
                Menu(menu_window)
                menu_window.mainloop()
            else:
                self.show_message("Invalid Email or Password", "red")

        except mysql.connector.Error as err:
            self.show_message(f"Error: {err}", "red")

    # Forget password handling
    def forget_password(self):
        self.master.destroy()
        forget_pass_window = customtkinter.CTk()
        forget_pass_window.geometry("600x400")
        forget_pass_window.title("Forgot Password")
        Forget(forget_pass_window)
        forget_pass_window.mainloop()

    # Open Create Account window
    def open_create(self):
        self.master.destroy()
        create_window = customtkinter.CTk()
        create_window.geometry("1280x720")
        create_window.title("Create Account")
        Create(create_window)
        create_window.mainloop()

    # Helper method to show messages on the login frame
    def show_message(self, message, color):
        label = customtkinter.CTkLabel(self.frameLogin, text=message, font=("Century Gothic", 14), text_color=color)
        label.place(x=90, y=330)


class Create:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgC = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lC = customtkinter.CTkLabel(master=self.master, image=self.imgC)
        self.lC.pack()

        # Create Account frame
        self.frameCreate = customtkinter.CTkFrame(master=self.lC, width=420, height=460, corner_radius=15)
        self.frameCreate.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title
        self.lCreate = customtkinter.CTkLabel(master=self.frameCreate, text="Create Account", font=("Century Gothic", 30))
        self.lCreate.place(x=10, y=20)

        # Input fields
        self.eLastN = customtkinter.CTkEntry(master=self.frameCreate, width=320, placeholder_text="Last Name")
        self.eLastN.place(x=50, y=80)

        self.eFirstN = customtkinter.CTkEntry(master=self.frameCreate, width=320, placeholder_text="First Name")
        self.eFirstN.place(x=50, y=130)

        self.eEmailC = customtkinter.CTkEntry(master=self.frameCreate, width=320, placeholder_text="Email")
        self.eEmailC.place(x=50, y=180)

        self.ePasswordC = customtkinter.CTkEntry(master=self.frameCreate, width=320, placeholder_text="Password", show="*")
        self.ePasswordC.place(x=50, y=230)

        self.eAge = customtkinter.CTkEntry(master=self.frameCreate, width=50, placeholder_text="Age")
        self.eAge.place(x=50, y=280)

        self.ePhoneN = customtkinter.CTkEntry(master=self.frameCreate, width=100, placeholder_text="Phone No.")
        self.ePhoneN.place(x=130, y=280)

        self.eLicense = customtkinter.CTkEntry(master=self.frameCreate, width=100, placeholder_text="License No.")
        self.eLicense.place(x=260, y=280)

        self.eAddress = customtkinter.CTkEntry(master=self.frameCreate, width=320, placeholder_text="Address")
        self.eAddress.place(x=50, y=330)

        # Terms and Conditions checkbox
        self.cTerms = customtkinter.CTkCheckBox(master=self.frameCreate, text="I Agree To Terms and Conditions", font=("Century Gothic", 10))
        self.cTerms.place(x=125, y=360)

        # Buttons for Create Account and Back to Login
        self.bCreateC = customtkinter.CTkButton(master=self.frameCreate, text='Create Account', width=120, corner_radius=6, command=self.save_data)
        self.bCreateC.place(x=80, y=400)

        self.bBack = customtkinter.CTkButton(master=self.frameCreate, text='Back to Login', width=120, corner_radius=6, command=self.open_login)
        self.bBack.place(x=220, y=400)

    def save_data(self):
        # Retrieve form data
        last_name = self.eLastN.get()
        first_name = self.eFirstN.get()
        email = self.eEmailC.get()
        password = self.ePasswordC.get()
        age = self.eAge.get()
        phone_no = self.ePhoneN.get()
        license_no = self.eLicense.get()
        address = self.eAddress.get()

        # Validate form data
        if any(field == '' for field in [last_name, first_name, email, password, age, phone_no, license_no, address]):
            self.show_message("All fields are required", "red")
            return

        if not self.cTerms.get():
            self.show_message("Accept the Terms and Conditions", "red")
            return

        # Insert data into the database
        sql_query = """
            INSERT INTO customer (last_name, first_name, email, password, age, phone_no, license_no, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (last_name, first_name, email, password, age, phone_no, license_no, address)

        try:
            cursor.execute(sql_query, values)
            connection.commit()
            self.show_message("Account created successfully!", "green")
        except mysql.connector.Error as err:
            self.show_message(f"Error: {err}", "red")

    def show_message(self, message, color):
        """Helper function to display messages on the frame."""
        message_label = customtkinter.CTkLabel(master=self.frameCreate, text=message, font=("Century Gothic", 14), text_color=color)
        message_label.place(x=50, y=380)

    def open_login(self):
        """Open the login window."""
        self.master.destroy()
        login = customtkinter.CTk()
        login.geometry("600x400")
        login.title("Login")
        Login(login)
        login.mainloop()


class Menu:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgM = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lM = customtkinter.CTkLabel(master=self.master, image=self.imgM)
        self.lM.pack()

        # Menu frame
        self.frameMenu = customtkinter.CTkFrame(master=self.lM, width=730, height=670, corner_radius=15)
        self.frameMenu.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Manufacturer images
        self.imgAston = ImageTk.PhotoImage(Image.open("AstonMartin/Aston Martin.png").resize((200, 100)))
        self.imgToyota = ImageTk.PhotoImage(Image.open("Toyota/Toyota logo.png").resize((200, 100)))
        self.imgLambo = ImageTk.PhotoImage(Image.open("Lambo/Lambo.png").resize((200, 100)))
        self.imgBMW = ImageTk.PhotoImage(Image.open("BMW/BMW Logo.png").resize((200, 100)))
        self.imgAccount = ImageTk.PhotoImage(Image.open("Misc/accounticon.png").resize((50, 50)))
        self.imgLogout = ImageTk.PhotoImage(Image.open("Misc/accountout.png").resize((50, 50)))

        # Title
        self.lTCV = customtkinter.CTkLabel(master=self.frameMenu, text="Choose Your Vehicle Manufacturer", font=("Century Gothic", 20))
        self.lTCV.place(x=10, y=75)

        # Vehicle buttons
        self.bAston = customtkinter.CTkButton(
            master=self.frameMenu, image=self.imgAston, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_aston)
        self.bAston.place(x=120, y=410)

        self.bToyota = customtkinter.CTkButton(
            master=self.frameMenu, image=self.imgToyota, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_toyota)
        self.bToyota.place(x=120, y=210)

        self.bLambo = customtkinter.CTkButton(
            master=self.frameMenu, image=self.imgLambo, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_lambo)
        self.bLambo.place(x=390, y=210)

        self.bBMW = customtkinter.CTkButton(
            master=self.frameMenu, image=self.imgBMW, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_bmw)
        self.bBMW.place(x=390, y=410)

        # Account buttons
        self.bAccount = customtkinter.CTkButton(
            master=self.frameMenu, image=self.imgAccount, width=120, fg_color="transparent",
            text="", corner_radius=6, hover_color="#A4A4A4", command=self.open_account)
        self.bAccount.place(x=630, y=0)

        self.bLogout = customtkinter.CTkButton(
            master=self.frameMenu, image=self.imgLogout, width=120, fg_color="transparent",
            text="", corner_radius=6, hover_color="#A4A4A4", command=self.open_login)
        self.bLogout.place(x=0, y=0)

    def open_login(self):
        """Open the login window."""
        self.master.destroy()
        login = customtkinter.CTk()
        login.geometry("600x400")
        login.title("Login")
        Login(login)
        login.mainloop()

    def open_account(self):
        """Open the account window."""
        self.master.destroy()
        account = customtkinter.CTk()
        account.geometry("600x400")
        account.title("Account")
        Account(account)
        account.mainloop()

    def open_aston(self):
        """Open Aston Martin selection."""
        self.master.destroy()
        aston = customtkinter.CTk()
        aston.geometry("1280x720")
        aston.title("Car Selection - Aston Martin")
        AstonMartin(aston)
        aston.mainloop()

    def open_toyota(self):
        """Open Toyota selection."""
        self.master.destroy()
        toyota = customtkinter.CTk()
        toyota.geometry("1280x720")
        toyota.title("Car Selection - Toyota")
        Toyota(toyota)
        toyota.mainloop()

    def open_lambo(self):
        """Open Lamborghini selection."""
        self.master.destroy()
        lambo = customtkinter.CTk()
        lambo.geometry("1280x720")
        lambo.title("Car Selection - Lamborghini")
        Lamborghini(lambo)
        lambo.mainloop()

    def open_bmw(self):
        """Open BMW selection."""
        self.master.destroy()
        bmw = customtkinter.CTk()
        bmw.geometry("1280x720")
        bmw.title("Car Selection - BMW")
        BMW(bmw)
        bmw.mainloop()


class AstonMartin:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgA = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lA = customtkinter.CTkLabel(master=self.master, image=self.imgA)
        self.lA.pack()

        # Frame to contain the buttons and labels
        self.frame = customtkinter.CTkFrame(master=self.lA, width=1150, height=700, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Vehicle images
        self.imgDBX70 = ImageTk.PhotoImage(Image.open("AstonMartin/2022 Aston Martin DBX70.png").resize((300, 170)))
        self.imgDB7 = ImageTk.PhotoImage(Image.open("AstonMartin/1997 Aston Martin DB7.png").resize((300, 170)))
        self.imgDB12 = ImageTk.PhotoImage(Image.open("AstonMartin/2024 Aston Martin DB12.png").resize((300, 170)))
        self.imgDB11 = ImageTk.PhotoImage(Image.open("AstonMartin/DB11.png").resize((300, 170)))
        self.imgDBVirage = ImageTk.PhotoImage(Image.open("AstonMartin/2012 Aston Martin Virage.png").resize((300, 170)))

        # Title label
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Choose Your Vehicle to Rent", font=("Century Gothic", 30))
        self.l2.place(x=10, y=20)

        # Buttons and labels for each Aston Martin car

        # 2022 Aston Martin DBX7
        self.bAston1 = customtkinter.CTkButton(
            master=self.frame, image=self.imgDBX70, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bAston1.place(x=180, y=90)

        self.lAston1 = customtkinter.CTkLabel(
            master=self.frame, text=f"2022 Aston Martin DBX7\nAutomatic\n5-seats\nPrice: ₱21,000 per day",
            font=("Century Gothic", 15)
        )
        self.lAston1.place(x=250, y=270)

        # 1997 Aston Martin DB7
        self.bAston2 = customtkinter.CTkButton(
            master=self.frame, image=self.imgDB7, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bAston2.place(x=620, y=90)

        self.lAston2 = customtkinter.CTkLabel(
            master=self.frame, text=f"1997 Aston Martin DB7\nManual\n4-Passenger\nPrice: ₱21,500 per day",
            font=("Century Gothic", 15)
        )
        self.lAston2.place(x=700, y=270)

        # 2024 Aston Martin DB12
        self.bAston3 = customtkinter.CTkButton(
            master=self.frame, image=self.imgDB12, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bAston3.place(x=0, y=370)

        self.lAston3 = customtkinter.CTkLabel(
            master=self.frame, text=f"2024 Aston Martin DB12\nAutomatic\n4-Passenger\nPrice: ₱30,000 per day",
            font=("Century Gothic", 15)
        )
        self.lAston3.place(x=80, y=550)

        # 2020 Aston Martin DB11
        self.bAston4 = customtkinter.CTkButton(
            master=self.frame, image=self.imgDB11, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bAston4.place(x=420, y=370)

        self.lAston4 = customtkinter.CTkLabel(
            master=self.frame, text=f"2020 Aston Martin DB11\nAutomatic\n4-Passenger\nPrice: ₱27,000 per day",
            font=("Century Gothic", 15)
        )
        self.lAston4.place(x=500, y=550)

        # 2012 Aston Martin Virage
        self.bAston5 = customtkinter.CTkButton(
            master=self.frame, image=self.imgDBVirage, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bAston5.place(x=835, y=370)

        self.lAston5 = customtkinter.CTkLabel(
            master=self.frame, text=f"2012 Aston Martin Virage\nAutomatic w/ Manual Shift\n4-Passenger\nPrice: ₱26,000 per day",
            font=("Century Gothic", 15)
        )
        self.lAston5.place(x=900, y=550)

        # Cancel button to go back to the menu
        self.bCancel = customtkinter.CTkButton(
            master=self.frame, text="Cancel", width=220, height=30, corner_radius=10, command=self.open_menu
        )
        self.bCancel.place(x=460, y=660)

    def open_payment(self):
        """Open the payment method window."""
        self.master.destroy()
        payment = customtkinter.CTk()
        payment.geometry("600x400")
        payment.title("Payment Method")
        Payment(payment)
        payment.mainloop()

    def open_menu(self):
        """Return to the main menu."""
        self.master.destroy()
        menu = customtkinter.CTk()
        menu.geometry("1280x720")
        menu.title("Menu")
        Menu(menu)
        menu.mainloop()


class Toyota:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgT = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lT = customtkinter.CTkLabel(master=self.master, image=self.imgT)
        self.lT.pack()

        # Frame for the car selection interface
        self.frame = customtkinter.CTkFrame(master=self.lT, width=1150, height=700, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Car images
        self.imgSupra = ImageTk.PhotoImage(Image.open("Toyota/1994 Toyota MK4 Supra.png").resize((300, 170)))
        self.imgFortuner = ImageTk.PhotoImage(Image.open("Toyota/2023 Toyota Fortuner GR-S 4x4 AT.png").resize((300, 170)))
        self.imgGR86 = ImageTk.PhotoImage(Image.open("Toyota/2024 Toyota GR86.png").resize((300, 170)))
        self.imgInnova = ImageTk.PhotoImage(Image.open("Toyota/2024 Toyota Innova 2.8 XE Disele AT.png").resize((300, 170)))
        self.imgVios = ImageTk.PhotoImage(Image.open("Toyota/2024 Toyota Vios 1.3 XLE CVT.png").resize((300, 170)))

        # Title label
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Choose Your Car to Rent", font=("Century Gothic", 30))
        self.l2.place(x=10, y=20)

        # Buttons and labels for each Toyota car

        # 1994 Toyota MK4 Supra
        self.bToyota1 = customtkinter.CTkButton(
            master=self.frame, image=self.imgSupra, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bToyota1.place(x=180, y=90)

        self.lToyota1 = customtkinter.CTkLabel(
            master=self.frame, text=f"1994 Toyota MK4 Supra\nManual\n4-seats\nPrice: ₱26,000 per day",
            font=("Century Gothic", 15)
        )
        self.lToyota1.place(x=250, y=270)

        # 2023 Toyota Fortuner GR-S 4x4 AT
        self.bToyota2 = customtkinter.CTkButton(
            master=self.frame, image=self.imgFortuner, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bToyota2.place(x=650, y=90)

        self.lToyota2 = customtkinter.CTkLabel(
            master=self.frame, text=f"2023 Toyota Fortuner GR-S 4x4 AT\nAutomatic\n7-Passenger\nPrice: ₱2,500 per day",
            font=("Century Gothic", 15)
        )
        self.lToyota2.place(x=700, y=270)

        # 2024 Toyota GR86
        self.bToyota3 = customtkinter.CTkButton(
            master=self.frame, image=self.imgGR86, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bToyota3.place(x=0, y=370)

        self.lToyota3 = customtkinter.CTkLabel(
            master=self.frame, text=f"2024 Toyota GR86\nAutomatic\n4-Passenger\nPrice: ₱25,000 per day",
            font=("Century Gothic", 15)
        )
        self.lToyota3.place(x=80, y=550)

        # 2024 Toyota Innova 2.8 XE Diesel AT
        self.bToyota4 = customtkinter.CTkButton(
            master=self.frame, image=self.imgInnova, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bToyota4.place(x=420, y=370)

        self.lToyota4 = customtkinter.CTkLabel(
            master=self.frame, text=f"2024 Toyota Innova 2.8 XE Diesel AT\nAutomatic\n7-Passenger\nPrice: ₱2,500 per day",
            font=("Century Gothic", 15)
        )
        self.lToyota4.place(x=450, y=550)

        # 2024 Toyota Vios 1.3 XLE CVT
        self.bToyota5 = customtkinter.CTkButton(
            master=self.frame, image=self.imgVios, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bToyota5.place(x=835, y=370)

        self.lToyota5 = customtkinter.CTkLabel(
            master=self.frame, text=f"2024 Toyota Vios 1.3 XLE CVT\nAutomatic\n5-Passenger\nPrice: ₱1,500 per day",
            font=("Century Gothic", 15)
        )
        self.lToyota5.place(x=900, y=550)

        # Cancel button to return to the menu
        self.bCancel = customtkinter.CTkButton(
            master=self.frame, text="Cancel", width=220, height=30, corner_radius=10, command=self.open_menu
        )
        self.bCancel.place(x=460, y=660)

    def open_payment(self):
        """Open the payment method window."""
        self.master.destroy()
        payment = customtkinter.CTk()
        payment.geometry("600x400")
        payment.title("Payment Method")
        Payment(payment)
        payment.mainloop()

    def open_menu(self):
        """Return to the main menu."""
        self.master.destroy()
        menu = customtkinter.CTk()
        menu.geometry("1280x720")
        menu.title("Menu")
        Menu(menu)
        menu.mainloop()


class Lamborghini:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Frame for the Lamborghini car selection interface
        self.frame = customtkinter.CTkFrame(master=self.lL, width=1150, height=700, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Car images
        self.imgUrraco = ImageTk.PhotoImage(Image.open("Lambo/1957 Lamborghini Urraco P200.png").resize((300, 170)))
        self.imgGallardo = ImageTk.PhotoImage(Image.open("Lambo/2010 Lamborghini Gallardo LP550-2.png").resize((300, 170)))
        self.imgHuracanaSpyder = ImageTk.PhotoImage(Image.open("Lambo/2018 Lamborghini Huracana Performante Spyder.png").resize((300, 170)))
        self.imgHuracanaEVO = ImageTk.PhotoImage(Image.open("Lambo/2020 Lamborghini Huracan EVO RWD.png").resize((300, 170)))
        self.imgUrus = ImageTk.PhotoImage(Image.open("Lambo/2018 Lamborghini Urus.png").resize((300, 170)))

        # Title label
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Choose Your Vehicle Type", font=("Century Gothic", 30))
        self.l2.place(x=10, y=20)

        # Buttons and labels for each Lamborghini car

        # 1957 Lamborghini Urraco P200
        self.bLambo1 = customtkinter.CTkButton(
            master=self.frame, image=self.imgUrraco, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo1.place(x=180, y=90)

        self.lLambo1 = customtkinter.CTkLabel(
            master=self.frame, text=f"1957 Lamborghini Urraco P200\nManual\n4-seats\nPrice: ₱21,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo1.place(x=230, y=270)

        # 2010 Lamborghini Gallardo LP550-2
        self.bLambo2 = customtkinter.CTkButton(
            master=self.frame, image=self.imgGallardo, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo2.place(x=620, y=90)

        self.lLambo2 = customtkinter.CTkLabel(
            master=self.frame, text=f"2010 Lamborghini Gallardo LP550-2\nManual\n2-Passenger\nPrice: ₱21,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo2.place(x=650, y=270)

        # 2018 Lamborghini Huracana Performante Spyder
        self.bLambo3 = customtkinter.CTkButton(
            master=self.frame, image=self.imgHuracanaSpyder, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo3.place(x=0, y=370)

        self.lLambo3 = customtkinter.CTkLabel(
            master=self.frame, text=f"2018 Lamborghini Huracana Performante Spyder\nAutomatic\n2-Passenger\nPrice: ₱28,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo3.place(x=0, y=550)

        # 2020 Lamborghini Huracan EVO RWD
        self.bLambo4 = customtkinter.CTkButton(
            master=self.frame, image=self.imgHuracanaEVO, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo4.place(x=420, y=370)

        self.lLambo4 = customtkinter.CTkLabel(
            master=self.frame, text=f"2020 Lamborghini Huracan EVO RWD\nAutomatic\n2-Passenger\nPrice: ₱29,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo4.place(x=450, y=550)

        # 2018 Lamborghini Urus
        self.bLambo5 = customtkinter.CTkButton(
            master=self.frame, image=self.imgUrus, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo5.place(x=835, y=370)

        self.lLambo5 = customtkinter.CTkLabel(
            master=self.frame, text=f"2018 Lamborghini Urus\nAutomatic\n4-Passenger\nPrice: ₱13,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo5.place(x=900, y=550)

        # Cancel button to return to the menu
        self.bCancel = customtkinter.CTkButton(
            master=self.frame, text="Cancel", width=220, height=30, corner_radius=10, command=self.open_menu
        )
        self.bCancel.place(x=460, y=660)

    def open_payment(self):
        """Open the payment method window."""
        self.master.destroy()
        payment = customtkinter.CTk()
        payment.geometry("600x400")
        payment.title("Payment Method")
        Payment(payment)
        payment.mainloop()

    def open_menu(self):
        """Return to the main menu."""
        self.master.destroy()
        menu = customtkinter.CTk()
        menu.geometry("1280x720")
        menu.title("Menu")
        Menu(menu)
        menu.mainloop()


class BMW:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Frame for the Lamborghini car selection interface
        self.frame = customtkinter.CTkFrame(master=self.lL, width=1150, height=700, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Car images
        self.imgUrraco = ImageTk.PhotoImage(Image.open("Lambo/1957 Lamborghini Urraco P200.png").resize((300, 170)))
        self.imgGallardo = ImageTk.PhotoImage(Image.open("Lambo/2010 Lamborghini Gallardo LP550-2.png").resize((300, 170)))
        self.imgHuracanaSpyder = ImageTk.PhotoImage(Image.open("Lambo/2018 Lamborghini Huracana Performante Spyder.png").resize((300, 170)))
        self.imgHuracanaEVO = ImageTk.PhotoImage(Image.open("Lambo/2020 Lamborghini Huracan EVO RWD.png").resize((300, 170)))
        self.imgUrus = ImageTk.PhotoImage(Image.open("Lambo/2018 Lamborghini Urus.png").resize((300, 170)))

        # Title label
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Choose Your Vehicle Type", font=("Century Gothic", 30))
        self.l2.place(x=10, y=20)

        # Buttons and labels for each Lamborghini car

        # 1957 Lamborghini Urraco P200
        self.bLambo1 = customtkinter.CTkButton(
            master=self.frame, image=self.imgUrraco, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo1.place(x=180, y=90)

        self.lLambo1 = customtkinter.CTkLabel(
            master=self.frame, text=f"1957 Lamborghini Urraco P200\nManual\n4-seats\nPrice: ₱21,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo1.place(x=230, y=270)

        # 2010 Lamborghini Gallardo LP550-2
        self.bLambo2 = customtkinter.CTkButton(
            master=self.frame, image=self.imgGallardo, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo2.place(x=620, y=90)

        self.lLambo2 = customtkinter.CTkLabel(
            master=self.frame, text=f"2010 Lamborghini Gallardo LP550-2\nManual\n2-Passenger\nPrice: ₱21,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo2.place(x=650, y=270)

        # 2018 Lamborghini Huracana Performante Spyder
        self.bLambo3 = customtkinter.CTkButton(
            master=self.frame, image=self.imgHuracanaSpyder, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo3.place(x=0, y=370)

        self.lLambo3 = customtkinter.CTkLabel(
            master=self.frame, text=f"2018 Lamborghini Huracana Performante Spyder\nAutomatic\n2-Passenger\nPrice: ₱28,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo3.place(x=0, y=550)

        # 2020 Lamborghini Huracan EVO RWD
        self.bLambo4 = customtkinter.CTkButton(
            master=self.frame, image=self.imgHuracanaEVO, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo4.place(x=420, y=370)

        self.lLambo4 = customtkinter.CTkLabel(
            master=self.frame, text=f"2020 Lamborghini Huracan EVO RWD\nAutomatic\n2-Passenger\nPrice: ₱29,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo4.place(x=450, y=550)

        # 2018 Lamborghini Urus
        self.bLambo5 = customtkinter.CTkButton(
            master=self.frame, image=self.imgUrus, width=200, height=100, text="",
            corner_radius=6, text_color="Black", fg_color="white", hover_color="#A4A4A4", command=self.open_payment
        )
        self.bLambo5.place(x=835, y=370)

        self.lLambo5 = customtkinter.CTkLabel(
            master=self.frame, text=f"2018 Lamborghini Urus\nAutomatic\n4-Passenger\nPrice: ₱13,000 per day",
            font=("Century Gothic", 15)
        )
        self.lLambo5.place(x=900, y=550)

        # Cancel button to return to the menu
        self.bCancel = customtkinter.CTkButton(
            master=self.frame, text="Cancel", width=220, height=30, corner_radius=10, command=self.open_menu
        )
        self.bCancel.place(x=460, y=660)

    def open_payment(self):
        """Open the payment method window."""
        self.master.destroy()
        payment = customtkinter.CTk()
        payment.geometry("600x400")
        payment.title("Payment Method")
        Payment(payment)
        payment.mainloop()

    def open_menu(self):
        """Return to the main menu."""
        self.master.destroy()
        menu = customtkinter.CTk()
        menu.geometry("1280x720")
        menu.title("Menu")
        Menu(menu)
        menu.mainloop()


class Payment:
    def __init__(self, master):
        self.master = master

        # Load Background Image
        self.imgP = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lP = customtkinter.CTkLabel(master=self.master, image=self.imgP)
        self.lP.pack()

        # Main Frame
        self.frame = customtkinter.CTkFrame(master=self.lP, width=360, height=360, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title Label
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Choose Your Payment Method", font=("Century Gothic", 20))
        self.l2.place(x=10, y=45)

        # Payment Buttons
        self.create_payment_button(self.frame, "Pay Online", 70, 120, self.open_online)
        self.create_payment_button(self.frame, "Cash on Hand", 70, 190, self.open_offline)

        # Cancel Button
        self.bCancel = customtkinter.CTkButton(master=self.frame, text="Cancel", width=220, height=30, corner_radius=10, command=self.open_menu)
        self.bCancel.place(x=70, y=320)

        # Result Label
        self.result = customtkinter.CTkLabel(master=self.frame, text="", font=("Century Gothic", 16))
        self.result.place(x=70, y=260)

    def create_payment_button(self, frame, text, x, y, command):
        """Helper function to create payment buttons."""
        button = customtkinter.CTkButton(master=frame, text=text, width=220, height=50, corner_radius=10, command=command)
        button.place(x=x, y=y)

    def open_menu(self):
        self.master.destroy()
        menu = customtkinter.CTk()
        menu.geometry("1280x720")
        menu.title("Menu")
        Menu(menu)
        menu.mainloop()

    def open_online(self):
        self.master.destroy()
        online = customtkinter.CTk()
        online.geometry("1280x720")
        online.title("Online")
        Online(online)
        online.mainloop()

    def open_offline(self):
        self.master.destroy()
        offline = customtkinter.CTk()
        offline.geometry("1280x720")
        offline.title("Offline")
        Offline(offline)
        offline.mainloop()


class Forget:
    def __init__(self, master):
        self.master = master
        self.master.title("Forget Password")

        # Database Connection
        self.connection = mysql.connector.connect(
            host='localhost',
            database='rental_system',
            user='root',
            password=''
        )
        self.cursor = self.connection.cursor()

        # Load Background Image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Frame for Forget Password Form
        self.frameForget = customtkinter.CTkFrame(master=self.master, width=320, height=360, corner_radius=15)
        self.frameForget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title Label
        self.lLT = customtkinter.CTkLabel(master=self.frameForget, text="Change Password", font=("Century Gothic", 20))
        self.lLT.place(x=10, y=45)

        # Email Entry
        self.eNewEmail = customtkinter.CTkEntry(master=self.frameForget, width=220, placeholder_text="Enter Your Email")
        self.eNewEmail.place(x=50, y=110)

        # New Password Entry
        self.eNewpassword = customtkinter.CTkEntry(master=self.frameForget, width=220, placeholder_text="Enter Your New Password", show="*")
        self.eNewpassword.place(x=50, y=150)

        # Update Button
        self.bCreate = customtkinter.CTkButton(master=self.frameForget, width=220, text='Update', corner_radius=6, command=self.save_data)
        self.bCreate.place(x=50, y=260)

        # Back to Login Button
        self.bBack = customtkinter.CTkButton(master=self.frameForget, width=220, text='Back To Login', corner_radius=6, command=self.open_login)
        self.bBack.place(x=50, y=300)

    def save_data(self):
        """Saves new password to the database if the email exists."""
        password = self.eNewpassword.get()
        email = self.eNewEmail.get()

        if not password or not email:
            self.display_message("Please fill in all fields!", "red")
            return

        sql_query = "UPDATE customer SET password=%s WHERE email=%s"
        values = (password, email)

        try:
            self.cursor.execute(sql_query, values)
            if self.cursor.rowcount > 0:
                self.connection.commit()
                self.display_message("Password changed successfully!", "green")
            else:
                self.display_message("Email not found!", "red")
        except mysql.connector.Error as err:
            self.display_message(f"Error: {err}", "red")

    def display_message(self, message, color):
        """Displays status message on the form."""
        customtkinter.CTkLabel(self.frameForget, text=message, font=("Century Gothic", 14), text_color=color).place(x=50, y=380)

    def open_login(self):
        """Opens the login window."""
        self.master.destroy()
        login = customtkinter.CTk()
        login.geometry("600x400")
        login.title("Login")
        Login(login)
        login.mainloop()


class Online:
    def __init__(self, master):
        self.master = master

        # Load background image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Online payment frame
        self.frameOnline = customtkinter.CTkFrame(master=self.lL, width=320, height=400, corner_radius=15)
        self.frameOnline.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title label
        self.lLT = customtkinter.CTkLabel(master=self.frameOnline, text="Online Payment", font=("Century Gothic", 20))
        self.lLT.place(x=85, y=20)

        # Rental days entry
        self.rental_days = customtkinter.CTkEntry(master=self.frameOnline, width=150, placeholder_text="Enter Rental Days")
        self.rental_days.place(x=80, y=80)
        self.rental_days.bind("<KeyRelease>", self.calculate_total)

        # Car amount entry
        self.amount = customtkinter.CTkEntry(master=self.frameOnline, width=150, placeholder_text="Enter Car Amount")
        self.amount.place(x=80, y=120)
        self.amount.bind("<KeyRelease>", self.calculate_total)

        # Payment method dropdown
        self.payment_options = ["Paypal", "Visa", "MasterCard", "Gcash"]
        self.choice = customtkinter.CTkComboBox(master=self.frameOnline, values=self.payment_options, command=self.select_payment_method)
        self.choice.place(x=85, y=160)

        # Total amount label
        self.total_label = customtkinter.CTkLabel(master=self.frameOnline, text="Total: $0.00", font=("Century Gothic", 16))
        self.total_label.place(x=85, y=200)

        # Proceed button
        self.proceed = customtkinter.CTkButton(master=self.frameOnline, text="Proceed", command=self.process_payment)
        self.proceed.place(x=85, y=240)

        # Generate receipt button
        self.receipt = customtkinter.CTkButton(master=self.frameOnline, text="Generate Receipt", command=self.generate_receipt)
        self.receipt.place(x=85, y=280)

    def calculate_total(self, event=None):
        """Calculates the total cost based on rental days and car amount."""
        try:
            rental_days = int(self.rental_days.get()) if self.rental_days.get() else 0
            car_amount = float(self.amount.get()) if self.amount.get() else 0.0
            self.total = rental_days * car_amount
            self.total_label.configure(text=f"Total: ${self.total:.2f}")
        except ValueError:
            self.total_label.configure(text="Total: $0.00")

    def select_payment_method(self, selected_value):
        """Sets the selected payment method."""
        self.selected_payment_method = selected_value
        print(f"Payment method selected: {selected_value}")

    def process_payment(self):
        """Processes payment based on the selected method."""
        if hasattr(self, 'selected_payment_method'):
            method = self.selected_payment_method.lower()
            payment_methods = {
                'paypal': self.paypal,
                'visa': self.visa,
                'mastercard': self.mastercard,
                'gcash': self.gcash
            }
            if method in payment_methods:
                payment_methods[method]()
            else:
                print("Invalid selection.")
        else:
            print("Please select a payment method first.")

    def confirm_payment(self, method):
        """Confirms the payment method."""
        self.payment_method_used = method
        print(f"Payment confirmed using {method}.")

    def paypal(self):
        self.confirm_payment("Paypal")

    def visa(self):
        self.confirm_payment("Visa")

    def mastercard(self):
        self.confirm_payment("MasterCard")

    def gcash(self):
        self.confirm_payment("Gcash")

    def generate_receipt(self):
        """Generates and saves the receipt after payment confirmation."""
        if hasattr(self, 'payment_method_used'):
            try:
                rental_days = self.rental_days.get()
                car_amount = self.amount.get()
                total_amount = self.total if hasattr(self, 'total') else 0

                receipt_content = f"""
                Car Rental Payment Receipt
                ----------------------------
                Rental Duration: {rental_days} days
                Car Amount per Day: ${car_amount}
                Payment Method: {self.payment_method_used}
                Total Amount: ${total_amount:.2f}
                ----------------------------
                We will deliver the car to your address.
                Thank you for trusting our rental service!
                Have a safe journey.
                """

                with open("CarRentalReceipt.txt", "w") as receipt_file:
                    receipt_file.write(receipt_content)

                print("Receipt generated successfully. Check 'CarRentalReceipt.txt' for details.")
                self.display_message("Receipt Generated Successfully!", "green")
            except ValueError:
                self.display_message("Invalid input values.", "red")
        else:
            self.display_message("Please complete the payment first!", "red")

    def display_message(self, message, color):
        """Displays status messages."""
        self.receipt_confirmation_label = customtkinter.CTkLabel(master=self.frameOnline, text=message, text_color=color, font=("Century Gothic", 14))
        self.receipt_confirmation_label.place(x=50, y=340)


class Account:
    def __init__(self, master):
        self.master = master

        # Background image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Account deletion frame
        self.frameAccount = customtkinter.CTkFrame(master=self.lL, width=320, height=360, corner_radius=15)
        self.frameAccount.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title
        self.lLT = customtkinter.CTkLabel(master=self.frameAccount, text="Delete Account", font=("Century Gothic", 20))
        self.lLT.place(x=60, y=45)

        # Email entry field
        self.eEmail = customtkinter.CTkEntry(master=self.frameAccount, width=220, placeholder_text="Email")
        self.eEmail.place(x=50, y=110)

        # Password entry field
        self.ePassword = customtkinter.CTkEntry(master=self.frameAccount, width=220, placeholder_text="Password", show="*")
        self.ePassword.place(x=50, y=165)

        # Delete account button
        self.bDeleteAccount = customtkinter.CTkButton(master=self.frameAccount, width=150, text="Delete Account", command=self.delete_account)
        self.bDeleteAccount.place(x=85, y=225)

    def delete_account(self):
        """Handles account deletion by verifying the email and password fields."""
        email = self.eEmail.get().strip()
        password = self.ePassword.get().strip()

        # Validate input fields
        if not email or not password:
            self.display_message("All fields are required", "red")
            return

        # SQL query to delete account
        sql_query = "DELETE FROM customer WHERE email = %s AND password = %s"
        values = (email, password)

        try:
            cursor.execute(sql_query, values)
            connection.commit()

            if cursor.rowcount > 0:  # Check if any row was deleted
                self.display_message("Account deleted successfully!", "green")
                self.master.after(1500, self.redirect_to_login)  # Redirect to login after success
            else:
                self.display_message("Invalid email or password", "red")
        except mysql.connector.Error as err:
            self.display_message(f"Error: {err}", "red")

    def display_message(self, message, color):
        """Displays feedback messages to the user."""
        self.clear_previous_message()  # Clear any previous message
        self.message_label = customtkinter.CTkLabel(master=self.frameAccount, text=message, font=("Century Gothic", 14), text_color=color)
        self.message_label.place(x=50, y=300)

    def clear_previous_message(self):
        """Clears any existing message to avoid overlapping labels."""
        if hasattr(self, 'message_label'):
            self.message_label.destroy()

    def redirect_to_login(self):
        """Destroys current window and redirects to the login screen."""
        self.master.destroy()
        login_window = customtkinter.CTk()
        login_window.geometry("600x400")
        login_window.title("Login")
        Login(login_window)
        login_window.mainloop()


class Offline:
    def __init__(self, master):
        self.master = master
        self.payment_method_used = False

        # Background image
        self.imgL = ImageTk.PhotoImage(Image.open("Misc/Car.jpg"))
        self.lL = customtkinter.CTkLabel(master=self.master, image=self.imgL)
        self.lL.pack()

        # Offline ticket frame
        self.frameOffline = customtkinter.CTkFrame(master=self.lL, width=320, height=400, corner_radius=15)
        self.frameOffline.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title
        self.lLT = customtkinter.CTkLabel(master=self.frameOffline, text="Offline Ticket", font=("Century Gothic", 20))
        self.lLT.place(x=85, y=20)

        # Manufacturer input
        self.Manufacturer = customtkinter.CTkEntry(master=self.frameOffline, width=150, placeholder_text="Manufacturer")
        self.Manufacturer.place(x=80, y=80)

        # Model input
        self.Model = customtkinter.CTkEntry(master=self.frameOffline, width=150, placeholder_text="Car Model")
        self.Model.place(x=80, y=120)

        # Rental days input
        self.Days = customtkinter.CTkEntry(master=self.frameOffline, width=150, placeholder_text="Rental Days")
        self.Days.place(x=80, y=160)

        # Generate receipt button
        self.bGenerateReceipt = customtkinter.CTkButton(master=self.frameOffline, width=220, text='Generate Receipt',
                                                        corner_radius=6, command=self.generate_receipt)
        self.bGenerateReceipt.place(x=50, y=225)

    def generate_receipt(self):
        """Generates a rental receipt and saves it to a file."""
        manufacturer = self.Manufacturer.get().strip()
        model = self.Model.get().strip()
        days = self.Days.get().strip()

        # Validate inputs
        if not manufacturer or not model or not days:
            self.display_message("All fields are required!", "red")
            return

        # Receipt content
        receipt_content = f"""
        Car Rental Payment Receipt
        ----------------------------
        Manufacturer: {manufacturer}
        Car Model: {model}
        Rental Days: {days}
        ----------------------------
        Please visit our store to complete the payment procedure.
        Thank you for trusting us for your rental service!
        Have a safe journey.
        """

        # Save receipt to a file
        with open("CarRentalTicket.txt", "w") as receipt_file:
            receipt_file.write(receipt_content)

        # Display success message
        self.display_message("Receipt Generated Successfully!", "green")

        # Auto-close after successful generation
        self.master.after(1500, self.master.destroy)

    def display_message(self, message, color):
        """Displays feedback message to the user."""
        self.clear_previous_message()  # Clear any previous message
        self.message_label = customtkinter.CTkLabel(master=self.frameOffline, text=message, text_color=color,
                                                    font=("Century Gothic", 14))
        self.message_label.place(x=50, y=340)

    def clear_previous_message(self):
        """Clears any previous message displayed."""
        if hasattr(self, 'message_label'):
            self.message_label.destroy()

Login(app)
app.mainloop()
connection.close()
