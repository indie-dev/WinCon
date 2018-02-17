from wincon import WinCon

#Load from json
win = WinCon()
win.loadFromJSON("https://softy.000webhostapp.com/first.json", "first.json")

#Make .win archive
win = WinCon()
win.makeWinCon("C:\\Users\\bremo\\Desktop\\Projects","C:\\Users\\bremo\\Desktop\\Projects" )

#Decompress .win
win = WinCon()
win.decompressWinCon("C:\\Users\\bremo\\Desktop\\Projects.win", "C:\\Users\\bremo\\Desktop\\Projekts")