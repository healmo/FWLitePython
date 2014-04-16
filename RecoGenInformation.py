import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
import matchFunction as matchFunction
getMatchedParticle = matchFunction.getMatchedParticle
#def getMatchedParticle(genPart,collection):
#    resPart = collection[0]
#    resPartVec = TLorentzVector(resPart.px(),resPart.py(),resPart.pz(), resPart.energy())
#    genPartVec = TLorentzVector(genPart.px(),genPart.py(),genPart.pz(),genPart.energy())
#    deltaRDist = genPartVec.DeltaR( resPartVec )     
#    #print "deltaRDist ",deltaRDist
#    for part in collection:
#      tmpVec = TLorentzVector(part.px(),part.py(),part.pz(), part.energy())
#      tmpDeltaR = genPartVec.DeltaR(tmpVec)
#      if deltaRDist > tmpDeltaR:
#        resPart = part
#        resPartVec = tmpVec
#        deltaRDist = tmpDeltaR
#     #print "deltaRDist ",deltaRDist,' tmpDeltaR ',tmpDeltaR
#    return resPart



     
jetsLabel  = "ak5PFJets"
jetsHandle = Handle("vector<reco::PFJet>")
muonsRecoLabel  = "muons"
muonsRecoHandle = Handle("vector<reco::Muon>")
particlesGenLabel  = "genParticles"
particlesGenHandle = Handle("vector<reco::GenParticle>")

muonsRecoPtHist = ROOT.TH1D("muonsRecoPtHist","1 muon-momentum Reco",200,0,200)
twomuonsRecoPtHist = ROOT.TH1D("twomuonsRecoPtHist","2 muons-momentum Reco",200,0,200)
jetsRecoPtHist = ROOT.TH1D("jetsRecoPtHist","Jets-momentum (1Muon) Reco",200,0,200)
jetsDiRecoPtHist = ROOT.TH1D("jetsDiRecoPtHist","Jets-momentum (2Muons) Reco",200,0,200)

muonsGenPtHist = ROOT.TH1D("muonsGenPtHist","1 muon-momentum Gen",200,0,200)
twomuonsGenPtHist = ROOT.TH1D("twomuonsGenPtHist","2 muons-momentum Gen",200,0,200)
jetsGenPtHist = ROOT.TH1D("jetsGenPtHist","Jets-momentum (1Muon) Gen",200,0,200)
jetsDiGenPtHist = ROOT.TH1D("jetsDiGenPtHist","Jets-momentum (2Muons) Gen",200,0,200)

resPtmuonsHist = ROOT.TH1D("resPtmuonsHist","Resolution Momentum Reco-Gen 1 muon",200,0,1.5)
deltaRmuonsHist = ROOT.TH1D("deltaRmuonsHist","DeltaR Reco-Gen 1 muon",200,0,0.3)
resPtdimuonsHist = ROOT.TH1D("resPtdimuonsHist","Resolution Momentum Reco-Gen 2 muons",200,0,1.5)
deltaRdimuonsHist = ROOT.TH1D("deltaRdimuonsHist","DeltaR Reco-Gen 2 muons",200,0,0.3)


resPtjetsmuonsHist = ROOT.TH1D("resPtjetsmuonsHist","Resolution Momentum Reco-Gen Jets 1muon",200,0,1.5)
deltaRjetsmuonsHist = ROOT.TH1D("deltaRjetsmuonsHist","DeltaR Reco-Gen Jets 1 Muon",200,0,0.3)
resPtjetsdimuonsHist = ROOT.TH1D("resPtjetsdimuonsHist","Resolution Momentum Reco-Gen Jets 2 Muon",200,0,1.5)
deltaRjetsdimuonsHist = ROOT.TH1D("deltaRjetsdimuonsHist","DeltaR Reco-Gen Jets 2 Muon",200,0,0.3)


massdistHist = ROOT.TH1D("massdistHist","Mass Reconstructed Distribution",250,0,350)
resmassHist = ROOT.TH1D("resmassHist","Resolution Mass Reconstruction",200,0,1.5)
massjetdistHist = ROOT.TH1D("massjetdistHist","Mass Jet Reconstructed Distribution",900,0,900)
resmassjetHist = ROOT.TH1D("resmassjetHist","Resolution Mass obtained with Jets",200,0,1.5)
jetsmasssizeHist = ROOT.TH1D("jetsmasssizeHist","# Jets Recolected",10,0,20)

