
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
# I did it! Took me like 30 minutes. Total time spent coding at this point: ~2.5 hours.

# Next up, the add window. Just have to make a new widget class called 'addWindow' or something, and figure out how to have multiple ingredients and stuff. We'll get there...
# I've made a lot of progress. There is an add recipe button, a window that pops up with fields to enter the name of the recipe as well as an ingredient and how much to use.
# The problem is with my method of adding more ingredients. I thought it would be nice, UX-wise, to just click a button and add another ingredient. 
# This turned out to be really difficult, or at least I made it that way. I was able to do it, but everytime an ingredient was added all the fields went blank...
# So, now I'm going to just pop up a window that asks how many ingredients it has, then move on to adding in all the data. 
# It's not ideal but it's what I got.

# I LIED! I can totally use the add ingredient button. I was just being a dummy and forgot about self.update(), which is exactly what I needed. Removed 30 lines of code and replaced it with two :).

# So now I can add ingredients without everything disappearing, but I need to figure out how to loop over the lineedits and arrange them into ingredients and amounts in a dictionary.
# This dictionary can then be assembled into the final recipe output, which can be added to the list of recipes.

# I did it! 
# I took a different approach than above, however; 
# the QLineEdit objects are added to a list as they are made, then that list is looped over to extract the text and those strings are converted into an ingredient dictionary.
# This took about 30 minutes to figure out/code.
# I also added a delete button when looking at a recipe. It doesn't close the menu, and it doesn't update the main menu, but closing and opening the program works. I'll fix this next.
# I'm so happy! I can now create, delete, store, load, and visualize pyrotechnic compositions, with my own software!

# I've sort of fixed the not updating thing, it just restarts instead of doing anything fancy.

# Added delete confirmation when deleting a recipe. Also added close button to recipe window. Fixed not saving new recipe name. Total time programming up to this point: ~5 hours.

# Fixed being able to click into and edit cells of the table while in recipe window.


# Woot woot! Categories are now implemented. It wasn't awful, but it had some hiccups. Sets are amazing, basically a hashmap for regular data.
# Also, moved open recipe window to double click, instead of single


# NEW FEATURES THAT WOULD BE COOL (* = what i'm working on)

# A comment/notes section for each recipe would be really cool. Basically just a textedit widget in the add recipe area, but also have to integrate into the save/load system.

# Button/Option to open JSON file.

# Need to save the order of recipes once dragged and dropped, or it's annoying. I don't know how to attach the recipes list to the visual representation of it. It seems like a co-dependence issue.

import sys
import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtgui
import json

saveFile = "recipes.json"
categories = set([])
recipes = []

class Recipe:
    def __init__(self):
        self.name = ""
        self.ingredients = {}
        self.category = ""

    # GETTER AND SETTER METHODS
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addIngredient(self, ingredientName, ingredientRatio):
        self.ingredients[ingredientName] = ingredientRatio

    def getIngredients(self):
        return self.ingredients

    def setCat(self, category):
        self.category = category

    def getCat(self):
        return self.category

# Helper function to turn a recipe into serializable data.
def recipeToTuple(recipe):
    name = recipe.getName()
    ingredients = recipe.getIngredients()
    category = recipe.getCat()
    recipeTuple = (name, ingredients, category)
    return recipeTuple

def saveRecipesJSON():
    recipeTuples = []
    for Recipe in recipes:
        recipeTuples.append(recipeToTuple(Recipe))
    with open(saveFile, 'w') as f:
        json.dump(recipeTuples, f, indent=2)
    print("SAVED RECIPES TO JSON SUCCESSFULLY")

