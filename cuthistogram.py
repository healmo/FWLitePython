import ROOT,math,sys
from ROOT import TLorentzVector

#--------------------------------CutHistogram-----------------------------------------
fileDataRunA = ROOT.TFile("cutprocessDataHistRunA.root")
fileDataRunB = ROOT.TFile("cutprocessDataHistRunB.root")
filettdilepMC = ROOT.TFile("cutprocessTTHistdilep.root")
filettsemilepMC = ROOT.TFile("cutprocessTTHistsemilep.root")
filettttMC = ROOT.TFile("cutprocessTTTTHist.root")
c5 = ROOT.TCanvas("c5","Cut Process",200,10,700,500)
datacutprocessA = fileDataRunA.Get("cutprocessDataHistRunA")
datacutprocessB = fileDataRunB.Get("cutprocessDataHistRunB")
datacutprocess = datacutprocessA.Clone("cutprocessDataHist")
datacutprocess.Add(datacutprocessB)
ttdilepcutprocess = filettdilepMC.Get("cutprocessTTHistdilep")
ttsemilepcutprocess = filettsemilepMC.Get("cutprocessTTHistsemilep")
ttcutprocess = ttdilepcutprocess.Clone("cutprocessTTHist")
ttcutprocess.Add(ttsemilepcutprocess)
ttttcutprocess = filettttMC.Get("cutprocessTTTTHist")

ttcutprocess.Scale(1.26)

datacutprocess.SetLineColor(ROOT.kRed)
ttcutprocess.SetLineColor(ROOT.kGreen)
ttttcutprocess.SetLineColor(ROOT.kBlue)


datacutprocess.Draw()
ttcutprocess.Draw("sames")
#ttttcutprocess.Draw("sames")

leyMuons = ROOT.TLegend(0.4,0.6,0.89,0.89)
leyMuons.SetFillColor(ROOT.kWhite)
leyMuons.AddEntry(datacutprocess,"Data","l")
leyMuons.AddEntry(ttcutprocess,"t#bar{t}","l")
#leyMuons.AddEntry(ttttcutprocess,"Cut process in TTTTMCSample","l")
leyMuons.Draw()
c5.SaveAs("cutprocess_Data_vs_MCSamples.root")
c5.cd()

#-----------------------------VtxSize----------------------------------------------

fileDataRunA = ROOT.TFile("vtxSizeHistDataHistRunA.root")
fileDataRunB = ROOT.TFile("vtxSizeHistDataHistRunB.root")
filettdilepMC = ROOT.TFile("vtxSizeHistTTHistdilep.root")
filettsemilepMC = ROOT.TFile("vtxSizeHistTTHistsemilep.root")
filettsinMC = ROOT.TFile("vtxSizeHistTTHist.root")
c1 = ROOT.TCanvas("c1","Vertex",200,10,700,500)
datavtxRunA = fileDataRunA.Get("vtxSizeHistDataHistRunA")
datavtxRunB = fileDataRunB .Get("vtxSizeHistDataHistRunB")
ttdilep = filettdilepMC.Get("vtxSizeHistTTHistdilep")
ttsemilep = filettsemilepMC.Get("vtxSizeHistTTHistsemilep")
ttsin = filettsinMC.Get("vtxSizeHistTTHist")
ttcon = ttdilep.Clone("vtxSizeHistTTcon")
ttcon.Add(ttsemilep)
datavtx = datavtxRunA.Clone("vtxSizeHistDataHist")
datavtx.Add(datavtxRunB)

ttcon.Sumw2()
ttsin.Sumw2()
ttcon.SetLineColor(ROOT.kBlue)
ttsin.SetLineColor(ROOT.kRed)
datavtx.SetMarkerStyle(20)

ttcon.Scale(1.149)
ttsin.Scale(1.264)
scale = 1/ttcon.Integral()
ttcon.Scale(scale)
scale = 1/ttsin.Integral()
ttsin.Scale(scale)
scale = 1/datavtx.Integral()
datavtx.Scale(scale)
datavtx.Draw("p9")
ttsin.Draw("sames")
ttcon.Draw("sames")

leyMuons = ROOT.TLegend(0.4,0.6,0.89,0.89)
leyMuons.SetFillColor(ROOT.kWhite)
leyMuons.AddEntry(datavtx,"Data","p")
leyMuons.AddEntry(ttsin,"t#bar{t} Simulation Sample 1","l")
leyMuons.AddEntry(ttcon,"t#bar{t} Simulation Sample 2","l")
leyMuons.Draw()
c1.SaveAs("pileupcorrections.root")
c1.cd()


#------------------------------NumberJetsTT---------------------------------


fileTTdilep = ROOT.TFile("numberjetsBeforeTTHistdilep_mc.root")
fileTTsemilep = ROOT.TFile("numberjetsBeforeTTHistsemilep_mc.root")
fileTTfullhad = ROOT.TFile("numberjetsBeforeTTHistfullhad_mc.root")
c9 = ROOT.TCanvas("c9","Number Jets Event",200,10,700,500)

ttdilepnumber = fileTTdilep.Get("numberjetsBeforeTTHistdilep")
ttsemilepnumber = fileTTsemilep.Get("numberjetsBeforeTTHistsemilep")
ttfullhadnumber = fileTTfullhad.Get("numberjetsBeforeTTHistfullhad")

ttdilepnumber.SetLineColor(ROOT.kBlue)
ttsemilepnumber.SetLineColor(ROOT.kGreen)
ttfullhadnumber.SetLineColor(ROOT.kOrange)

scale = 1/ttdilepnumber.Integral()
ttdilepnumber.Scale(scale)
scale = 1/ttsemilepnumber.Integral()
ttsemilepnumber.Scale(scale)
scale = 1/ttfullhadnumber.Integral()
ttfullhadnumber.Scale(scale)

ttfullhadnumber.Draw()
ttsemilepnumber.Draw("sames")
ttdilepnumber.Draw("sames")

leyMuons = ROOT.TLegend(0.4,0.6,0.89,0.89)
leyMuons.SetFillColor(ROOT.kWhite)
leyMuons.AddEntry(ttfullhadnumber,"TTSample full hadronic channel","l")
leyMuons.AddEntry(ttsemilepnumber,"TTSample semileptonic channel","l")
leyMuons.AddEntry(ttdilepnumber,"TTSample dileptonic channel","l")
leyMuons.Draw()
c9.SaveAs("numberjetseventtmc.root")
c9.cd()

#------------------------------NumberJetsData---------------------------------
fileDataRunA = ROOT.TFile("numberjetsBeforeDataHistRunA_mc.root")
fileDataRunB = ROOT.TFile("numberjetsBeforeDataHistRunB_mc.root")
datanumberRunA = fileDataRunA.Get("numberjetsBeforeDataHistRunA")
datanumberRunB = fileDataRunB.Get("numberjetsBeforeDataHistRunB") 
datanumber = datanumberRunA.Clone("numberjetsData")
datanumber.Add(datanumberRunB)

scale = 1/datanumber.Integral()
datanumber.Scale(scale)

datanumber.SaveAs("numberjetseventData.root")

#------------------------------NumberJetsTTTT---------------------------------
fileTTTT = ROOT.TFile("numberjetsBeforeTTTTHist_mc.root")
ttttnumber = fileTTTT.Get("numberjetsBeforeTTTTHist")

scale = 1/ttttnumber.Integral()
ttttnumber.Scale(scale)
ttttnumber.Draw()
ttttnumber.SaveAs("numberjetseventTTTT.root")




