# So I need a data type, 'recipe' with a name and a dictionary of ingredients and their %'s.
# I'm going to try to make it a constructable class.
# IT WORKED! Only took me 20 minutes :/

# After the data type is constructed, I need a way to modify it. I'm going to TRY and use PyQt5
# The plan is to have a list of recipes that are displayed in a 'list' widget in QT, that can each be clicked on to open a dialog box with a table containing that recipes ingredients.
# I did it! It took way too fucking long, but it worked. I can now see the hard-coded recipes appear in the app, as well as click on them to view their ingredients and ratios. This bit took a good two hours.

# Next would be either the ability to save and load the list of recipes, or the ability to add new recipes and remove them. I think saving and loading is harder, so I'll work on that first.
# If I can't work it out, I'll move on to just making another window with inputs for a new recipe.
# So I can't just serialize the 'recipe' class. Meaning I have to create 'transition' methods that turn a recipe into a dictionary or list or something, then another to load from the file and do the reverse.
# This is awful.
# 20 minutes later, I've done it, sort of.
# One recipe can be saved and loaded!
# Now to extend that to a list of recipes...
# Done! I can now save a list of recipes. Took me like 10 minutes.
# Time to work on loading!

import PyQt5.QtWidgets as qtw
import json

saveFile = "recipes.json"
recipes = []

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

# Helper function to turn a recipe into serializable data.
def recipeToTuple(recipe):
    name = recipe.getName()
    ingredients = recipe.getIngredients()
    recipeTuple = (name, ingredients)
    return recipeTuple

def saveRecipesJSON():
    recipeTuples = []
    for Recipe in recipes:
        recipeTuples.append(recipeToTuple(Recipe))
    with open(saveFile, 'w') as f:
        json.dump(recipeTuples, f, indent=2)
    print("SAVED RECIPES TO JSON SUCCESSFULLY")

def LoadRecipesFromJSON():
    # FROM JSON, LOAD LIST OF 'RECIPES', which is really just a tuple with a string (name) and a dictionary (ingredients).
    with open(saveFile, 'r') as f:
        recipeTuples = json.load(f)

    for recipeTuple in recipeTuples:
        # Seperate the tuple for each recipe into a string and a dictionary.
        name, ingredients = recipeTuple
        # Use the deserialized recipe information to create a new recipe, and add it to the list.
        recipe = Recipe()
        recipe.setName(name)
        for key, value in ingredients.items():
            recipe.addIngredient(key, value)
        recipes.append(recipe)
    print("LOADED RECIPES FROM JSON SUCCESSFULLY")

class RecipeWindow(qtw.QWidget):
    def __init__(self, recipeName):
        super().__init__()

        self.setWindowTitle(recipeName + " Ingredients") 
        self.setLayout(qtw.QVBoxLayout())

        for item in recipes:
            tmpName = item.getName()
            if item.getName() == recipeName:
                currentRecipe = item

        ingredientsTable = qtw.QTableWidget()
        ingredientsTable.setRowCount(len(currentRecipe.getIngredients()))
        ingredientsTable.setColumnCount(2)
        ingredientsTable.setHorizontalHeaderItem(0, qtw.QTableWidgetItem("Ingredient"))
        ingredientsTable.setHorizontalHeaderItem(1, qtw.QTableWidgetItem("Percentage"))
        
        i = 0
        for key, value in currentRecipe.getIngredients().items():
            ingredientsTable.setItem(i, 0, qtw.QTableWidgetItem(str(key)))
            ingredientsTable.setItem(i, 1, qtw.QTableWidgetItem(str(value)))
            i += 1

        self.layout().addWidget(ingredientsTable)

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

        saveButton = qtw.QPushButton("Save")
        saveButton.setToolTip("Saves the current list of recipes")
        container.layout().addWidget(saveButton, 12, 0, 1, 2)
        saveButton.clicked.connect(saveRecipesJSON)

        for Recipe in recipes:
            qtw.QListWidgetItem(Recipe.getName(), list)

        self.layout().addWidget(container)

def main():
    # INITIALIZE DATA
    LoadRecipesFromJSON()

    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()

main()




## This is how "IT WORKED!"
#StandardBP = Recipe()
#StandardBP.setName("Black Powder")
#StandardBP.addIngredient("KNO3", 75)
#StandardBP.addIngredient("Charcoal", 15)
#StandardBP.addIngredient("Sulfur", 10)
#print(StandardBP.getIngredients())
#recipes.append(StandardBP)
#print()
#MillerBangor165 = Recipe()
#MillerBangor165.setName("Miller - Bangor (16.5%)")
#MillerBangor165.addIngredient("KNO3", 67)
#MillerBangor165.addIngredient("Al (pyro)", 16.5)
#MillerBangor165.addIngredient("Sulfur", 16.5)
#print(MillerBangor165.getIngredients())
#recipes.append(MillerBangor165)
#print()
#Comp604 = Recipe()
#Comp604.setName("Composition 604")
#Comp604.addIngredient("KNO3", 54)
#Comp604.addIngredient("Al (pyro)", 40)
#Comp604.addIngredient("Sulfur", 5)
#Comp604.addIngredient("Boric Acid", 1)
#print(Comp604.getIngredients())
#recipes.append(Comp604)
#print()