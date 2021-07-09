from django.shortcuts import render, HttpResponseRedirect, reverse
from dogs.models import Dog
from dogs.forms import DogProfileForm
import os

# Create your views here.


def dog_profile_form_view(request):
    if request.method == 'POST':
        form = DogProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_dog = Dog.objects.create(
                name=data['name'],
                owner=data['owner'],
                breed=data['breed'],
                age_years=data['age_years'],
                age_months=data['age_months'],
                vet_name=data['vet_name'],
                vet_number=data['vet_number'],
                vet_address=data['vet_address'],
                special_needs=data['special_needs'],
                extra_notes=data['extra_notes'],
                img_media=data['img_media'],
                profile_pic=data['profile_pic'],
            )
            return HttpResponseRedirect(reverse('all_dogs_view'))
    form = DogProfileForm()
    return render(request, 'dog_profile_form.html', {'form': form})


def dog_profile_view(request, dog_id: int):
    dog = Dog.objects.get(id=dog_id)
    vids = []
    pics = []
    # from : https://www.codespeedy.com/how-to-iterate-over-files-in-a-given-directory-in-python/
    for subdirectories, directories, files in os.walk(r'./static/'):
        for file_name in files:
            file_loc = subdirectories + os.path.sep + file_name
            if file_loc.endswith(".m4v"):
                vids.append(file_loc)
            elif file_loc.endswith('.jpg'):
                pics.append(file_loc)
    # these next dozen lines are probably not the best way to do this, but it works for now
    vids_path = []
    pics_path = []
    prof_pic = ''
    for vid in vids:
        vids_path.append(vid[9:])
    for pic in pics:
        if pic.startswith('./static/profile/'):
            pics_path.append(pic[17:])
            prof_pic += pic[17:]
        else:
            pics_path.append(pic[9:])

    return render(request, 'dog_profile_view.html', {'dog': dog, 'pics_path': pics_path, 'vids_path': vids_path, 'prof_pic': prof_pic})


def all_dogs_view(request):
    all_dogs = Dog.objects.all()
    return render(request, 'all_dogs.html', {'dogs': all_dogs})
