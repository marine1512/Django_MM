import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("menu hamburger")

def menu():
    def ferme_menu():
        menu_frame.destroy()
        menu_btn.config(text="☰")
        menu_btn.config(command=menu)
    menu_frame = tk.Frame(root, bg="black")

    Home = tk.Button(menu_frame, text="Home", font=("times new roman", 15, "bold"), fg="black", bg="black").place(x=20, y=20)
    Membre = tk.Button(menu_frame, text="Membre", font=("times new roman", 15, "bold"), fg="black", bg="black").place(x=20, y=60)
    Media = tk.Button(menu_frame, text="Media", font=("times new roman", 15, "bold"), fg="black", bg="black").place(x=20, y=100)

    hauteur = root.winfo_height()
    menu_frame.place(x=0, y=50, height=400, width=150)
    menu_btn.config(text='X')
    menu_btn.config(command=ferme_menu)

entete_frame = tk.Frame(root, bg="black", highlightbackground="white", highlightthickness=1)

menu_btn = tk.Button(entete_frame, text="☰", bg='black', fg="black", font=("bold", 20), bd=0, activebackground="black", activeforeground="black", command=menu)
menu_btn.pack(side=tk.LEFT, anchor=tk.W)

menu_label = tk.Label(entete_frame, text="Menu", bg="black", fg="white", font=("bold", 20))
menu_label.pack(side=tk.LEFT)

entete_frame.pack(side=tk.TOP, fill=tk.X)
entete_frame.pack_propagate(False)
entete_frame.config(height=50)

root.mainloop()


