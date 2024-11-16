import time
from os import system
import subprocess
import asyncio



def showNotepad1():
    try:
        TiempoCargaS = time.time()
        subprocess.run(['notepad.exe', ])
        TiempoFinS = time.time()
        TiempoTotalS = TiempoFinS - TiempoCargaS
        print(f'El programa ha tardado {TiempoTotalS}')
    except subprocess.CalledProcessError as e:

        print(e.output)
async def showNotepad2():
    try:
        TiempoCargaA = time.time()
        await asyncio.create_subprocess_exec('notepad.exe')
        TiempoFinalS = time.time()

        TiempoFinalA = TiempoFinalS - TiempoCargaA
        print(f'El programa ha tardado {TiempoFinalA}')
    except subprocess.CalledProcessError as e:
        print(e.output)


async def main():
    respuesta = 0

    while respuesta !="3":

        respuesta = input("""
Selecciona una de las dos opciones:
    1. Ejecución Síncrona
    2. Ejecución Asíncrona
    3. Salir
        """)
        if respuesta == "1":
            showNotepad1()
        elif respuesta == "2":
            await showNotepad2()
            system('Pause')

if __name__ == "__main__":
    asyncio.run(main())
