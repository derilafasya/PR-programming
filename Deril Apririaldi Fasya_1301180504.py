import os
import math           
inputan="1"
pi=float(math.pi)
while(inputan!="0"):
  print("= - = - = - MENGHITUNG LUAS & VOLUME BANGUN RUANG = - = - = -")
  print("(Input (1-3), and 0 to exit)")
  print("1 -- Kerucut ")
  print("2 -- bola")
  print("3 -- Tabung")
  inputan = input()
  type(inputan)
  if (inputan=="1"):
    jari2 =   float(input("Jari-jari : "))
    tinggi =  float(input("tinggi    : "))
    apotema = float(input("Apotema   : "))
    print("")
    volume=1/3*pi*jari2**2*tinggi
    luaspermukaan=pi*jari2**2
    luasselimut=pi*jari2*apotema    
    luasalas=luaspermukaan+luasselimut
    print("Volume         : ", end=" ")
    print("%.2f" % volume)
    print("Luas Alas      : ", end=" ")
    print("%.2f" % luasalas)
    print("Luas Permukaan : ", end=" ")
    print("%.2f" % luaspermukaan)
    print("Luas Selimut   : ", end=" ")
    print("%.2f" % luasselimut)
  if (inputan=="2"):
    jari2 =   float(input("Jari-jari : "))
    print("")
    volume=4/3*pi*jari2**3
    luaspermukaan=4*pi*jari2**2
    print("Volume         : ", end=" ")
    print("%.2f" % volume)
    print("Luas Permukaan : ", end=" ")
    print("%.2f" % luaspermukaan)
  if (inputan=="3"):
    jari2 = float(input("Jari-jari : "))
    tinggi= float(input("tinggi    : "))
    print("")
    volume=pi*jari2**2*tinggi
    luaspermukaan=2*pi*jari2*(jari2+tinggi)
    luasselimut=pi*(jari2+jari2)*tinggi
    luasalas=pi*jari2**2
    print("Volume         : ", end=" ")
    print("%.2f" % volume)
    print("Luas Permukaan : ", end=" ")
    print("%.2f" % luaspermukaan)
    print("Luas selimut : ", end=" ")
    print("%.2f" % luasselimut)
    print("Luas alas    : ", end=" ")
    print("%.2f" % luasalas)