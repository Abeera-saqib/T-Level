import tkinter as tk
def generate_table():
    try:
        num = int(entry.get())
        result.delete(1.0, tk.END) # Clear previous reult

        for i in range(1,11):
            result.insert(tk.END, f"{num} x {i} = {num*i}\n")
    except ValueError:
        result.delete(1.0, tk.END)
        result.insert(tk.END, "please enter a valid number!")

root = tk.Tk()
root.title("Multiplactioin Table Generator")

#Create label and entry for user to enter the number
label = tk.Label(root, text="Enter a number: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

#create button to generate table
button = tk.Button(root, text="Generator Table", command=generate_table)
button.pack()

# Create text widget to display the table
result = tk.Text(root, height=10, width=30)
result.pack()

root.mainloop()
