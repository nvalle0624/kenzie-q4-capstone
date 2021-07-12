from django.shortcuts import render
from training_sessions.models import Session
from django.contrib.auth.decorators import login_required


@login_required
def calendar(request):
    User = request.user
    appointments = Session.object.filter(user=User)
    return render(request, 'schedule.html', {'appointments': appointments})

    ''' 
    PSUEDOCODE
    ___________________
    
    if user == admin:
        sessions = sessions.object.all()
        return render(request, 'schedule.html', {'sessions':sessions})  
    elif user == trainer:
        User = user.id
        sessions = sessions.object.filter(trainer=User)
        return render(request, 'schedule.html', {'sessions':sessions})   
    else:
        User = user.id
        appointments = sessions.object.filter(user=User)
        return render(request, 'schedule.html', {'sessions':sessions})
    '''
