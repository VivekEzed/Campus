from django.shortcuts import render
from django.http import HttpResponse
from campus_admin.models import Offers,Posts,Points,Login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=('renderloginpage'))
def user_homepage(request):
	objoffers=Offers.objects.all()
	objposts=Posts.objects.all()
	return render(request,'user_index.html',{'offerss':objoffers,'postss':objposts})


@login_required(login_url=('renderloginpage'))
def load_offerspage(request):
	objoffers=Offers.objects.all()
	count=len(objoffers)
	if count>0:
		return render(request,'user_offers.html',{'offers':objoffers})
	else:
		message="No records found"
		return render(request,'user_offers.html',{'msg':message})
	
@login_required(login_url=('renderloginpage'))
def load_postspage(request):
	objposts=Posts.objects.all()
	count=len(objposts)
	if count>0:
		return render(request,'user_posts.html',{'postss':objposts})
	else:
		message="No records found"
		return render(request,'user_posts.html',{'msg':message})
	
@login_required(login_url=('renderloginpage'))
def load_pointstspage(request):
	objpoints=Points.objects.all()
	count=len(objpoints)
	if count>0:
		return render(request,'user_points.html',{'pointss':objpoints})
	else:
		message="No records found"
		return render(request,'user_points.html',{'msg':message})

@login_required(login_url=('renderloginpage'))
def load_yourprofile(request):
	em=request.session['useremail']
	objlogin=Login.objects.get(email=em)
	# return HttpResponse(em)
	return render(request,'yourprofile.html',{'profile':objlogin})