import tkinter as tk
from tkinter import Grid, ttk, filedialog
from PIL import Image, ImageTk


def create_output(name, id, blood_letter, rh_factor, donation):
    out_str = "Patient Name: {}\n".format(name)
    out_str = out_str+"Blood Type: {}{}\n".format(blood_letter, rh_factor)
    out_str = out_str+"Donation Center: {}\n".format(donation)
    return out_str

def load_and_resize_image(filename):
    pil_image = Image.open(filename)
    image_size = pil_image.size
    resize_factor = 3
    pil_image = pil_image.resize((image_size[0]//resize_factor, 
                                  image_size[1]//resize_factor))
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

def design_window():

    def ok_button_cmd():
        # get data from the GUI
        name = name_data.get()
        id = id_data.get()
        blood_letter = blood_letter_data.get()
        rh_factor= rh_data.get()
        center = donation_center_data.get()
        # Call a testable external function to do the actual work
        answer = create_output(name, id, blood_letter, rh_factor, center)

        # Update GUI
        print(answer)

    def cancel_button_cmd():
        root.destroy()
    
    def change_picture_cmd():
        filename = filedialog.askopenfilename(initialdir='images')
        if filename == "":
            return
        tk_image = load_and_resize_image(filename)
        image_label.configure(image=tk_image)
        image_label.image = tk_image


    root = tk.Tk()
    root.title("Health Database GUI")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0)

    ttk.Label(root, text="Name").grid(column=0, row=1, sticky='e')

    name_data = tk.StringVar()
    name_entry_box = ttk.Entry(root, width=50, textvariable=name_data)
    name_entry_box.grid(column=1, row=1)

    ttk.Label(root, text="ID").grid(column=0, row=2)

    id_data = tk.StringVar()
    id_entry_box = ttk.Entry(root, width=10, textvariable=id_data)
    id_entry_box.grid(column=1, row=2)

    blood_letter_data = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter_data,
                     value='A').grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text="B", variable=blood_letter_data,
                     value='B').grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter_data,
                     value='AB').grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text="O", variable=blood_letter_data,
                     value='O').grid(column=0, row=6, sticky=tk.W)

    rh_data = tk.StringVar()
    rh_checkbox = ttk.Checkbutton(root, text="Rh Positive",
                                  variable=rh_data, onvalue="+",
                                  offvalue="-")
    rh_checkbox.grid(column=1, row=4)

    donation_center_data = tk.StringVar()
    combo_box = ttk.Combobox(root, textvariable=donation_center_data)
    combo_box.state(["readonly"])
    combo_box.grid(column=3, row=1)
    combo_box["values"] = ["Raleigh", "Durham", "Chapel Hill"]
    

    ok_button = ttk.Button(root, text="OK", command=ok_button_cmd)
    ok_button.grid(column=2, row=7)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_button_cmd)
    cancel_button.grid(column=3, row=7)

    tk_image = load_and_resize_image("images/bbwijKR.jpg")
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=0, row=7)

    change_picture_btn = ttk.Button(root, text="Change Picture", 
                                    command=change_picture_cmd)
    change_picture_btn.grid(column=1, row=7)

    root.mainloop()


if __name__ == "__main__":
    design_window()