class Phone:
    dataProvider = ""
    battery = 0
    crackedScreen = False

    def __init__(self, dataProvider, batteryPercentage, screenStatus):
        self.dataProvider = dataProvider
        self.battery = batteryPercentage
        self.crackedScreen = screenStatus

    def getBattery(self):
        return self.battery

    def getDataProvider(self):
        return self.dataProvider

    def Cracks(self):
        self.crackedScreen = True
        self.battery -= 40


class iPhone(Phone):
    IOSVersion = 0

    def __init__(self, dataProvider, batteryPercentage, screenStatus, IOSVersion):
        self.dataProvider = dataProvider
        self.battery = batteryPercentage
        self.crackedScreen = screenStatus
        self.IOSVersion = IOSVersion

    def getIOSVersion(self):
        return self.IOSVersion
