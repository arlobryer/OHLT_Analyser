import math as m
import time
import sys
t0 = time.clock()

import Objects as obj


class Event:
    def __init__(self, c):
        # L1 trigger bits
        self.L1_HTT100 = getattr(c, "L1_HTT100")
        self.L1_ETM30 = getattr(c, "L1_ETM30")

        self.recoMET = getattr(c, "recoMetCal")
        self.pfMHT = getattr(c, "pfMHT")
        self.sumHT = 0.
        # cor jets
        self.nJetCorCal = getattr(c, 'NohJetCorCal')
        self.JetCorCalE = getattr(c, 'ohJetCorCalE')
        self.JetCorCalPt = getattr(c, "ohJetCorCalPt")
        self.JetCorCalEta = getattr(c, "ohJetCorCalEta")
        self.JetCorCalEMF = getattr(c, "ohJetCorCalEMF")
        #reco cor jets
        self.nrecoJetCorCal = getattr(c, 'NrecoJetCorCal')
        self.recoJetCorCalE = getattr(c, 'recoJetCorCalE')
        self.recoJetCorCalPt = getattr(c, 'recoJetCorCalPt')
        self.recoJetCorCalEta = getattr(c, 'recoJetCorCalEta')
        self.recoJetCorCalEMF = getattr(c, 'recoJetCorCalEMF')
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
        #reco electrons
        self.nRecoEle = getattr(c, 'NrecoElec')
        self.recoElePt = getattr(c, 'recoElecPt')
        self.recoElePhi = getattr(c, 'recoElecPhi')
        self.recoEleEta = getattr(c, 'recoElecEta')
        # muons
        self.nMuL3 = getattr(c, 'NohMuL3')
        self.MuL3Pt = getattr(c, 'ohMuL3Pt')
        self.MuL3Eta = getattr(c, 'ohMuL3Eta')
        self.MuL3Dr = getattr(c, 'ohMuL3Dr')
        self.MuL3Iso = getattr(c, 'ohMuL3Iso')
        self.MuL3L2idx = getattr(c, 'ohMuL3L2idx')
        self.MuL2Eta = getattr(c, 'ohMuL2Eta')
        # reco muons
        self.nRecoMu = getattr(c, 'NrecoMuon')
        self.recoMuPt = getattr(c, 'recoMuonPt')
        self.recoMuPhi = getattr(c, 'recoMuonPhi')
        self.recoMuEta = getattr(c, 'recoMuonEta')
        # self.MuL2Nhits = getattr(c, 'ohMuL2Nhits') to be investigated
        # self.MuL2Nstat = getattr(c, 'ohMuL2Nstat') ditto
        self.MuL2Pt = getattr(c, 'ohMuL2Pt')
        self.MuL2Iso = getattr(c, 'ohMuL2Iso')
        self.MuL2Phi = getattr(c, 'ohMuL2Phi')
        self.MuL2Eta = getattr(c, 'ohMuL2Eta')
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
        #reco taus
        self.nRecoPfTau = getattr(c, 'NRecoPFTau')
        self.recoPfTauPt = getattr(c, 'recopfTauPt')
        self.recoPfTauEta = getattr(c, 'recopfTauEta')
        self.recoPfTauPhi = getattr(c, 'recopfTauPhi')
        self.recoPfTauLeadTrackPt = getattr(c, 'recopfTauLeadTrackPt')
        self.recoPfTauTrkIso = getattr(c, 'recopfTauTrkIso')
        self.recoPfTauGammaIso = getattr(c, 'recopfTauGammaIso')

        # set the collections of objects
        self.setElectrons()
        self.setPFTaus()
        self.setUnCorJets()
        self.setCorJets()
        self.setRecoCorJets()
        self.setRecoElectrons()
        self.setRecoPfTaus()
        self.recoCorHT = self.Ht(self.recoCorJets)
        self.CorHT = self.Ht(self.CorJets)
        # access methods
        # specific objects should probably be in their own class
    def getRecoMET(self):
        return self.recoMET
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

    def setRecoElectrons(self):
        recoEle=[]
        for e in range(self.nRecoEle):
            recoEle.append(obj.RecoElectron(self.recoElePt[e], self.recoElePhi[e],
                                            self.recoEleEta[e]))
        self.recoElectrons = recoEle

        

    def setPFTaus(self):
        pfT=[]
        for i in range (self.nPfTau):
            pfT.append(obj.pfTau(self.pfTauPt[i], self.pfTauEta[i], self.pfTauPhi[i],
                                   self.pfTauLeadTrackPt[i], self.pfTauTrkIso[i],
                                   self.pfTauGammaIso[i]))
        self.pfTau = pfT

    def setRecoPfTaus(self):
        rpfT=[]
        for i in range (self.nRecoPfTau):
            rpfT.append(obj.recoPfTau(self.recoPfTauPt[i], self.recoPfTauEta[i],
                                      self.recoPfTauPhi[i], self.recoPfTauLeadTrackPt[i],
                                      self.recoPfTauTrkIso[i], self.recoPfTauGammaIso[i]))
        self.recoPfTau = rpfT
                        
    def setUnCorJets(self):
        uncorJ=[]
        for i in range (self.nJetCal):
            uncorJ.append(obj.UnCorJet(self.JetCalPt[i], self.JetCalPhi[i],
                                        self.JetCalEta[i]))
        self.UnCorJets = uncorJ

    def setCorJets(self):
        corJ=[]
        for i in range (self.nJetCorCal):
            corJ.append(obj.CorJet(self.JetCorCalE[i], self.JetCorCalPt[i],
                                    self.JetCorCalEta[i], self.JetCorCalEMF[i]))
        self.CorJets = corJ

    def setRecoCorJets(self):
        RecoCorJ = []
        for j in range(self.nrecoJetCorCal):
            RecoCorJ.append(obj.RecoCorJet(self.recoJetCorCalE[i], self.recoJetCorCalPt[i],
                                           self.recoJetCorCalEta[i], self.recoJetCorCalEMF[i]))
        self.recoCorJets = RecoCorJ


    def Ht(self, jet_type, jet_thresh = 40, eta_thresh = 3.0):
        ht = 0
        for jet in jet_type:
            if (jet.ID() and jet.getPt() > jet_thresh and m.fabs(jet.getEta()) < eta_thresh):
                ht += jet.E/m.cosh(jet.getEta())
        return ht

    
        
               
    def pfMHTPassed(self, thresh):
        if self.pfMHT >= thresh:
            return True
        return False

    def OneMuonPassed(self, muThresh = [5.,4.,3], dr = 2., iso = 0.,
                      etal2 = 2.5, etal3 = 2.5,
                      minNhits = 0, minNstats = 0):
        rcL1 = 0
        rcL2 = 0
        rcL3 = 0
        rcL1L2L3 = 0
        nL1mu = 8
        L1MinQuality = 1
        L1MaxQuality = 7
        doL1L2match = False

        L3MuCandIdForOnia = []
        for i in range(10):
            L3MuCandIdForOnia.append(-1)

        for mu in range(self.nMuL3):
            bestL1L2drMatchInd = -1
            bestL1L2drmatch = 999.

            if(m.fabs(self.MuL3Eta[mu]) < etal3 and
               self.MuL3Pt[mu] > muThresh[2] and
               self.MuL3Dr[mu] < dr and
               self.MuL3Iso[mu] >= iso):
                rcL3+=1

            j = self.MuL3L2idx[mu]

            if(m.fabs(self.MuL2Eta[j]) < etal2):
                if (m.fabs(self.MuL2Eta[j]) < 0.9 or
                    (m.fabs(self.MuL2Eta[j]) > 1.5 and
                     m.fabs(self.MuL2Eta[j]) < 2.1)
                    # or (MuL2Nhits[j] > minNhits and muL2Nstat[j] > minNstats)
                    ):
                    if(self.MuL2Pt[j] > muThresh[1] and self.MuL2Iso[j] >= iso):
                        rcL2+=1

                        for k in range(self.nMuL1):
                            if (self.MuL1Pt[k] < muThresh[0]):
                                continue

                            deltaphi = m.fabs(self.MuL2Phi[j] - self.MuL1Phi[k])
                            if deltaphi > 3.14159:
                                deltaphi = (2.0 * 3.14150) - deltaphi
                            deltarl1l2 = m.sqrt((self.MuL2Eta[j] - self.MuL1Eta[k]) *
                                               (self.MuL2Eta[j] - self.MuL1Eta[k]) +
                                               (deltaphi * deltaphi))
                            if deltarl1l2 < bestL1L2drmatch:
                                bestL1L2drMatchInd = k
                                bestL1L2drmatch = deltarl1l2

                        if doL1L2match:
                            pass
                            #some stuff is in here but the bool is set to false in
                            #OHLT... don't worry about it for now.

                        else:
                            L3MuCandIdForOnia[rcL1L2L3] = mu
                            rcL1L2L3+=1

            return rcL1L2L3
                



    




