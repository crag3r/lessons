import tkinter
import customtkinter
from tkintermapview import TkinterMapView
import time

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("420x500")
        self.resizable(False,False)
        self.title("Niezbędnik Ucznia")


    def create_widgets(self):
        self.menu_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, sticky="nw")
        self.menu_frame.grid_rowconfigure(4, weight=1)

        self.clock_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.clock_frame.place(relx=1, rely=0, anchor="ne")

        self.srednia = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Oblicz Średnią", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.srednia.grid(row=1, column=0, sticky="ew")

        self.mapa = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Mapa", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=lambda: self.open_map())
        self.mapa.grid(row=2, column=0, sticky="ew")

        self.tekst = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Edytor Tekstu", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.tekst.grid(row=3, column=0, sticky="ew")

        self.calc = customtkinter.CTkButton(self.menu_frame, corner_radius=0, height=40, border_spacing=10, text="Kalkulator", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.calc.grid(row=4, column=0, sticky="ew")

        self.clock = customtkinter.CTkLabel(self.clock_frame, corner_radius=0, height=40, padx=10, pady=10, text="clock.time", fg_color="transparent", text_color=("gray10", "gray90"), anchor="e")
        self.clock.grid(row=1, column=0, sticky="we")
         

    def update_time(self):
        curr_time=time.strftime("%H:%M:%S")
        self.clock.configure(text=curr_time)
        self.after(1000, self.update_time)

    def open_map(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("800x500")
        window.resizable(False,False)

        map_widget = TkinterMapView(window, width=800, height=500, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def run(self):
        self.mainloop()

if __name__=="__main__":
    app = App()
    app.create_widgets()
    app.update_time()
    app.run()
