import ROOT
from DataFormats.FWLite import Events,Handle
muonsLabel  = "muons"
muonsHandle = Handle("vector<reco::Muon>")
muonsPtHist = ROOT.TH1D("muonsPtHist","muonsPtHist",200,0,200)
####
events = Events('dcap://grid-dcap.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/data/Run2012A/MultiJet/AOD/22Jan2013-v1/20000/0036C47E-0B74-E211-B992-00266CF32684.root') #part of /MultiJet/Run2012A-22Jan2013-v1/AOD which is data
#events = Events('dcap://grid-dcap.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/7083D246-AA0A-E211-ADA5-001E67397F26.root') # part of /TTTT_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM
###
for i,event in enumerate(events):
  event.getByLabel(muonsLabel,muonsHandle)
  muons = muonsHandle.product()
  for muon in muons:
    muonsPtHist.Fill(muon.pt())
  if i%100 == 0:
    print "processed ",i+1," events"
##############
muonsPtHist.SaveAs(muonsPtHist.GetName()+'.root')
