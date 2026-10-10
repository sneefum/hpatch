import customtkinter as ctk
from PIL import ImageTk
import os

ctk.deactivate_automatic_dpi_awareness()

class PatchElement(ctk.CTkFrame):
    def __init__(self, master, name, **kwargs):
        super().__init__(master, 
            width=520, 
            height=100,
            fg_color="gray20",
        **kwargs)

        self.grid_propagate(False)
        
        self.label = ctk.CTkLabel(self, 
            text=name,
            width=370,
            height=100,
            fg_color="transparent",
            justify="left"
        )

        self.label.grid_propagate(False)
        self.label.grid(
            row=0, 
            column=0,
            padx=90,
        )

class PatchesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.elements = []

    def add_element(self, element):
        self.elements.append(element)
        element.grid(
            row=len(self.elements) - 1,
            column=0,
            padx=20,
            pady=20
        )
        self.update()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("600x800")
        self.title("hPatch")
        self.resizable(False, False)

        self.iconpath = ImageTk.PhotoImage(file=os.path.join("assets","hpatch.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

        self.patches_frame = PatchesFrame(
            master=self, 
            width=560, 
            height=560
        )
        
        for i in range(30):
            self.patches_frame.add_element(
                PatchElement(
                    master=self.patches_frame, 
                    name="test " + str(i),
                )
            )
        
        self.patches_frame.place(
            x=10,
            y=10
        )

app = App()

app.update()

app.mainloop()
