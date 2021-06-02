# So I need a data type, 'recipe' with a name and a dictionary of ingredients and their %'s.
# I'm going to try to make it a constructable class.
# IT WORKED! Only took me 20 minutes :/

# After the data type is constructed, I need a way to modify it. I'm going to TRY and use PyQt5
# The plan is to have a list of recipes that are displayed in a 'list' widget in QT, that can each be clicked on to open a dialog box with a table containing that recipes ingredients.

import PyQt5.QtWidgets as qtw

class Recipe:
    def __init__(self):
        self.name = ""
        self.ingredients = {}

    # GETTER AND SETTER METHODS
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addIngredient(self, ingredientName, ingredientRatio):
        self.ingredients[ingredientName] = ingredientRatio

    def getIngredients(self):
        return self.ingredients

# DUMMY RECIPE LIST THAT WILL LATER BE SAVED AND LOADED FROM FILE
recipes = []
# This is how "IT WORKED!"
StandardBP = Recipe()
StandardBP.setName("Black Powder")
StandardBP.addIngredient("KNO3", 75)
StandardBP.addIngredient("Charcoal", 15)
StandardBP.addIngredient("Sulfur", 10)
print(StandardBP.getIngredients())
recipes.append(StandardBP)
print()
MillerBangor165 = Recipe()
MillerBangor165.setName("Miller - Bangor (16.5%)")
MillerBangor165.addIngredient("KNO3", 67)
MillerBangor165.addIngredient("Al (pyro)", 16.5)
MillerBangor165.addIngredient("Sulfur", 16.5)
print(MillerBangor165.getIngredients())
recipes.append(MillerBangor165)
print()
Comp604 = Recipe()
Comp604.setName("Composition 604")
Comp604.addIngredient("KNO3", 54)
Comp604.addIngredient("Al (pyro)", 40)
Comp604.addIngredient("Sulfur", 5)
Comp604.addIngredient("Boric Acid", 1)
print(Comp604.getIngredients())
recipes.append(Comp604)
print()

for Recipe in recipes:
    print(Recipe.getName())
    print()
    tmpingredients = Recipe.getIngredients()
    for key, value in tmpingredients.items():
        print(key, str(value) + "%")
    print()


class RecipeWindow(qtw.QWidget):
    def __init__(self, recipeName):
        super().__init__()

        self.setWindowTitle(recipeName + " Ingredients") 
        self.setLayout(qtw.QVBoxLayout())

        thisRecipe = Recipe()
        for Recipe in recipes:
            if Recipe.getName == recipeName:
                thisRecipe = Recipe

        ingredientsTable = qtw.QTableWidget()
        ingredientsTable.setRowCount(len(thisRecipe.getIngredients()))

        self.show()


class RecipeList(qtw.QListWidget):
        def clicked(self, item):
            self.newWindow = RecipeWindow(item.text())


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe App")

        # SET MAIN LAYOUT (VERTICAL BOX)
        self.setLayout(qtw.QVBoxLayout())

        # INITIALIZE UI
        self.makeUI()

        self.show()

    def makeUI(self):
        # CREATE GRID LAYOUT FOR UI. WE WILL THIS ONE WIDGET IS ADDED TO THE MAIN LAYOUT.
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        title = qtw.QLabel("Recipe App")
        container.layout().addWidget(title, 0, 0, 1, 4)

        list = RecipeList()
        container.layout().addWidget(list, 1, 0, 10, 4)
        list.setAlternatingRowColors(True)
        list.setDragDropMode(qtw.QAbstractItemView.InternalMove)
        list.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
        list.itemClicked.connect(list.clicked)

        for Recipe in recipes:
            qtw.QListWidgetItem(Recipe.getName(), list)

        self.layout().addWidget(container)


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
