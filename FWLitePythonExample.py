import ROOT
from DataFormats.FWLite import Events,Handle
muonsLabel  = "muons"
muonsHandle = Handle("vector<reco::Muon>")
muonsPtHist = ROOT.TH1D("muonsPtHist","muonsPtHist",200,0,200)
muonsSizeHist = ROOT.TH1D("muonsSizeHist","# muons/event Hist",200,0,200)
####
events = Events('dcap://grid-dcap.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/data/Run2012A/MultiJet/AOD/22Jan2013-v1/20000/0036C47E-0B74-E211-B992-00266CF32684.root') #part of /MultiJet/Run2012A-22Jan2013-v1/AOD
###
for i,event in enumerate(events):
  event.getByLabel(muonsLabel,muonsHandle)
  muons = muonsHandle.product()
  muonsSizeHist.Fill(muons.size())
  for muon in muons:
    muonsPtHist.Fill(muon.pt())
  if i%100 == 0:
    print "processed ",i+1," events"
##############
muonsPtHist.SaveAs(muonsPtHist.GetName()+'.root')
muonsSizeHist.SaveAs(muonsSizeHist.GetName()+'.root')
