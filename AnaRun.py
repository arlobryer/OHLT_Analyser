#!/usr/bin/env python
#small python analyser
import ROOT as r
import Event as e
import Helpers as h
import AGB_TriggerPaths as trigs
import os

def run(chain, path = None):
    Ents = chain.GetEntries()
    path_sets={}
    file_out = './AGB_ssdl_trigEff.root'
    path_sets['MET'] = {'pfmht50_ele5':trigs.PFMHT50_Ele5, 'pfmht50_mu5':trigs.PFMHT50_Mu5,
                      'pfmht50_doubleTau':trigs.PFMHT50_DoubleTau10}
    path_sets['HT'] = {'ht400_pfmht50':trigs.HT400_PFMHT50}
    path_sets['EleHad'] = {'ht400_ele5_pfmht50':trigs.HT400_DoubleTau10_PFMHT50, 'ht400_ele5':trigs.HT400_Ele5}
    path_sets['MuHad'] = {'ht400_mu5_pfmht50':trigs.HT400_Mu5_PFMHT50, 'ht400_mu5':trigs.HT400_Mu5}
    path_sets['TauX'] = {'ht400_doubleTau_pfmht50':trigs.HT400_DoubleTau10_PFMHT50, 'ht400_doubleTau':trigs.HT400_DoubleTau10,
                         'pfmht50_doubleTau':trigs.PFMHT50_DoubleTau10}
    
    if path not in path_sets.keys():
        import sys
        'Print: You\'ve asked for a set of paths that are not defined.'
        sys.exit(1)
    print "Running " + path + " type paths."

    #Some messing around with the ROOT file/hists. Should ultimately be in
    #it's own class.
    if os.path.exists(file_out):
        print 'Output file already exists. Opening it and updating contents.'
        f_trig_eff = r.TFile(file_out, 'update')
    else:
        print 'Creating new output file.'
        f_trig_eff = r.TFile(file_out, 'create')
        for p in path_sets.keys():
            f_trig_eff.mkdir(p)

    #histograms
    #MET ds
    pfmht50_ele5_ht = r.TH1D('pfmht50_ele5_ht', 'pfmht50_ele5_ht', 600, 0, 600)
    pfmht50_mu5_ht = r.TH1D('pfmht50_mu5_ht', 'pfmht50_mu5_ht', 600, 0, 600)
    pfmht50_doubTau_ht = r.TH1D('pfmht50_doubTau_ht', 'pfmht50_doubTau_ht', 600, 0, 600)
    #HT ds
    ht400_pfmht50_ePt = r.TH1D('ht400_pfmht50_ePt', 'ht400_pfmht50_ePt', 200, 0, 200)
    ht400_pfmht50_mPt = r.TH1D('ht400_pfmht50_mPt', 'ht400_pfmht50_mPt', 200, 0, 200)
    ht400_pfmht50_tPt = r.TH1D('ht400_pfmht50_tPt', 'ht400_pfmht50_tPt', 200, 0, 200)
    #EleHad
    ht400_ele5_pfmht50_ht = r.TH1D('ht400_ele5_pfmht50_ht', 'ht400_ele5_pfmht50_ht', 600, 0, 600)
    ht400_ele5_pfmht50_ePt = r.TH1D('ht400_ele5_pfmht50_ePt', 'ht400_ele5_pfmht50_ePt', 200, 0, 200)
    ht400_ele5_pfmht50_mht = r.TH1D('ht400_ele5_pfmht50_mht', 'ht400_ele5_pfmht50_mht', 200, 0, 200)
    ht400_ele5_mht = r.TH1D('ht400_ele5_mht', 'ht400_ele5_mht', 200, 0, 200)
    #MuHad
    ht400_mu5_pfmht50_ht = r.TH1D('ht400_mu5_pfmht50_ht', 'ht400_mu5_pfmht50_ht', 600, 0, 600)
    ht400_mu5_pfmht50_mPt = r.TH1D('ht400_mu5_pfmht50_mPt', 'ht400_mu5_pfmht50_mPt', 200, 0, 200)
    ht400_mu5_pfmht50_mht = r.TH1D('ht400_mu5_pfmht50_mht', 'ht400_mu5_pfmht50_mht', 200, 0, 200)
    ht400_mu5_mht = r.TH1D('ht400_mu5_mht', 'ht400_mu5_mht', 200, 0, 200)
    #tauX
    ht400_doubTau_pfmht50_ht = r.TH1D('ht400_doubTau_pfmht50_ht', 'ht400_doubTau_pfmht50_ht',
                                      600, 0, 600)
    ht400_doubTau_pfmht50_tPt = r.TH1D('ht400_doubTau_pfmht50_tPt', 'ht400_doubTau_pfmht50_tPt',
                                       200, 0, 200)
    ht400_doubTau_pfmht50_mht = r.TH1D('ht400_doubTau_pfmht50_mht', 'ht400_doubTau_pfmht50_mht',
                                       100, 0, 100)
    ht400_doubTau_mht = r.TH1D('ht400_doubTau_mht', 'ht400_doubTau_mht', 100, 0, 100)
    
            

    #Start event loop.
    for i in range(Ents):
        if i%1000==0:
            print 'Event: ' + str(i)
        chain.GetEntry(i)
        ev = e.Event(chain)

        # here you do whatever analysis etc
        for name, p in path_sets[path].iteritems():
            if p(ev):
                print i
                if name == 'pfmht50_doubleTau':
                    print name + ' ' + str(p(ev))
        
        
            
        # if paths == 'HT':
        #     print HT400_PFMHT50()

        # if paths == 'MuHad':
        #     print HT400_Mu5()

        # if paths == 'EleHad':
        #     print HT400_Ele5()

        # if paths == 'TauX':
        #     print HT400_DoubleTau10()
        #     print PFMHT50_DoubleTau10()
        
        
                    


if __name__=='__main__':
    elehad_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_ElectronHad_2011A/"
    muhad_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_MuHad_2011A/"
    tauX_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_TauPlusX_2011A/"
    ht_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_HT_2011A/"
    mht_path = "/vols/cms03/aeg04/HLTntup_r165970/"
    fname = 'openhlt_*.root'
    elehadfiles = h.file_get(elehad_path, fname)
    muhadfiles = h.file_get(muhad_path, fname)
    tauXfiles = h.file_get(tauX_path, fname)
    htfiles = h.file_get(ht_path, fname)
    mhtfiles = h.file_get(mht_path, fname)
    
    Elechain = h.getChain(elehadfiles, 'HltTree')
    Muchain = h.getChain(muhadfiles, 'HltTree')
    tauXchain = h.getChain(tauXfiles, 'HltTree')
    htchain = h.getChain(htfiles, 'HltTree')
    mhtchain = h.getChain(mhtfiles, 'HltTree')
    
    # run(Elechain, paths = 'EleHad')
    run(Elechain, path = 'EleHad')
    
