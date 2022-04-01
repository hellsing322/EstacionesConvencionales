from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic import View

from rest_framework.parsers import JSONParser
from rest_framework import serializers

from ApiRestEstacionesConvencionales.models import *
from ApiRestEstacionesConvencionales.serializers import *

class Principal(View):

     def __init__(self, serial,model):

          self.s= serial
          self.m= model

     def post(self,request):
          data=JSONParser().parse(request)
          serializer=self.s(data=data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse('Se agrrego correctamente',safe=False)
          return   JsonResponse('No se pudo agregar ',safe=False)

     def get(self,request):

          data_model = self.m.objects.all()
          serializer=self.s(data_model,many=True)
          return JsonResponse(serializer.data,safe=False)

     def put(self,request):

          data=JSONParser().parse(request)
          data_model=self.m.objects.get(id_temp_int_baro=data['id_temp_int_baro'])
          serializer=self.s(data_model,data=data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse("Updated Successfully",safe=False)
          return JsonResponse("Failed to Update")

     def delete(self,request,id):
          data_model=self.m.objects.get(id_temp_int_baro=id)
          data_model.delete()
          return JsonResponse("Deleted Successfully",safe=False)

class T1073161HView(Principal):

     def __init__(self):
          Principal.__init__(self,T1073161HSerializer,T1073161H)

class T1073161HValView(Principal):

    def __init__(self):
         Principal.__init__(self,T1073161HValSerializer,T1073161HVal)

class T1123161HView(Principal):

        def __init__(self):
             Principal.__init__(self,T1123161HSerializer,T1123161H)

class T1123161HValView(Principal):

        def __init__(self):
             Principal.__init__(self,T1123161HValSerializer,T1123161HVal)

class T1263011DView(Principal):

        def __init__(self):
             Principal.__init__(self,T1263011DSerializer,T1263011D)

class T1263011MView(Principal):

    def __init__(self):
         Principal.__init__(self,T1263011MSerializer,T1263011M)

class T1263021DView(Principal):

    def __init__(self):
         Principal.__init__(self,T1263021DSerializer,T1263021D)

class T1263021MView(Principal):

    def __init__(self):
         Principal.__init__(self,T1263021MSerializer,T1263021M)

class T1263041DView(Principal):

    def __init__(self):
         Principal.__init__(self,T1263041DSerializer,T1263041D)

class T1263041MView(Principal):

    def __init__(self):
         Principal.__init__(self,T1263041MSerializer,T1263041M)

class T12827161DView(Principal):

    def __init__(self):
         Principal.__init__(self,T12827161DSerializer,T12827161D)

class T12827161HView(Principal):

    def __init__(self):
             Principal.__init__(self,T12827161HSerializer,T12827161H)

class T12827161HValView(Principal):

    def __init__(self):
         Principal.__init__(self,T12827161HValSerializer,T12827161HVal)

class T12827161MView(Principal):

    def __init__(self):
        Principal.__init__(self,T12827161MSerializer,T12827161M)

class T13028161DView(Principal):

    def __init__(self):
        Principal.__init__(self,T13028161DSerializer,T13028161D)

class T13028161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T13028161HSerializer,T13028161H)

class T13028161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T13028161HValSerializer,T13028161HVal)

class T13028161MView(Principal):

    def __init__(self):
        Principal.__init__(self,T13028161MSerializer,T13028161M)

class T141011DView(Principal):

    def __init__(self):
        Principal.__init__(self,T141011DSerializer,T141011D)

class T141011MView(Principal):

    def __init__(self):
        Principal.__init__(self,T141011MSerializer,T141011M)

class T1410161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T1410161HSerializer,T1410161H)

class T1410161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T1410161HValSerializer,T1410161HVal)

class T141021DView(Principal):

    def __init__(self):
        Principal.__init__(self,T141021DSerializer,T141021D)

class T141021MView(Principal):

    def __init__(self):
        Principal.__init__(self,T141021MSerializer,T141021M)

class T141041DView(Principal):

    def __init__(self):
        Principal.__init__(self,T141041DSerializer,T141041D)

class T141041MView(Principal):

    def __init__(self):
        Principal.__init__(self,T141041MSerializer,T141041M)

class T1714161DView(Principal):

    def __init__(self):
         Principal.__init__(self,T1714161DSerializer,T1714161D)

class T1714161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T1714161HSerializer,T1714161H)

class T1714161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T1714161HValSerializer,T1714161HVal)

class T171481DView(Principal):

    def __init__(self):
         Principal.__init__(self,T171481DSerializer,T171481D)

