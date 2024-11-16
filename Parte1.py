import psutil

lista_nombre = []
nombre_proceso = 'a'
terminado = False
while nombre_proceso != '':
    print('Dale al enter para salir')
    print('Dame los nombre del proceso que desee encontrar')
    nombre_proceso = input()
    lista_nombre.append(nombre_proceso)
lista_nombre.pop(len(lista_nombre)-1)
try:
    for proceso in psutil.process_iter(['name','pid', 'memory_percent']):
      for nombre in lista_nombre:
         if nombre.lower() in proceso.info['name'].lower() :
             print('Nombre', proceso.info['name'],'--ID' ,proceso.info['pid'],'--Memoria', proceso.info['memory_percent'])
except (psutil.NoSuchProcess):
        print ('ERROR: no existe ese id del proceso')
except (psutil.AccessDenied):
        print ('ERROR: no tienes acceso para matar este proceso')


print('¿Quieres terminar algún proceso?')
respuesta = input()
if respuesta.lower() == 'si':
    print('Dame el nombre del proceso que desee terminar')
    nombre_proceso_terminar = input()
    try:
        for proc in psutil.process_iter(['name','pid']):
            nombre_proceso_Aterminar = proc.info['name']
            if  nombre_proceso_terminar.lower() in nombre_proceso_Aterminar.lower():
                proc.terminate()
                terminado = True
        if terminado:
            print('El proceso se ha terminado')
        else:
            print('ERROR: no se ha podido terminar')

    except (psutil.NoSuchProcess):
        print ('ERROR: no existe ese id del proceso')
    except (psutil.AccessDenied):
        print ('ERROR: no tienes acceso para matar este proceso')