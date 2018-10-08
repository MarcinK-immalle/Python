class ClockDisplay:
    def __init__(self):
        self.hours = numberDisplay(24)
        self.minutes = numberDisplay(60)
        
    def updateDisplay(self):
        displayString = str(self.hours.getDisplayValue())+ " : " +str(self.minutes.getDisplayValue())
        print(displayString)
    
    def ClockDisplay(self):
        self.hours = numberDisplay(24)
        self.minutes = numberDisplay(60)
        self.setTime(self.hour, self.minutes)
    
    def timeTick(self):
        self.minutes.increment()
        if self.minutes.getValue() == 0:
             self.hours.increment()
        self.updateDisplay()

    # def setTime(self, hour):
    #     self.hours.setValue(hour)
    #     self.minutes.setValue(minute)
    #     self.updateDisplay()
    
    def getTime(self):
        return self.displayString
    
class numberDisplay:
    def __init__(self, rollOverLimit):
        self.limit = rollOverLimit
        self.value = 0

    def getValue(self):
        return self.value
    
    def getDisplayValue(self):
        if self.value <= 10: 
            return "0" + value
        else: 
            return " " + value

    # def setValue(self, replacementValue):
    #     if (replacementValue >= 0) && (replacementValue <= self.limit):
    #          value = replacementValue

    def increment(self):
        self.value = (self.value + 1) % self.limit

    if __name__ == '__main__':
        c1 = ClockDisplay()