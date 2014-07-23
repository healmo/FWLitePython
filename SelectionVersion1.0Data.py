import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from selectionFunction import myClass





multiJetFiles = open('/home/home2/institut_3b/almazan/MultiJetfiles.txt')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))



events = Events(multiJetFiles)
test = myClass(events,"DataHist")
test.selectionloop()
print 'Number of selected events is ',test.numberselectedevents, 'in a total of ',test.numbersignalevents,' events'
print "triggeredEvts ",test.numbertrigger
print "muonsEvts ",test.numbertotalmuons
print "jetsEvts ",test.numbertotaljets
print "btagEvts ",test.numbertotalbjets
