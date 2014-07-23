import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
import matchFunction as matchFunction
getMatchedParticle = matchFunction.getMatchedParticle


     
jetsLabel  = "selectedPatJetsPFlow"
jetsHandle = Handle("vector<pat::Jet>")
muonsRecoLabel  = "selectedPatMuonsPFlow"
muonsRecoHandle = Handle("vector<pat::Muon>")
particlesGenLabel  = "genParticles"
particlesGenHandle = Handle("vector<reco::GenParticle>")

muonsRecoPtHist = ROOT.TH1D("muonsRecoPtHist","1 muon-momentum Reco",200,0,200)
twomuonsRecoPtHist = ROOT.TH1D("twomuonsRecoPtHist","2 muons-momentum Reco",200,0,200)
jetsRecoPtHist = ROOT.TH1D("jetsRecoPtHist","Jets-momentum (1Muon) Reco",200,0,200)
jetsDiRecoPtHist = ROOT.TH1D("jetsDiRecoPtHist","Jets-momentum (2Muons) Reco",200,0,200)

muonsGenPtHist = ROOT.TH1D("muonsGenPtHist","1 muon-momentum Gen",200,0,200)
twomuonsGenPtHist = ROOT.TH1D("twomuonsGenPtHist","2 muons-momentum Gen",200,0,200)
jetsGenPtHist = ROOT.TH1D("jetsGenPtHist","Jets-momentum (1Muon) Gen",200,0,200)
jetsDiGenPtHist = ROOT.TH1D("jetsDiGenPtHist","JetFjs-momentum (2Muons) Gen",200,0,200)

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

massdistdimuonsHist = ROOT.TH1D("massdistdimuonsHist","Invariant Mass Reconstruced Distribution",250,0,350)
resmassdimuonsHist = ROOT.TH1D("resmassdimuonsHist","Resolution Mass Reconstruction",200,0,1.5)
massjetdistdimuonsHist = ROOT.TH1D("massjetdistdimuonsHist","Mass Jet Reconstructed Distribution",900,0,900)
resmassjetdimuonsHist = ROOT.TH1D("resmassjetdimuonsHist","Resolution Mass obtained with Jets",200,0,1.5)
jetsmasssizedimuonsHist = ROOT.TH1D("jetsmasssizedimuonsHist","# Jets Recolected",10,0,20)

bjetsDiscriminatorHist = ROOT.TH1D("bjetsDiscriminatorHist","bDiscriminator Value",10,0,1)
quarksjetsDiscriminatorHist = ROOT.TH1D("quarksjetsDiscriminatorHist","bDiscriminator Value",10,0,1)

####################################
recJetPtHist = ROOT.TH1D("recJetPtHist","pt recojets",200,0,200)
genGenPtHist = ROOT.TH1D("genGenPtHist","pt genjets",200,0,200)
recMuonsPtHist = ROOT.TH1D("recMuonsPtHist","pt recojets",200,0,200)
genMuonsPtHist = ROOT.TH1D("genMuonsPtHist","pt genjets",200,0,200)
####################################