def LoadRecipesFromJSON():
    try:
        # FROM JSON, LOAD LIST OF 'RECIPES', which is really just a tuple with a string (name) and a dictionary (ingredients).
        with open(saveFile, 'r') as f:
            recipeTuples = json.load(f)

        for recipeTuple in recipeTuples:
            # Seperate the tuple for each recipe into a string and a dictionary.
            name, ingredients, category = recipeTuple
            # Use the deserialized recipe information to create a new recipe, and add it to the list.
            recipe = Recipe()
            recipe.setName(name)
            for key, value in ingredients.items():
                recipe.addIngredient(key, value)
            recipe.setCat(category)
            recipes.append(recipe)
        print("LOADED RECIPES FROM JSON SUCCESSFULLY")
    except FileNotFoundError:
        print("NO SAVE FILE FOUND")
        CreateSaveFile()
        print("NEW SAVE FILE CREATED")

def CreateSaveFile():
    with open(saveFile, 'w') as f:
        f.write("{}")

# Recipe Window: Display the data of a given recipe, as well as house the option to delete a recipe.
class RecipeWindow(qtw.QWidget):
    def __init__(self, recipeName):
        super().__init__()

        self.setWindowIcon(qtgui.QIcon("RecipeAppIcon.png"))
        self.setWindowTitle(recipeName + " Ingredients") 

        self.setLayout(qtw.QVBoxLayout())

        self.makeUI(recipeName)
        self.show()

    def makeUI(self, recipeName):
        self.automaticIngredientsTable(recipeName)

        deleteButton = qtw.QPushButton("Delete")
        self.layout().addWidget(deleteButton)
        deleteButton.clicked.connect(self.deleteButtonFunc)

        closeButton = qtw.QPushButton("Close")
        self.layout().addWidget(closeButton)
        closeButton.clicked.connect(self.close)

    def automaticIngredientsTable(self, recipeName):
        for item in recipes:
            if item.getName() == recipeName:
                self.currentRecipe = item

        ingredientsTable = qtw.QTableWidget()
        ingredientsTable.setRowCount(len(self.currentRecipe.getIngredients()))
        ingredientsTable.setColumnCount(2)
        ingredientsTable.setHorizontalHeaderItem(0, qtw.QTableWidgetItem("Ingredient"))
        ingredientsTable.setHorizontalHeaderItem(1, qtw.QTableWidgetItem("Amount"))
        ingredientsTable.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        
        i = 0
        for key, value in self.currentRecipe.getIngredients().items():
            ingredientsTable.setItem(i, 0, qtw.QTableWidgetItem(str(key)))
            ingredientsTable.setItem(i, 1, qtw.QTableWidgetItem(str(value)))
            ingredientsTable.setVerticalHeaderItem(i, qtw.QTableWidgetItem(""))
            i += 1

        ingredientsTable.resizeColumnsToContents()
        self.layout().addWidget(ingredientsTable)

    def deleteButtonFunc(self):
        recipeName = self.currentRecipe.getName()
        # USER CONFIRMATION POP-UP BOX
        choice = qtw.QMessageBox.question(self, 'Delete Recipe Confirmation', 'Actually delete "' + recipeName + '"?', qtw.QMessageBox.Yes | qtw.QMessageBox.No)
        if choice == qtw.QMessageBox.Yes:                                               # USER SAID YES
            for recipe in recipes:
                if recipe.getName() == recipeName:
                    recipes.pop(recipes.index(recipe))                                  # Delete the recipe at the index of the currently displayed recipe
                    saveRecipesJSON()                                                   # Serialize new recipe data list to JSON
                    self.close()                                                        # Hide recipe window from user
                    qtc.QCoreApplication.quit()                                         # Close entire application
                    status = qtc.QProcess.startDetached(sys.executable, sys.argv)       # Start the application again just before everything shuts down
        else: pass

