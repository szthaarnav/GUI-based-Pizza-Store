import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os

pizza_prices = {}
pizzas = []
pizza_images = {}
cart = []

def load_pizza_prices(csv_file="pizza_prices.csv"):
    pizza_prices.clear()
    pizzas.clear()
    with open(csv_file, mode='r') as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if len(row) < 2: continue
            name, price = row
            name = name.strip()
            pizza_prices[name] = float(price)
            pizzas.append(name)

def get_image(pizza_name,size=(100, 100)):
    VALID_IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg"]
    for extsn_each in VALID_IMAGE_EXTENSIONS:
        img_path = f"pizzas_imgs/{pizza_name}{extsn_each}"
        if os.path.exists(img_path):
            if img_path not in pizza_images:
                img = Image.open(img_path).resize(size)
                pizza_images[img_path] = ImageTk.PhotoImage(img)
            return pizza_images[img_path]
    print(f"Error found while finding images.")
    return None

root = tk.Tk()
root.title("GUI-based Pizza Store")
root.geometry("1920x1080")

top_menu_frame = tk.Frame(root,height=50,bg="lightgray")
top_menu_frame.pack(fill="x")

pizza_display_frame = tk.Frame(root,bg="red",height=400)
pizza_display_frame.pack(fill="both",expand=True)

pizza_detail_frame = tk.Frame(pizza_display_frame,bg="black",width=400)
pizza_detail_frame.pack(side="right",fill="y")
pizza_detail_frame.pack_propagate(False)

order_details_frame = tk.Frame(root,bg="green",height=300)
order_details_frame.pack(fill="both")

def clear_content_frames():
    if pizza_display_frame.winfo_exists():
        for widget in pizza_display_frame.winfo_children():
            if widget != pizza_detail_frame:
                widget.destroy()

    if pizza_detail_frame.winfo_exists():
        for widget in pizza_detail_frame.winfo_children():
            widget.destroy()

    if order_details_frame.winfo_exists():
        for widget in order_details_frame.winfo_children():
            widget.destroy()

    pizza_display_frame.config(bg="red")
    pizza_detail_frame.config(bg="red")
    order_details_frame.config(bg="red")

def show_all_pizzas():
    clear_content_frames()
    pizza_display_frame.config(bg="red")
    pizza_detail_frame.config(bg="black")
    order_details_frame.config(bg="green")

    pizzas_row_each = 5
    row_frame = None
    for i, name in enumerate(pizzas):
        img = get_image(name)
        if not img:
            print(f"Image not found.")
            continue

        if i % pizzas_row_each == 0:
            row_frame = tk.Frame(pizza_display_frame,bg="red")
            row_frame.pack(fill="x",pady=5)

        bttn = tk.Button(row_frame,image=img,text=name,compound="top",command=lambda n=name: show_pizza_detail(n))
        bttn.image = img
        bttn.pack(side="left",padx=10)

    show_bttn.config(state="disabled",bg="gray")
    clear_bttn.config(state="normal",bg="SystemButtonFace")

def clear_all_pizzas():
    clear_content_frames()
    clear_pizza_detail()
    clear_bttn.config(state="disabled",bg="gray")
    show_bttn.config(state="normal",bg="SystemButtonFace")

def clear_pizza_detail():
    for widget in pizza_detail_frame.winfo_children():
        widget.destroy()

def show_pizza_detail(name):
    clear_pizza_detail()
    pizza_detail_frame.columnconfigure(0,minsize=146)
    pizza_detail_frame.columnconfigure(1,minsize=146)
    pizza_detail_frame.columnconfigure(2,minsize=96)

    img = get_image(name,size=(150,150))
    price = pizza_prices.get(name,0.0)

    if img:
        img_label = tk.Label(pizza_detail_frame,image=img,bg="white")
        img_label.image = img
        img_label.grid(row=0,column=0,pady=(10, 5),padx=10)

    name_label = tk.Label(pizza_detail_frame, text=name, font=("Arial", 11, "bold"), bg="white",width=17,anchor='center')
    name_label.grid(row=0,column=1,pady=5)

    price_label = tk.Label(pizza_detail_frame,text=f"Price: £{price:.2f}",bg="white")
    price_label.grid(row=1,column=0,padx=10,pady=10)

    qty_label = tk.Label(pizza_detail_frame,text="Quantity:",bg="white")
    qty_label.grid(row=1,column=1,padx=10)
    qty_var = tk.IntVar(value=1)
    qty_spinbox = tk.Spinbox(pizza_detail_frame,from_=1,to=10, textvariable=qty_var,width=5,bg="white")
    qty_spinbox.grid(row=1,column=2,padx=(10,20))

    def add_to_cart():
        for i,(p,q) in enumerate(cart):
            if p == name:
                cart[i] = (p,q + qty_var.get())
                break
        else:
            cart.append((name,qty_var.get()))
        clear_pizza_detail()
        update_order_details()

    tk.Button(pizza_detail_frame,text="Cancel",command=clear_pizza_detail).grid(row=3,column=0,padx=10,pady=10)
    tk.Button(pizza_detail_frame,text="Add to Cart",command=add_to_cart).grid(row=3,column=1,padx=10)

