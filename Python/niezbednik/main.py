import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("420x500")
        self.resizable(False,False)
        self.title("Niezbędnik Ucznia")

        self.menu_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.menu_frame.grid_rowconfigure(4, weight=1)

        self.srednia = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Oblicz Średnią",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.srednia.grid(row=1, column=0, sticky="ew")

        self.mapa = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Mapa",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.mapa.grid(row=2, column=0, sticky="ew")

        self.tekst = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Edytor Tekstu",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.tekst.grid(row=3, column=0, sticky="ew")

        self.calc = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Kalkulator",fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.calc.grid(row=4, column=0, sticky="ew")



if __name__=="__main__":
    app = App()
    app.mainloop()