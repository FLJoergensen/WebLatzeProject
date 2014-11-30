
def getInfos():
    #return a tupe of ("PluginName","CreatorName",ShortDiscriptption,pluginID,pluginID)
    pass

def getInfoPage():
    #return a custem disigend webSeit
    pass
def getSetupPage(req,para1="",para2=""):
    #return the basic Plugin Setup Page with custom count of parameters
    pass
def getSetupPageAdvanced(req,para1="",para2=""):
    #return the advanced Plugin Setup Page with custom count of parameters
    #it will be only used if the Setupmode set on Advanced Mode
    pass
def getSetupButtons(req,mode="base|advanced"):
    #return Tuppel as Button
    #1.Para "NameOfThePlugin#"+"ButtonName"
    #2.Para "ButtonInfo"
    #3-00.Para "ParaString"-??
    return [("PluginName#Name","Info","PARA[")]
