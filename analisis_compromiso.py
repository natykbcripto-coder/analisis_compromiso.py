# =============================================
# SISTEMA DE CLASIFICACIÓN DE COMPROMISO
# =============================================

def clasificar_compromiso(duracion: int, clics: int) -> str:
    """
    Clasifica el nivel de compromiso según las reglas de negocio.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_informe(datos):
    """Genera y muestra el informe de compromiso."""
    print("="*50)
    print("INFORME DE NIVEL DE COMPROMISO")
    print("="*50)
    print(f"{'ID Cliente':<12} {'Duración(s)':<12} {'Clics':<8} {'Clasificación':<10}")
    print("-"*50)
    
    for sesion in datos:
        id_cliente, duracion, clics = sesion
        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12} {duracion:<12} {clics:<8} {clasificacion:<10}")
    
    print("="*50)


# ====================== DATOS DE PRUEBA ======================
datos_sesiones = [
    ["C001", 250, 12],
    ["C002", 45, 5],
    ["C003", 120, 6],
    ["C004", 200, 7],
    ["C005", 30, 2],
    ["C006", 90, 2],
    ["C007", 300, 15],
    ["C008", 55, 1]
]

# ====================== EJECUCIÓN ======================
if __name__ == "__main__":
    generar_informe(datos_sesiones)
