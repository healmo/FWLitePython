import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector

class myClass(object):
  def __init__(self,evts,postfix):
    self.evts = evts
    self.postfix = postfix 
    print "testing"
  def selectionloop(self):
    print "starting starting"
    jetsLabel  = "selectedPatJetsPFlow"
    jetsHandle = Handle("vector<pat::Jet>")
    muonsRecoLabel  = "selectedPatMuonsPFlow"
    muonsRecoHandle = Handle("vector<pat::Muon>")
    vtxRecoHandle = Handle("vector<reco::Vertex>")
    vtxRecoLabel = "offlinePrimaryVertices"
    self.jetsmomentumbefore = ROOT.TH1D("jetsmomentumtriggeredbefore"+self.postfix,"Jets momentum pass trigger (before cut)",100,0,100)
    self.jetsmomentumafter = ROOT.TH1D("jetsmomentumtriggeredafter"+self.postfix,"Jets momentum pass trigger (after cut)",100,0,100)
    self.jetshighmomentum = ROOT.TH1D("jetshighmomentum"+self.postfix,"Jets High energetic",60,0,60)
    self.numberjetsBeforeDataHist = ROOT.TH1D("numberjetsBefore"+self.postfix,"Number jets/event Data",8,0,8)
    self.numberjetsAfterDataHist = ROOT.TH1D("numberjetsAfter"+self.postfix,"Number jets/event Data",8,0,8)
    self.cutprocess = ROOT.TH1D("cutprocess"+self.postfix,"Cut Process in the Selection",5,0,5)
    self.wmassdistribution = ROOT.TH1D("wmassdistribution"+self.postfix,"Number jets/event Data",300,0,300)
    self.topmassdistribution = ROOT.TH1D("topmassdistribution"+self.postfix,"Number jets/event Data",300,0,300)
    self.vtxSizeHist = ROOT.TH1D("vtxSizeHist"+self.postfix,"Vtx Size - Pileup",100,0,100)
    self.numberselectedsixevents = 0 
    self.numberselectedsixeventsbjets = 0 
    self.numberselectedsevenevents = 0 
    self.numberselectedseveneventsbjets = 0 
    self.numbersignalevents = 0
    self.numbertrigger = 0
    self.numbertotalmuons = 0
    self.numbertotalsixjets = 0
    self.numbertotalsevenjets = 0
    self.numbertotalsixbjets = 0
    self.numbertotalsevenbjets = 0
    self.numbertotalsevenjetsmomentum = 0
    self.scaletop = 0
    self.scalew = 0
    self.wmassselected = 0
    self.wmassselected7 = 0
    self.totaljetcombevents = 0
    TrigResultslabel=("TriggerResults");TrigResultshandle=Handle("edm::TriggerResults") 
    fileList=self.evts._filenames
    #print fileList
    #self.evts = Events(fileList[:100])
    #print self.evts._filenames
    print self.postfix
    for i,event in enumerate(self.evts):
      self.numbersignalevents+=1
      self.cutprocess.Fill(0)
 
      if i%10000 == 0 or i == 1 or i == 0:
        print "processed ",i+1," events"

      self.listmuons=[]
      self.listjets=[]
      self.listhighjets=[]
      self.listbjets=[]
      self.wmasslist=[]
      self.topmasslist=[]
      self.wmasslist7=[]
      self.topmasslist7=[]
      self.listcombjets=[]
      self.high1counter = 0 
      self.high2counter = 0
      self.high3counter = 0
      self.lowcounter = 0
      self.combevents = 0
      event.getByLabel(muonsRecoLabel,muonsRecoHandle)
      event.getByLabel(jetsLabel,jetsHandle)
      event.getByLabel((TrigResultslabel,"","HLT"),TrigResultshandle); 
      event.getByLabel(vtxRecoLabel,vtxRecoHandle)
      TrigResults=TrigResultshandle.product()
      TriggerNames=event.object().triggerNames(TrigResults)
  
      availTriggerMu=(" ".join([ tr for tr in TriggerNames.triggerNames() if "HLT_IsoMu24_eta2p1_v" in tr])).strip()
      #availTriggerEl=(" ".join([ tr for tr in TriggerNames.triggerNames() if "HLT_Ele27_WP80_v" in tr])).strip()
  
      if not TrigResults[TriggerNames.triggerIndex(availTriggerMu)].accept():
        continue
      self.numbertrigger += 1
      self.cutprocess.Fill(1)
  
      muons = muonsRecoHandle.product()
      jets = jetsHandle.product()
      vtxs = vtxRecoHandle.product()

      for jet in jets:
        self.jetsmomentumbefore.Fill(jet.pt())
        if math.fabs(jet.eta()) < 2.4:     
          self.listcombjets.append(jet)
          if jet.pt() > 40:
            self.listjets.append(jet)
            if jet.bDiscriminator("combinedSecondaryVertexBJetTags") > 0.5:
              self.listbjets.append(jet)

  
      for muon in muons:
        if muon.pt() > 30 and muon.isGlobalMuon():
          self.listmuons.append(muon)


      self.numberjetsBeforeDataHist.Fill(len(self.listjets))

      if len(self.listmuons) >= 1:
        self.numbertotalmuons += 1
        self.cutprocess.Fill(2)
        if len(self.listjets) >= 7:          
          for k in range(len(self.listjets)):
            self.listcombjets.append(self.listjets[k])
          self.numbertotalsevenjets += 1
          if len(self.listbjets) >= 3:
            self.numbertotalsevenbjets += 1
        if len(self.listjets) >= 6:
          self.numbertotalsixjets += 1
          if len(self.listbjets) >= 3:
            self.numbertotalsixbjets += 1

      if len(self.listjets) >= 6 and len(self.listmuons) >= 1:
        self.numberselectedsixevents+=1
    
        for j in range(len(self.listjets)):
          self.jetsmomentumafter.Fill(self.listjets[j].pt())
          self.numberjetsBeforeDataHist.Fill(len(self.listjets))
          for k in range(j+1,len(self.listjets)):
            if (self.listjets[j].p4()+self.listjets[k].p4()).M() >= 65 and (self.listjets[j].p4()+self.listjets[k].p4()).M() <= 95:
              self.wmasslist.append((self.listjets[j].p4()+self.listjets[k].p4()).M())
            for l in range(k+1,len(self.listjets)):
              if (self.listjets[j].p4()+self.listjets[k].p4()+self.listjets[l].p4()).M() >= 155 and (self.listjets[j].p4()+self.listjets[k].p4()+self.listjets[l].p4()).M() <= 185:
                self.topmasslist.append((self.listjets[j].p4()+self.listjets[k].p4()+self.listjets[l].p4()).M())
        if len(self.wmasslist) > 0:
          self.wmassselected += 1

      if len(self.listjets) >= 7 and len(self.listmuons) >= 1:
        self.numberselectedsevenevents+=1
        self.cutprocess.Fill(3)
        for j in range(len(self.listjets)):
          for k in range(j+1,len(self.listjets)):
            if (self.listjets[j].p4()+self.listjets[k].p4()).M() >= 65 and (self.listjets[j].p4()+self.listjets[k].p4()).M() <= 95:
              self.wmasslist7.append((self.listjets[j].p4()+self.listjets[k].p4()).M())
              for l in range(k+1,len(self.listjets)):
                if (self.listjets[j].p4()+self.listjets[k].p4()+self.listjets[l].p4()).M() >= 155 and (self.listjets[j].p4()+self.listjets[k].p4()+self.listjets[l].p4()).M() <= 185:
                  self.topmasslist7.append((self.listjets[j].p4()+self.listjets[k].p4()+self.listjets[l].p4()).M())
        if len(self.wmasslist7) > 0:
          self.wmassselected7 += 1
          self.cutprocess.Fill(4)
          self.vtxSizeHist.Fill(vtxs.size())
	  

      if len(self.listcombjets) >= 7 and len(self.listmuons) >= 1:
        for l in range(len(self.listcombjets)):
          if self.listcombjets[l].pt() > 50:
            self.high1counter += 1
          elif self.listcombjets[l].pt() > 40:
            self.high2counter += 1
          elif self.listcombjets[l].pt() >= 30:
            self.high3counter += 1
          elif self.listcombjets[l].pt() <= 30:
            self.lowcounter += 1
          if self.high1counter >=1 and self.high2counter >=1 and self.high3counter >=1 and self.lowcounter>=1:
            self.combevents +=1
            continue
      if len(self.wmasslist) == 0:
        continue
      if self.combevents >=1:
        self.totaljetcombevents +=1 
      for l in range(len(self.wmasslist)):
        self.wmassdistribution.Fill(self.wmasslist[l],1./len(self.wmasslist))
      for l in range(len(self.topmasslist)):
        self.topmassdistribution.Fill(self.topmasslist[l],1./len(self.wmasslist))



        

#########################
