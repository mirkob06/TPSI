class TransuctionModel:
    """Represents a transuction with structured attributes."""
    def __init__ (self, code, enter, timeIn, exit, timeOut, amount):
        self.code = code
        self.enter = enter 
        self.timeIn = timeIn
        self.exit = exit
        self.timeOut = timeOut
        self.amount = amount
    
    @classmethod
    def from_xml(cls,data):
        return cls(
            code=data.get("data"),
            enter=data.get("enter"),
            timeIn=data.get("timeIn"),
            exit=data.get("exit"),
            timeOut=data.get("timeOut"),
            amount=data.get("amount")
        )
    