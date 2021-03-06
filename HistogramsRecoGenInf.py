import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector


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


filediRecoMC = ROOT.TFile("recMuonsPtHist.root")
filediGenMC = ROOT.TFile("genMuonsPtHist.root")
c2 = ROOT.TCanvas("c2","Muon Pt",200,10,700,500)
TwoMuonRecoPt = filediRecoMC.Get("recMuonsPtHist")
TwoMuonGenPt = filediGenMC.Get("genMuonsPtHist")
TwoMuonGenPt.SetLineColor(ROOT.kRed)
TwoMuonGenPt.Draw()
TwoMuonRecoPt.Draw("sames")
leyJets2 = ROOT.TLegend(0.5,0.6,0.79,0.79)
leyJets2.AddEntry(TwoMuonGenPt,"Pt Gen Muons","l")
leyJets2.AddEntry(TwoMuonRecoPt,"Pt Reco Muons","l")
leyJets2.Draw()
c2.SaveAs("twomuonsPtHist_Reco_vs_Gen2.root")
c2.cd()

fileJDiRecoMC = ROOT.TFile("recJetPtHist.root")
fileJDiGenMC = ROOT.TFile("genGenPtHist.root")
c3 = ROOT.TCanvas("c3","Jets Pt Gen/Reco",200,10,700,500)
JetsDiRecoPt = fileJDiRecoMC.Get("recJetPtHist")
JetsDiGenPt = fileJDiGenMC.Get("genGenPtHist")
JetsDiGenPt.SetLineColor(ROOT.kOrange)
JetsDiRecoPt.SetLineColor(ROOT.kViolet)
JetsDiRecoPt.Draw()
JetsDiGenPt.Draw("sames")
leyJets = ROOT.TLegend(0.5,0.6,0.79,0.79)
#leyJets.SetHeader("Some histograms")
leyJets.AddEntry(JetsDiGenPt,"Pt Gen Jets","l")
leyJets.AddEntry(JetsDiRecoPt,"Pt Reco Jets","l")
leyJets.Draw()
c3.SaveAs("jetsPtHist_Reco_vs_Gen.root")
c3.cd()

filebjetsDiscriminatorMC = ROOT.TFile("bjetsDiscriminatorHist_mc.root")
filequarkjetsDiscriminatorMC = ROOT.TFile("quarksjetsDiscriminatorHist_mc.root")
c5 = ROOT.TCanvas("c5","Discriminator Values",200,10,700,500)
bjetsDiscriminator = filebjetsDiscriminatorMC.Get("bjetsDiscriminatorHist")
quarksjetsDiscriminator = filequarkjetsDiscriminatorMC.Get("quarksjetsDiscriminatorHist")
bjetsDiscriminator.SetLineColor(ROOT.kRed)
quarksjetsDiscriminator.Draw()
bjetsDiscriminator.Draw("sames")
c5.SaveAs("discriminatorvalues_bquarks_Wquarks.root")
c5.cd()


filemassMC = ROOT.TFile("massdistdimuonsHist_mc.root")
filemassJMC = ROOT.TFile("massjetdistdimuonsHist_mc.root")
c4 = ROOT.TCanvas("c4","JMass distribution",200,10,700,500)
Massdist = filemassMC.Get("massdistdimuonsHist")
Massjetdist = filemassJMC.Get("massjetdistdimuonsHist")
Massjetdist.SetLineColor(ROOT.kRed)
Massdist.Draw()
Massjetdist.Draw("sames")
c4.SaveAs("massHist_Matched_vs_NotMatched.root")
c4.cd()
