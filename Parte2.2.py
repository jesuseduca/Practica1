import os
import string
import sys




def main():

    fd = os.pipe()

    pid = os.fork()

    if pid < 0:
        print("No se ha podido crear el proceso hijo...")
        sys.exit(1)

    elif pid == 0:
    #Lo que hace el hijo

        mensaje = os.read(fd[0], 80).decode("utf-8")
        os.close(fd[0])


        num_linea = len(mensaje.split("/n"))
        palabras = 0

        for linea in mensaje.split("/n"):
            palabras += len(linea.split())

        mensaje_Archivo = f"{palabras},{num_linea}"


        os.write(fd[1],mensaje_Archivo.encode('utf-8'))
        print(f"El hijo recibe algo del pipe: {mensaje_Archivo}")

        os.close(fd[1])
    else:
    #Lo que hace el padre
        mensaje_enviar = """ Hola hijo
        espero que te vaya bien
        mucho animo 
        un abrazo, tu padre """


        os.write(fd[1],mensaje_enviar.encode("utf-8"))

        print("El padre envía un mensaje al hijo...")

        os.close(fd[1])

        os.wait()

        mensaje_P = os.read(fd[0], 80).decode("utf-8")

        palabras, lineas = string.split(",")

        os.close(fd[0])
        print(f"El mensaje tiene una cantidad de {lineas} lineas y una cantidad total de {palabras} palabras ")


if __name__ == "__main__":
    main()