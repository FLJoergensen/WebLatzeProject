import socket


def ConnectToPackageServer(IP="latzes.no-ip.org",PORT=666):
    S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SADDR=(IP,PORT)
    S.connect(SADDR)
    S.sendall("<#+#>LATZEWebToolPackageService ")
    return S
def SendComand(s="EXIT|",BackRecv=True):
    import time
    S=ConnectToPackageServer()
    S.sendall(s)
    if not BackRecv:
        S.close()
        return None
    time.sleep(0.5)
    b=""
    c=-1
    while (len(b) == c):
        c=len(b)
        time.sleep(0.01)
        b=b+S.recv(32)
    return b

def GetPackageInfo(PackString):
    #return: ID|Name|creatorName|Version+|lastPatch|Rating(0-9)|Wichtigkeit(0-3)
    return SendComand("INFO|"+PackString)
def GetNextVersion(PackageString,VersionString):
    return SendComand("NVersion|"+PackString+"#"+VersionString)
def GetNewestVersion(PackageString):
    return SendComand("VERSION+|"+PackString)
def GetAllPackages(start=1,stop="~"):
    #return: ID1|ID2|... |§
    return SendComand("CHECALL|"+str(start)+" "+str(stop))

def DownloadPackage(PackageString,LUName,LUPW):
    return SendComand("GET|~"+LUName+" "+LUPW+"~"+PackString+"#00:00:00:00")
def DownloadPatch(PackageString,PackageVersion="00:00:00:00",LUName,LUPW):
    #PackageVersion The Version to download
    return SendComand("GET|~"+LUName+" "+LUPW+"~"+PackString+"#"+PackageVersion)

def CreateAcc(LUName,LUPW):
    return SendComand("ACCCREATE|"+LUName+" "+LUPW)
    pass
def AccChangePW(LUName,LUPW,NEWPW):
    return SendComand("ACCCHANGEPW|"+LUName+" "+LUPW+"#"+NEWPW)
    pass
def DelAcc(LUName,LUPW):
    return SendComand("ACCDEL|"+LUName+" "+LUPW)
