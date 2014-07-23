import ROOT,math
from DataFormats.FWLite import Events,Handle
particlesLabel  = "genParticles"
particlesHandle = Handle("vector<reco::GenParticle>")
branchingratioHist = ROOT.TH1D("branchingratioHist","Branching Ratio Wdecay",5,0,5)
events = Events('/user/Samples/TTTTJetsMC/7083D246-AA0A-E211-ADA5-001E67397F26.root')
totalmassvalues = 0
totalmass = 0
totalmass2 = 0
totalevents = 0
totalevents = 0
leptonic = 0
trileptonic = 0
dileptonic = 0
lepton = 0
alljets = 0

for i,event in enumerate(events):
  numberTopEvent = 0
  numberbq = 0
  numberqjets = 0
  benergy = 0
  topmass = 0
  event.getByLabel(particlesLabel,particlesHandle)
  particles = particlesHandle.product()
  for part in particles:
    if part.status() == 3:
      if math.fabs(part.pdgId()) == 6:
		  numberTopEvent += 1
      elif math.fabs(part.pdgId()) <= 5 and math.fabs(part.mother().pdgId()) == 24:
        numberqjets += 1   
  if numberTopEvent == 4:
    totalevents += 1
    if numberqjets == 0:
      leptonic += 1
      branchingratioHist.Fill(0)
    elif numberqjets == 2:
      trileptonic += 1
      branchingratioHist.Fill(2) 
    elif numberqjets == 4:
      dileptonic += 1
      branchingratioHist.Fill(1)
    elif numberqjets == 6:
      lepton += 1
      branchingratioHist.Fill(3)
    elif numberqjets == 8:
      alljets += 1
      branchingratioHist.Fill(4)
      for part in particles:
        if part.status() == 3:
          if math.fabs(part.pdgId()) <= 5:
            if math.fabs(part.pdgId()) == 5 and math.fabs(part.mother().pdgId()) == 6:
              benergy = part.energy()
              b4Momentum = part.p4()
              tmomentum = part.mother().p()
              qenergyA = 0
              qenergyB = 0
            if math.fabs(part.pdgId())%2 == 0 and math.fabs(part.mother().pdgId()) == 24:
              qenergyB = part.energy()
              q2_4Momentum = part.p4()
            elif math.fabs(part.pdgId())%2 != 0 and math.fabs(part.mother().pdgId()) == 24:
              qenergyA = part.energy()
              q1_4Momentum = part.p4()
            if qenergyA != 0 and qenergyB != 0 and benergy != 0: 
              topmass = math.sqrt(math.fabs((qenergyA + qenergyB + benergy)**2-tmomentum**2)) 
              totalmassvalues += 1         
              totalmass = totalmass + topmass
              tMass = (b4Momentum + q1_4Momentum + q2_4Momentum).M()
              totalmass2 = totalmass2 + tMass
    else:
      print 'EvenNumber',i,'withqjets=',numberqjets
 
  
  if i%100 == 0:
    print "processed ",i," events"

scale = 1/branchingratioHist.Integral()
branchingratioHist.Scale(scale)

leptonic = leptonic*100/totalevents
trileptonic = trileptonic*100/totalevents
dileptonic = dileptonic*100/totalevents
lepton = lepton*100/totalevents
alljets = alljets*100/totalevents
meanvalue = totalmass/totalmassvalues
meanvalue2 = totalmass2/totalmassvalues			
print 'TotalnumberEvents=',totalevents
print '   BR(TotalLeptonic)=',leptonic,'%'
print '   BR(Trileptonic)=',trileptonic,'%'
print '   BR(Dileptonic)=',dileptonic,'%'
print '   BR(Only1lepton)=',lepton,'%'
print '   BR(AllJets)=',alljets,'%'
print '   TopMassMeanValue=',meanvalue
print '   TopMassMeanValue2=',meanvalue2
#############


branchingratioHist.SaveAs(branchingratioHist.GetName()+'_mc.root')
