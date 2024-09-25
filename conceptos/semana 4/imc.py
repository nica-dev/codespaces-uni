def calcular_imc(peso_kg, altura_m):
    """Función que calcula el IMC de una persona"""
    
    # Calculamos el IMC
    IMC = peso_kg / (altura_m ** 2)
    return IMC

def main():
    """"Función principal"""
    
    cant_personas = int(input("Ingrese la cantidad de personas"))

    for i in cant_personas:
        # Solicitamos al usuario peso y altura
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        imc = calcular_imc(peso, altura)

main()