from tkinter import ttk
from Model import *
from Controller import *
import tkinter as tk
from tkinter import *
from tkinter import simpledialog,messagebox

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Головне вікно")
        self.root.config(bg="#F5F5F5")
        self.root.geometry("1000x750")
        self.root.resizable(False, False)
        self.menu=Label(root, text='Меню', font='Georgia 14',bg="#F5F5F5", fg="#3F2305").place(x=320)
        self.tree=ttk.Treeview(self.root, column=("c1", "c2", "c3"), show='headings', height=5)
        self.tree.column("# 1", anchor=CENTER, width=500)
        self.tree.heading("# 1", text="Назва")
        self.tree.column("# 2", anchor=CENTER, width=100)
        self.tree.heading("# 2", text="Час (хв)")
        self.tree.column("# 3", anchor=CENTER, width=100)
        self.tree.heading("# 3", text="Ціна")
        self.tree.place(x=10,y=30)
        self.dishesadd_button = tk.Button(self.root, text="Додати страву",bg="#F2EAD3", fg="#3F2305", command=lambda: self.add_dish_to_list())
        self.dishesadd_button.place(x=800,y=50)
        self.dishesdel_button = tk.Button(self.root, text="Видалити страву",bg="#F2EAD3", fg="#3F2305", command=lambda:self.remove_dish())
        self.dishesdel_button.place(x=800,y=80)
        self.disheschange_button = tk.Button(self.root, text="Змінити страву",bg="#F2EAD3", fg="#3F2305", command=lambda:self.update_dish_in_list())
        self.disheschange_button.place(x=800,y=110)

        self.ing=Label(root, text='Інгредієнти', font='Georgia 14',bg="#F5F5F5", fg="#3F2305")
        self.ing.place(x=300, y=170)
        self.ingredients_list = tk.Listbox(self.root)
        self.ingredients_list.place(x=300, y=200)
        self.ingredientsadd_button = tk.Button(self.root, text="Додати інгредієнт",bg="#F2EAD3", fg="#3F2305", command=lambda: self.add_ingridient_to_list())
        self.ingredientsadd_button.place(x=800, y=220)
        self.ingredientdel_button = tk.Button(self.root, text="Видалити інгредієнт",bg="#F2EAD3", fg="#3F2305", command=lambda: self.remove_ingredient_from_list())
        self.ingredientdel_button.place(x=800, y=250)
        self.ingredientchange_button = tk.Button(self.root, text="Змінити інгредієнт",bg="#F2EAD3", fg="#3F2305", command=lambda: self.Change_ingredient_from_list())
        self.ingredientchange_button.place(x=800, y=280)

        self.ord=Label(root, text='Замовлення', font='Georgia 14',bg="#F5F5F5", fg="#3F2305")
        self.ord.place(x=300, y=380)
        self.tree1 = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4", "c4"), show='headings', height=5)
        self.tree1.column("# 1", anchor=CENTER, width=300)
        self.tree1.heading("# 1", text="Назва")
        self.tree1.column("# 2", anchor=CENTER, width=200)
        self.tree1.heading("# 2", text="додати")
        self.tree1.column("# 3", anchor=CENTER, width=70)
        self.tree1.heading("# 3", text="Ціна")
        self.tree1.column("# 4", anchor=CENTER, width=70)
        self.tree1.heading("# 4", text="Кількість")
        self.tree1.column("# 5", anchor=CENTER, width=60)
        self.tree1.heading("# 5", text="Столик")
        self.tree1.place(x=10, y=410)
        self.dishebuy_button = tk.Button(self.root, text="Додати страву",bg="#F2EAD3", fg="#3F2305", command=lambda: self.add_dish_to_order())
        self.dishebuy_button.place(x=800, y=400)
        self.dishesdcancle_button = tk.Button(self.root, text="Видалити страву",bg="#F2EAD3", fg="#3F2305", command=lambda: self.remove_dish_from_order())
        self.dishesdcancle_button.place(x=800, y=430)
        self.table_button = tk.Button(self.root, text="Редагувати замовлення",bg="#F2EAD3", fg="#3F2305", command=lambda: self.UPDATE_ORDER_WINDOW())
        self.table_button.place(x=800, y=460)

        self.cancleadd_button = tk.Button(self.root, text="Додати інгредієнт",bg="#F2EAD3", fg="#3F2305", command=lambda: self.add_ingtidient_to_order())
        self.cancleadd_button.place(x=800, y=520)
        self.Ndishes_button = tk.Button(self.root, text="Видалити інгредієнт",bg="#F2EAD3", fg="#3F2305", command=lambda: self.remove_ingredients_from_order())
        self.Ndishes_button.place(x=800, y=550)

        self.tip_text = Label(root, text='Додати чайові', font='Georgia 14',bg="#F5F5F5", fg="#3F2305")
        self.tip_text.place(x=10, y=670)
        self.tip_entry=Entry(root, width=5, font="Georgia 12")
        self.tip_entry.place(x=200, y=670)
        self.order_fin_button = tk.Button(self.root, text="Замовити",bg="#F2EAD3", fg="#3F2305", command=lambda: self.complete_order())
        self.order_fin_button.place(x=400, y=700)

        self.ing_search_text = Label(root, text='Пошук інгредієнтів:', font='Georgia 14',bg="#F5F5F5", fg="#3F2305")
        self.ing_search_text.place(x=10, y=550)
        self.ing_search_entry = Entry(root, width=20, font="Georgia 12")
        self.ing_search_entry.place(x=200, y=550)
        self.ing_search_button = tk.Button(self.root, text="Знайти",bg="#F2EAD3", fg="#3F2305", command=self.search_ingredients)
        self.ing_search_button.place(x=420, y=545)


        self.order_search_text = Label(root, text='Пошук замовлень:', font='Georgia 14',bg="#F5F5F5", fg="#3F2305")
        self.order_search_text.place(x=10, y=590)
        self.order_search_entry = Entry(root, width=20, font="Georgia 12")
        self.order_search_entry.place(x=200, y=590)
        self.order_search_button = tk.Button(self.root, text="Знайти",bg="#F2EAD3", fg="#3F2305", command=self.search_orders)
        self.order_search_button.place(x=420, y=585)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.login_button = tk.Button(self.root, text="Увійти/Вийти",bg="#F2EAD3", fg="#3F2305", command=lambda: self.Login())
        self.login_button.place(x=900, y=10)

        self.access_rights = 0

        self.current_frame = None

    def set_controller(self, controller):
        self.controller = controller

    def search_ingredients(self):
        keyword = self.ing_search_entry.get()
        self.controller.search_ingredients(keyword)

    def search_orders(self):
        keyword = self.order_search_entry.get()
        self.controller.search_orders(keyword)

    def display_search_results(self, results, search_type):
        if search_type == "ingredients":
            self.ingredients_list.delete(0, END)
            for result in results:
                self.ingredients_list.insert(tk.END, result)
        elif search_type == "orders":
            self.tree1.delete(*self.tree1.get_children())
            for ind, result in enumerate(results):
                self.tree1.insert('', 'end', iid=ind, values=(result))

    def Login(self):
        if self.access_rights:
            self.access_rights = 0
        else:
            self.access_rights=self.check_access()

    def add_dish_to_list(self):
        self.pos=None
        self.ADD_NEW_DISH_WINDOW()

    def update_dish_in_list(self):
        self.pos=self.tree.focus()
        self.ADD_NEW_DISH_WINDOW()

    def add_ingridient_to_list(self):
        if self.access_rights == 1:
            self.pos = self.tree.focus()
            ingredient = simpledialog.askstring("Input", "Enter ingredient name:")
            if ingredient:
                self.controller.add_ingredient(ingredient, self.pos)
        else:
            messagebox.showerror('', "у доступі відказано")

    def remove_ingredient_from_list(self):
        if self.access_rights == 1:
            self.pos = self.tree.focus()
            ingredient = self.ingredients_list.get(tk.ACTIVE)
            if ingredient:
                self.controller.remove_ingredient(ingredient,self.pos)
        else:
            messagebox.showerror('', "у доступі відказано")

    def Change_ingredient_from_list(self):
        if self.access_rights == 1:
            self.pos = self.tree.focus()
            new_ingredient = simpledialog.askstring("Input", "Enter ingredient name:")
            ingredient = self.ingredients_list.get(tk.ACTIVE)
            if ingredient:
                self.controller.update_ingredient(ingredient,new_ingredient,self.pos)
        else:
            messagebox.showerror('', "у доступі відказано")

    def add_dish_to_order(self):
        if self.tree.focus():
            table = simpledialog.askinteger("Input", "Номер столика:")
            dish=int(self.tree.focus())
            self.controller.add_order(dish, table)

    def remove_dish_from_order(self):
        dish = int(self.tree1.focus())
        self.controller.remove_order(dish)


    def ADD_NEW_DISH_WINDOW(self):
        if self.access_rights == 1:
            self.adddishWindow = Tk()
            self.adddishWindow.lift()
            self.adddishWindow.geometry("300x400")
            self.adddishWindow.config(bg="#F5F5F5")
            self.adddishWindow.title("Нова страва")
            self.adddishWindow.resizable(False, False)
            self.name_text = Label(self.adddishWindow, text='Додати назву:',bg="#F5F5F5", fg="#3F2305", font='Georgia 14')
            self.name_text.place(x=30, y=20)
            self.name_entry = Entry(self.adddishWindow, width=20, font="Georgia 12")
            self.name_entry.place(x=30, y=60)
            self.ing_text = Label(self.adddishWindow, text='Додати інгредієнти:',bg="#F5F5F5", fg="#3F2305", font='Georgia 14')
            self.ing_text.place(x=30, y=100)
            self.ing_entry = Entry(self.adddishWindow, width=20, font="Georgia 12")
            self.ing_entry.place(x=30, y=140)
            self.time_cost_text = Label(self.adddishWindow, text='Час приготування та ціна:',bg="#F5F5F5", fg="#3F2305", font='Georgia 14')
            self.time_cost_text.place(x=30, y=180)
            self.time_entry = Entry(self.adddishWindow, width=5, font="Georgia 12")
            self.time_entry.place(x=30, y=220)
            self.cost_entry = Entry(self.adddishWindow, width=5, font="Georgia 12")
            self.cost_entry.place(x=100, y=220)
            self.Add_dish_button = tk.Button(self.adddishWindow, text="Додати", command=self.add_dish, font='Georgia 16',bg="#F2EAD3", fg="#3F2305")
            self.Add_dish_button.place(x=90, y=280)
            self.adddishWindow.mainloop()
        else:
            messagebox.showerror('', "у доступі відказано")

    def UPDATE_ORDER_WINDOW(self):
        self.pos1 = self.tree1.focus()
        self.updateorderWindow = Tk()
        self.updateorderWindow.lift()
        self.updateorderWindow.geometry("300x400")
        self.updateorderWindow.config(bg="#F5F5F5")
        self.updateorderWindow.title("Редактор замовлення")
        self.updateorderWindow.resizable(False, False)
        self.table_text = Label(self.updateorderWindow, text='Змінити столик:',bg="#F5F5F5", fg="#3F2305", font='Georgia 14')
        self.table_text.place(x=30, y=20)
        self.table_entry = Entry(self.updateorderWindow, width=3, font="Georgia 12")
        self.table_entry.place(x=30, y=60)
        self.ing_text = Label(self.updateorderWindow, text='Додати інгредієнти:',bg="#F5F5F5", fg="#3F2305", font='Georgia 14')
        self.ing_text.place(x=30, y=100)
        self.ing_entry = Entry(self.updateorderWindow, width=20, font="Georgia 12")
        self.ing_entry.place(x=30, y=140)
        self.amount_cost_text = Label(self.updateorderWindow, text='Кількість страв:',bg="#F5F5F5", fg="#3F2305", font='Georgia 14')
        self.amount_cost_text.place(x=30, y=180)
        self.amount_entry = Entry(self.updateorderWindow, width=5, font="Georgia 12")
        self.amount_entry.place(x=30, y=220)
        self.update_dish_button = tk.Button(self.updateorderWindow, text="Змінити", command=self.update_order, font='Georgia 16',bg="#F2EAD3", fg="#3F2305")
        self.update_dish_button.place(x=90, y=280)
        self.updateorderWindow.mainloop()

    def check_access(self):
        code = simpledialog.askstring("Input", "Введіть код адміністратора:")

        return self.controller.check_code(code)

    def add_dish(self):
        self.dish = []
        self.dish.append(self.name_entry.get())
        self.dish.append(self.time_entry.get())
        self.dish.append(self.cost_entry.get())
        self.dish.append(self.ing_entry.get().split(', '))
        dish =self.dish
        if self.pos==None:
            self.controller.add_dish(dish)
        else:
            self.controller.update_dish(dish,self.pos)

    def remove_dish(self):
        dish = int(self.tree.focus())

        self.controller.remove_dish(dish)

    def update_order(self):
        self.dish = []

        self.dish.append(self.ing_entry.get())
        self.dish.append(self.amount_entry.get())
        self.dish.append(self.table_entry.get())
        self.controller.update_order(self.dish, self.pos1)

    def add_ingtidient_to_order(self):
        self.pos = self.tree1.focus()
        ingredient = simpledialog.askstring("Input", "Enter ingredient name:")
        if ingredient:
            self.controller.add_ingredient_to_order(ingredient, self.pos)

    def remove_ingredients_from_order(self):
            self.pos = self.tree1.focus()
            self.controller.remove_ingredient_from_order(self.pos)

    def complete_order(self):
        price=self.price
        if float(self.tip_entry.get())>0:
            price+=float(self.tip_entry.get())
        messagebox.showinfo('Замовлення прийнято', "Дякуємо! Вартість замовлення: {} грн".format(price))

    def update(self, model):
        self.price=0
        ind=0
        self.tree.delete(*self.tree.get_children())
        for dish in model.dishes:
            self.tree.insert('', 'end',iid=ind, values=(dish))
            ind += 1
        ind = 0
        self.tree1.delete(*self.tree1.get_children())
        for order in model.orders:
            self.tree1.insert('', 'end',iid=ind, values=(order))
            ind += 1
        for i in range(len(model.orders)):
            self.price+=float(model.orders[i][2])*float(model.orders[i][3])

        self.price_text = Label(root, text='Ціна замовлення: {} грн                  '.format(round(self.price, 2)), font='Georgia 14',bg="#F5F5F5", fg="#3F2305")
        self.price_text.place(x=10, y=620)

    def on_tree_select(self, event):
        self.ingredients_list.delete(0, END)
        if self.tree.focus():
            ind=int(self.tree.focus())
        else:
            return
        for ingridient in model.dishes[ind][3]:
            self.ingredients_list.insert(tk.END, ingridient)





if __name__ == "__main__":
    root = tk.Tk()
    model = Model()
    view = View(root)
    controller = Controller(model, view)
    root.mainloop()