massdistdimuonsHist = ROOT.TH1D("massdistdimuonsHist","Mass Reconstructed Distribution",250,0,350)
resmassdimuonsHist = ROOT.TH1D("resmassdimuonsHist","Resolution Mass Reconstruction",200,0,1.5)
massjetdistdimuonsHist = ROOT.TH1D("massjetdistdimuonsHist","Mass Jet Reconstructed Distribution",900,0,900)
resmassjetdimuonsHist = ROOT.TH1D("resmassjetdimuonsHist","Resolution Mass obtained with Jets",200,0,1.5)
jetsmasssizedimuonsHist = ROOT.TH1D("jetsmasssizedimuonsHist","# Jets Recolected",10,0,20)


events = Events('/user/Samples/TTTTJetsMC/7083D246-AA0A-E211-ADA5-001E67397F26.root')


for i,event in enumerate(events):
  #if i == 200:
   # break
  if i%100 == 0:
    print "processed ",i+1," events"
  numberTopEvent = 0
  numbermuons = 0
  event.getByLabel(muonsRecoLabel,muonsRecoHandle)
  muons = muonsRecoHandle.product()
  event.getByLabel(particlesGenLabel,particlesGenHandle)
  particles = particlesGenHandle.product()
  event.getByLabel(jetsLabel,jetsHandle)
  jets = jetsHandle.product()
 
 
  fourTopGenParts=dict()
  tops=[]
  listjets=[]
  masslist=[]
  b1 = 0
  q11 = 0
  q12 = 0
  b2 = 0 
  q21 = 0
  q22 = 0
  b3 = 0 
  q31 = 0
  q32 = 0

  for jet in jets:
    jetsRecoPtHist.Fill(jet.pt())
    if jet.pt() >= 40.0:
      listjets.append(jet)

  for part in particles:
    if part.status() == 3:
      if math.fabs(part.pdgId()) == 6:
        tops.append(part)
  if not len(tops) == 4:
    print "attention no four tops found"
  fourTopGenParts["top1"]={"top":tops[0] }
  fourTopGenParts["top2"]={"top":tops[1] }
  fourTopGenParts["top3"]={"top":tops[2] }
  fourTopGenParts["top4"]={"top":tops[3] }
  for key in fourTopGenParts.keys():
   for part in particles:
      if part.status() == 3:        
        if math.fabs(part.pdgId()) == 5 and part.mother() == fourTopGenParts[key]["top"]: 
          fourTopGenParts[key]["bquark"] = part
        if math.fabs(part.pdgId()) == 24 and part.mother() == fourTopGenParts[key]["top"]: 
          fourTopGenParts[key]["W"] = part
   for part in particles:
     if part.status() == 3:
       if math.fabs(part.pdgId()) <= 5 and part.mother() == fourTopGenParts[key]["W"]:
         if not fourTopGenParts[key].has_key("quarks"):
           fourTopGenParts[key]["quarks"] = []
         fourTopGenParts[key]["quarks"].append(part)    
       if math.fabs(part.pdgId()) == 13 and part.mother() == fourTopGenParts[key]["W"]:
         fourTopGenParts[key]["muon"] = part


  countGenMuons=0
  for key in fourTopGenParts.keys():
    if fourTopGenParts[key].has_key("muon"):
      countGenMuons+=1
  for muon in muons:
    if countGenMuons == 2:
      twomuonsRecoPtHist.Fill(muon.pt())
    if countGenMuons == 1:
      muonsRecoPtHist.Fill(muon.pt())

  for key in fourTopGenParts.keys():
    if fourTopGenParts[key].has_key("muon"):
      if countGenMuons == 2:
        twomuonsGenPtHist.Fill(fourTopGenParts[key]["muon"].pt())
      if countGenMuons == 1:
        muonsGenPtHist.Fill(fourTopGenParts[key]["muon"].pt())
      muonGenVec = TLorentzVector(fourTopGenParts[key]["muon"].px(),fourTopGenParts[key]["muon"].py(),fourTopGenParts[key]["muon"].pz(),fourTopGenParts[key]["muon"].energy())
      if not muons.size() > 0:
        continue
      bestMuon = getMatchedParticle(fourTopGenParts[key]["muon"],muons)
      bestMuonVec = TLorentzVector(bestMuon.px(),bestMuon.py(),bestMuon.pz(), bestMuon.energy())
      deltaRDist = muonGenVec.DeltaR( bestMuonVec )     
      if deltaRDist < 0.3:
        fourTopGenParts[key]["recoMuon"] = bestMuon
        if countGenMuons == 2:
          deltaRdimuonsHist.Fill(deltaRDist) 
          resPtdimuonsHist.Fill(math.fabs(bestMuon.pt() - fourTopGenParts[key]["muon"].pt())/fourTopGenParts[key]["muon"].pt())
        if countGenMuons == 1:
          deltaRmuonsHist.Fill(deltaRDist) 
          resPtmuonsHist.Fill(math.fabs(bestMuon.pt() - fourTopGenParts[key]["muon"].pt())/fourTopGenParts[key]["muon"].pt())
            
   
    if fourTopGenParts[key].has_key("bquark"):
      bquarkGenVec = TLorentzVector(fourTopGenParts[key]["bquark"].px(),fourTopGenParts[key]["bquark"].py(),fourTopGenParts[key]["bquark"].pz(),fourTopGenParts[key]["bquark"].energy())
      bestbquark = getMatchedParticle(fourTopGenParts[key]["bquark"],jets)
      bestbquarkVec = TLorentzVector(bestbquark.px(),bestbquark.py(),bestbquark.pz(),bestbquark.energy())
      deltaRDist = bquarkGenVec.DeltaR( bestbquarkVec )     
      if deltaRDist < 0.3:
        fourTopGenParts[key]["recobquark"] = getMatchedParticle(fourTopGenParts[key]["bquark"],jets)


    if fourTopGenParts[key].has_key("quarks") and len(fourTopGenParts[key]["quarks"]) == 2:
      jetsGenPtHist.Fill(fourTopGenParts[key]["quarks"][0].pt())
      jetsGenPtHist.Fill(fourTopGenParts[key]["quarks"][1].pt())
      quarkoneGenVec = TLorentzVector(fourTopGenParts[key]["quarks"][0].px(),fourTopGenParts[key]["quarks"][0].py(),fourTopGenParts[key]["quarks"][0].pz(),fourTopGenParts[key]["quarks"][0].energy())
      bestquarkone = getMatchedParticle(fourTopGenParts[key]["quarks"][0],jets)
      bestbquarkoneVec = TLorentzVector(bestquarkone.px(),bestquarkone.py(),bestquarkone.pz(),bestquarkone.energy())
      deltaRDistOne = quarkoneGenVec.DeltaR(bestbquarkoneVec)     
      if deltaRDistOne < 0.3:
        fourTopGenParts[key]["recoQuarkOne"] = bestquarkone
        if countGenMuons == 1: 
          deltaRjetsmuonsHist.Fill(deltaRDistOne)
          print "test ",bestquarkone.pt()
	  print "test ",fourTopGenParts[key]["quarks"][0].pt()
          resPtjetsmuonsHist.Fill(math.fabs(bestquarkone.pt() - fourTopGenParts[key]["quarks"][0].pt())/fourTopGenParts[key]["quarks"][0].pt())
        if countGenMuons == 2: 
          deltaRjetsdimuonsHist.Fill(deltaRDistOne)
          resPtjetsdimuonsHist.Fill(math.fabs(bestquarkone.pt() - fourTopGenParts[key]["quarks"][0].pt())/fourTopGenParts[key]["quarks"][0].pt())


      quarkTwoGenVec = TLorentzVector(fourTopGenParts[key]["quarks"][1].px(),fourTopGenParts[key]["quarks"][1].py(),fourTopGenParts[key]["quarks"][1].pz(),fourTopGenParts[key]["quarks"][1].energy())
      bestquarktwo = getMatchedParticle(fourTopGenParts[key]["quarks"][1],jets)
      bestbquarktwoVec = TLorentzVector(bestquarktwo.px(),bestquarktwo.py(),bestquarktwo.pz(),bestquarktwo.energy())
      deltaRDistTwo = quarkTwoGenVec.DeltaR(bestbquarktwoVec)     
      if deltaRDistTwo < 0.3:
        fourTopGenParts[key]["recoQuarkTwo"] = bestquarktwo
        if countGenMuons == 1: 
          deltaRjetsmuonsHist.Fill(deltaRDistTwo)
          resPtjetsmuonsHist.Fill(math.fabs(bestquarktwo.pt() - fourTopGenParts[key]["quarks"][1].pt())/fourTopGenParts[key]["quarks"][1].pt())
        if countGenMuons == 2: 
          deltaRjetsdimuonsHist.Fill(deltaRDistTwo)
          resPtjetsdimuonsHist.Fill(math.fabs(bestquarktwo.pt() - fourTopGenParts[key]["quarks"][1].pt())/fourTopGenParts[key]["quarks"][1].pt())


    if fourTopGenParts[key].has_key("recoQuarkTwo") and fourTopGenParts[key].has_key("recoQuarkOne") and fourTopGenParts[key].has_key("recobquark"):
      b4Momentum = fourTopGenParts[key]["recobquark"].p4()
      q1_4Momentum = fourTopGenParts[key]["recoQuarkOne"].p4() 
      q2_4Momentum = fourTopGenParts[key]["recoQuarkTwo"].p4()
      if countGenMuons == 1:
        massdistHist.Fill((b4Momentum + q1_4Momentum + q2_4Momentum ).M())
        resmassHist.Fill(math.fabs((b4Momentum + q1_4Momentum + q2_4Momentum ).M()- 173.34)/173.34)
      if countGenMuons == 1:
        massdistdimuonsHist.Fill((b4Momentum + q1_4Momentum + q2_4Momentum ).M())
        resmassdimuonsHist.Fill(math.fabs((b4Momentum + q1_4Momentum + q2_4Momentum ).M()- 173.34)/173.34)
      for m in range(len(listjets)):
        if listjets[m] == fourTopGenParts[key]["recobquark"]:
          if b1 == 0: 
            b1 = m
            continue
          elif b2 == 0:
            b2 = m 
            continue
          elif b3 == 0:
            b3 = m 
            continue
        if listjets[m] == fourTopGenParts[key]["recoQuarkOne"]:
          if q11 == 0: 
            q11 = m
            continue
          elif q21 == 0:
            q21 = m 
            continue
          elif q31 == 0:
            q31 = m 
            continue
        if listjets[m] == fourTopGenParts[key]["recoQuarkTwo"]:
          if q12 == 0: 
            q12 = m
            continue
          elif q22 == 0:
            q22 = m 
            continue
          elif q32 == 0:
            q32 = m 
            continue

       
         
  
  for j in range(len(listjets)):
    
    for k in range(j+1,len(listjets)):
      for l in range(k+1,len(listjets)):
        if j == b1 and k == q11 and l == q12:
          continue
        if j == b2 and k == q21 and l == q22:
          continue
        if j == b3 and k == q31 and l == q32:
          continue
        masslist.append((listjets[j].p4()+listjets[k].p4()+listjets[l].p4()).M())
        
  mi = masslist[0]
  for t in range(len(masslist)):
    if t == 0:
      dif = math.fabs(172 - masslist[0])
      continue
    md = masslist[t]
    if math.fabs(md - 172) < dif:
      mf = masslist[t]
      dif = math.fabs(md - 172)
    if countGenMuons == 1:
      resmassjetHist.Fill(math.fabs(masslist[t]-172))
    if countGenMuons == 2:
      resmassjetdimuonsHist.Fill(math.fabs(masslist[t]-172))

  if countGenMuons == 1:
    massjetdistHist.Fill(mf)
    jetsmasssizeHist.Fill(len(listjets))
  if countGenMuons == 2:
    massjetdistdimuonsHist.Fill(mf)
    jetsmasssizedimuonsHist.Fill(len(listjets))



