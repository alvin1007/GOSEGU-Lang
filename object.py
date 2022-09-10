from typing import Dict

NULL_OBJECT = "NULL_OBJECT"

BOOLEAN_OBJECT = "BOOLEAN_OBJECT"
INTEGER_OBJECT = "INTEGER_OBJECT"

NULL = {}

TRUE:Dict[str, bool] = {
    "Value": True
}

FALSE:Dict[str, bool] = {
    "Value": False
}

class Null:
    def __init__(self) -> None:
        return
    
    def Type(self) -> str:
        return NULL_OBJECT
    
    def Inspect(self) -> str:
        return "null"

class Booolean:
    def __init__(self, Value:bool) -> None:
        self.Value = Value
    
    def Type(self) -> str:
        return BOOLEAN_OBJECT

    def Inspect(self) -> str:
        if self.Value:
            return "true"
        return "false"

class Integer:
    def __init__(self, Value:int) -> None:
        self.Value = Value
    
    def Type(self) -> str:
        return INTEGER_OBJECT
    
    def Inspect(self) -> str:
        return str(self.Value)
