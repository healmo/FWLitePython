import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from selectionFunction import myClass

#---------------Information--From--TTTTMCFile------------------------------------------
events = Events('/user/Samples/TTTTJetsMC/TTTT_TuneZ2star_8TeV-madgraph-tauola_patTuple.root')

test = myClass(events,"TTTTHist")
test.selectionloop()

print "-----------------------------Selection-----------------------------------------"
print "Total Events ",test.numbersignalevents
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


#---------------Information--From--TTMCFile------------------------------------------
multiJetFiles = open('/user/almazan/CMSSW_5_3_16/FWLitePython/TTJetsMC.txt')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))




events = Events(multiJetFiles)

test = myClass(events,"TTHist")
test.selectionloop()


print "-----------------------------Selection,TTHist-----------------------------------------"
print "Total Events ",test.numbersignalevents
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



#---------------Information--From--TTMCFile------------------------------------------
multiJetFiles = open('/user/almazan/CMSSW_5_3_16/FWLitePython/TTJetsMCdilep.txt')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))




events = Events(multiJetFiles)

test = myClass(events,"TTHistdilep")
test.selectionloop()


print "-----------------------------Selection,TTHistdilep-----------------------------------------"
print "Total Events ",test.numbersignalevents
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

#---------------Information--From--TTMCFile------------------------------------------
multiJetFiles = open('/user/almazan/CMSSW_5_3_16/FWLitePython/TTJetsMCsemilep.txt')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))




events = Events(multiJetFiles)

test = myClass(events,"TTHistsemilep")
test.selectionloop()


print "-----------------------------Selection,TTHistsemilep-----------------------------------------"
print "Total Events ",test.numbersignalevents
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

#---------------Information--From--TTMCFile------------------------------------------
multiJetFiles = open('/user/almazan/CMSSW_5_3_16/FWLitePython/TTJetsMCfullhad.txt')
files=multiJetFiles.readlines()
multiJetFiles=[]
for f in files:
  multiJetFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))




events = Events(multiJetFiles)

test = myClass(events,"TTHistfullhad")
test.selectionloop()


print "-----------------------------Selection,TTHistfullhad-----------------------------------------"
print "Total Events ",test.numbersignalevents
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

