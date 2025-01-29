from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import Manager
from ..forms.employee import *
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password



def create_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('manager:manager_list')
    else:
        form = ManagerForm()
    context = {'form': form}
    return render(request, 'manager/create.html', context)


def update_manager(request,id):
    manager=get_object_or_404(Manager,pk=id)
    if request.method=='POST':
        form=ManagerUpdateForm(request.POST,instance=manager)
        if form.is_valid():
            form.save()
            return redirect('manager:manager_list')
        else:
            context = {
                'form': form,
                'id':manager.id   
                       }
            return render(request, 'manager/update.html', context)
    form=ManagerUpdateForm(instance=manager)
    context={'form':form,
             'id':manager.id 
             }
    return render(request,'manager/update.html',context)

def manager_list(request):
    managers=Manager.objects.all()
    context={
        'managers':managers
    }
    return render(request,'manager/list.html',context)


def manager_change_password(request,id):
        manager=get_object_or_404(Manager,id=id)
        password=request.POST['password']
        manager.password=make_password(password)
        manager.save()
        return redirect('manager:update-manager',id)

def delete_manager(request,id):
     manager=get_object_or_404(Manager,id=id)
     manager.delete()
     return redirect('manager:manager_list')