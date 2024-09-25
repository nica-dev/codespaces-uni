def calcular_imc(peso_kg, altura_m):
    """Función que calcula el IMC de una persona"""
    
    # Calculamos el IMC
    IMC = peso_kg / (altura_m ** 2)

    # Por descarte la categoría sería Obesidad
    categoria = "Obesidad"

    if IMC < 18.5:
        categoria = "Bajo peso"
    elif IMC < 25:
        categoria = "Normal"
    elif IMC < 30:
        categoria = "Sobrepeso"

    print(f"Su IMC es {IMC}, su categoría es {categoria}.")

def main():
    """"Función principal"""
    cant_personas = int(input("Ingrese la cantidad de personas"))

    for i in cant_personas:
        # Solicitamos al usuario peso y altura
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        calcular_imc(peso, altura)

main()