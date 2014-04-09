import ROOT,math
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
muonsRecoLabel  = "muons"
muonsRecoHandle = Handle("vector<reco::Muon>")
muonsRecoPtHist = ROOT.TH1D("muonsRecoPtHist","muon-momentum Reco",80,0,80)
particlesGenLabel  = "genParticles"
particlesGenHandle = Handle("vector<reco::GenParticle>")
muonsGenPtHist = ROOT.TH1D("muonsGenPtHist","muon-momentum Gen",200,0,200)
lepton = 0
resPtHist = ROOT.TH1D("resPtHist","Resolution Momentum Reco-Gen",200,0,1.5)
deltaRHist = ROOT.TH1D("deltaRHist","DeltaR Reco-Gen",200,0,0.3)
events = Events('/user/Samples/TTTTJetsMC/7083D246-AA0A-E211-ADA5-001E67397F26.root')


for i,event in enumerate(events):

  numberTopEvent = 0
  numbermuons = 0
  event.getByLabel(muonsRecoLabel,muonsRecoHandle)
  muons = muonsRecoHandle.product()
  event.getByLabel(particlesGenLabel,particlesGenHandle)
  particles = particlesGenHandle.product()
  v1Gen = TLorentzVector(0,0,0,0)
#Primero seleccion solo los eventos que tenga 1 muon, asi me aseguro que el momento que estoy cogiendo
#es el de la misma particula (ademas de que es mas sencillo)

  for part in particles:
    if part.status() == 3:
      if math.fabs(part.pdgId()) == 6:
		  numberTopEvent += 1
      elif math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) == 24:
        numbermuons += 1   
  
  if numberTopEvent == 4 and numbermuons == 1:
    lepton += 1
    for muon in muons:
      v1 = TLorentzVector(muon.px(),muon.py(),muon.pz(), muon.energy())
    for part in particles:
      if part.status() == 3:
        if math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) == 24:
          v2 = TLorentzVector(part.px(),part.py(),part.pz(),part.energy())
    if v1.DeltaR(v2) < 0.3:
      deltaRHist.Fill(v1.DeltaR(v2))
      for muon in muons:
        muonsRecoPtHist.Fill(muon.pt())
        muonRecoPt = muon.pt()
      for part in particles:
        if part.status() == 3:
          if math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) == 24:
            muonsGenPtHist.Fill(part.pt()) 
            muonGenPt = part.pt()
      resPtHist.Fill(math.fabs(muonRecoPt - muonGenPt)/math.fabs(muonGenPt))


  elif numberTopEvent == 4 and numbermuons == 2:
    print "EventoNo",i,"con ",numbermuons,"muones"
    for part in particles:
      if part.status() == 3:
        if math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) == 24:
          if v1Gen == TLorentzVector(0,0,0,0):
            v1Gen = TLorentzVector(part.px(),part.py(),part.pz(),part.energy())
          else:
            v2Gen = TLorentzVector(part.px(),part.py(),part.pz(),part.energy())
    for muon in muons:
      vReco = TLorentzVector(muon.px(),muon.py(),muon.pz(), muon.energy())
      if v1Gen.DeltaR(vReco) < 0.3 or v2Gen.DeltaR(vReco) < 0.3:
        print "Conseguido!!", v1Gen.DeltaR(vReco),v2Gen.DeltaR(vReco) #Aqui tengo que anadir lo de rellenar los histogramas

  if i == 50:
   break

  if i%100 == 0:
    print "processed ",i+1," events"

scale = 1/muonsRecoPtHist.Integral()
muonsRecoPtHist.Scale(scale)
scale = 1/muonsGenPtHist.Integral()
muonsGenPtHist.Scale(scale)



##############Save:
print 'Number1MuonEvents=',lepton
muonsRecoPtHist.SaveAs(muonsRecoPtHist.GetName()+'_mc.root')
muonsGenPtHist.SaveAs(muonsGenPtHist.GetName()+'_mc.root')
resPtHist.SaveAs(resPtHist.GetName()+'_mc.root')
deltaRHist.SaveAs(deltaRHist.GetName()+'_mc.root')

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

