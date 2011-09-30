#!/usr/bin/env python
#small python analyser

import Event as e
import Helpers as h

def run(chain):
    for i in range(chain.GetEntries()):
        if i%1000==0:
            print 'Event: ' + str(i)
        chain.GetEntry(i)
        ev = e.Event(chain)
        # here you do whatever analysis etc.
        if ev.Electrons is not None:
            for ele in ev.Electrons:
                print ele.ElectronPassed()



if __name__=='__main__':
    elehad_path = "/vols/cms02/aeg04/HLTntup/r163374_2011A-v1/r163374_ElectronHad_2011A/"
    fname = 'openhlt_*.root'
    elehadfiles = h.file_get(elehad_path, fname)
    chain = h.getChain(elehadfiles, 'HltTree')
    run(chain)
