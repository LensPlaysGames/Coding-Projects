# NEW FEATURES THAT WOULD BE COOL (* = what i'm working on)

# Options Window
    # Option to change default sort order of recipe list (ascending, descending).

# Error handling for not being able to open a recipe with the same name as the a category

# Clone and Edit Recipe. From an existing recipe, create a new one, automatically populating the fields with the cloned recipes ingredients. This makes it easy to make variations and such.

# Edit Recipe. I'm thinking just re-open the add a recipe window and populate it programatically, but I'm not certain of how to go about this exactly.


import sys
import os
import subprocess
import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtgui
import json

saveFile = "recipes.json"
categories = set([])
recipes = []

# An object that stores all the necessary data slots and functions for a recipe.
class Recipe:
    def __init__(self):
        self.category = ""          # String for what category this recipe belongs in
        self.name = ""              # String for name of recipe
        self.ingredients = {}       # Dictionary for list of ingredients and their amounts
        self.notes = ""             # String for user notes on the recipe

    # GETTER AND SETTER METHODS
    # These technically aren't necessary, but help me keep things organized.
    def setCat(self, category):
        self.category = category

    def getCat(self):
        return self.category

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addIngredient(self, ingredientName, ingredientRatio):
        self.ingredients[ingredientName] = ingredientRatio

    def getIngredients(self):
        return self.ingredients

    def setNotes(self, notes):
        self.notes = notes

    def getNotes(self):
        return self.notes

# Custom TreeWidget item clicked implementation
class RecipeTree(qtw.QTreeWidget):
        # When user wants to open a given recipe
        def clicked(self, item):
            # Get text from selected tree item, column 0 (the name)
            name = item.text(0)
            # A category isn't a recipe, but can still be clicked on. This checks for that.
            if not name in categories:
                # Open a recipe window to display the recipe data to the user
                self.newWindow = RecipeWindow(name)

# SAVE AND LOAD | JSON
def saveRecipesJSON():
    # Initiate list to save
    recipeTuples = []
    # Populate list with a tuple for each recipe
    for Recipe in recipes:
        recipeTuples.append(recipeToTuple(Recipe))
    # Save populated list to save file
    with open(saveFile, 'w') as f:
        json.dump(recipeTuples, f, indent=2)
    print("SAVED RECIPES TO JSON SUCCESSFULLY")

def LoadRecipesFromJSON():
    # Try to load from save file
    try:
        # Open save file and read into memory as 'recipeTuples' variable
        with open(saveFile, 'r') as f:
            recipeTuples = json.load(f)

        for recipeTuple in recipeTuples:
            # Seperate the tuple for each recipe into it's corresponding data. THE ORDER OF VARIABLES HAS TO MATCH THE 'recipeToTuple' FUNCTION BELOW!
            category, name, ingredients, notes = recipeTuple
            # Use the deserialized recipe information to populate a new recipe object, and add it to the list.
            recipe = Recipe()
            recipe.setCat(category)
            recipe.setName(name)
            for key, value in ingredients.items():
                recipe.addIngredient(key, value)
            recipe.setNotes(notes)
            recipes.append(recipe)
        print("LOADED RECIPES FROM JSON SUCCESSFULLY")
    except FileNotFoundError:
        print("NO SAVE FILE FOUND")
        CreateSaveFile()
        print("NEW SAVE FILE CREATED")

# Helper function to turn a recipe into serializable data.
def recipeToTuple(recipe):
    category = recipe.getCat()
    name = recipe.getName()
    ingredients = recipe.getIngredients()
    notes = recipe.getNotes()
    recipeTuple = (category, name, ingredients, notes)      # ORDER OF VARIABLES HAS TO MATCH 'LoadRecipesFromJSON' FUNCTION ABOVE!
    return recipeTuple

