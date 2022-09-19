from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from io import StringIO


# Create your views here.

def index(request):
#    print(request)

    command5 = "docker ps --format '{{.Names}}'"
    returned_text = subprocess.check_output(command5, shell=True, universal_newlines=True)
    i = 1
    s = StringIO()

    for row in returned_text.split('\n'): 
        command = "docker inspect " + row + " | grep Host | grep traefik"
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
        p.wait()  
        if p.returncode != 1:  
            returned_text_for = subprocess.check_output(command, shell=True, universal_newlines=True)
            x = returned_text_for.split(":")
            y = x[1].split(",")
            index = y[0].find("||")
            if index == -1:
                z = y[0].split("`")
                print (f"{i:>3} Container name = {row:30} \t/ URL (one) = https://{z[1]:40}<br/>", file=s)
                i+=1
            else: 
                z = y[0].split("|")
                zz = z[0].split("`")
                zzz = z[2].split("`")  
                print (f"{i:>3} Container name = {row:30} \t/ URL (any) = https://{zz[1]:40} ### https://{zzz[1]}<br/>", file=s)
                i+=1
    
    result = s.getvalue()
    return HttpResponse(result)
