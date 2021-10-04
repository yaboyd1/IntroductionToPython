# Scheduler Parent
class SchedulerSPM:
    def __init__(self):
        pass
    def __str__(self):
        pass
    def Configure(self):
        pass

# Scheduler Children (Inherits from SchedulerSPM)
class SchedulerAedesAegypti(SchedulerSPM):
    def __init__(self):
        self.aedesAegypti = AedesAegypti()
    def __str__(self):
        return "Scheduler:\n{}".format(self.aedesAegypti)

class SchedulerMammal(SchedulerSPM):
    def __init__(self):
        self.mammal = Mammal()
    def __str__(self):
        return "Scheduler:\n{}".format(self.mammal)

class SchedulerVegetation(SchedulerSPM):
    def __init__(self):
        self.vegetation = Vegetation()
    def __str__(self):
        return "Scheduler:\n{}".format(self.vegetation)

class SchedulerContainer(SchedulerSPM):
    def __init__(self):
        self.container = Container()
    def __str__(self):
        return "Scheduler:\n{}".format(self.container)

class SchedulerMeteorology(SchedulerSPM):
    def __init__(self):
        self.meteorology = Meteorology()
    def __str__(self):
        return "Scheduler for {}".format(self.meteorology)

# Used by the Scheduler Children
class AedesAegypti:
    def __init__(self, lifeStage, energyLevel):
        self.lifeStage = lifeStage
        self.energyLevel = energyLevel
    def __str__(self):
        return "Life Stage: {}\nEnergy Level: {}".format(self.lifeStage, self.energyLevel)
    
    def Birth(self):
        pass
    def Metamorphosis(self):
        pass
    def Death(self):
        pass
    def FlyingRandomly(self):
        pass
    def LookForRestingPlace(self):
        pass
    def LookForPlant(self):
        pass
    def Feeding(self):
        pass
    def Mating(self):
        pass
    def Ovipositing(self):
        pass

class Mammal:
    def __init__(self, traceIntensity):
        self.traceIntensity = traceIntensity
    def __str__(self):
        return "Trace Intensity: {}".format(self.traceIntensity)
    
    def MovingRandomly(self):
        pass
    def UpdateTrace(self):
        pass

class Vegetation:
    def __init__(self, trace-intensity):
        self.trace-intensity = trace-intensity
    def __str__(self):
        return "Trace Intensity: {}".format(self.traceIntensity)

    def UpdateTrace(self):
        pass

class Container:
    def __init__(self, percentageLiquid, volatilityLiquid, percentageExposure, traceIntensity):
        self.percentageLiquid = percentageLiquid
        self.volatilityLiquid = volatilityLiquid
        self.percentageExposure = percentageExposure
        self.traceIntensity = traceIntensity
    def __str__(self):
        return "Percentage Liquid: {}\nVolatility Liquid: {}\nPercentage Exposure: {}\nTrace Intensity: {}".format(self.percentageLiquid, self.volatilityLiquid, self.percentageExposure, self.traceIntensity)
    
    def updateVolume(self):
        pass
    def UpdateTrace(self):
        pass

class Meteorology:
    def __init__(self, windDirection, windDirectionMaxSpeed, accumRainfall, accumSolarRadiation, globalSolarRadiation, airTemp, highAirTemp, lowAirTemp, airRelativeHumidity, windSpeed, highWindSpeed):
        self.windDirection = windDirection
        self.windDirectionMaxSpeed = windDirectionMaxSpeed
        self.accumRainfall = accumRainfall
        self.accumSolarRadiation = accumSolarRadiation
        self.globalSolarRadiation = globalSolarRadiation
        self.airTemp = airTemp
        self.highAirTemp = highAirTemp
        self.lowAirTemp = lowAirTemp
        self.airRelativeHumidity = airRelativeHumidity
        self.windSpeed = windSpeed
        self.highWindSpeed = highWindSpeed
    def __str__(self):
        return "Wind Direction: {}\nWind Direction Max Speed: {}\nAccum Rainfall: {}\nAccum Solar Radiation: {}\nGlobal Solar Radiation: {}\nAir Temp: {}\nHigh Air Temp: {}\nLow Air Temp: {}\nAir Relative Humidity: {}\nWind Speed: {}\nHigh Wind Speed: {}".format(self.windDirection, self.windDirectionMaxSpeed, self.accumRainfall, self.accumSolarRadiation, self.globalSolarRadiation, self.airTemp, self.highAirTemp, self.lowAirTemp, self.airRelativeHumidity, self.windSpeed, self.highWindSpeed)
    
    def updateData(self):
        pass
