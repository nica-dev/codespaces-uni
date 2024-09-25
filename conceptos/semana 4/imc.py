def calcular_imc(peso_kg, altura_m):
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

cant_personas = int(input("Ingrese la cantidad de personas"))