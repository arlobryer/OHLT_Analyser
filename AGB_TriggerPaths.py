#analysis backup triggers:
def HT400_DoubleTau10_PFMHT50(ev):
    if ev.L1_HTT100 and ev.SumCorHTPassed(thresh = 400.) and ev.pfMHTPassed(50.) and ev.pfTau is not None:
        taus = 0
        for t in ev.pfTau:
            if t.PFTauPassedNoMuonIDNoeEleID(ev.UncorJets):
                taus += 1
        if taus>=2:
            return True
        else:
            return False
    return False

def HT400_Ele5_PFMHT50(ev):
    if ev.L1_HTT100 and ev.SumCorHTPassed(thresh = 400.) and ev.pfMHTPassed(50.) and ev.Electrons is not None:
        for e in ev.Electrons:
            if e.ElectronPassed():
                return True
        return False
    return False

def HT400_Mu5_PFMHT50(ev):
    if ev.L1_HTT100 and ev.SumCorHTPassed(thresh = 400.) and ev.pfMHTPassed(50.) and ev.OneMuonPassed():
        return True
    return False


#control triggers:
def HT400_Ele5(ev):
    if ev.L1_HTT100 and ev.SumCorHtPassed(thresh = 400.) and ev.Electrons is not None:
        for ele in ev.Electrons:
            if ele.ElectronPassed():
                return True
    return False

def HT400_Mu5(ev):
    if ev.L1_HTT100 and ev.SumCorHtPassed(thresh = 400.) and ev.OneMuonPassed():
        return True
    return False

def HT400_DoubleTau10(ev):
    if ev.L1_HTT100 and ev.SumCorHtPassed(thresh = 400.) and ev.pfTau is not None:
        taus = 0
        for t in ev.pfTau:
            if t.PFTauPassedNoMuonIDNoEleID(ev.UncorJets):
                taus+=1
        if taus>=2:
            return True
    return False


def PFMHT50_Ele5(ev):
    if ev.L1_ETM30 and ev.pfMHTPassed(50.) and ev.Electrons is not None:
        for ele in ev.Electrons:
            if ele.ElectronPassed():
                return True
        return False

def PFMHT50_Mu5(ev):
    if ev.L1_ETM30 and ev.pfMHTPassed(50.) and ev.OneMuonPassed():
        return True
    return False

def PFMHT50_DoubleTau10(ev):
    if ev.L1_ETM30 and ev.pfMHTPassed(50.) and ev.pfTau is not None:
        taus = 0
        for t in ev.pfTau:
            if t.PFTauPassedNoMuonIDNoEleID(ev.UnCorJets):
                taus+=1
        if taus>=2:
            return True
    return False

def HT400_PFMHT50(ev):
    if ev.L1_HTT100 and ev.pfMHTPassed(50.) and ev.SumCorHtPassed(thresh = 400.):
        return True
    return False
