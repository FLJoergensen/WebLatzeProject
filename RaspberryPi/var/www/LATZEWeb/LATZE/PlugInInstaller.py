import os
import cPickle as pickle

OBJ=None

class PlugInRegister:
    self.PlugInInfos=[]
    self.LATZEUName=""
    self.LATZEUPW=""
    def __init__(self):
        try:
            a=self.LOAD()
            self.PlugInInfos=a.PlugInInfos
            self.LATZEUName=a.LATZEUName
            self.LATZEUPW=a.LATZEUPW
        finally:
            print "Create new PlugInRegister"
        pass
    def __del__(self):
        self.SAVE()
        pass
    def AddPlugIn(self,Name,ID,InstalledVersion,From,LastUpdate):
        PlugInInfos.append((Name,ID,InstalledVersion,From,LastUpdate))
        pass
    def SAVE(self):
        with open("/var/www/LATZEWeb/plugin/pluginInfo.LFP","w") as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)
    def LOAD(self):
        with open("/var/www/LATZEWeb/plugin/pluginInfo.LFP","r") as f:
            return pickle.load(f)

def __ControlPlugInRegister():
    if OBJ==None:
        OBJ=PlugInRegister()
def __CPIR():
    __ControlPlugInRegister()
def getPlugInRegister():
    __CPIR()
    r=OBJ.PlugInInfos
    return r
def getPlugInIDs():
    __CPIR()
    r=[]
    for item in OBJ.PlugInInfos:
        r.append(irem[1])
    return r
def getPlugInNames():
    __CPIR()
    r=[]
    for item in OBJ.PlugInInfos:
        r.append(irem[0])
    return r

def UpdateAllPlugInsFULL():
    __CPIR()
    updetet=False
    import ServerConector as SC
    import SSAService as SSA
    import Packager as PACK
    import thread
    for item in OBJ.PlugInInfos:
        V=SC.GetNextVersion(item[1],item[2])
        Source=SC.DownloadPatch(item[1],V,OBJ.LATZEUName,OBJ.LATZEUPW)
        try:
            objPackage=pickle.loads(Source)
        except:
            objPackage=None
        if objPackage != None:
            updated=True
            thread.start_new_thread(PACK.InstallPack,(objPackage,))
    if updated:
        UpdateAllPlugInsFULL()
        
def UpdateAllPlugIns():
    __CPIR()
    import ServerConector as SC
    import SSAService as SSA
    import Packager as PACK
    import thread
    LUName,LUPW=SSA.getSSALATZEUserACC()
    for item in OBJ.PlugInInfos:
        V=SC.GetNextVersion(item[1],item[2])
        Source=SC.DownloadPatch(item[1],V,LUName,LUPW)
        try:
            objPackage=pickle.loads(Source)
        except:
            objPackage=None
        if objPackage != None:
            thread.start_new_thread(PACK.InstallPack,(objPackage,))
