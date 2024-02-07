import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = tkinker.CTk()
root.geometry("500x350")

def login():
    print("testing.......")



label = tkinker.CTkLabel(master=frame, text="login system", text_font=("Roboto"))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", commend="login")
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkEntry(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop