import ROOT as r
import glob
import math as m

def getChain(files, chainName):
    c = r.TChain(chainName)
    for f in  files:
        c.AddFile(f)
    return c

def file_get(path, fname):
    files = glob.glob(path + fname)
    return files



#Some functions that may be necessary


def deltaPhi(phi1, phi2):
    dphi = m.fabs(phi1 - phi2)
    if dphi > 6.283185308:
        dphi -= 6.283185308
    if (dphi > 3.141592654):
        dphi = 6.283185308 - dphi
    return dphi

def deltaEta(eta1, eta2):
    return m.fabs(eta1 - eta2)

def ParticleMatching(eta, phi, part, partsPt = 8, r = 0.3):
    if Part.getPt() < partsPt:
        return False
    deltaphi = m.fabs(phi - part.getPhi())
    if deltaphi > 3.14159:
        deltaphi = (2.0 * 3.14159) - deltaphi
        deltaeta = m.fabs(eta - part.getEta())
        if (deltaeta < r and deltaphi < r):
            #note that this actually defines a SQUARE (not a circle as you'd
            #expect from a dR...but this is the way it is in OHLT...
            return True
        else:
            return False
        
