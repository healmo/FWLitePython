import ROOT,math,sys
import math
from array import array

dataEvts=221
numBkgEvts=210
points=500
scale=1.2
errorEvts=20
x=[];y=[];xMinus=[]; xPlus=[];x2Minus=[]; x2Plus=[];x3Minus=[]; x3Plus=[]; xerrorpos=[]; xerrorneg=[]; x2errorpos=[]; x2errorneg=[]; x3errorpos=[]; x3errorneg=[]
for i in range(0,points):
  numEvts = numBkgEvts+i
  y.append(i)
  x.append(numEvts)
  xerrorpos.append(numEvts+10)
  xerrorneg.append(numEvts-10)
  xMinus.append(numEvts - math.sqrt(errorEvts*errorEvts+scale*i))
  xPlus.append(numEvts + math.sqrt(errorEvts*errorEvts+scale*i))
  x2Minus.append(numEvts - 2*math.sqrt(errorEvts*errorEvts+scale*i))
  x2Plus.append(numEvts + 2*math.sqrt(errorEvts*errorEvts+scale*i))
  x3Minus.append(numEvts - 3*math.sqrt(errorEvts*errorEvts+scale*i))
  x3Plus.append(numEvts + 3*math.sqrt(errorEvts*errorEvts+scale*i))
  x2errorneg.append(numEvts - math.sqrt(2*2*(errorEvts*errorEvts+scale*i)+10*10)) 
  x2errorpos.append(numEvts + math.sqrt(2*2*(errorEvts*errorEvts+scale*i)+10*10))
  x3errorneg.append(numEvts - math.sqrt(3*3*(errorEvts*errorEvts+scale*i)+10*10)) 
  x3errorpos.append(numEvts + math.sqrt(3*3*(errorEvts*errorEvts+scale*i)+10*10))  

