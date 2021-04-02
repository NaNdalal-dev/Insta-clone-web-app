from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseBadRequest
from .InstaGram import getIgProfile
from instaloader import ProfileNotExistsException
def home(request):
	return render(request,"home.html",{'title':'Instagram clone'})
def getUser(request):
	try:

		user = request.GET['uname']
		profile = getIgProfile(user)
		details = {
			'title':f"{user}",
			'uname' : user,
			'profile':profile
		}
		print(type(profile.exURL))
		return render(request,"profile.html",details)
	except ProfileNotExistsException:
		return HttpResponse(ProfileNotExistsException)