# Creates empty save file.
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
        # Create ingredients table from data programatically.
        self.automaticIngredientsTable(recipeName)

        # Buttons
        buttonsContainer = qtw.QWidget()
        buttonsContainer.setLayout(qtw.QHBoxLayout())

        deleteButton = qtw.QPushButton("Delete")
        buttonsContainer.layout().addWidget(deleteButton)
        deleteButton.clicked.connect(self.deleteButtonFunc)

        closeButton = qtw.QPushButton("Close")
        buttonsContainer.layout().addWidget(closeButton)
        closeButton.clicked.connect(self.close)

        self.layout().addWidget(buttonsContainer)

    def automaticIngredientsTable(self, recipeName):
        # Create and initiate container for ingredients table and notes
        container = qtw.QWidget()
        container.setLayout(qtw.QHBoxLayout())

        # Find current recipe from list using name. Not the best, but it works.
        for recipe in recipes:
            if recipe.getName() == recipeName:
                self.currentRecipe = recipe

        # Create ingredients table widget and initiate
        ingredientsTable = qtw.QTableWidget()
        ingredientsTable.setRowCount(len(self.currentRecipe.getIngredients()))
        ingredientsTable.setColumnCount(2)

        # Set Header Labels
        ingredientsTable.setHorizontalHeaderItem(0, qtw.QTableWidgetItem("Ingredient"))
        ingredientsTable.setHorizontalHeaderItem(1, qtw.QTableWidgetItem("Amount"))

        # Configure the table widget
        ingredientsTable.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)              # Disables user editing the table.
        ingredientsTable.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)   # Sets ingredients and amount columns to fill the space they are given evenly and completely.
        ingredientsTable.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        
        # Populate the table
        i = 0
        font = qtgui.QFont()
        font.setPointSize(15)
        for key, value in self.currentRecipe.getIngredients().items():
            ingredientItem = qtw.QTableWidgetItem(str(key))
            ingredientItem.setFont(font)
            ingredientsTable.setItem(i, 0, ingredientItem)
            amountItem = qtw.QTableWidgetItem(str(value))
            amountItem.setFont(font)
            amountItem.setTextAlignment(qtc.Qt.AlignCenter)
            ingredientsTable.setItem(i, 1, amountItem)
            ingredientsTable.setVerticalHeaderItem(i, qtw.QTableWidgetItem(""))
            i += 1

        # Create section to display recipe notes.
        notesDisplay = qtw.QTextEdit(self.currentRecipe.getNotes())
        notesDisplay.setReadOnly(True)
        
        container.layout().addWidget(ingredientsTable)
        container.layout().addWidget(notesDisplay) 

        self.layout().addWidget(container)

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
        self.ingredientContainers = []

        self.makeUI()

        self.show()


    def makeUI(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QVBoxLayout())

        # CATEGORY INPUT SECTION
        catContainer = qtw.QWidget()
        catContainer.setLayout(qtw.QHBoxLayout())
        catLabel = qtw.QLabel("Category: ")
        catComboBox = qtw.QComboBox()
        catComboBox.addItem("New Category")
        tmpCatList = list(categories)
        tmpCatList.sort()
        catComboBox.addItems(tmpCatList)
        self.catLE = qtw.QLineEdit()
        catComboBox.setLineEdit(self.catLE)
        catContainer.layout().addWidget(catLabel)
        catContainer.layout().addWidget(catComboBox)
        
        # NAME INPUT SECTION
        nameContainer = qtw.QWidget()
        nameContainer.setLayout(qtw.QHBoxLayout())
        nameLabel = qtw.QLabel("Name: ")
        self.nameLE = qtw.QLineEdit()
        nameContainer.layout().addWidget(nameLabel)
        nameContainer.layout().addWidget(self.nameLE)

        # NOTES INPUT SECTION
        notesContainer = qtw.QWidget()
        notesContainer.setLayout(qtw.QVBoxLayout())
        notesLabel = qtw.QLabel("Notes: ")
        self.notesTE = qtw.QPlainTextEdit()
        notesContainer.layout().addWidget(notesLabel)
        notesContainer.layout().addWidget(self.notesTE)

        # ADD INGREDIENTS SECTION
        # LABELS FOR INPUT FIELD
        ingredientsHeadersContainer = qtw.QWidget()
        ingredientsHeadersContainer.setLayout(qtw.QHBoxLayout())
        self.ingredientsHeader = qtw.QLabel("1 Ingredient")
        amountHeader = qtw.QLabel("Amount")
        ingredientsHeadersContainer.layout().addWidget(self.ingredientsHeader)
        ingredientsHeadersContainer.layout().addWidget(amountHeader)

        self.ingredientsContainer = qtw.QWidget()
        self.ingredientsContainer.setLayout(qtw.QVBoxLayout())

        self.ingredientsContainer.layout().addWidget(ingredientsHeadersContainer)

        # INPUT FIELD
        self.addIngredientField()

        # BUTTONS CONTAINER
        buttonsContainer = qtw.QWidget()
        buttonsContainer.setLayout(qtw.QGridLayout())

        # REMOVE INGREDIENT BUTTON
        addIngredientButton = qtw.QPushButton("Remove Ingredient")
        addIngredientButton.clicked.connect(self.removeIngredientButtonFunc)
        buttonsContainer.layout().addWidget(addIngredientButton, 0, 0, 1, 2)

        # ADD INGREDIENT BUTTON
        addIngredientButton = qtw.QPushButton("Add Ingredient")
        addIngredientButton.clicked.connect(self.addIngredientButtonFunc)
        # buttonsContainer.layout().addWidget(addIngredientButton, 0, 0, 1, 4)
        buttonsContainer.layout().addWidget(addIngredientButton, 0, 2, 1, 2)

        # CANCEL BUTTON
        cancelButton = qtw.QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        buttonsContainer.layout().addWidget(cancelButton, 1, 0, 1, 2)

        # SAVE RECIPE BUTTON
        saveRecipeButton = qtw.QPushButton("Save New Recipe")
        saveRecipeButton.clicked.connect(self.saveRecipeButtonFunc)
        buttonsContainer.layout().addWidget(saveRecipeButton, 1, 2, 1, 2)

        # ADD WIDGETS TO CONTAINER (IN TOP-TO-BOTTOM ORDER)
        container.layout().addWidget(catContainer)
        container.layout().addWidget(nameContainer)
        container.layout().addWidget(notesContainer)
        container.layout().addWidget(self.ingredientsContainer)
        container.layout().addWidget(buttonsContainer)

        self.layout().addWidget(container)

    def setIngredientsCount(self, count):
        self.ingredientsCount = count
        self.ingredientsHeader.setText(str(self.ingredientsCount) + " Ingredients" if self.ingredientsCount > 1 else "1 Ingredient")

    def removeIngredientButtonFunc(self):
        if self.ingredientsCount > 1:
            self.removeIngredientField()
            self.update()

    def removeIngredientField(self):
        # Get reference to all widgets related to latest ingredient added
        self.containerWidget = self.ingredientContainers.pop()
        self.nameWidget = self.ingredientsNames.pop()
        self.amountWidget = self.ingredientsAmounts.pop()
        
        # Remove latest ingredient's widgets from the layout
        self.layout().removeWidget(self.containerWidget)
        self.layout().removeWidget(self.nameWidget)
        self.layout().removeWidget(self.amountWidget)

        # Allow latest ingredient's widgets to be deleted
        self.containerWidget.deleteLater()
        self.nameWidget.deleteLater()
        self.amountWidget.deleteLater()

        # Delete latest ingredient's widgets
        self.containerWidget = None
        self.nameWidget = None
        self.amountWidget = None

        # Update total count of ingredients
        self.setIngredientsCount(self.ingredientsCount - 1)

    def addIngredientButtonFunc(self):
        self.addIngredientField()
        self.update()

    # CONSTRUCTS INGREDIENT FIELD AND ADDS IT TO INGREDIENTS CONTAINER
    # This function is used by the application user to vary the amount of ingredients in a recipe.
    def addIngredientField(self):
        ingredientContainer = qtw.QWidget()                                 # Create container for new ingredient input field
        ingredientContainer.setLayout(qtw.QHBoxLayout())                    # Each ingredient is a 'row' so everything should be in a horizontal layout
        self.ingredientContainers.append(ingredientContainer)              # Keep reference to ingredient container by adding to list
        self.ingredientName = qtw.QLineEdit()                               # Create Line Edit for ingredient name input
        self.ingredientAmount = qtw.QLineEdit()                             # Create Line Edit for ingredient amount input
        self.ingredientsNames.append(self.ingredientName)                   # Keep reference to ingredient name by adding to list
        self.ingredientsAmounts.append(self.ingredientAmount)               # Keep reference to ingredient amount by adding to list
        ingredientContainer.layout().addWidget(self.ingredientName)         # Add section for name input to ingredient field container
        ingredientContainer.layout().addWidget(self.ingredientAmount)       # Add section for amount input to ingredient field container
        self.ingredientsContainer.layout().addWidget(ingredientContainer)   # Add new ingredient field to container of all ingredient fields
        self.setIngredientsCount(self.ingredientsCount + 1)                 # Update total count of ingredients

    def saveRecipeButtonFunc(self):
        # Create new recipe object
        newRecipe = Recipe()

        # Set recipe category from category input field. Would be smart to check if it's empty, or something.
        newRecipe.setCat(self.catLE.text())
        
        # Set recipe name from name input field. Would be smart to check if it's empty, or something.
        newRecipe.setName(self.nameLE.text())

        # Set recipe notes from notes input field.
        newRecipe.setNotes(str(self.notesTE.toPlainText()))

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

