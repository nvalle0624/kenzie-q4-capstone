from django.shortcuts import render


def calendar(request):
    ''' 
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
