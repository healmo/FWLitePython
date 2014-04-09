import ROOT,math
from DataFormats.FWLite import Events,Handle
muonsRecoLabel  = "muons"
muonsRecoHandle = Handle("vector<reco::Muon>")
muonsRecoPtHist = ROOT.TH1D("muonsRecoPtHist","muon-momentum Reco",80,0,80)
particlesGenLabel  = "genParticles"
particlesGenHandle = Handle("vector<reco::GenParticle>")
muonsGenPtHist = ROOT.TH1D("muonsGenPtHist","muon-momentum Gen",200,0,200)

events = Events('/user/Samples/TTTTJetsMC/7083D246-AA0A-E211-ADA5-001E67397F26.root')


for i,event in enumerate(events):
  event.getByLabel(muonsRecoLabel,muonsRecoHandle)
  muons = muonsRecoHandle.product()
  event.getByLabel(particlesGenLabel,particlesGenHandle)
  particles = particlesGenHandle.product()
#cojo las informacion de los muones(sacados de reco::Muon)
  for muon in muons:
    muonsRecoPtHist.Fill(muon.pt())
#busco los muones en genParticle y tomo el momento de dichos muones
  for part in particles:
    if part.status() == 3:
      if math.fabs(part.pdgId()) == 13:
        muonsGenPtHist.Fill(part.pt()) 
  if i%100 == 0:
    print "processed ",i+1," events"
scale = 1/muonsRecoPtHist.Integral()
muonsRecoPtHist.Scale(scale)
scale = 1/muonsGenPtHist.Integral()
muonsGenPtHist.Scale(scale)



##############Save:

muonsRecoPtHist.SaveAs(muonsRecoPtHist.GetName()+'_mc.root')
muonsGenPtHist.SaveAs(muonsGenPtHist.GetName()+'_mc.root')

fileRecoMC = ROOT.TFile("muonsRecoPtHist_mc.root")
fileGenMC = ROOT.TFile("muonsGenPtHist_mc.root")


c1 = ROOT.TCanvas("c1","Muon Pt",200,10,700,500)
MuonRecoPt = fileRecoMC.Get("muonsRecoPtHist")
MuonGenPt = fileGenMC.Get("muonsGenPtHist")
MuonGenPt.SetLineColor(ROOT.kRed)
MuonRecoPt.Draw()
MuonGenPt.Draw("sames")
c1.SaveAs("muonPtHist_Reco_vs_Gen.root")
c1.cd()