scale = 1/muonsRecoPtHist.Integral()
muonsRecoPtHist.Scale(scale)
scale = 1/muonsGenPtHist.Integral()
muonsGenPtHist.Scale(scale)
scale = 1/twomuonsRecoPtHist.Integral()
twomuonsRecoPtHist.Scale(scale)
scale = 1/twomuonsGenPtHist.Integral()
twomuonsGenPtHist.Scale(scale)

scale = 1/resPtmuonsHist.Integral()
resPtmuonsHist.Scale(scale)
scale = 1/deltaRmuonsHist.Integral()
deltaRmuonsHist.Scale(scale)

scale = 1/resPtdimuonsHist.Integral()
resPtdimuonsHist.Scale(scale)
scale = 1/deltaRdimuonsHist.Integral()
deltaRdimuonsHist.Scale(scale)

scale = 1/jetsGenPtHist.Integral()
jetsGenPtHist.Scale(scale)
scale = 1/jetsRecoPtHist.Integral()
jetsRecoPtHist.Scale(scale)

scale = 1/deltaRjetsmuonsHist.Integral()
deltaRjetsmuonsHist.Scale(scale)
scale = 1/resPtjetsmuonsHist.Integral()
resPtjetsmuonsHist.Scale(scale)
scale = 1/deltaRjetsdimuonsHist.Integral()
deltaRjetsdimuonsHist.Scale(scale)
scale = 1/resPtjetsdimuonsHist.Integral()
resPtjetsdimuonsHist.Scale(scale)


