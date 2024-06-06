class Model:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Model, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.dishes = []
            self.orders = []
            self._observers = []
            self._initialized = True

    def Check_Code(self, code1):
        self.code = '1488n'
        if self.code == code1:
            return 1
        else:
            return 0

    def add_ingredient(self, ingredient, pos):
        self.dishes[pos][3].append(ingredient)
        self.notify_observers()

    def add_ingredient_to_order(self, ingredient, pos):
        self.orders[pos][1].append(ingredient)
        self.notify_observers()

    def remove_ingredient(self, ingredient, pos):
        if ingredient in self.dishes[pos][3]:
            self.dishes[pos][3].remove(ingredient)
            self.notify_observers()

    def remove_ingredients_from_order(self, pos):
            self.orders[pos][1]=[]
            self.notify_observers()

    def update_ingredient(self, ingredient, new_ingredient, pos):
        for i, ing in enumerate(self.dishes[pos][3]):
            if ing == ingredient:
                self.dishes[pos][3][i] = new_ingredient
        self.notify_observers()


    def add_dish(self, dish):
        self.dishes.append(dish)
        self.notify_observers()

    def remove_dish(self, dish):
        self.dishes.pop(dish)
        self.notify_observers()

    def update_dish(self,dish, pos):
        self.pos=int(pos)
        self.dishes[self.pos] = dish
        self.notify_observers()

    def add_order(self, order, table):
        self.orders1=[]
        self.orders1.append(self.dishes[order][0])
        self.orders1.append([])
        self.orders1.append(self.dishes[order][2])
        self.orders1.append(1)
        self.orders1.append(table)
        self.orders.append( self.orders1)
        self.notify_observers()

    def remove_order(self, order):
        self.orders.pop(order)
        self.notify_observers()

    def update_order(self, order, pos):

        self.orders[pos][1]=order[0]
        self.orders[pos][3] = order[1]
        self.orders[pos][4] = order[2]
        self.notify_observers()

    def search_ingredients(self, keyword):
        results = []
        for dish in self.dishes:
            for ingredient in dish[3]:
                if keyword.lower() in ingredient.lower():
                    results.append(f"{dish[0]}: {ingredient}")
        return results

    def search_orders(self, keyword):
        results = []
        for order in self.orders:
            for item in order:
                if keyword.lower() in str(item).lower():
                    results.append(order)
                    break
        return results

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)