events = Events('/user/Samples/TTTTJetsMC/TTTT_TuneZ2star_8TeV-madgraph-tauola_patTuple.root')
oneMuonRestHadevts=0
diMuonicRestHadFourTopEvts = 0
nonOneOrDiMuonRestHadEvts = 0
allHadronicFourTopEvts = 0
for i,event in enumerate(events):
  #if i == 200:
    #break
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
       if (math.fabs(part.pdgId()) == 11 or math.fabs(part.pdgId()) == 15) and part.mother() == fourTopGenParts[key]["W"]:
         fourTopGenParts[key]["nonMuonLep"] = part 
  ########### event charaterisation
  countGenMuons=0
  counthadTopDecay = 0
  countGenLepNonMuon = 0
  for key in fourTopGenParts.keys():
    if fourTopGenParts[key].has_key("muon"):
      countGenMuons+=1
    if fourTopGenParts[key].has_key("quarks") and len(fourTopGenParts[key]["quarks"]) == 2:
      counthadTopDecay+=1
    if fourTopGenParts[key].has_key("nonMuonLep"):
      countGenLepNonMuon+=1
  ########### cheching branching ratios
  if countGenMuons ==1 and counthadTopDecay == 3:
    oneMuonRestHadevts+=1
  elif countGenMuons ==2 and counthadTopDecay == 2:
    diMuonicRestHadFourTopEvts+=1
  elif counthadTopDecay == 4:
    allHadronicFourTopEvts+=1
  else:
    nonOneOrDiMuonRestHadEvts+=1
  if counthadTopDecay > 4 or  countGenMuons > 4:
    print "wupsi"
  #####
  for muon in muons:
    if countGenMuons == 2:
      twomuonsRecoPtHist.Fill(muon.pt())
    if countGenMuons == 1:
      muonsRecoPtHist.Fill(muon.pt())
  ############################## reco jets vs gen for 2 muonic 4 top events
  if countGenMuons == 2 and counthadTopDecay == 2:
    for jet in jets:
      recJetPtHist.Fill(jet.pt())
    for muon in muons:
      recMuonsPtHist.Fill(muon.pt())
    countHadTops = 0
    for key in fourTopGenParts.keys():
      if fourTopGenParts[key].has_key("quarks") and len(fourTopGenParts[key]["quarks"]) == 2:
        genGenPtHist.Fill(fourTopGenParts[key]["quarks"][0].pt())
        genGenPtHist.Fill(fourTopGenParts[key]["quarks"][1].pt())
      if fourTopGenParts[key].has_key("bquark"):
        genGenPtHist.Fill(fourTopGenParts[key]["bquark"].pt())
      if fourTopGenParts[key].has_key("muon"):
        genMuonsPtHist.Fill(fourTopGenParts[key]["muon"].pt())
  ##################################   
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
      bvalue = getMatchedParticle(fourTopGenParts[key]["bquark"],jets).bDiscriminator("combinedSecondaryVertexBJetTags")
      bjetsDiscriminatorHist.Fill(bvalue) 
      if deltaRDist < 0.3 and bestbquark.bDiscriminator("combinedSecondaryVertexBJetTags") > 0.5:
        fourTopGenParts[key]["recobquark"] = getMatchedParticle(fourTopGenParts[key]["bquark"],jets)


    if fourTopGenParts[key].has_key("quarks") and len(fourTopGenParts[key]["quarks"]) == 2:
      jetsGenPtHist.Fill(fourTopGenParts[key]["quarks"][0].pt())
      jetsGenPtHist.Fill(fourTopGenParts[key]["quarks"][1].pt())
      quarkoneGenVec = TLorentzVector(fourTopGenParts[key]["quarks"][0].px(),fourTopGenParts[key]["quarks"][0].py(),fourTopGenParts[key]["quarks"][0].pz(),fourTopGenParts[key]["quarks"][0].energy())
      bestquarkone = getMatchedParticle(fourTopGenParts[key]["quarks"][0],jets)
      bestbquarkoneVec = TLorentzVector(bestquarkone.px(),bestquarkone.py(),bestquarkone.pz(),bestquarkone.energy())
      deltaRDistOne = quarkoneGenVec.DeltaR(bestbquarkoneVec)     
      if bestquarkone.bDiscriminator("combinedSecondaryVertexBJetTags") > 0:
        quarkonevalue = bestquarkone.bDiscriminator("combinedSecondaryVertexBJetTags")
        quarksjetsDiscriminatorHist.Fill(quarkonevalue)
      if deltaRDistOne < 0.3:
#and bestquarkone.bDiscriminator("combinedSecondaryVertexBJetTags") < 0.5:
        fourTopGenParts[key]["recoQuarkOne"] = bestquarkone
        if countGenMuons == 1: 
          deltaRjetsmuonsHist.Fill(deltaRDistOne)
          resPtjetsmuonsHist.Fill(math.fabs(bestquarkone.pt() - fourTopGenParts[key]["quarks"][0].pt())/fourTopGenParts[key]["quarks"][0].pt())
        if countGenMuons == 2: 
          deltaRjetsdimuonsHist.Fill(deltaRDistOne)
          resPtjetsdimuonsHist.Fill(math.fabs(bestquarkone.pt() - fourTopGenParts[key]["quarks"][0].pt())/fourTopGenParts[key]["quarks"][0].pt())
          #print 'quark1', fourTopGenParts[key]["quarks"][0].pt()
          jetsDiGenPtHist.Fill(fourTopGenParts[key]["quarks"][0].pt())
          #print 'recoquark1',fourTopGenParts[key]["recoQuarkOne"].pt()
          jetsDiRecoPtHist.Fill(fourTopGenParts[key]["recoQuarkOne"].pt())


      quarkTwoGenVec = TLorentzVector(fourTopGenParts[key]["quarks"][1].px(),fourTopGenParts[key]["quarks"][1].py(),fourTopGenParts[key]["quarks"][1].pz(),fourTopGenParts[key]["quarks"][1].energy())
      bestquarktwo = getMatchedParticle(fourTopGenParts[key]["quarks"][1],jets)
      bestbquarktwoVec = TLorentzVector(bestquarktwo.px(),bestquarktwo.py(),bestquarktwo.pz(),bestquarktwo.energy())
      deltaRDistTwo = quarkTwoGenVec.DeltaR(bestbquarktwoVec)  
      if bestquarktwo.bDiscriminator("combinedSecondaryVertexBJetTags") > 0:   
        quarktwovalue = bestquarktwo.bDiscriminator("combinedSecondaryVertexBJetTags")
        quarksjetsDiscriminatorHist.Fill(quarktwovalue)
      if deltaRDistTwo < 0.3: 
#and bestquarktwo.bDiscriminator("combinedSecondaryVertexBJetTags") < 0.5:
        fourTopGenParts[key]["recoQuarkTwo"] = bestquarktwo
        if countGenMuons == 1: 
          deltaRjetsmuonsHist.Fill(deltaRDistTwo)
          resPtjetsmuonsHist.Fill(math.fabs(bestquarktwo.pt() - fourTopGenParts[key]["quarks"][1].pt())/fourTopGenParts[key]["quarks"][1].pt())
        if countGenMuons == 2: 
          deltaRjetsdimuonsHist.Fill(deltaRDistTwo)
          resPtjetsdimuonsHist.Fill(math.fabs(bestquarktwo.pt() - fourTopGenParts[key]["quarks"][1].pt())/fourTopGenParts[key]["quarks"][1].pt())
          #print 'quark2', fourTopGenParts[key]["quarks"][1].pt()
          jetsDiGenPtHist.Fill(fourTopGenParts[key]["quarks"][1].pt())
          #print 'recoquark2',fourTopGenParts[key]["recoQuarkTwo"].pt()
          jetsDiRecoPtHist.Fill(fourTopGenParts[key]["recoQuarkTwo"].pt())


    if fourTopGenParts[key].has_key("recoQuarkTwo") and fourTopGenParts[key].has_key("recoQuarkOne") and fourTopGenParts[key].has_key("recobquark"):
      b4Momentum = fourTopGenParts[key]["recobquark"].p4()
      q1_4Momentum = fourTopGenParts[key]["recoQuarkOne"].p4() 
      q2_4Momentum = fourTopGenParts[key]["recoQuarkTwo"].p4()
      if countGenMuons == 1:
        massdistHist.Fill((b4Momentum + q1_4Momentum + q2_4Momentum ).M())
        resmassHist.Fill(math.fabs((b4Momentum + q1_4Momentum + q2_4Momentum ).M()- 173.34)/173.34)
      if countGenMuons == 2:
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

       
         
  wrongJetCombinbationList = []
  for j in range(len(listjets)):
    
    for k in range(j+1,len(listjets)):
      for l in range(k+1,len(listjets)):
        if j == b1 and k == q11 and l == q12:
          continue
        if j == b2 and k == q21 and l == q22:
          continue
        if j == b3 and k == q31 and l == q32:
          continue
	wrongJetCombinbationList.append([j,k,l])


  if len(wrongJetCombinbationList) == 0:
    continue
  bestTopGuess = matchFunction.getBetTopGuess( wrongJetCombinbationList , listjets)
  #print "bestTop guess ",bestTopGuess
  #print " mass ",matchFunction.getJetThreeMass(bestTopGuess, listjets)
  if countGenMuons == 1:
    resmassjetHist.Fill(matchFunction.getJetThreeMass(bestTopGuess, listjets) -172  )
    massjetdistHist.Fill(matchFunction.getJetThreeMass(bestTopGuess, listjets))
    jetsmasssizeHist.Fill(len(listjets))
  if countGenMuons == 2:
    resmassjetdimuonsHist.Fill(matchFunction.getJetThreeMass(bestTopGuess, listjets) -172 )
    massjetdistdimuonsHist.Fill(matchFunction.getJetThreeMass(bestTopGuess, listjets) )
    jetsmasssizedimuonsHist.Fill(len(listjets))


