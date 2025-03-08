import customtkinter as CTk
from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        
        #window
        self.geometry("500x500")
        self.title("Password Generator")
        self.resizable(False, False)

        #logo
        self.logo = CTk.CTkImage(dark_image=Image.open("img/logo.png"),size =(500,200))
        self.logo_label = CTk.CTkLabel(master=self, text = "", image = self.logo)
        self.logo_label.grid(row=0,column=0)

        self.password_frame = CTk.CTkFrame(master = self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20),sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame,width=300)
        self.entry_password.grid(row=0, column=0,padx=(0, 20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="generate",width=100,
                                          command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.password_lenght_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_lenght_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_lenght_entry = CTk.CTkEntry(master=self.settings_frame,width=50)
        self.password_lenght_entry.grid(row=1, column=3,padx=(20, 10),sticky="ew")


    def slider_event(self):
        pass

    def set_password(self):
        pass
#hello 



if __name__ == "__main__":
    app = App()
    app.mainloop()