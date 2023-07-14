from django.shortcuts import render , redirect
from django.http import JsonResponse
from . forms import SignUpForm
from django.contrib.auth import login
#from core.chat import get_response

#from core.chat import get_response
def frontpage(request):
    #text = request.POST.get('message')
    #response = get_response(text)
    #message = {"answer":response}
    #context = JsonResponse(message)
    return render(request,template_name='core/frontpage.html')
    

def signup(request):
    
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('frontpage')
         
    else:
        form=SignUpForm()
    return render(request,'core/signup.html',{'form':form})
