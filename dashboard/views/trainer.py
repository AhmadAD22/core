from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import Trainer
from ..forms.trainer import TrainerForm,TrainerUpdateForm
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password



def create_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('trainer:trainer_list')
    else:
        form = TrainerForm()
    context = {'form': form}
    return render(request, 'trainer/create.html', context)


def update_trainer(request,id):
    trainer=get_object_or_404(Trainer,pk=id)
    if request.method=='POST':
        form=TrainerUpdateForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer:trainer_list')
        else:
            context = {
                'form': form,
                'id':trainer.id   
                       }
            return render(request, 'trainer/update.html', context)
    form=TrainerUpdateForm(instance=trainer)
    context={'form':form,
             'id':trainer.id 
             }
    return render(request,'trainer/update.html',context)

def trainer_list(request):
    trainers=Trainer.objects.all()
    context={
        'trainers':trainers
    }
    return render(request,'trainer/list.html',context)


def trainer_change_password(request,id):
        trainer=get_object_or_404(Trainer,id=id)
        password=request.POST['password']
        trainer.password=make_password(password)
        trainer.save()
        return redirect('trainer:update-trainer',id)

def delete_trainer(request,id):
     trainer=get_object_or_404(Trainer,id=id)
     trainer.delete()
     return redirect('trainer:trainer_list')