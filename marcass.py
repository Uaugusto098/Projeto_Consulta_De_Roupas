import webbrowser
from sites_taamanhos import *

def takeoffSTB():

    print("\n---TAKEOFF----")
    print("\n1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:XG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(streetbusiness['takeofftmSTB'].get("p"))
              
        case "2":
            webbrowser.open(streetbusiness['takeofftmSTB'].get("m"))
                 
        case "3":
            webbrowser.open(streetbusiness['takeofftmSTB'].get("g"))
        
        case "4":
            webbrowser.open(streetbusiness['takeofftmSTB'].get("gg"))
        
        case "5":
            webbrowser.open(streetbusiness['takeofftmSTB'].get("xg"))


def madSTB():

    print("\n---MAD----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(streetbusiness['madtmSTB'].get("pp"))
              
        case "2":
            webbrowser.open(streetbusiness['madtmSTB'].get("p"))
                 
        case "3":
            webbrowser.open(streetbusiness['madtmSTB'].get("m"))
        
        case "4":
            webbrowser.open(streetbusiness['madtmSTB'].get("g"))
        
        case "5":
            webbrowser.open(streetbusiness['madtmSTB'].get("gg"))

        case "6":
            webbrowser.open(streetbusiness['madtmSTB'].get("exg"))

        case "7":
            webbrowser.open(streetbusiness['madtmSTB'].get("exgg"))


def sufSTB():

    print("\n---SUFGANG----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(streetbusiness['suftmSTB'].get("ppSTB"))
              
        case "2":
            webbrowser.open(streetbusiness['suftmSTB'].get("pSTB"))
                 
        case "3":
            webbrowser.open(streetbusiness['suftmSTB'].get("mSTB"))
        
        case "4":
            webbrowser.open(streetbusiness['suftmSTB'].get("gSTB"))
        
        case "5":
            webbrowser.open(streetbusiness['suftmSTB'].get("ggSTB"))

        case "6":
            webbrowser.open(streetbusiness['suftmSTB'].get("exgSTB"))

        case "7":
            webbrowser.open(streetbusiness['suftmSTB'].get("exggSTB"))


def clsSTB():

    print("\n---CLASS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(streetbusiness['classtmSTB'].get("p"))
            
            
        case "2":
            webbrowser.open(streetbusiness['classtmSTB'].get("m"))
                 

        case "3":
            webbrowser.open(streetbusiness['classtmSTB'].get("g"))
        

        case "4":
            webbrowser.open(streetbusiness['classtmSTB'].get("gg"))
        

        case "5":
            webbrowser.open(streetbusiness['classtmSTB'].get("exg"))
  