linGraph = ROOT.TGraph(points,array('d',x),array('d',y))
linGraph_fit = ROOT.TF1("linGraph_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGraph.Fit(linGraph_fit,"NR")#QN
linGrapherrorpos = ROOT.TGraph(points,array('d',xerrorpos),array('d',y))
linGrapherrorpos_fit = ROOT.TF1("linGrapherrorpos_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGrapherrorpos.Fit(linGrapherrorpos_fit,"NR")#QN
linGrapherrorneg = ROOT.TGraph(points,array('d',xerrorneg),array('d',y))
linGrapherrorneg_fit = ROOT.TF1("linGrapherrorneg_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGrapherrorneg.Fit(linGrapherrorneg_fit,"NR")#QN
linGraph2errorpos = ROOT.TGraph(points,array('d',x2errorpos),array('d',y))
linGraph2errorpos_fit = ROOT.TF1("linGraph2errorpos_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGraph2errorpos.Fit(linGraph2errorpos_fit,"NR")#QN
linGraph2errorneg = ROOT.TGraph(points,array('d',x2errorneg),array('d',y))
linGraph2errorneg_fit = ROOT.TF1("linGraph2errorneg_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGraph2errorneg.Fit(linGraph2errorneg_fit,"NR")#QN
linGraph3errorpos = ROOT.TGraph(points,array('d',x3errorpos),array('d',y))
linGraph3errorpos_fit = ROOT.TF1("linGraph3errorpos_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGraph3errorpos.Fit(linGraph3errorpos_fit,"NR")#QN
linGraph3errorneg = ROOT.TGraph(points,array('d',x3errorneg),array('d',y))
linGraph3errorneg_fit = ROOT.TF1("linGraph3errorneg_fit","[0] + [1]*x",dataEvts-20,dataEvts+20)
linGraph3errorneg.Fit(linGraph3errorneg_fit,"NR")#QN

limitGrapg = ROOT.TCanvas("limit","limit",200,10,700,500)
limitGrapg.cd()


linGraphMinus = ROOT.TGraph(points,array('d',xMinus),array('d',y))
linGraphMinus.SetLineColor(ROOT.kGreen+1)
linGraphMinus.SetLineWidth(2)
linGraphMinus.SetLineStyle(5)
linGraphMinus_fit = ROOT.TF1("linGraphMinus_fit","[0] + [1]*x +[2]*x*x + [3]*x*x*x",dataEvts-20,dataEvts+20)
linGraphMinus.Fit(linGraphMinus_fit,"NR")#QN
linGraphPlus = ROOT.TGraph(points,array('d',xPlus),array('d',y))
linGraphPlus.SetLineColor(ROOT.kGreen+1)
linGraphPlus.SetLineWidth(2)
linGraphPlus.SetLineStyle(5)
linGraphPlus_fit = ROOT.TF1("linGraphPlus_fit","[0] + [1]*x +[2]*x*x + [3]*x*x*x",dataEvts-20,dataEvts+20)
linGraphPlus.Fit(linGraphPlus_fit,"NR")#QN

linGraph2Minus = ROOT.TGraph(points,array('d',x2Minus),array('d',y))
linGraph2Minus.SetLineColor(ROOT.kCyan)
linGraph2Minus.SetLineWidth(2)
linGraph2Minus.SetLineStyle(5)
linGraph2Minus_fit = ROOT.TF1("linGraph2Minus_fit","[0] + [1]*x +[2]*x*x + [3]*x*x*x",dataEvts-20,dataEvts+20)
linGraph2Minus.Fit(linGraph2Minus_fit,"NR")#QN
linGraph2Plus = ROOT.TGraph(points,array('d',x2Plus),array('d',y))
linGraph2Plus.SetLineColor(ROOT.kCyan)
linGraph2Plus.SetLineWidth(2)
linGraph2Plus.SetLineStyle(5)
linGraph2Plus_fit = ROOT.TF1("linGraph2Plus_fit","[0] + [1]*x +[2]*x*x + [3]*x*x*x",dataEvts-20,dataEvts+20)
linGraph2Plus.Fit(linGraph2Plus_fit,"NR")#QN


linGraph3Minus = ROOT.TGraph(points,array('d',x3Minus),array('d',y))
linGraph3Minus.SetLineColor(ROOT.kOrange+2)
linGraph3Minus.SetLineWidth(2)
linGraph3Minus.SetLineStyle(5)
linGraph3Minus_fit = ROOT.TF1("linGraph3Minus_fit","[0] + [1]*x +[2]*x*x + [3]*x*x*x",dataEvts-20,dataEvts+20)
linGraph3Minus.Fit(linGraph3Minus_fit,"NR")#QN
linGraph3Plus = ROOT.TGraph(points,array('d',x3Plus),array('d',y))
linGraph3Plus.SetLineColor(ROOT.kOrange+2)
linGraph3Plus.SetLineWidth(2)
linGraph3Plus.SetLineStyle(5)
linGraph3Plus_fit = ROOT.TF1("linGraph3Plus_fit","[0] + [1]*x +[2]*x*x + [3]*x*x*x",dataEvts-20,dataEvts+20)
linGraph3Plus.Fit(linGraph3Plus_fit,"NR")#QN


linGrapherrorpos.SetLineWidth(2)
linGrapherrorpos.SetLineStyle(5)
linGrapherrorneg.SetLineWidth(2)
linGrapherrorneg.SetLineStyle(5)

mg = ROOT.TMultiGraph();
mg.SetTitle("UL Limit Calculation");
mg.Add(linGraph)
mg.Add(linGraphMinus)
mg.Add(linGraphPlus)
mg.Add(linGraph2Minus)
mg.Add(linGraph2Plus)
mg.Add(linGraph3Minus)
mg.Add(linGraph3Plus)
mg.Draw('AL')

data = ROOT.TLine(dataEvts,0,dataEvts,120)
data.SetLineColor(ROOT.kRed)
data.Draw("sames")

leyCL = ROOT.TLegend(0.4,0.4,0.89,0.89)
leyCL.SetLineColor(ROOT.kWhite)
leyCL.SetFillColor(ROOT.kWhite)
leyCL.AddEntry(linGraph,"N_{BG}+N_{signal}","l")
leyCL.AddEntry(linGraphMinus,"1#sigma (68.27%)","l")
leyCL.AddEntry(linGraph2Minus,"2#sigma (95.45%)","l")
leyCL.AddEntry(linGraph3Minus,"3#sigma (99.73%)","l")
leyCL.AddEntry(data,"N_{data}","l")
leyCL.Draw()

limitGrapg.SaveAs("limitcalculation.root")


limitGrapgerrors = ROOT.TCanvas("limit2","limit",200,10,700,500)
limitGrapgerrors.cd()

mg2 = ROOT.TMultiGraph();
mg2.SetTitle("UL Limit Calculation with Errors");
mg2.Add(linGraph)
mg2.Add(linGrapherrorpos)
mg2.Add(linGrapherrorneg)
mg2.Add(linGraph2errorpos)
mg2.Add(linGraph2errorneg)
mg2.Add(linGraph3errorpos)
mg2.Add(linGraph3errorneg)
mg2.Add(linGraphMinus)
mg2.Add(linGraphPlus)
mg2.Add(linGraph2Minus)
mg2.Add(linGraph2Plus)
mg2.Add(linGraph3Minus)
mg2.Add(linGraph3Plus)
mg2.Draw('AL')

data2 = ROOT.TLine(dataEvts,0,dataEvts,120)
data2.SetLineColor(ROOT.kRed)
data2.Draw()

leyCL2 = ROOT.TLegend(0.4,0.4,0.89,0.89)
leyCL2.SetLineColor(ROOT.kWhite)
leyCL2.SetFillColor(ROOT.kWhite)
leyCL2.AddEntry(linGraph,"N_{BG}+N_{signal}","l")
leyCL2.AddEntry(linGraphMinus,"1#sigma (68.27%)","l")
leyCL2.AddEntry(linGraph2Minus,"2#sigma (95.45%)","l")
leyCL2.AddEntry(linGraph3Minus,"3#sigma (99.73%)","l")
leyCL2.AddEntry(linGrapherrorpos,"sys error","l")
leyCL2.AddEntry(linGraph2errorpos,"2#sigma + sys error","l")
leyCL2.AddEntry(linGraph3errorpos,"3#sigma + sys error","l")
leyCL2.AddEntry(data,"N_{data}","l")
leyCL2.Draw()

limitGrapgerrors.SaveAs("limitcalculationsyserror.root")

print "eval dataEvts Value", linGraph_fit.Eval(dataEvts)
print "eval dataEvts Value+Error", linGrapherrorpos_fit.Eval(dataEvts)
print "eval dataEvts Value-Error", linGrapherrorneg_fit.Eval(dataEvts)
print "eval dataEvts 1SigmaMinus", linGraphMinus_fit.Eval(dataEvts)
print "eval dataEvts 1SigmaPlus", linGraphPlus_fit.Eval(dataEvts)
print "eval dataEvts 2SigmaMinus", linGraph2Minus_fit.Eval(dataEvts)
print "eval dataEvts 2SigmaMinus+sys", linGraph2errorneg_fit.Eval(dataEvts)
print "eval dataEvts 3SigmaMinus", linGraph3Minus_fit.Eval(dataEvts)
print "eval dataEvts 3SigmaMinus+sys", linGraph3errorneg_fit.Eval(dataEvts)