# Add-a-Recipe Window: Input form to create a new recipe and add it to the list in the main window.
class addWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(qtgui.QIcon("RecipeAppIcon.png"))
        self.setWindowTitle("Add a Recipe")

        self.setLayout(qtw.QVBoxLayout())   

        self.ingredientsCount = 0
        self.ingredientsNames = []
        self.ingredientsAmounts = []
        self.makeUI()

        self.show()


    def makeUI(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QVBoxLayout())

        # CATEGORY INPUT SECTION
        catContainer = qtw.QWidget()
        catContainer.setLayout(qtw.QHBoxLayout())
        catLabel = qtw.QLabel("Category: ")
        self.catLE = qtw.QLineEdit()
        catContainer.layout().addWidget(catLabel)
        catContainer.layout().addWidget(self.catLE)
        
        # NAME INPUT SECTION
        nameContainer = qtw.QWidget()
        nameContainer.setLayout(qtw.QHBoxLayout())
        nameLabel = qtw.QLabel("Name: ")
        self.nameLE = qtw.QLineEdit()
        nameContainer.layout().addWidget(nameLabel)
        nameContainer.layout().addWidget(self.nameLE)

        # ADD INGREDIENTS SECTION
        ingredientsHeadersContainer = qtw.QWidget()
        ingredientsHeadersContainer.setLayout(qtw.QHBoxLayout())
        ingredientsHeader = qtw.QLabel("Ingredients")
        amountHeader = qtw.QLabel("Amount")
        ingredientsHeadersContainer.layout().addWidget(ingredientsHeader)
        ingredientsHeadersContainer.layout().addWidget(amountHeader)

        self.ingredientsContainer = qtw.QWidget()
        self.ingredientsContainer.setLayout(qtw.QVBoxLayout())

        self.ingredientsContainer.layout().addWidget(ingredientsHeadersContainer)

        self.addIngredientField()

        # ADD INGREDIENT BUTTON
        addIngredientButton = qtw.QPushButton("Add Ingredient")
        addIngredientButton.clicked.connect(self.addIngredientButtonFunc)

        # SAVE RECIPE BUTTON
        saveRecipeButton = qtw.QPushButton("Save New Recipe")
        saveRecipeButton.clicked.connect(self.saveRecipeButtonFunc)

        # ADD WIDGETS TO CONTAINER (IN TOP-TO-BOTTOM ORDER)
        container.layout().addWidget(catContainer)
        container.layout().addWidget(nameContainer)
        container.layout().addWidget(self.ingredientsContainer)
        container.layout().addWidget(addIngredientButton)
        container.layout().addWidget(saveRecipeButton)

        self.layout().addWidget(container)

    def addIngredientButtonFunc(self):
        self.addIngredientField()
        self.update()

    # CONSTRUCTS INGREDIENT FIELD AND ADDS IT TO INGREDIENTS CONTAINER
    # This function is used by the application user to vary the amount of ingredients in a recipe.
    def addIngredientField(self):
        ingredientContainer = qtw.QWidget()                                 # Create container for new ingredient input field
        ingredientContainer.setLayout(qtw.QHBoxLayout())                    # Each ingredient is a 'row' so everything should be in a horizontal layout
        self.ingredientName = qtw.QLineEdit()                               # Create Line Edit for ingredient name input
        self.ingredientAmount = qtw.QLineEdit()                             # Create Line Edit for ingredient amount input
        self.ingredientsNames.append(self.ingredientName)                   # Keep reference to ingredient name by adding to list
        self.ingredientsAmounts.append(self.ingredientAmount)               # Keep reference to ingredient amount by adding to list
        ingredientContainer.layout().addWidget(self.ingredientName)         # Add section for name input to ingredient field container
        ingredientContainer.layout().addWidget(self.ingredientAmount)       # Add section for amount input to ingredient field container
        self.ingredientsContainer.layout().addWidget(ingredientContainer)   # Add new ingredient field to container of all ingredient fields
        self.ingredientsCount += 1

    def saveRecipeButtonFunc(self):
        # Create new recipe object
        newRecipe = Recipe()

        # Set recipe category from category input field. Would be smart to check if it's empty, or something.
        newRecipe.setCat(self.catLE.text())
        
        # Set recipe name from name input field. Would be smart to check if it's empty, or something.
        newRecipe.setName(self.nameLE.text())

        # Loop through both lists of ingredient names and amounts at once, adding each ingredient to the recipe
        for ingredientName, ingredientAmount in zip(self.ingredientsNames, self.ingredientsAmounts):
            newRecipe.addIngredient(ingredientName.text(), ingredientAmount.text())

        recipes.append(newRecipe)       # Add completed recipe to list of all recipes
        saveRecipesJSON()               # Save entire list of recipes to JSON file.

        self.close()                    # Close 'Add-a-Recipe' window

        # Restarts application. Only needed because otherwise the list of recipes doesn't refresh and the new recipe you just created does not show up.
        # I would use the 'update' function in PyQt5 but I can't figure out how to call it on the main window when clicking a button in the add window,
        # unless I add all windows to a list or something to keep global reference to them.
        qtc.QCoreApplication.quit()                                         # Close entire application
        status = qtc.QProcess.startDetached(sys.executable, sys.argv)       # Start the application again just before everything shuts down

