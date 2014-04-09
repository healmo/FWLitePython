import ROOT,math
from DataFormats.FWLite import Events,Handle
particlesLabel  = "genParticles"
particlesHandle = Handle("vector<reco::GenParticle>")
events = Events('/user/hoehle/Samples/TTTTJetsMC/7083D246-AA0A-E211-ADA5-001E67397F26.root')
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
    elif numberqjets == 2:
      trileptonic += 1
    elif numberqjets == 4:
      dileptonic += 1
    elif numberqjets == 6:
      lepton += 1
    elif numberqjets == 8:
      alljets += 1
    else:
      print 'EvenNumber',i,'withqjets=',numberqjets
#  if i == 1800:
#    break
  if i%100 == 0:
    print "processed ",i+1," events"
leptonic = leptonic*100 / totalevents
trileptonic = trileptonic*100 / totalevents
dileptonic = dileptonic*100 / totalevents
lepton = lepton*100 / totalevents
alljets = alljets*100 / totalevents			
print 'TotalnumberEvents=',totalevents
print '   TotalLeptonic=',leptonic,'%'
print '   Trileptonic=',trileptonic,'%'
print '   Dileptonic=',dileptonic,'%'
print '   Only1lepton=',lepton,'%'
print '   AllJets=',alljets,'%'
#############
