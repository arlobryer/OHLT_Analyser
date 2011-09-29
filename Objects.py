class Electron:
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
        # L1dupl bs needs to be added


        def OneElectronSamHarperPassed(Et, L1iso, Tisobarrel, Tisoendcap,
                                 Tisoratiobarrel, Tisoratioendcap,
                                 HisooverETbarrel, HisooverETendcap,
                                 EisooverETbarrel, EisooverETendcap,
                                 hoverEbarrel, hoverEendcap, clushapebarrel,
                                 clusshapeendcap, r9barrel, r9endcap, detabarrel,
                                 detaendcap, dphibarrel, dphiendcap):


            barreleta = 1.479
            endcapeta = 2.65

            if(m.fabs(self.Eta < barreleta)):
               self.isBar = True
            if(barreleta < m.fabs(self.Eta) and m.fabs(self.Eta) < endcapeta):
                self.isEC = True

            if(self.Et > Et and m.fabs(self.Eta < endcapeta) and
               self.NewSC <= 1 and self.PixSeeds > 0 and self.L1Iso >= L1iso):
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

               
               

class pfTau:
    def __init__(self, Pt, eta, phi, leadTrkPt, TrkIso, GammaIso):
        self.Pt = Pt
        self.Eta = eta
        self.Phi = phi
        self.leadTrkPt = leadTrkPt
        self.TrkIso = TrkIso
        self.GammaIso = GammaIso


    def PFTauPassedNoMuonIDNoEleID(Et, L25TrkPt, L3TrkIso, L3GammaIso):
        if(self.Pt >= Et and m.fabs(self.Eta) < 2.5
               and self.leadTrackPt >= L25TrkPt
               and self.uTrkIso < L3TrkIso
               and self.GammaIso < L3GammaIso
               and TauPFtoCaloMatching(self.pfTauEta[i],pfTauPhi[i])):
                t += 1
        return t


class UnCorJets:
    def __init__(self, Pt, phi, eta):
        self.Pt = Pt
        self.Phi = phi
        self.Eta = eta


class CorJets:
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
        
