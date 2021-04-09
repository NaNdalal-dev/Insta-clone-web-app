from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .InstaGram import getIgProfile, featured, getFollowList
from instaloader import ProfileNotExistsException, ConnectionException

def home(request):
	popAcc = featured()
	popAcc = popAcc.popularcelebs()

	return render(request,"home.html",{'title':'Instagram clone','popAcc':popAcc, 'getFollowList':getFollowList})

def getUser(request):
	try:

		user = request.GET['uname']
		profile = getIgProfile(user)
		details = {
			'title':f"{user}",
			'uname' : user,
			'profile':profile
		}
		return render(request, "profile.html", details)

	except ConnectionException:
		return render(request, 'ConnectionError.html',{'title':'No Connection'})

	except ProfileNotExistsException:
		return render(request, "profileNotFound.html",{'title':'Not found'})
