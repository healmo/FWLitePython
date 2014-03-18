import ROOT
from DataFormats.FWLite import Events,Handle
jetsLabel  = "ak5PFJets"
jetsHandle = Handle("vector<reco::PFJet>")
jetsPtHist = ROOT.TH1D("jetsPtHist","jetsPtHist",200,0,200)
jetsSizeHist = ROOT.TH1D("jetsSizeHist","# jets/event Hist",200,0,200)
####
#events = Events('dcap://grid-dcap.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/data/Run2012A/MultiJet/AOD/22Jan2013-v1/20000/0036C47E-0B74-E211-B992-00266CF32684.root') #part of /MultiJet/Run2012A-22Jan2013-v1/AOD which is data
events = Events('dcap://grid-dcap.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/7083D246-AA0A-E211-ADA5-001E67397F26.root') # part of /TTTT_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM
###
for i,event in enumerate(events):
  event.getByLabel(jetsLabel,jetsHandle)
  jets = jetsHandle.product()
  jetsSizeHist.Fill(jets.size())
  for jet in jets:
    jetsPtHist.Fill(jet.pt())
  if i%100 == 0:
    print "processed ",i+1," events"
scale = 1/jetsPtHist.Integral()
jetsPtHist.Scale(scale)
scale2 = 1/jetsSizeHist.Integral()
jetsSizeHist.Scale(scale2)
##############
#jetsPtHist.SaveAs(jetsPtHist.GetName()+'.root')
#jetsSizeHist.SaveAs(jetsSizeHist.GetName()+'.root')
jetsPtHist.SaveAs(jetsPtHist.GetName()+'_mc.root')
jetsSizeHist.SaveAs(jetsSizeHist.GetName()+'_mc.root')
