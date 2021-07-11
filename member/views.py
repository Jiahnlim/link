from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
# Create your views here.
def main(request):
    template = loader.get_template( "main.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )
    
def profile(request):
    template = loader.get_template( "profile.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )
    
def login(request):
    template = loader.get_template( "login.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )
    
def signup(request):
    template = loader.get_template( "signup.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )
    