scale = 1/massdistHist.Integral()
massdistHist.Scale(scale)
scale = 1/resmassHist.Integral()
resmassHist.Scale(scale)
scale = 1/massjetdistHist.Integral()
massjetdistHist.Scale(scale)
scale = 1/resmassjetHist.Integral()
resmassjetHist.Scale(scale)
scale = 1/jetsmasssizeHist.Integral()
jetsmasssizeHist.Scale(scale)

scale = 1/massdistdimuonsHist.Integral()
massdistdimuonsHist.Scale(scale)
scale = 1/resmassdimuonsHist.Integral()
resmassdimuonsHist.Scale(scale)
scale = 1/massjetdistdimuonsHist.Integral()
massjetdistdimuonsHist.Scale(scale)
scale = 1/resmassjetdimuonsHist.Integral()
resmassjetHist.Scale(scale)
scale = 1/jetsmasssizedimuonsHist.Integral()
jetsmasssizedimuonsHist.Scale(scale)







##############Save:
twomuonsRecoPtHist.SaveAs(twomuonsRecoPtHist.GetName()+'_mc.root')
twomuonsGenPtHist.SaveAs(twomuonsGenPtHist.GetName()+'_mc.root')
resPtdimuonsHist.SaveAs(resPtdimuonsHist.GetName()+'_mc.root')
deltaRdimuonsHist.SaveAs(deltaRdimuonsHist.GetName()+'_mc.root')

