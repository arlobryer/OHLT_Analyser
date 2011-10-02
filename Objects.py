import math as m
import Helpers as h

class Particle:
    def __init__(self):
        self.Eta = None
        self.Phi = None
        self.Pt = None
        
    def getPhi(self):
        return self.Phi

    def getEta(self):
        return self.Eta

    def getPt(self):
        return self.Pt
    

class Electron(Particle):
    def __init__(self, E, Et, eta, phi,
                 HforHoverE, NewSC,
                 PixSeeds, L1Iso,
                 Hiso, Eiso, Tiso, Clusshape,
                 R9, Deta, Dphi):
        self.E = E
        self.Et = Et
        self.Eta = eta
        self.Phi = phi
        self.HforHoverE = HforHoverE
        self.NewSC = NewSC
        self.PixSeeds = PixSeeds
        self.L1Iso = L1Iso
        self.Hiso = Hiso
        self.Eiso = Eiso
        self.Tiso = Tiso
        self.Clusshape = Clusshape
        self.R9 = R9
        self.Deta = Deta
        self.Dphi = Dphi
        self.HoverE = self.HforHoverE/self.E
        self.isBar = False
        self.isEC = False
        if self.L1Iso == 1:
            self.L1Dupl = False
        elif self.L1Iso == 0:
            self.L1Dupl = True
        # L1dupl bs needs to be added - there's a massive bug in OHLT to evaluate this,
        #sigh...emulate it since we need the same behaviour...
        
            
    
    def ElectronPassed(self, Et = 10, L1iso = 0,
                                   Tisobarrel = 999., Tisoendcap = 999.,
                                   Tisoratiobarrel = 0.2, Tisoratioendcap = 0.2,
                                   HisooverETbarrel = 0.2, HisooverETendcap = 0.2,
                                   EisooverETbarrel = 0.2, EisooverETendcap = 0.2,
                                   hoverEbarrel = 0.15, hoverEendcap = 0.10,
                                   clusshapebarrel = 0.024, clusshapeendcap = 0.040,
                                   r9barrel = 0.98, r9endcap = 1.0,
                                   detabarrel = 0.01, detaendcap = 0.01,
                                   dphibarrel = 0.15, dphiendcap = 0.10):

        """This is a copy of the OneElectronSamHarperPassed method in the OHLT code"""
        barreleta = 1.479
        endcapeta = 2.65

        if(m.fabs(self.Eta < barreleta)):
            self.isBar = True
        if(barreleta < m.fabs(self.Eta) and m.fabs(self.Eta) < endcapeta):
            self.isEC = True

        if(self.Et > Et and m.fabs(self.Eta < endcapeta) and
           self.NewSC <= 1 and self.PixSeeds > 0 and
           self.L1Iso >= L1iso and
           self.L1Dupl == False):
            # and dupl condition
            if ((self.isBar and
                 self.Hiso/self.Et < HisooverETbarrel and
                 self.Eiso/self.Et < EisooverETbarrel and
                 self.HoverE < hoverEbarrel and
                 self.Tiso < Tisobarrel and
                 self.Tiso != -999. and
                 self.Tiso/self.Et < Tisoratiobarrel and
                 self.Clusshape < clusshapebarrel and
                 self.R9 < r9barrel and
                 m.fabs(self.Deta) < detabarrel and
                 m.fabs(self.Dphi) < dphibarrel) or
                (self.isEC and
                 self.Hiso/self.Et < HisooverETendcap and
                 self.Eiso/self.Et < EisooverETendcap and
                 self.HoverE < hoverEendcap and
                 self.Tiso < Tisoendcap and
                 self.Tiso != -999. and
                 self.Tiso/self.Et < Tisoratioendcap and
                 self.Tiso/self.Et < Tisoratioendcap and
                 self.Clusshape < clusshapeendcap and
                 self.R9 < r9endcap and
                 m.fabs(self.Deta) < detaendcap and
                 m.fabs(self.Dphi) < dphiendcap)):

                return True
            else:
                return False
               
               

class pfTau(Particle):
    def __init__(self, Pt, eta, phi, leadTrkPt, TrkIso, GammaIso):
        self.Pt = Pt
        self.Eta = eta
        self.Phi = phi
        self.leadTrkPt = leadTrkPt
        self.TrkIso = TrkIso
        self.GammaIso = GammaIso


    def PFTauPassedNoMuonIDNoEleID(self, matchParts, Et = 10, L25TrkPt = 3,
                                   L3TrkIso = 1.5, L3GammaIso = 999.,
                                   ):
        if(self.Pt >= Et and m.fabs(self.Eta) < 2.5
               and self.leadTrkPt >= L25TrkPt
               and self.TrkIso < L3TrkIso
               and self.GammaIso < L3GammaIso
               and h.ParticleMatching(self.Eta, self.Phi, matchParts)):
            return True


class UnCorJet(Particle):
    def __init__(self, Pt, phi, eta):
        self.Pt = Pt
        self.Phi = phi
        self.Eta = eta


class CorJet(Particle):
    """should probably inherit from UncorJets?"""
    def __init__(self, E, Pt, eta, emf):
        self.E = E
        self.Pt = Pt
        self.Eta = eta
        self.EMF = emf

    def ID(self):
        id = (m.fabs(self.Eta) < 2.6 and self.EMF > 1.0E-6
              and self.EMF < 999.)
        return id
        
