#!/usr/bin/env python
#small python analyser

import Event as e
import Helpers as h
import AGB_TriggerPaths as trigs

def run(chain, path = None):
    r = chain.GetEntries()
    # path_sets={'MET':[], 'TauX':[], 'EleHad':[], 'MuHad':[], 'HT':[]}
    path_sets={}
    path_sets['MET'] = {'pfmht50_ele5':trigs.PFMHT50_Ele5, 'pfmht50_mu5':trigs.PFMHT50_Mu5,
                      'pfmht50_doubleTau':trigs.PFMHT50_DoubleTau10}
    path_sets['HT'] = {'ht400_pfmht50':trigs.HT400_PFMHT50}
    path_sets['EleHad'] = {'ht400_ele5_pfmht50':trigs.HT400_DoubleTau10_PFMHT50, 'ht400_ele5':trigs.HT400_Ele5}
    path_sets['MuHad'] = {'ht400_mu5_pfmht50':trigs.HT400_Mu5_PFMHT50, 'ht400_mu5':trigs.HT400_Mu5}
    path_sets['TauX'] = {'ht400_doubleTau_pfmht50':trigs.HT400_DoubleTau10_PFMHT50, 'ht400_doubleTau':trigs.HT400_DoubleTau10,
                         'pfmht50_doubleTau':trigs.PFMHT50_DoubleTau10}
    
    if path not in path_sets.keys():
        import sys
        'Print: You\'ve asked for a set of paths that are not defined'
        sys.exit(1)
    print "Running " + path + " type paths."

    

    
    for i in range(r):
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
    run(mhtchain, path = 'MET')
    
