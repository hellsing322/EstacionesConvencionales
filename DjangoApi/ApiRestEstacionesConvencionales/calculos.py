import sys
import os
import django,pathlib

ruta = pathlib.Path(__file__).parent.absolute()
ruta=str(str(ruta))
caracter= '\\'
reemplazo="/"
ruta=ruta.replace(caracter, reemplazo)
caracter2='/ApiRestEstacionesConvencionales'
ruta=ruta.replace(caracter2, '')
sys.path.append(ruta)
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoApi.settings'
django.setup()
from ApiRestEstacionesConvencionales.models import *

from datetime import datetime,timedelta
import pytz
import datetime as datatime2
class Calculos():
    

    def precipitacion_suma_diaria_171481h(self):

           fecha_actual = datetime.now(pytz.timezone('America/Guayaquil'))
           fecha_dia_siguiente =fecha_actual+timedelta(1)
           fecha_actual=fecha_actual.strftime("%Y-%m-%d")
           fecha_dia_gurdado=fecha_dia_siguiente.strftime("%Y-%m-%d %h:%m:%s")
           fecha_dia_siguiente=fecha_dia_siguiente.strftime("%Y-%m-%d")
           
           id_estacion=T1714161H.objects.filter(fecha_ingreso__range=(fecha_actual+" 13:00:00",fecha_actual+" 13:59:59")).values('id_estacion')
           valor13h =T1714161H.objects.filter(fecha_ingreso__range=(fecha_actual+" 13:00:00",fecha_actual+" 13:59:59")).values('valor')
           valor19h =T1714161H.objects.filter(fecha_ingreso__range=(fecha_actual+" 19:00:00",fecha_actual+" 19:59:59")).values('valor')
           valor07hdiasiguiente =T1714161H.objects.filter(fecha_ingreso__range=(fecha_dia_siguiente+" 07:00:00",fecha_dia_siguiente+" 07:59:59")).values('valor')
           
           for a in id_estacion:
                    estacion=a['id_estacion']


           if valor13h.exists()==True :
               for a in valor13h:
                    valor1=a['valor']
           else:
                valor1='no existe valor 13 horas '
                return (valor1)

           if valor19h.exists()==True :
               for a in valor19h:
                    valor2=a['valor']
           else:
                valor2='no existe valor 19 horas'
                return (valor2)

           if valor07hdiasiguiente.exists()==True :
               for a in valor07hdiasiguiente:
                    valor3=a['valor']
           else:
                valor3='no existe valor 07 horas dia siguiente'
                return (valor3)
          

           valor=valor1+valor2+valor3
           
           objeto = T171481H()
           objeto.id_estacion=estacion
           objeto.id_usuario=0
           objeto.fecha_ingreso=fecha_dia_gurdado
           objeto.valor=valor
           objeto.validado=False
           objeto.save()

           
    def calculo_evaporacion_diaria_1294161d(self):
        fecha_actual = datetime.now(pytz.timezone('America/Guayaquil'))
        fecha_actual=fecha_actual.strftime("%Y-%m-%d")
        id_estacion=T1714161H.objects.filter(fecha_ingreso__range=(fecha_actual+" 13:00:00",fecha_actual+" 13:59:59")).values('id_estacion')
        valor07hprec =T1714161H.objects.filter(fecha_ingreso__range=(fecha_actual+" 07:00:00",fecha_actual+" 07:59:59")).values('valor')
        valor13h_agua_sacada =T614161H.objects.filter(fecha_ingreso__range=(fecha_actual+" 13:00:00",fecha_actual+" 13:59:59")).values('valor')
        valor19h_agua_añadida =T775161D.objects.filter(fecha_ingreso__range=(fecha_actual+" 19:00:00",fecha_actual+" 19:59:59")).values('valor')
        
        if valor07hprec.exists()==True :
               for a in valor07hprec:
                    valor1=a['valor']
        else:
                valor1='no existe valor 07 horas'
                return (valor1)

        if valor13h_agua_sacada.exists()==True :
               for a in valor13h_agua_sacada:
                    valor2=a['valor']
        else:
                valor2='no existe valor 13 horas'
                return (valor2)

        if valor19h_agua_añadida.exists()==True :
               for a in valor19h_agua_añadida:
                    valor3=a['valor']
        else:
                valor3='no existe valor 19 horas'
                return (valor3)
          

        valor=valor1-(valor2/20)+(valor3/20)
        objeto = T614161H()
        objeto.id_estacion=estacion
        objeto.id_usuario=0
        objeto.fecha_ingreso=fecha_dia_gurdado
        objeto.valor=valor
        objeto.validado=False
        objeto.save()
           
    

principal=Calculos()
print(principal.precipitacion_suma_diaria_171481h())



           
           