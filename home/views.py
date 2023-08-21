from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):

    peoples=[
        {'name':'Kushagra','age':25},
        {'name':'Sohan','age':24}
    ]

    text="hi this is a sample text"
    return render(request,"home/index.html", context={'peoples':peoples,'text':text})



def success_page(request):
    print('*'*10)
    return HttpResponse("""<h1>Hey, this is a success page.</h1>
    <p>Hey this is coming from the Django server
    <hr><p> hope you are loving it</p>""")

def test_page(request):
    print("Hi Testing")
    return HttpResponse("othiing")