"""
This script contains all of the code for the startup menu.
It will be the first UI element launched when the program 
is started. It is responsible for setting the initial 
parameters before starting the simulation.
"""

## Modules / Libraries ##
from tkinter import ttk # Used for creating more modern-looking UI
from tkinter import *

## Initial Variables ##
rain = None
temp = None

## Define the main window before the styles ##
mainMenuWindow = Tk()

"""
Defining styles:
Styles allow for the customisation of Tkinter UI elements,
changing mainly font and text size.
"""

largeButtonStyle = ttk.Style()
largeButtonStyle.configure("my.largeButtonStyle.TButton", font=("Formula1 Display Regular", 26))

smallButtonStyle = ttk.Style()
smallButtonStyle.configure("my.smallButtonStyle.TButton", font=("Formula1 Display Regular", 12))

smallTextStyle = ttk.Style()
smallTextStyle.configure("my.smallTextStyle.TLabel", font=("Formula1 Display Regular", 11))

largeOptionMenu = ttk.Style()
largeOptionMenu.configure("my.largeOptionMenuStyle.TButton", font=("Formula1 Display Regular", 26))

"""
Error Popup Class:
This will be used to bring up alerts to the user if they
make an invalid choice or something happens that requires 
attention.
"""

class errorPopup():
    def __init__(self, 
                 errorMsg: str) -> None:
        self.errorMsg = errorMsg

        self.errorWindow = Toplevel(mainMenuWindow)
        self.errorWindow.title("Error") # Create the window with a title of "Error"
        self.errorFrame = ttk.Frame(self.errorWindow, padding=30)
        self.errorFrame.pack() # Place the frame within the window

        self.errorMsgLabel = ttk.Label(self.errorFrame, text=self.errorMsg, style="my.smallTextStyle.TLabel")
        self.errorMsgLabel.pack(side="top") # Place the error message at the top of the window

        self.okButton = ttk.Button(self.errorFrame, text="OK", command=self.errorWindow.destroy, style="my.smallButtonStyle.TButton")
        self.okButton.pack(side="bottom") # Place the OK button below the error message

        self.errorWindow.mainloop() # Mainloop the GUI so that it is functional

"""
Initial menu:
This will be the first UI element to show up. It will show
the user the different categories of settings that they
can change.
"""

mainMenuWindow.title("Startup Menu")
mainMenuWindow.resizable(width=False, height=False) ## Stops the user from resizing the window

mainMenuFrame = ttk.Frame(mainMenuWindow)
mainMenuFrame.grid()


#######COMMENTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS#########
## Create a grid of 4 buttons and define their subroutines ##
def openWeatherMenu():
    print("Open Weather Menu")

    weatherMenuWindow = Toplevel(mainMenuWindow) ## Creates a window that descends from the main menu
    weatherMenuWindow.title("Weather Settings")
    weatherMenuWindow.resizable(width=False, height=False) ## Stops the user from resizing the window

    weatherMenuFrame = ttk.Frame(weatherMenuWindow, padding=20)
    weatherMenuFrame.grid()

    rainOptions = ("Clear", "Light Rain", "Heavy Rain", "Dynamic [WIP]") ## Dropdown options
    rainTkVar = StringVar(value="Clear")
    rainSelect = ttk.OptionMenu(weatherMenuFrame, rainTkVar, "Clear", *rainOptions, style="my.largeOptionMenuStyle.TButton")
    rainSelect.grid(column=0, row=0, padx=20, pady=10) ## Add plenty of padding for a modern look
    
    temperature = DoubleVar(value=12)
    temperatureLabel = ttk.Label(weatherMenuFrame, text=f"Adjust Temperature: {temperature.get()}", style="my.smallTextStyle.TLabel")
    temperatureLabel.grid(column=1, row=1, padx=20, pady=10)

    def updateTempLabel(*args, **kwargs):
        temperatureLabel.config(text=f"Adjust Temperature: {int(temperature.get())}") ## Updates the temperature label under the slider continuously

    tempSlider = ttk.Scale(weatherMenuFrame, ## Parent
                           variable=temperature, ## Variable that the slider changes
                           from_=12, to=40, ## Temperature bounds
                           orient="horizontal", ## LR slider
                           length=200, ## Width of the slider
                           command=updateTempLabel) ## Updates label every time it is moved
    tempSlider.grid(column=1, row=0, padx=25, pady=10)

    rainLabel = ttk.Label(weatherMenuFrame, text="Adjust Rain", style="my.smallTextStyle.TLabel")
    rainLabel.grid(column=0, row=1, padx=20, pady=10)

    ## Saves the current settings to the global variables and closes the window ##
    def saveChanges():
        global rain
        global temp
        rain = str(rainTkVar.get())
        temp = int(temperature.get())
        weatherMenuWindow.destroy()
    saveChangesButton = ttk.Button(weatherMenuFrame, text="Save Changes", command=saveChanges, style="my.largeButtonStyle.TButton")
    saveChangesButton.grid(column=0, row=2, padx=20, pady=10)

    discardChangesButton = ttk.Button(weatherMenuFrame, text="Discard Changes", command=weatherMenuWindow.destroy, style="my.largeButtonStyle.TButton")
    discardChangesButton.grid(column=1, row=2, padx=20, pady=10)



    



def openStrategyMenu():
    print("Open Strategy Menu")
def openDriverMenu():
    print("Open Driver Menu")
def openRaceFormatMenu():
    print("Open Race Format Menu")
def startSim():
    errorPopup("Please configure weather settings before continuing.")

weatherButton = ttk.Button(mainMenuFrame,
                           text="Weather Settings",
                           command=openWeatherMenu,
                           style="my.largeButtonStyle.TButton")
weatherButton.grid(column=0, row=0, padx=20, pady=12)

strategyButton = ttk.Button(mainMenuFrame,
                            text="Adjust Strategy",
                            command=openStrategyMenu,
                            style="my.largeButtonStyle.TButton")
strategyButton.grid(column=1, row=0, padx=20, pady=12)

driverButton = ttk.Button(mainMenuFrame,
                          text="Select Driver",
                          command=openDriverMenu,
                          style="my.largeButtonStyle.TButton")
driverButton.grid(column=0, row=1, padx=20, pady=12)

raceFormatButton = ttk.Button(mainMenuFrame,
                              text="Race Format",
                              command=openRaceFormatMenu,
                              style="my.largeButtonStyle.TButton")
raceFormatButton.grid(column=1, row=1, padx=20, pady=12)

startSimButton = ttk.Button(mainMenuFrame,
                            text="START SIMULATION",
                            command=startSim,
                            style="my.largeButtonStyle.TButton")
startSimButton.grid(row=2, columnspan=2, padx=20, pady=12)







## Entrypoint ##
if __name__ == "__main__":
    mainMenuWindow.mainloop()