#scale = 1/muonsRecoPtHist.Integral()
#muonsRecoPtHist.Scale(scale)
#scale = 1/muonsGenPtHist.Integral()
#muonsGenPtHist.Scale(scale)
#scale = 1/twomuonsRecoPtHist.Integral()
#twomuonsRecoPtHist.Scale(scale)
#scale = 1/twomuonsGenPtHist.Integral()
#twomuonsGenPtHist.Scale(scale)

#scale = 1/resPtmuonsHist.Integral()
#resPtmuonsHist.Scale(scale)
#scale = 1/deltaRmuonsHist.Integral()
#deltaRmuonsHist.Scale(scale)

#scale = 1/resPtdimuonsHist.Integral()
#resPtdimuonsHist.Scale(scale)
#scale = 1/deltaRdimuonsHist.Integral()
#deltaRdimuonsHist.Scale(scale)

#scale = 1/jetsGenPtHist.Integral()
#jetsGenPtHist.Scale(scale)
#scale = 1/jetsRecoPtHist.Integral()
#jetsRecoPtHist.Scale(scale)
#scale = 1/jetsDiGenPtHist.Integral()
#jetsDiGenPtHist.Scale(scale)
#scale = 1/jetsDiRecoPtHist.Integral()
#jetsDiRecoPtHist.Scale(scale)




#scale = 1/deltaRjetsmuonsHist.Integral()
#deltaRjetsmuonsHist.Scale(scale)
#scale = 1/resPtjetsmuonsHist.Integral()
#resPtjetsmuonsHist.Scale(scale)
#scale = 1/deltaRjetsdimuonsHist.Integral()
#deltaRjetsdimuonsHist.Scale(scale)
#scale = 1/resPtjetsdimuonsHist.Integral()
#resPtjetsdimuonsHist.Scale(scale)


#scale = 1/massdistHist.Integral()
#massdistHist.Scale(scale)
#scale = 1/resmassHist.Integral()
#resmassHist.Scale(scale)
#scale = 1/massjetdistHist.Integral()
#massjetdistHist.Scale(scale)
#scale = 1/resmassjetHist.Integral()
#resmassjetHist.Scale(scale)
#scale = 1/jetsmasssizeHist.Integral()
#jetsmasssizeHist.Scale(scale)

#scale = 1/massdistdimuonsHist.Integral()
#massdistdimuonsHist.Scale(scale)
#scale = 1/resmassdimuonsHist.Integral()
#resmassdimuonsHist.Scale(scale)
#scale = 1/massjetdistdimuonsHist.Integral()
#massjetdistdimuonsHist.Scale(scale)
#scale = 1/resmassjetdimuonsHist.Integral()
#resmassjetdimuonsHist.Scale(scale)
#scale = 1/jetsmasssizedimuonsHist.Integral()
#jetsmasssizedimuonsHist.Scale(scale)

