import random
import time


def escaneo_pendejez():
    print("Mantén oprimido el espacio para escanearte...")
    input("Presiona la tecla espacio y mantenla presionada...")

    print("\nEscaneando...\n")
    # Simula un escaneo que dura entre 2 y 5 segundos
    time.sleep(random.uniform(2, 5))

    porcentaje_pendejez = random.randint(0, 100)
    print(f"Pendejez detectada: {porcentaje_pendejez}%\n")

    if porcentaje_pendejez < 30:
        print("¡Felicidades! Eres un genio.")
    elif porcentaje_pendejez < 60:
        print(
            "Eres un poco pendejo, pero no te preocupes, todos lo somos en algún momento.")
    else:
        print("¡Alerta! Niveles de pendejez críticos. Necesitas ayuda.")


if __name__ == "__main__":
    escaneo_pendejez()