class RecipeTree(qtw.QTreeWidget):
        def clicked(self, item):
            name = item.text(0)
            # A category isn't a recipe, but can still be clicked on. This checks for that.
            if not name in categories:
                self.newWindow = RecipeWindow(name)
            return

# Main Application Window: Display the list of recipes
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(qtgui.QIcon("RecipeAppIcon.png"))
        self.setWindowTitle("Recipe App")

        self.setLayout(qtw.QVBoxLayout())

        self.makeUI()
        self.show()

    def makeUI(self):
        # All UI is added to a container, which then gets added to the main layout.
        container = qtw.QWidget()                                       # Create the container object
        container.setLayout(qtw.QGridLayout())                          # Select layout style

        # In-window Title
        title = qtw.QLabel("Recipe App")                                # App Title (not needed, but looks too barebones without it)
        container.layout().addWidget(title, 0, 0, 1, 3)                 # Add title widget to container

        # The list of recipes
        # I am thinking about making this a tree-view. Each recipe would have a field for a 'category', which would designate which drop-down it resides in in the main recipe list.

        tree = RecipeTree()
        tree.setHeaderHidden(True)
        container.layout().addWidget(tree, 1, 0, 10, 4)
        tree.itemDoubleClicked.connect(tree.clicked)                    # Call custom clicked function on double click. Opens recipe window to display ingredients & more.

        # Button that saves the list of recipes to JSON (should never be needed, kind of a relic from how it used to work).
        saveButton = qtw.QPushButton("Save")
        saveButton.setToolTip("Saves the current list of recipes")
        container.layout().addWidget(saveButton, 12, 0, 1, 2)           # Add save button widget to the container
        saveButton.clicked.connect(saveRecipesJSON)                     # Attach 'clicked' event to 'save-to-JSON' function.

        addButton = qtw.QPushButton("Add Recipe")                       
        addButton.setToolTip("Opens a window to add an additional recipe")
        container.layout().addWidget(addButton, 12, 2, 1, 2)            # Add 'add recipe' button to the container.
        addButton.clicked.connect(self.showAddWindow)                   # Attach 'clicked' event to show the 'add recipe' window.

        # Populate the list of categories to place recipes in
        for Recipe in recipes:
            category = Recipe.getCat()
            categories.add(category)

        for category in categories:
            catItem = qtw.QTreeWidgetItem(tree)
            catItem.setText(0, category)
        # Populate the visual recipe list from data list of recipes
        for Recipe in recipes:
            category = tree.findItems(Recipe.getCat(), qtc.Qt.MatchExactly, 0)
            category = category[0]
            tmp_item = qtw.QTreeWidgetItem(category)
            tmp_item.setText(0, Recipe.getName())

        self.layout().addWidget(container)                              # Add entire container to the main layout

    def showAddWindow(self, checked):
        self.addWin = addWindow()
        self.addWin.show()


if __name__ == "__main__":
    # INITIALIZE DATA
    LoadRecipesFromJSON()

    # CREATE GUI
    app = qtw.QApplication([])
    app.setStyle(qtw.QStyleFactory.create('fusion'))
    mw = MainWindow()

    # RUN
    app.exec_()
