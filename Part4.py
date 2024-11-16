import subprocess
import pyclip
def con():
    p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    comandos = \
       [b"verbose\n",
        b"open ftp.freebsd.org\n",
        b"anonymous\n",
        b"password\n",
        b"get /pub/FreeBSD/README.TXT\n",]
    for cmd in comandos:
        p1.stdin.write(cmd)



    respuesta = p1.communicate(timeout=10)[0]
    print(respuesta.decode("cp850", "ignore"))

def comprobarArchivo():
    f = open("readme.txt", "r")
    texto = f.read()

    copiaPrevia = pyclip.paste()
    pyclip.copy(texto)

    if copiaPrevia != texto:
        print('El contenido ha cambiado')





opcion = "si"
while opcion == "si":
    con()
    comprobarArchivo()
    opcion = input("¿Te quieres volver a conectar? sí o no ")