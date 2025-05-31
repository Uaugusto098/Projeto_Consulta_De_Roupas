import webbrowser
from sites_taamanhos import *
def takeoff():

    print("\n---TAKEOFF----")
    print("\n1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:XG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(takeofftm.get("p"))
              
        case "2":
            webbrowser.open(takeofftm.get("m"))
                 
        case "3":
            webbrowser.open(takeofftm.get("g"))
        
        case "4":
            webbrowser.open(takeofftm.get("gg"))
        
        case "5":
            webbrowser.open(takeofftm.get("xg"))


def mad():

    print("\n---MAD----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(madtm.get("pp"))
              
        case "2":
            webbrowser.open(madtm.get("p"))
                 
        case "3":
            webbrowser.open(madtm.get("m"))
        
        case "4":
            webbrowser.open(madtm.get("g"))
        
        case "5":
            webbrowser.open(madtm.get("gg"))

        case "6":
            webbrowser.open(madtm.get("exg"))

        case "7":
            webbrowser.open(madtm.get("exgg"))


def suf():

    print("\n---SUFGANG----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(suftm.get("ppSTB"))
              
        case "2":
            webbrowser.open(suftm.get("pSTB"))
                 
        case "3":
            webbrowser.open(suftm.get("mSTB"))
        
        case "4":
            webbrowser.open(suftm.get("gSTB"))
        
        case "5":
            webbrowser.open(suftm.get("ggSTB"))

        case "6":
            webbrowser.open(suftm.get("exgSTB"))

        case "7":
            webbrowser.open(suftm.get("exggSTB"))


def cls():

    print("\n---CLASS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(classtm.get("p"))
            
            
        case "2":
            webbrowser.open(classtm.get("m"))
                 

        case "3":
            webbrowser.open(classtm.get("g"))
        

        case "4":
            webbrowser.open(classtm.get("gg"))
        

        case "5":
            webbrowser.open(classtm.get("egg"))
  





