import webbrowser
from sites_taamanhos import *

def takeoffSTB():

    print("\n---TAKEOFF----")
    print("\n1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:XG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(takeofftmSTB.get("p"))
              
        case "2":
            webbrowser.open(takeofftmSTB.get("m"))
                 
        case "3":
            webbrowser.open(takeofftmSTB.get("g"))
        
        case "4":
            webbrowser.open(takeofftmSTB.get("gg"))
        
        case "5":
            webbrowser.open(takeofftmSTB.get("xg"))


def madSTB():

    print("\n---MAD----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(madtmSTB.get("pp"))
              
        case "2":
            webbrowser.open(madtmSTB.get("p"))
                 
        case "3":
            webbrowser.open(madtmSTB.get("m"))
        
        case "4":
            webbrowser.open(madtmSTB.get("g"))
        
        case "5":
            webbrowser.open(madtmSTB.get("gg"))

        case "6":
            webbrowser.open(madtmSTB.get("exg"))

        case "7":
            webbrowser.open(madtmSTB.get("exgg"))


def sufSTB():

    print("\n---SUFGANG----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(suftmSTB.get("ppSTB"))
              
        case "2":
            webbrowser.open(suftmSTB.get("pSTB"))
                 
        case "3":
            webbrowser.open(suftmSTB.get("mSTB"))
        
        case "4":
            webbrowser.open(suftmSTB.get("gSTB"))
        
        case "5":
            webbrowser.open(suftmSTB.get("ggSTB"))

        case "6":
            webbrowser.open(suftmSTB.get("exgSTB"))

        case "7":
            webbrowser.open(suftmSTB.get("exggSTB"))


def clsSTB():

    print("\n---CLASS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(classtmSTB.get("p"))
            
            
        case "2":
            webbrowser.open(classtmSTB.get("m"))
                 

        case "3":
            webbrowser.open(classtmSTB.get("g"))
        

        case "4":
            webbrowser.open(classtmSTB.get("gg"))
        

        case "5":
            webbrowser.open(classtmSTB.get("exg"))
  