jetsGenPtHist.SaveAs(jetsGenPtHist.GetName()+'_mc.root')
jetsRecoPtHist.SaveAs(jetsRecoPtHist.GetName()+'_mc.root')
deltaRjetsHist.SaveAs(deltaRjetsHist.GetName()+'_mc.root')
resPtjetsHist.SaveAs(resPtjetsHist.GetName()+'_mc.root')

massdistHist.SaveAs(massdistHist.GetName()+'_mc.root')
resmassHist.SaveAs(resmassHist.GetName()+'_mc.root')
massjetdistHist.SaveAs(massjetdistHist.GetName()+'_mc.root')
resmassjetHist.SaveAs(resmassjetHist.GetName()+'_mc.root')
jetsmasssizeHist.SaveAs(jetsmasssizeHist.GetName()+'_mc.root')


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


filediRecoMC = ROOT.TFile("twomuonsRecoPtHist_mc.root")
filediGenMC = ROOT.TFile("twomuonsGenPtHist_mc.root")
c2 = ROOT.TCanvas("c2","Muon Pt",200,10,700,500)
TwoMuonRecoPt = filediRecoMC.Get("twomuonsRecoPtHist")
TwoMuonGenPt = filediGenMC.Get("twomuonsGenPtHist")
TwoMuonGenPt.SetLineColor(ROOT.kRed)
TwoMuonRecoPt.Draw()
TwoMuonGenPt.Draw("sames")
c2.SaveAs("twomuonsPtHist_Reco_vs_Gen.root")
c2.cd()

fileJRecoMC = ROOT.TFile("jetsRecoPtHist_mc.root")
fileJGenMC = ROOT.TFile("jetsGenPtHist_mc.root")
c3 = ROOT.TCanvas("c3","Jets Pt",200,10,700,500)
JetsRecoPt = fileJRecoMC.Get("jetsRecoPtHist")
JetsGenPt = fileJGenMC.Get("jetsGenPtHist")
JetsGenPt.SetLineColor(ROOT.kRed)
JetsRecoPt.Draw()
JetsGenPt.Draw("sames")
c3.SaveAs("jetsPtHist_Reco_vs_Gen.root")
c3.cd()

filemassMC = ROOT.TFile("massdistHist_mc.root")
filemassJMC = ROOT.TFile("massjetdistHist_mc.root")
c4 = ROOT.TCanvas("c4","JMass distribution",200,10,700,500)
Massdist = filemassMC.Get("massdistHist")
Massjetdist = filemassJMC.Get("massdistjetHist")
Massjetdist.SetLineColor(ROOT.kRed)
Massdist.Draw()
Massjetdist.Draw("sames")
c4.SaveAs("massHist_Matched_vs_NotMatched.root")
c4.cd()


