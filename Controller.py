class Command:
    def execute(self):
        pass

class CheckCodeCommand(Command):
    def __init__(self, model, code):
        self.model = model
        self.code = code

    def execute(self):
        return self.model.Check_Code(self.code)

class AddIngredientCommand(Command):
    def __init__(self, model, ingredient,pos):
        self.model = model
        self.ingredient = ingredient
        self.pos= int(pos)

    def execute(self):
        self.model.add_ingredient(self.ingredient, self.pos)

class AddIngredientToOrderCommand(Command):
    def __init__(self, model, ingredient,pos):
        self.model = model
        self.ingredient = ingredient
        self.pos= int(pos)

    def execute(self):
        self.model.add_ingredient_to_order(self.ingredient, self.pos)

class RemoveIngredientCommand(Command):
    def __init__(self, model, ingredient, pos):
        self.model = model
        self.ingredient = ingredient
        self.pos = int(pos)

    def execute(self):
        self.model.remove_ingredient(self.ingredient,self.pos)

class RemoveIngredientsFromOrderCommand(Command):
    def __init__(self, model, pos):
        self.model = model
        self.pos = int(pos)

    def execute(self):
        self.model.remove_ingredients_from_order(self.pos)

class UpdateIngredientCommand(Command):
    def __init__(self, model, ingredient, new_ingredient,pos):
        self.model = model
        self.ingredient = ingredient
        self.new_ingredient = new_ingredient
        self.pos = int(pos)
    def execute(self):
        self.model.update_ingredient(self.ingredient, self.new_ingredient, self.pos)

class AddDishCommand(Command):
    def __init__(self, model, dish):
        self.model = model
        self.dish = dish

    def execute(self):
        self.model.add_dish(self.dish)

class RemoveDishCommand(Command):
    def __init__(self, model, dish):
        self.model = model
        self.dish = dish

    def execute(self):
        self.model.remove_dish(self.dish)

class UpdateDishCommand(Command):
    def __init__(self, model, dish, pos):
        self.model = model
        self.dish = dish
        self.pos = pos

    def execute(self):
        self.model.update_dish(self.dish, self.pos)

class AddOrderCommand(Command):
    def __init__(self, model, order, table):
        self.model = model
        self.order = order
        self.table=table

    def execute(self):
        self.model.add_order(self.order, self.table)

class RemoveOrderCommand(Command):
    def __init__(self, model, order):
        self.model = model
        self.order = order

    def execute(self):
        self.model.remove_order(self.order)

class UpdateOrderCommand(Command):
    def __init__(self, model, order, pos):
        self.model = model
        self.order = order
        self.pos = int(pos)

    def execute(self):
        self.model.update_order(self.order, self.pos)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.model.add_observer(self.view)
    def check_code(self, code):
        command = CheckCodeCommand(self.model, code)
        return command.execute()

    def add_ingredient(self, ingredient,pos):
        command = AddIngredientCommand(self.model, ingredient,pos)
        command.execute()

    def add_ingredient_to_order(self, ingredient,pos):
        command = AddIngredientToOrderCommand(self.model, ingredient,pos)
        command.execute()

    def remove_ingredient(self, ingredient, pos):
        command = RemoveIngredientCommand(self.model, ingredient, pos)
        command.execute()

    def remove_ingredient_from_order(self, pos):
        command = RemoveIngredientsFromOrderCommand(self.model, pos)
        command.execute()

    def update_ingredient(self, ingredient, new_ingredient, pos):
        command = UpdateIngredientCommand(self.model, ingredient, new_ingredient,pos)
        command.execute()

    def add_dish(self, dish):
        command = AddDishCommand(self.model, dish)
        command.execute()

    def remove_dish(self, dish):
        command = RemoveDishCommand(self.model, dish)
        command.execute()

    def update_dish(self,dish, pos):
        command = UpdateDishCommand(self.model,dish, pos)
        command.execute()

    def add_order(self, order, table):
        command = AddOrderCommand(self.model, order, table)
        command.execute()

    def remove_order(self, order):
        command = RemoveOrderCommand(self.model, order)
        command.execute()

    def update_order(self, order, pos):
        command = UpdateOrderCommand(self.model, order, pos)
        command.execute()

    def search_ingredients(self, keyword):
        results = self.model.search_ingredients(keyword)
        self.view.display_search_results(results, "ingredients")

    def search_orders(self, keyword):
        results = self.model.search_orders(keyword)
        self.view.display_search_results(results, "orders")