# Main Application Window: Display the list of recipes
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 420, 300)                            # Open in the top left of the screen, big enough to see what's going on.
        self.setWindowIcon(qtgui.QIcon("RecipeAppIcon.png"))            # Set the little picture at the top
        self.setWindowTitle("Recipe App")                               # Set the title of the window

        self.makeMenuBar()
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

        addButton = qtw.QPushButton("Add Recipe")                       
        addButton.setToolTip("Opens a window to add an additional recipe")
        container.layout().addWidget(addButton, 12, 0, 1, 4)            # Add 'add recipe' button to the container.
        addButton.clicked.connect(self.showAddWindow)                   # Attach 'clicked' event to show the 'add recipe' window.

        # I could do with less loops here, but I can't for the life of me figure out how.
        # Populate the list of categories to place recipes in
        for Recipe in recipes:
            category = Recipe.getCat()
            categories.add(category)

        # Create category items from list of categories
        for category in categories:
            catItem = qtw.QTreeWidgetItem(tree)
            catItem.setText(0, category)

        # Populate the visual recipe list from data list of recipes
        for Recipe in recipes:
            category = tree.findItems(Recipe.getCat(), qtc.Qt.MatchExactly, 0)
            category = category[0]
            tmp_item = qtw.QTreeWidgetItem(category)
            tmp_item.setText(0, Recipe.getName())

        tree.sortItems(0, qtc.Qt.AscendingOrder)                        # Sort items in ascending alphabetical order

        self.setCentralWidget(container)                                # Add entire container to the main layout

    def showAddWindow(self, checked):
        self.addWin = addWindow()
        self.addWin.show()

    def makeMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('&File')

        saveAction = qtw.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setToolTip('Saves the current recipes')
        saveAction.triggered.connect(saveRecipesJSON)

        viewJSONAction = qtw.QAction('View JSON', self)
        viewJSONAction.setShortcut('Ctrl+O')
        viewJSONAction.setToolTip('View the JSON save file')
        viewJSONAction.triggered.connect(self.viewJSON)

        exitAction = qtw.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setToolTip('Exits the application')
        exitAction.triggered.connect(self.saveAndQuit)

        fileMenu.addAction(saveAction)
        fileMenu.addAction(viewJSONAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

    def viewJSON(self):
        if os.path.exists(saveFile):
            if sys.platform == "win32":
                os.startfile(saveFile)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, saveFile])

    def saveAndQuit(self):
        saveRecipesJSON()
        qtc.QCoreApplication.quit()

if __name__ == "__main__":
    # INITIALIZE DATA
    LoadRecipesFromJSON()

    # CREATE GUI
    app = qtw.QApplication([])
    app.setStyle(qtw.QStyleFactory.create('fusion'))
    mw = MainWindow()

    # RUN
    app.exec_()
