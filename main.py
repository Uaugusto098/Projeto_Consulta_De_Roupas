from marcass import *
print("\n          Consulta de roupas")
print("\nMarcas disponiveis:Sufgang,Class,Mad,Takeoff\n")
inicio=1

while inicio==1:
    print('''       -----MARCAS-----
        1-SUFGANG
        2-TAKEOFF
        3-CLASS
        4-MAD ENLATADOS
        0-sair
      ''')
    
    c=input("Opção: ")
    match c:
        case'0':
            break

        case'1':
            streetbusines(sufSTB)
        
        case'2':
            takeoffSTB()

        case'3':
            clsSTB()

        case'4':
            madSTB()










        # case'5':
        #     variavel=input("digite o termo a ser pesquisado")
        #     pesquisa = variavel.replace(' ','+')
        #     webbrowser.open('https://www.wallsgeneralstore.com.br/loja/busca.php?loja=690339&palavra_busca='+pesquisa)         

        