import ROOT
filePtData = ROOT.TFile("jetsPtHist.root")
fileSizeData = ROOT.TFile("jetsSizeHist.root")
filePtMC = ROOT.TFile("jetsPtHist_mc.root")
fileSizeMC = ROOT.TFile("jetsSizeHist_mc.root")

c1 = ROOT.TCanvas("c1","Jet Pt",200,10,700,500)
dataJetPt = filePtData.Get("jetsPtHist")
mcJetPt = filePtMC.Get("jetsPtHist")
mcJetPt.SetLineColor(ROOT.kRed)
dataJetPt.Draw()
mcJetPt.Draw("sames")
c1.SaveAs("jetsPtHist_data_vs_mc.root")
c1.cd()

c2 = ROOT.TCanvas("c1","Jet Size",200,10,700,500)
dataJetSize = fileSizeData.Get("jetsSizeHist")
mcJetSize = fileSizeMC.Get("jetsSizeHist")
mcJetSize.SetLineColor(ROOT.kRed)
dataJetSize.Draw()
mcJetSize.Draw("sames")
c2.SaveAs("jetsSizeHist_data_vs_mc.root")
c2.cd()


