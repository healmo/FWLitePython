print "starting"
import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from selectionFunction import myClass




#multiJetFiles = open('/user/almazan/SingleMu__Run2012A-22Jan2013-v1__AOD_gridOutputFiles.txt')
#multiJetFiles = open('/home/home2/institut_3b/almazan/SingleMu.txt')

#---------------Information--From--DataRunA------------------------------------------
multiJetFiles = open('/user/almazan/CMSSW_5_3_16/FWLitePython/SingleMu_SoftJetSkim.txt')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))



print "before creating Events"
events = Events(multiJetFiles)
print "after creating Events"
test = myClass(events,"DataHistRunA")
test.selectionloop()
print "-----------------------------Selection-----------------------------------------"
print "triggeredEvts ",test.numbertrigger
print "muonsEvts ",test.numbertotalmuons
print '---6jets Criteria------'
print "jetsEvts ",test.numbertotalsixjets
print "wmasscriteria ",test.wmassselected
print '---7jets Criteria------'
print "jetsEvts ",test.numbertotalsevenjets
print "jetsEvts+highenergetic",test.numbertotalsevenjetsmomentum
print "jetsEvts + Wmass criteria ",test.wmassselected7 
print "Number Comb Jets ",test.totaljetcombevents

test.jetsmomentumbefore.SaveAs(test.jetsmomentumbefore.GetName()+'_mc.root')
test.jetsmomentumafter.SaveAs(test.jetsmomentumafter.GetName()+'_mc.root')
test.numberjetsBeforeDataHist.SaveAs(test.numberjetsBeforeDataHist.GetName()+'_mc.root')
test.numberjetsAfterDataHist.SaveAs(test.numberjetsAfterDataHist.GetName()+'_mc.root')
test.wmassdistribution.SaveAs(test.wmassdistribution.GetName()+'.root')
test.topmassdistribution.SaveAs(test.topmassdistribution.GetName()+'.root')
test.cutprocess.SaveAs(test.cutprocess.GetName()+'.root')
test.vtxSizeHist.SaveAs(test.vtxSizeHist.GetName()+'.root')


#---------------Information--From--DataRunB------------------------------------------
multiJetFiles = open('/user/almazan/CMSSW_5_3_16/FWLitePython/SingleMuRunB.text')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))




events = Events(multiJetFiles)
test = myClass(events,"DataHistRunB")
test.selectionloop()
print "-----------------------------Selection-----------------------------------------"
print "triggeredEvts ",test.numbertrigger
print "muonsEvts ",test.numbertotalmuons
print '---6jets Criteria------'
print "jetsEvts ",test.numbertotalsixjets
print "wmasscriteria ",test.wmassselected
print '---7jets Criteria------'
print "jetsEvts ",test.numbertotalsevenjets
print "jetsEvts+highenergetic",test.numbertotalsevenjetsmomentum
print "jetsEvts + Wmass criteria ",test.wmassselected7 
print "Number Comb Jets ",test.totaljetcombevents

test.jetsmomentumbefore.SaveAs(test.jetsmomentumbefore.GetName()+'_mc.root')
test.jetsmomentumafter.SaveAs(test.jetsmomentumafter.GetName()+'_mc.root')
test.numberjetsBeforeDataHist.SaveAs(test.numberjetsBeforeDataHist.GetName()+'_mc.root')
test.numberjetsAfterDataHist.SaveAs(test.numberjetsAfterDataHist.GetName()+'_mc.root')
test.wmassdistribution.SaveAs(test.wmassdistribution.GetName()+'.root')
test.topmassdistribution.SaveAs(test.topmassdistribution.GetName()+'.root')
test.cutprocess.SaveAs(test.cutprocess.GetName()+'.root')
test.vtxSizeHist.SaveAs(test.vtxSizeHist.GetName()+'.root')