class T171481HView(Principal):

    def __init__(self):
        Principal.__init__(self,T171481HSerializer,T171481H)

class T171481HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T171481HValSerializer,T171481HVal)

class T171481MView(Principal):

    def __init__(self):
        Principal.__init__(self,T171481MSerializer,T171481M)

class T187161DView(Principal):

    def __init__(self):
        Principal.__init__(self,T187161DSerializer,T187161D)

class T187161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T187161HSerializer,T187161H)

class T187161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T187161HValSerializer,T187161HVal)

class T261111DView(Principal):

    def __init__(self):
        Principal.__init__(self,T261111DSerializer,T261111D)

class T261111MView(Principal):

    def __init__(self):
        Principal.__init__(self,T261111MSerializer,T261111M)

class T272981DView(Principal):

    def __init__(self):
        Principal.__init__(self,T272981DSerializer,T272981D)

class T272981HView(Principal):

    def __init__(self):
        Principal.__init__(self,T272981HSerializer,T272981H)

class T272981HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T272981HValSerializer,T272981HVal)

class T272981MView(Principal):

    def __init__(self):
        Principal.__init__(self,T272981MSerializer,T272981M)

class T293161DView(Principal):

    def __init__(self):
        Principal.__init__(self,T293161DSerializer,T293161D)

class T293161MView(Principal):

    def __init__(self):
        Principal.__init__(self,T293161MSerializer,T293161M)

class T29321MView(Principal):

    def __init__(self):
        Principal.__init__(self,T29321MSerializer,T29321M)

class T3211DView(Principal):

    def __init__(self):
        Principal.__init__(self,T3211DSerializer,T3211D)

class T3211MView(Principal):

    def __init__(self):
        Principal.__init__(self,T3211MSerializer,T3211M)

class T323161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T323161HSerializer,T323161H)

class T323161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T323161HValSerializer,T323161HVal)

class T32321DView(Principal):

    def __init__(self):
        Principal.__init__(self,T32321DSerializer,T32321D)

class T32321MView(Principal):

    def __init__(self):
        Principal.__init__(self,T32321MSerializer,T32321M)

class T3711161DView(Principal):

    def __init__(self):
        Principal.__init__(self, T3711161DSerializer, T3711161D)

class T3711161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T3711161HSerializer, T3711161H)

class T3711161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T3711161HValSerializer, T3711161HVal)

class T42161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T42161HSerializer, T42161H)

class T42161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T42161HValSerializer, T42161HVal)

class T573161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T573161HSerializer, T573161H)

class T573161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T573161HValSerializer, T573161HVal)

class T583161HView(Principal):

    def __init__(self):
         Principal.__init__(self,T583161HSerializer, T583161H)

class T583161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T583161HValSerializer, T583161HVal)

class T597161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T597161HSerializer, T597161H)

class T597161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T597161HValSerializer, T597161HVal)

class T603161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T603161HSerializer, T603161H)

class T603161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T603161HValSerializer, T603161HVal)

class T613161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T613161HSerializer, T613161H)

class T613161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T613161HValSerializer, T613161HVal)

class T614161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T614161HSerializer, T614161H)

class T614161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T614161HValSerializer, T614161HVal)

class T621161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T621161HSerializer, T621161H)

class T621161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T621161HValSerializer, T621161HVal)

class T644161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T644161HSerializer, T644161H)

class T644161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T644161HValSerializer, T644161HVal)

class T7127161DView(Principal):

    def __init__(self):
        Principal.__init__(self,T7127161DSerializer, T7127161D)

class T7127161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T7127161HSerializer, T7127161H)

class T7127161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T7127161HValSerializer, T7127161HVal)

class T7127161MView(Principal):

    def __init__(self):
        Principal.__init__(self,T7127161MSerializer, T7127161M)

class T7229161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T7229161HSerializer, T7229161H)

class T7229161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T7229161HValSerializer, T7229161HVal)

class T734161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T734161HSerializer, T734161H)

class T734161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T734161HValSerializer, T734161HVal)

class T775161DView(Principal):

    def __init__(self):
        Principal.__init__(self,T775161DSerializer, T775161D)

class T91161DView(Principal):

    def __init__(self):
        Principal.__init__(self,T91161DSerializer, T91161D)

class T91161HView(Principal):

    def __init__(self):
        Principal.__init__(self,T91161HSerializer, T91161H)

class T91161HValView(Principal):

    def __init__(self):
        Principal.__init__(self,T91161HValSerializer, T91161HVal)

class T91161MView(Principal):

    def __init__(self):
        Principal.__init__(self,T91161MSerializer, T91161M)
