#!/usr/bin/env python

#small python analyser


import ROOT as r
import math as m
import time
import sys
import glob
t0 = time.clock()

import Objects as obj

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
        # cor jets
        self.nJetCorCal = getattr(c, 'NohJetCorCal')
        self.JetCorCalE = getattr(c, 'ohJetCorCalE')
        self.JetCorCalPt = getattr(c, "ohJetCorCalPt")
        self.JetCorCalEta = getattr(c, "ohJetCorCalEta")
        self.JetCorCalEMF = getattr(c, "ohJetCorCalEMF")
        # uncor jets
        self.nJetCal = getattr(c, 'NohJetCal')
        self.JetCalPt = getattr(c, 'ohJetCalPt')
        self.JetCalPhi = getattr(c, 'ohJetCalPhi')
        self.JetCalEta = getattr(c, 'ohJetCalEta')
        # electrons
        self.nEle = getattr(c, 'NohEle')
        self.EleHforHoverE = getattr(c, 'ohEleHforHoverE')
        self.EleE = getattr(c, 'ohEleE')
        self.EleEta = getattr(c, 'ohEleEta')
        self.ElePhi = getattr(c, 'ohElePhi')
        self.EleEt = getattr(c, 'ohEleEt')
        self.EleNewSC = getattr(c, 'ohEleNewSC')
        self.ElePixelSeeds = getattr(c, 'ohElePixelSeeds')
        self.EleL1Iso = getattr(c, 'ohEleL1iso')
        self.EleHiso = getattr(c, 'ohEleHiso')
        self.EleEiso = getattr(c, 'ohEleEiso')
        self.EleTiso = getattr(c, 'ohEleTiso')
        self.EleClusShape = getattr(c, 'ohEleClusShap')
        self.EleR9 = getattr(c, 'ohEleR9')
        self.EleDeta = getattr(c, 'ohEleDeta')
        self.EleDphi = getattr(c, 'ohEleDphi')
        # muons
        self.nMuL3 = getattr(c, 'NohMuL3')
        self.MuL3Eta = getattr(c, 'ohMuL3Pt')
        self.MuL3Dr = getattr(c, 'ohMuL3Dr')
        self.MuL3Iso = getattr(c, 'ohMuL3Iso')
        self.MuL3L2idx = getattr(c, 'ohMuL3L2idx')
        self.MuL2Eta = getattr(c, 'ohMuL2Eta')
        # self.MuL2Nhits = getattr(c, 'ohMuL2Nhits') to be investigated
        # self.MuL2Nstat = getattr(c, 'ohMuL2Nstat') ditto
        self.MuL2Pt = getattr(c, 'ohMuL2Pt')
        self.MuL2Iso = getattr(c, 'ohMuL2Iso')
        self.MuL2Phi = getattr(c, 'ohMuL2Phi')
        self.muL2Eta = getattr(c, 'ohMuL2Eta')
        self.nMuL1 = getattr(c, 'NL1Mu')
        self.MuL1Pt = getattr(c, 'L1MuPt')
        self.MuL1Phi = getattr(c, 'L1MuPhi')
        self.MuL1Eta = getattr(c, 'L1MuEta')
        self.MuL1Qal = getattr(c, 'L1MuQal')
        # taus
        self.nPfTau = getattr(c, 'NohpfTau')
        self.pfTauPt = getattr(c, 'ohpfTauPt')
        self.pfTauEta = getattr(c, 'ohpfTauEta')
        self.pfTauPhi = getattr(c, 'ohpfTauPhi')
        self.pfTauLeadTrackPt = getattr(c, 'ohpfTauLeadTrackPt')
        self.pfTauTrkIso = getattr(c, 'ohpfTauTrkIso')
        self.pfTauGammaIso = getattr(c, 'ohpfTauGammaIso')

        # set the collections of objects
        self.setElectrons()
        self.setPFTaus()
        self.setUnCorJets()
        self.setCorJets()

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

    # set up the objects
    def setElectrons(self):
        ele=[]
        for i in range (self.nEle):
            ele.append(obj.Electron(self.EleE[i], self.EleEt[i],
                                    self.EleEta[i], self.ElePhi[i],
                                    self.EleHforHoverE[i], self.EleNewSC[i],
                                    self.ElePixelSeeds[i],
                                self.EleL1Iso[i], self.EleHiso[i], self.EleEiso[i],
                                self.EleTiso[i], self.EleClusShape[i],
                                self.EleR9[i], self.EleDeta[i], self.EleDphi[i]))
        self.Electrons = ele

    def setPFTaus(self):
        pfT=[]
        for i in range (self.nPfTau):
            pfT.append(obj.pfTau(self.pfTauPt[i], self.pfTauEta[i], self.pfTauPhi[i],
                                   self.pfTauLeadTrackPt[i], self.pfTauTrkIso[i],
                                   self.pfTauGammaIso[i]))
        self.pfTau = pfT

    def setUnCorJets(self):
        uncorJ=[]
        for i in range (self.nJetCal):
            uncorJ.append(obj.UnCorJets(self.JetCalPt[i], self.JetCalPhi[i],
                                        self.JetCalEta[i]))
        self.UnCorJets = uncorJ

    def setCorJets(self):
        corJ=[]
        for i in range (self.nJetCorCal):
            corJ.append(obj.CorJets(self.JetCorCalE[i], self.JetCorCalPt[i],
                                    self.JetCorCalEta[i], self.JetCorCalEMF[i]))
        self.CorJets = corJ




    def SumCorHtPassed(self, thresh, jet_thresh, eta_thres):
        sumHT = 0.
        for jet in self.CorJets:
            if(jet.ID() and jet.Pt > jet_thresh and m.fabs(jet.Eta) > eta_thresh):
                sumHT += jet.E/m.cosh(jet.Eta)
        if sumHT >= thresh:
            return True
               
    def pfMHTPassed(thres):
        if pfMHT >= thresh:
            return True

    
                
                
    def TauPFToCaloMatching(eta, phi):
        for i in range(self.nJetCal):
            if(self.JetCalPt[i] < 8):
                continue
            deltaphi = m.fabs(phi - self.JetCalPhi[i])
            if deltaphi > 3.14159:
                deltaphi = (2.0 * 3.14159) - deltaphi
            deltaeta = m.fabs(eta - self.JetCalEta[i])
            if (deltaeta < 0.3 and deltaphi < 0.3):
                return True
            else:
                return False

   


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
        if ev.Electrons is not None:
            for e in ev.Electrons:
                print e.E



if __name__=='__main__':
    elehad_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_ElectronHad_2011A/"
    fname = 'openhlt_*.root'
    elehadfiles = file_get(elehad_path, fname)
    chain = getChain(elehadfiles, 'HltTree')
    run(chain)


