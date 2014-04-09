import ROOT,math
from DataFormats.FWLite import Events,Handle
particlesLabel  = "genParticles"
particlesHandle = Handle("vector<reco::GenParticle>")
events = Events('/user/hoehle/Samples/TTTTJetsMC/7083D246-AA0A-E211-ADA5-001E67397F26.root')
totalmassvalues = 0
totalmass = 0
totalevents = 0

for i,event in enumerate(events):
  event.getByLabel(particlesLabel,particlesHandle)
  particles = particlesHandle.product()
  #print '-------',i,'Event-----------------------------------------'
  benergy = 0
  topmass = 0
  for part in particles:
    if part.status() == 3:
      #print part.pdgId()
      if math.fabs(part.pdgId()) <= 5:
        if math.fabs(part.pdgId()) == 5 and math.fabs(part.mother().pdgId()) == 6:
          benergy = part.energy()
          tmomentum = part.mother().p()
          qenergyA = 0
          qenergyB = 0
          #print 'bottom!=',benergy 
          #print 'qjetA!=',qenergyA 
          #print 'qjetB!=',qenergyB
        if math.fabs(part.pdgId())%2 == 0 and math.fabs(part.mother().pdgId()) == 24:
          qenergyB = part.energy()
          #print 'bottom!=',benergy 
          #print 'qjetA!=',qenergyA 
          #print 'qjetB!=',qenergyB
        elif math.fabs(part.pdgId())%2 != 0 and math.fabs(part.mother().pdgId()) == 24:
          qenergyA = part.energy()
          #print 'bottom!=',benergy 
          #print 'qjetA!=',qenergyA 
          #print 'qjetB!=',qenergyB
        if qenergyA != 0 and qenergyB != 0 and benergy != 0: 
          topmass = math.sqrt(math.fabs((qenergyA + qenergyB + benergy)**2-tmomentum**2)) 
          totalmassvalues += 1         
          totalmass = totalmass + topmass 
         
          
  #if i == 15:
    #break
  if i%100 == 0:
    print "processed ",i," events"
    
meanvalue = totalmass/totalmassvalues
print 'TopMassMeanValue=',meanvalue
#############

