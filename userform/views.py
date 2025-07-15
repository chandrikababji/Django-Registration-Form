from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'userform/thankyou.html')
    else:

        form=RegistrationForm()
    return render(request,'userform/register.html',{'form':form})    