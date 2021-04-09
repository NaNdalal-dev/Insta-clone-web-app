from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .InstaGram import getIgProfile, featured
from instaloader import ProfileNotExistsException, ConnectionException

def home(request):
	'''acc = featured()
				popAcc = acc.popularcelebs()
				fash = acc.fashionPages()
				print(fash)
				accDetails = {
						'title':'Instagram clone',
						'popAcc':popAcc,
						'fashionPages':fash
						}'''

	return render(request,"home.html",{'title':'Instagram'})

def getUser(request):
	try:

		user = request.GET['uname']
		profile = getIgProfile(user)
		fash = f
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