def update_order_details():
    for widget in order_details_frame.winfo_children():
        widget.destroy()

    if not cart:
        tk.Label(order_details_frame,text="Your cart is empty",bg="green",font=("Arial",12)).pack(pady=10)
        return

    tk.Label(order_details_frame,text="Your order details:",bg="white",fg="black").pack(anchor="w",padx=10,pady=10)
    grand_total = 0
    for name,qty in cart:
        item_frame = tk.Frame(order_details_frame,bg="white",bd=1,relief="solid",padx=5,pady=5)
        item_frame.pack(side="left",padx=10,pady=10)
        img = get_image(name,size=(80,80))
        if img:
            tk.Label(item_frame,image=img,bg="white").pack()
        tk.Label(item_frame,text=name,bg="white",font=("Arial",10,"bold")).pack(pady=(5,0))
        tk.Label(item_frame,text=f"Qty: {qty}",bg="white").pack(pady=2)
        total = qty * pizza_prices.get(name,0.0)
        grand_total += total
        tk.Label(item_frame,text=f"Total: £{total:.2f}",bg="white").pack(pady=2)

    tk.Label(order_details_frame,text=f"Grand Total: £{grand_total:.2f}",bg="white",font=("Arial",12,"bold")).pack(pady=10)
    bttn_frame = tk.Frame(order_details_frame,bg="green")
    bttn_frame.pack(pady=5)
    tk.Button(bttn_frame,text="Cancel",command=cancel_order).pack(side="left",padx=10)
    tk.Button(bttn_frame,text="Confirm",command=confirm_order).pack(side="left",padx=10)

def cancel_order():
    cart.clear()
    clear_pizza_detail()
    update_order_details()

def generate_receipt():
    if not cart:
        return

    lines = []
    lines.append("Pizza Order Receipt\n")
    lines.append("Items:\n")

    grand_total = 0
    for name,qty in cart:
        price = pizza_prices.get(name,0.0)
        total = qty * price
        grand_total += total
        lines.append(f"{name:<20} Qty: {qty:<3} Price: £{price:.2f}  Total: £{total:.2f}")

    lines.append(f"\nGrand Total: £{grand_total:.2f}")

    with open("receipt.txt","w") as f:
        f.write("\n".join(lines))

def confirm_order():
    if cart:
        generate_receipt()
        cart.clear()
        clear_pizza_detail()
        for widget in order_details_frame.winfo_children():
            widget.destroy()
        tk.Label(order_details_frame,text="Order successfully placed!",bg="green",font=("Arial",12,"bold"),fg="white").pack(pady=10)
        receipt_bttn = tk.Button(order_details_frame,text="Click for Receipt",command=open_receipt,bg="white",font=("Arial",8,"bold"))
        receipt_bttn.pack(pady=5)
    else:
        for widget in order_details_frame.winfo_children():
            widget.destroy()
        tk.Label(order_details_frame,text="Cart is empty!",bg="green",font=("Arial",12,"bold"), fg="white").pack(pady=10)

def open_receipt():
    os.startfile("receipt.txt")  

def nonfunc_add(): 
    print("Add New Button Activated")
    messagebox.showinfo("Add New","Feature to be implemented.")

def nonfunc_delete(): 
    print("Delete Button Activated")
    messagebox.showinfo("Delete","Feature to be implemented.")

def quit_app():
    confirm = messagebox.askyesno("Quit","Are you sure you want to quit the application?")
    if confirm:
        root.destroy()

show_bttn = tk.Button(top_menu_frame,text="Show All Pizzas",command=show_all_pizzas)
clear_bttn = tk.Button(top_menu_frame,text="Clear All Pizzas",command=clear_all_pizzas)
show_bttn.pack(side="left",padx=5,pady=5)
clear_bttn.pack(side="left",padx=5,pady=5)
tk.Button(top_menu_frame,text="Add New",command=nonfunc_add).pack(side="left",padx=5,pady=5)
tk.Button(top_menu_frame,text="Delete",command=nonfunc_delete).pack(side="left",padx=5,pady=5)
tk.Button(top_menu_frame,text="Quit",command=quit_app).pack(side="left",padx=5,pady=5)

def startup_empty_display():
    clear_content_frames()
    blank_space = tk.Label(pizza_display_frame,bg="red",height=10)
    blank_space.pack()
    pizza_detail_frame.config(bg="black")
    order_details_frame.config(bg="green")
    clear_bttn.config(state="disabled",bg="gray")

load_pizza_prices()
update_order_details()
startup_empty_display()
root.mainloop()