import os
import sys


def main():

    fd = os.pipe()

    saludoPadre = "Hola buenas tardes.\n"

    pid = os.fork()

    if pid < 0:
        print("No se ha podido crear el proceso hijo...")
        sys.exit(1)

    elif pid == 0:


        mensaje = os.read(fd[0], 80).decode("utf-8")

        print(f"El hijo recibe algo del pipe: {mensaje}")
        os.write(fd[1],mensaje.upper().encode('utf-8'))

        os.close(fd[0])
        os.close(fd[1])
    else:



        os.write(fd[1], saludoPadre.encode("utf-8"))
        print("El padre envía un mensaje al hijo...")

        os.close(fd[1])

        os.wait()

        mensaje = os.read(fd[0], 80).decode("utf-8")
        print(mensaje)

        os.close(fd[0])
if __name__ == "__main__":
    main()
