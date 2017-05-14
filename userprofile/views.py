from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from forms import UserProfileForm

def user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/account/loggedin/")
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
            
    args = {}
    args.update(csrf(request))
    args['form'] = form
        
    return render(request, "user_profile.html", args)
    