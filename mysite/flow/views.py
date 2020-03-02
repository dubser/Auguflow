from django.shortcuts import render
import syslog,time
from django.http import HttpResponse

# Message de démarrage de Django

syslog.syslog(time.strftime("#%S: ",time.localtime())+"Django is starting.")

# Module auguflow.py controle le GPIO du Pi dans un Thread

from auguflow import AuguFlo

augfl = AuguFlo("Th_Auguflow")
augfl.start()
augfl.join

# Create your views here.

def test(request):

    a=''
    j=0
    for x,y in request.GET.items():
        n= ' '+x +'='+y
        a= a + n
        j=j+1
    if j==0:
        a= "Pas d'arguments"
    return HttpResponse("Hello, réponse du serveur >  " + a )

def exec(request):
    syslog.syslog("This is a SDU test message")
    return HttpResponse("Procédure exec running" )