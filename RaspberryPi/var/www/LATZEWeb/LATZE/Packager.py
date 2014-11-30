import cPickle as pickle
class Packag:
    def __init__(self):
        self.PackageName=""
        self.PackageID="0000000000"#hexID
        self.PackageVersion="00:00:00:00"#hex plited
        self.PackageVersionSupfix="-0"#hex
        self.PreComands=[]
        self.PastComands=[]
        self.Files=[]
        pass
    def __del__(self):
        pass
    def AddFile(self,FilePath="file.file",FileContent="",ModType="replaceF"):
        #(FullFilePath,EdditMode,FileContent)
        FM="#"
        if ModType=="replaceF":
            FM="*"
        else if ModType=="addC":
            FM="+"
        else if ModType=="removeF":
            FM="/"
        else if ModType=="removeC":
            FM="-"
        else if ModType=="new":
            FM="#"
        self.Files.append((FilePath,FM,FileContent))
        pass
    def SavePackage(self,Path=""):
        P=""
        if Path != "":
            P=Path
        else:
            P=self.Name+
        pickle.dump(self,
        pass
    def getDumpedObject(self):
        return pickle.dumps(self)
def InstallPackag(obj):
    import os
    for item in obj.PreComands:
        os.system(item)
        pass
    
    for item in obj.PastComands:
        os.system(item)
        pass
    pass
