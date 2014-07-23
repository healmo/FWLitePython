from ROOT import TLorentzVector
import math
def getMatchedParticle(genPart,collection):
    resPart = collection[0]
    resPartVec = TLorentzVector(resPart.px(),resPart.py(),resPart.pz(), resPart.energy())
    genPartVec = TLorentzVector(genPart.px(),genPart.py(),genPart.pz(),genPart.energy())
    deltaRDist = genPartVec.DeltaR( resPartVec )     
    #print "deltaRDist ",deltaRDist
    for part in collection:
      tmpVec = TLorentzVector(part.px(),part.py(),part.pz(), part.energy())
      tmpDeltaR = genPartVec.DeltaR(tmpVec)
      if deltaRDist > tmpDeltaR:
        resPart = part
        resPartVec = tmpVec
        deltaRDist = tmpDeltaR
      #print "deltaRDist ",deltaRDist,' tmpDeltaR ',tmpDeltaR
    return resPart


def getJetThreeMass(comb,jets):
    return (jets[comb[0]].p4() + jets[comb[1]].p4() + jets[comb[2]].p4() ).M()
def getBetTopGuess(jetCombinationsList,jets):
    fristComb = jetCombinationsList.pop()
    diff = math.fabs( getJetThreeMass(fristComb,jets)-172.5 )
    bestComb = fristComb
    for comb in jetCombinationsList:
      tmpdiff = math.fabs( getJetThreeMass(comb,jets) -172.5 )
      #print "bestComb ",bestComb," diff ",diff," comb ",comb," tmpdiff ", tmpdiff
      if tmpdiff < diff:
        diff = tmpdiff
        bestComb = comb
    #print "bestComb ",bestComb," diff ",diff
    return bestComb
  
