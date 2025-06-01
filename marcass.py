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
  
  
  
def pietWGS():
    print("\n---PIET----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(wallsGeneralStore['pietWGS'].get("p"))
              
        case "2":
            webbrowser.open(wallsGeneralStore['pietWGS'].get("m"))
                 
        case "3":
            webbrowser.open(wallsGeneralStore['pietWGS'].get("g"))
        
        case "4":
            webbrowser.open(wallsGeneralStore['pietWGS'].get("gg"))
        
        case "5":
            webbrowser.open(wallsGeneralStore['pietWGS'].get("exg"))

def barracrewWGS():
    print("\n---BARRACREW----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(wallsGeneralStore['barracrewWGS'].get("p"))
              
        case "2":
            webbrowser.open(wallsGeneralStore['barracrewWGS'].get("m"))
                 
        case "3":
            webbrowser.open(wallsGeneralStore['barracrewWGS'].get("g"))
        
        case "4":
            webbrowser.open(wallsGeneralStore['barracrewWGS'].get("gg"))
        
        case "5":
            webbrowser.open(wallsGeneralStore['barracrewWGS'].get("egg"))

def madWGS():
    print("\n---MAD ENLATADOS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(wallsGeneralStore['madWGS'].get("p"))
              
        case "2":
            webbrowser.open(wallsGeneralStore['madWGS'].get("m"))
                 
        case "3":
            webbrowser.open(wallsGeneralStore['madWGS'].get("g"))
        
        case "4":
            webbrowser.open(wallsGeneralStore['madWGS'].get("gg"))
        
        case "5":
            webbrowser.open(wallsGeneralStore['madWGS'].get("exg"))

def classWGS():
    print("\n---CLASS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(wallsGeneralStore['classWGS'].get("p"))
            
            
        case "2":
            webbrowser.open(wallsGeneralStore['classWGS'].get("m"))
                 

        case "3":
            webbrowser.open(wallsGeneralStore['classWGS'].get("g"))
        

        case "4":
            webbrowser.open(wallsGeneralStore['classWGS'].get("gg"))
        

        case "5":
            webbrowser.open(wallsGeneralStore['classWGS'].get("exg"))
            
            
            
def pallaworldDPC():
    print("\n---PALLA WORLD----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(dropcompany['pallaworldDPC'].get("p"))
              
        case "2":
            webbrowser.open(dropcompany['pallaworldDPC'].get("m"))
                 
        case "3":
            webbrowser.open(dropcompany['pallaworldDPC'].get("g"))
        
        case "4":
            webbrowser.open(dropcompany['pallaworldDPC'].get("gg"))

def eghoDPC():
    print("\n---EGHO----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(dropcompany['eghoDPC'].get("p"))
              
        case "2":
            webbrowser.open(dropcompany['eghoDPC'].get("m"))
                 
        case "3":
            webbrowser.open(dropcompany['eghoDPC'].get("g"))
        
        case "4":
            webbrowser.open(dropcompany['eghoDPC'].get("gg"))

def madDPC():
    print("\n---MAD ENLATADOS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(dropcompany['madDPC'].get("p"))
              
        case "2":
            webbrowser.open(dropcompany['madDPC'].get("m"))
                 
        case "3":
            webbrowser.open(dropcompany['madDPC'].get("g"))
        
        case "4":
            webbrowser.open(dropcompany['madDPC'].get("gg"))

def barracrewDPC():
    print("\n---BARRACREW----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(dropcompany['barracrewDPC'].get("p"))
              
        case "2":
            webbrowser.open(dropcompany['barracrewDPC'].get("m"))
                 
        case "3":
            webbrowser.open(dropcompany['barracrewDPC'].get("g"))
        
        case "4":
            webbrowser.open(dropcompany['barracrewDPC'].get("gg"))

def classDPC():
    print("\n---CLASS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(dropcompany['classDPC'].get("p"))
              
        case "2":
            webbrowser.open(dropcompany['classDPC'].get("m"))
                 
        case "3":
            webbrowser.open(dropcompany['classDPC'].get("g"))
        
        case "4":
            webbrowser.open(dropcompany['classDPC'].get("gg"))

def pallaDPC():
    print("\n---ALL DPC----")
    print("1-PALLA WORLD\n2-EGHO\n3-MAD ENLATADOS\n4-BARRACREW\n5-CLASS")
    c=input("Opção: ")

    match c:

        case "1":
            pallaworldDPC()
              
        case "2":
            eghoDPC()
                 
        case "3":
            madDPC()
        
        case "4":
            barracrewDPC()
        
        case "5":
            classDPC()



def allSTB():
    print("\n---ALL STREET BUSINESS----")
    print("1-TAKEOFF\n2-MAD ENLATADOS\n3-SUFGANG\n4-CLASS\n5-Pesquisar")
    c=input("Opção: ")

    match c:

        case "1":
            takeoffSTB()
              
        case "2":
            madSTB()
                 
        case "3":
            sufSTB()
        
        case "4":
            clsSTB()
        case '5':
            pesquisa=input("Digite o que deseja pesquisar: ")
            pesquisacerta = pesquisa.replace(" ", "+")
            webbrowser.open('https://streetbusiness.com.br/search/?q='+pesquisacerta)
            

def allWGS():
    print("\n---ALL WALLS GENERAL STORE----")
    print("1-PIET\n2-BARRACREW\n3-MAD ENLATADOS\n4-CLASS")
    c=input("Opção: ")

    match c:

        case "1":
            pietWGS()
              
        case "2":
            barracrewWGS()
                 
        case "3":
            madWGS()
        
        case "4":
            classWGS()
        case '5':
            pesquisa=input("Digite o que deseja pesquisar: ")
            pesquisacerta = pesquisa.replace(" ", "+")
            webbrowser.open('https://www.wallsgeneralstore.com.br/loja/busca.php?loja=690339&palavra_busca='+pesquisacerta)
            

def allDPC():
    print("\n---ALL DROP COMPANY----")
    print("1-PALLA WORLD\n2-EGHO\n3-MAD ENLATADOS\n4-BARRACREW\n5-CLASS")
    c=input("Opção: ")

    match c:

        case "1":
            pallaworldDPC()
              
        case "2":
            eghoDPC()
                 
        case "3":
            madDPC()
        
        case "4":
            barracrewDPC()
        
        case "5":
            classDPC()
        case '6':
            pesquisa=input("Digite o que deseja pesquisar: ")
            pesquisacerta = pesquisa.replace(" ", "+")
            webbrowser.open('https://www.dropcompanybr.com/search/?q='+pesquisacerta)
            

def all():
    print("\n---ALL SITES----")
    print("1-STREET BUSINESS\n2-WALLS GENERAL STORE\n3-DROP COMPANY")
    c=input("Opção: ")

    match c:

        case "1":
            allSTB()
              
        case "2":
            allWGS()
                 
        case "3":
            allDPC()
            


