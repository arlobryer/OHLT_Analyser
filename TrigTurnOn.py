#!/usr/bin/env python

#small python analyser


import ROOT as r
import math as m
import time
import sys
import glob
t0 = time.clock()

def getChain(files, chainName):
    c = r.TChain(chainName)
    for f in  files:
        c.AddFile(f)
    return c


def file_get(path, fname):
    files = glob.glob(path + fname)
    return files


class Event:
    def __init__(self, c):
        self.pfMHT = getattr(c, "pfMHT")
        # jets
        self.nJetCorCal = getattr(c, 'NohJetCorCal')
        self.JetCorCalE = getattr(c, 'ohJetCorCalE')
        self.JetCorCalPt = getattr(c, "ohJetCorCalPt")
        self.JetCorCalEta = getattr(c, "ohJetCorCalEta")
        self.JetCorCalEMF = getattr(c, "ohJetCorCalEMF")
        # electrons
        self.nEle = getattr(c, 'NohEle')
        self.EleHforHoverE = getattr(c, 'ohEleHforHoverE')
        self.EleE = getattr(c, 'ohEleE')
        self.EleEta = getattr(c, 'ohEleEta')
        self.EleEt = getattr(c, 'ohEleEt')
        self.EleNewSC = getattr(c, 'ohEleNewSC')
        self.ElePixelSeeds = getattr(c, 'ohElePixelSeeds')
        self.EleL1Iso = getattr(c, 'ohEleL1iso')
        self.EleL1Dupl = getattr(c, 'ohEleL1Dupl')
        self.EleHiso = getattr(c, 'ohEleHiso')
        self.EleEiso = getattr(c, 'ohEleEiso')
        self.EleHoverE = getattr(c, 'ohEleHoverE')
        self.EleTiso = getattr(c, 'ohEleTiso')
        self.EleClusShape = getattr(c, 'ohEleClusShap')
        self.EleR9 = getattr(c, 'ohEleR9')
        self.EleDeta = getattr(c, 'ohEleDeta')
        self.EleDphi = getattr(c, 'ohEleDphi')
        # muons
        self.nMuL3 = getattr(c, 'nohMuL3')
        self.MuL3Eta = getattr(c, 'ohmuL3Pt')
        self.MuL3Dr = getattr(c, 'ohMuL3Dr')
        self.MuL3Iso = getattr(c, 'ohMuL3Iso')
        self.MuL3L2idx = getattr(c, 'ohMuL3l2idx')
        self.MuL2Eta = getattr(c, 'ohMuL2Eta')
        self.MuL2Nhits = getattr(c, 'ohMul2Nhits')
        self.MuL2Nstat = getattr(c, 'ohMuL2Nstat')
        self.MuL2Pt = getattr(c, 'ohMuL2Pt')
        self.MuL2Iso = getattr(c, 'ohMuL2Iso')
        self.MuL2Phi = getattr(c, 'ohMuL2Phi')
        self.muL2Eta = getattr(c, 'ohMuL2eta')
        self.nMuL1 = getattr(c, 'nL1Mu')
        self.MuL1Pt = getattr(c, 'L1MuPt')
        self.MuL1Phi = getattr(c, 'L1muPhi')
        self.MuL1Eta = getattr(c, 'L1MuEta')
        self.MuL1Qal = getattr(c, 'L1MuQal')
        # taus
        self.nPfTau = getattr(c, 'NohpfTau')
        self.pfTauPt = getattr(c, 'ohpfTauPt')
        self.pfTauEta = getattr(c, 'ohpfTauEta')
        self.pfTauPhi = getattr(c, 'ohpfTauPhi')
        self.pfTauLeadTrackPt = getattr(c, 'ohpfTauleadTrackPt')
        self.pfTauTrkIso = getattr(c, 'ohpfTauTrkIso')
        self.pfTauGammaIso = getattr(c, 'ohpfTauGammaIso')

        # access methods
        # specific objects should probably be in their own class
    def getpfMHT(self):
        return self.pfMHT
    def getNjets(self):
        return self.njetCorCal
    def getJetE(self, i):
        return self.JetCorCalE[i]
    def getJetPt(self, i):
        return self.JetCorCalPt[i]
    def getJetEta(self, i):
        return self.JetCorCalEta[i]

    
    # this is dirty as hell...should be split into sensible objects...will do for now
    # emulates OHltTreeOpen design (as if that was a good idea...).
    def jetID(self,jetInd):
        if jetInd >= self.njetCorCal:
            return False
        else:
            jID = (m.fabs(self.JetCorCalEta[jetInd]) and self.JetCorCalEMF[jetInd] > 1.0E-6 and self.JetCorCalEMF[jetInd] < 999.0)
        return jID

    def SumCorHtPassed(self, thresh, jet_thresh, eta_thres):
        sumHT = 0.
        for i in range (self.getNjets()):
            if(self.jetID(i) and self.getJetPt(i) > jet_thresh and m.fabs(self.getJetEta(i)) > eta_thresh):
                sumHT += getJetE(i)/m.cosh(getJetEta(i))
        if sumHT >= thresh:
            return True
               
    def pfMHTPassed(thres):
        if pfMHT >= thresh:
            return True

    def PFTauPassedNoMuonIDNoEleID(Et, L25TrkPt, L3TrkIso, L3GammaIso):
        t = 0
        for i in range(self.nPfTau):
            if(self.pfTauPt[i] >= Et and m.fabs(self.pfTauEta[i]) < 2.5
               and self.pfTauLeadTrackPt[i] >= L25TrkPt
               and self.pfTauTrkIso[i] < L3TrkIso
               and self.pfTauGammaIso < L3GammaIso
               and TauPFtoCaloMatching(self.pfTauEta[i],pfTauPhi[i]) == 1):
                t += 1
        return t
                
                
        


def deltaPhi(phi1, phi2):
    dphi = m.fabs(phi1 - phi2)
    if dphi > 6.283185308:
        dphi -= 6.283185308
    if (dphi > 3.141592654):
        dphi = 6.283185308 - dphi
    return dphi

def deltaEta(eta1, eta2):
    return m.fabs(eta1 - eta2)
    


def run(chain):
    for i in range(chain.GetEntries()):
        if i%1000==0:
            print 'Event: ' + str(i)
        chain.GetEntry(i)
        ev = Event(chain)
        # here you do whatever analysis etc.
    
        


if __name__=='__main__':
    elehad_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_ElectronHad_2011A/"
    fname = 'openhlt_*.root'
    elehadfiles = file_get(elehad_path, fname)
    chain = getChain(elehadfiles, 'HltTree')
    run(chain)


