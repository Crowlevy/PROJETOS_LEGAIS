def celsius(celsius):
    return (celsius*9/5)
def fahrenheit(fh):
    return (fh -32)*5/9
def metros(metros):
    return metros* 3.281
def pes(pes):
    return pes/ 3.281
def quilograma(quilograma):
    return quilograma*2.205
def libra(libra):
    return libra/2.205

print("ESSE É UM CONVERSOR DE MEDIDAS")
while True:
    pergunta=int(input("O QUE VOCÊ QUER CONVERTER [1]TEMPERATURA [2]PESO [3]COMPRIMENTO: "))

    if pergunta==1:
        escolha_temp=int(input("Deseja [1]FAHRENHEIT PARA CELSIUS [2]CELSIUS PARA FAHRENHEIT: "))
        if escolha_temp==1:
            graus=float(input("COLOQUE OS GRAUS EM FAHRENHEIT: "))
            transform= fahrenheit(graus)
            print(f'ISSO DÁ {transform:.2f}°C')
        elif escolha_temp==2:
            graus=float(input("COLOQUE OS GRAUS EM CELSIUS: "))
            transform= celsius(graus)
            print(f'ISSO DÁ {transform:.2f}°F')
        else:
            print("OPÇÃO INVÁLIDA")
            

    elif pergunta==2:
        escolha_peso=int(input("DESEJA CONVERTER [1]QUILOGRAMA PARA LIBRA [2]LIBRA PARA QUILOGRAMA: "))
        if escolha_peso==1:
            peso_kg=float(input("COLOQUE O VALOR EM QUILOGRAMA: "))
            libras=quilograma(peso_kg)
            print(f"{peso_kg}KG´S EM LIBRAS É {libras:.2f}")       
        if escolha_peso==2:
            peso_libra=float(input("COLOQUE O VALOR EM LIBRAS: "))
            kg=libra(peso_libra)
            print(f"{peso_libra} LIBRAS EM QUILOGRAMAS É {kg:.2f}") 

    elif pergunta==3:
        escolha_comp=int(input("DESEJA CONVERTER [1]METROS PARA PÉS [2]PÉS PARA METROS: "))
        if escolha_comp==1:
            medida=float(input("COLOQUE O COMPRIMENTO EM METROS: "))
            convert=metros(medida)
            print((f'SÃO {medida} METROS E {convert:.2f} PÉS'))
        elif escolha_comp==2:
            medida=float(input("COLOQUE O COMPRIMENTO EM PÉS: "))
            convert=metros(medida)
            print(f'SÃO {medida} PÉS E {convert:.2f} METROS')
        else:
            print("OPÇÃO INVÁLIDA")
    else:
        print("COLOQUE UMA OPÇÃO VÁLIDA")
    sair=str(input("DESEJA SAIR: S/N: ")).upper()

    if sair !='N':
        print('\033[1;32mEncerrando o programa...\033[m')
        break
        