#scale = 1/bjetsDiscriminatorHist.Integral()
#bjetsDiscriminatorHist.Scale(scale)
#scale = 1/quarksjetsDiscriminatorHist.Integral()
#quarksjetsDiscriminatorHist.Scale(scale)



##############Save:
muonsRecoPtHist.SaveAs(muonsRecoPtHist.GetName()+'_mc.root')
twomuonsRecoPtHist.SaveAs(twomuonsRecoPtHist.GetName()+'_mc.root')
muonsGenPtHist.SaveAs(muonsGenPtHist.GetName()+'_mc.root')
twomuonsGenPtHist.SaveAs(twomuonsGenPtHist.GetName()+'_mc.root')

resPtmuonsHist.SaveAs(resPtmuonsHist.GetName()+'_mc.root')
deltaRmuonsHist.SaveAs(deltaRmuonsHist.GetName()+'_mc.root')
resPtdimuonsHist.SaveAs(resPtdimuonsHist.GetName()+'_mc.root')
deltaRdimuonsHist.SaveAs(deltaRdimuonsHist.GetName()+'_mc.root')


jetsGenPtHist.SaveAs(jetsGenPtHist.GetName()+'_mc.root')
jetsRecoPtHist.SaveAs(jetsRecoPtHist.GetName()+'_mc.root')
jetsDiGenPtHist.SaveAs(jetsDiGenPtHist.GetName()+'_mc.root')
jetsDiRecoPtHist.SaveAs(jetsDiRecoPtHist.GetName()+'_mc.root')
deltaRjetsmuonsHist.SaveAs(deltaRjetsmuonsHist.GetName()+'_mc.root')
resPtjetsmuonsHist.SaveAs(resPtjetsmuonsHist.GetName()+'_mc.root')
deltaRjetsdimuonsHist.SaveAs(deltaRjetsdimuonsHist.GetName()+'_mc.root')
resPtjetsdimuonsHist.SaveAs(resPtjetsdimuonsHist.GetName()+'_mc.root')

massdistHist.SaveAs(massdistHist.GetName()+'_mc.root')
resmassHist.SaveAs(resmassHist.GetName()+'_mc.root')
massjetdistHist.SaveAs(massjetdistHist.GetName()+'_mc.root')
resmassjetHist.SaveAs(resmassjetHist.GetName()+'_mc.root')
jetsmasssizeHist.SaveAs(jetsmasssizeHist.GetName()+'_mc.root')

massdistdimuonsHist.SaveAs(massdistdimuonsHist.GetName()+'_mc.root')
resmassdimuonsHist.SaveAs(resmassdimuonsHist.GetName()+'_mc.root')
massjetdistdimuonsHist.SaveAs(massjetdistdimuonsHist.GetName()+'_mc.root')
resmassjetdimuonsHist.SaveAs(resmassjetdimuonsHist.GetName()+'_mc.root')
jetsmasssizedimuonsHist.SaveAs(jetsmasssizedimuonsHist.GetName()+'_mc.root')

bjetsDiscriminatorHist.SaveAs(bjetsDiscriminatorHist.GetName()+'_mc.root')
quarksjetsDiscriminatorHist.SaveAs(quarksjetsDiscriminatorHist.GetName()+'_mc.root')

##############################
print "One muon + jets",oneMuonRestHadevts
print "two muons + jets",diMuonicRestHadFourTopEvts
print "Non one or two muons + jets",nonOneOrDiMuonRestHadEvts
print "All hadronic events",allHadronicFourTopEvts
####################################
recJetPtHist.SaveAs(recJetPtHist.GetName()+'.root')
genGenPtHist.SaveAs(genGenPtHist.GetName()+'.root')
recMuonsPtHist.SaveAs(recMuonsPtHist.GetName()+'.root')
genMuonsPtHist.SaveAs(genMuonsPtHist.GetName()+'.root')
##############################

