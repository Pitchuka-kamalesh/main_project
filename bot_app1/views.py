from django.shortcuts import redirect,render
from .forms import Treatment_Form
from .models import Treatment_Model
# Create your views here.

def home(request):
    form = Treatment_Form()
    if request.method == 'POST':
        form = Treatment_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('home')
    data = Treatment_Model.objects.all()
    context = {"form":form,"datas":data}
    return render(request,'bot_app1/home.html',context)

