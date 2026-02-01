# This will be script where we do all calculations-related logic
# for the app, making this the primary backend script.

# TODO: Start writing relevant code;
# - We'll need to import the data from `Satisfactory Recipes - Compiled by FE6515.csv`

import pandas as pd

class Calculator:
    def __init__(self):
        pass

    def calculate(self, desired_item, desired_outputrate):
        pass
    
    def getItemNames(self):
        _data = pd.read_csv("Satisfactory Recipes - Compiled by FE6515.csv")
        _ = []
        for _tier in _data["LOCK"]:
            if _tier == "FICSMAS":
                continue
            _.append(_data["NAME"])
        return _ 