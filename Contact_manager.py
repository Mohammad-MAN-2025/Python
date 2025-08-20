import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x550")
        self.root.config(bg='#d3f3f5')
        self.root.title("Contact Book")
        self.root.resizable(0, 0)

        # Sample contact list
        self.contact_list = [
            ['Iman Rasuli', '09101234567'],
            ['Mani Roushandust', '09101234589'],
            ['Rahar Nikam', '091211111111'],
            ['Paul Pedro', '58745246'],
            ['Mohit Paul', '5846975'],
            ['Karan Patel', '5647892'],
            ['Sam Sharma', '89685320'],
        ]

        self.name_var = tk.StringVar()
        self.number_var = tk.StringVar()

        self.setup_widgets()
        self.update_listbox()

    def setup_widgets(self):
        # Labels and entries
        tk.Label(self.root, text='Name:', font=("Times New Roman", 18, "bold"), bg='#e0b422', fg='white')\
            .place(x=30, y=20)
        tk.Entry(self.root, textvariable=self.name_var, font=("Arial", 14), width=30)\
            .place(x=200, y=25)

        tk.Label(self.root, text='Contact No:', font=("Times New Roman", 18, "bold"), bg='#e30e95', fg='black')\
            .place(x=30, y=70)
        tk.Entry(self.root, textvariable=self.number_var, font=("Arial", 14), width=30)\
            .place(x=200, y=75)

        # Buttons
        tk.Button(self.root, text="Add", font='Arial 14 bold', bg='#c1f0d1',
                  command=self.add_contact, width=10).place(x=50, y=130)
        tk.Button(self.root, text="Edit", font='Arial 14 bold', bg='#f9f58f',
                  command=self.update_contact, width=10).place(x=200, y=130)
        tk.Button(self.root, text="Delete", font='Arial 14 bold', bg='#ff9999',
                  command=self.delete_contact, width=10).place(x=50, y=180)
        tk.Button(self.root, text="View", font='Arial 14 bold', bg='#add8e6',
                  command=self.view_contact, width=10).place(x=200, y=180)
        tk.Button(self.root, text="Reset", font='Arial 14 bold', bg='#eeeeee',
                  command=self.reset_form, width=10).place(x=50, y=230)
        tk.Button(self.root, text="Exit", font='Arial 14 bold', bg='#f4cccc',
                  command=self.root.quit, width=10).place(x=200, y=230)

        # Contact list (listbox + scrollbar)
        frame = tk.Frame(self.root)
        frame.place(x=450, y=20)
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(frame, font=('Arial', 14), width=25, height=20,
                                  yscrollcommand=scrollbar.set, bg='white', selectbackground='#d0eaff')
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    def update_listbox(self):
        self.contact_list.sort()
        self.listbox.delete(0, tk.END)
        for name, _ in self.contact_list:
            self.listbox.insert(tk.END, name)

    def get_selected_index(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a contact.")
            return None
        return selected[0]

    def reset_form(self):
        self.name_var.set("")
        self.number_var.set("")
        self.listbox.selection_clear(0, tk.END)

    def view_contact(self):
        index = self.get_selected_index()
        if index is not None:
            name, phone = self.contact_list[index]
            self.name_var.set(name)
            self.number_var.set(phone)

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.number_var.get().strip()
        if name and phone:
            self.contact_list.append([name, phone])
            self.update_listbox()
            self.reset_form()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in both name and number.")

    def update_contact(self):
        index = self.get_selected_index()
        if index is not None:
            name = self.name_var.get().strip()
            phone = self.number_var.get().strip()
            if name and phone:
                self.contact_list[index] = [name, phone]
                self.update_listbox()
                self.reset_form()
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showerror("Error", "Please fill in both name and number.")

    def delete_contact(self):
        index = self.get_selected_index()
        if index is not None:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
            if confirm:
                del self.contact_list[index]
                self.update_listbox()
                self.reset_form()

if __name__ == '__main__':
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
