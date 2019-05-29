from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Login,Offers,Posts,Points
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import FileForm,FileFormPost
from datetime import datetime
import datetime
import time
from django.utils.timezone import localtime,now 
from django.contrib.auth import logout


# Create your views here.
def login_(request):
	return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html')

    

def loginpage(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		
		if user is not None:
			login(request,user)
			try:
				request.session['useremail']=user.username
				obj=Login.objects.get(email=username)
				if obj.account_type == "user":
					return HttpResponseRedirect('http://127.0.0.1:8000/campus/')
				else:
					return HttpResponse('error')
			except:
				
				return render(request,'admin_index.html',{})	

		else:
			message="-- Wrong Username or Password --"
			return render(request,'login.html',{'msg':message})
	else:
		return render(request,'login.html')

def homepage(request):
	return render(request,'admin_index.html')

@login_required(login_url='renderloginpage')
def load_memberspage(request):

	admin_homepage_membersobj=Login.objects.all()
	count=len(admin_homepage_membersobj)
	if count>0:
		return render(request,'members.html',{'membersobj':admin_homepage_membersobj})
	else:
		msg="No Records Found"
		return render(request,'members.html',{'membersobj':admin_homepage_membersobj,'message':msg})

@login_required
def addmembers(request):
	if request.method=="POST":
		if request.POST.get('firstname'):
			# post=Login()
			# post.name=request.POST.get('firstname')
			# post.email=request.POST.get('email')
			# post.contactnumber=request.POST.get('contactnumber')
			# post.college=request.POST.get('collegename')
			# post.place=request.POST.get('place')
			# post.password=request.POST.get('password')
			# post.save()
			user = User.objects.create_user(request.POST.get('email'),request.POST.get('email'),request.POST.get('password'))
			# user.email_address=request.POST.get('email')
			# user.password=request.POST.get('password')
			user.first_name=request.POST.get('firstname')
			user.last_name=request.POST.get('secondname')
			user.save()
			post=Login()
			post.firstname=request.POST.get('firstname')	
			post.secondname=request.POST.get('secondname')
			post.email=request.POST.get('email')
			post.contactnumber=request.POST.get('contactnumber')
			post.college=request.POST.get('collegename')
			post.place=request.POST.get('place')
			post.password=request.POST.get('password')
			post.account_type="user"
			post.save()
			message="New Member Added Successfully..!"
			return render(request,'addmembers.html',{'msg':message})		
	else:		
		return render(request,'addmembers.html')

@login_required(login_url=('renderloginpage'))
def membersfullinfo(request,id):
	fullinfoobj=Login.objects.get(id=id)
	return render(request,'members_info.html',{'membersdetails':fullinfoobj})

	# return HttpResponse(id)

def load(request):
	message="hello"
	return render(request,'members_info.html',{'msg':message})

@login_required(login_url=('renderloginpage'))
def load_offerspage(request):
	message="No Records Found..!"
	offerobj=Offers.objects.all()
	count=len(offerobj)

	if count>0:
		return render(request,'offers.html',{'offers':offerobj})
	else:
		return render(request,'offers.html',{'msg':message})

@login_required(login_url=('renderloginpage'))
def add_offers(request):
	if request.method=="POST":
		if request.POST.get('title'):
			form=FileForm(request.POST,request.FILES)
			if form.is_valid():
				post=Offers()
				post.title=request.POST.get('title')
				post.description=request.POST.get('description')
				post.image=request.FILES['image']
				post.save()
				message="New Offer Added Successfully..!"
				return render(request,'addofferspage.html',{'msg':message})
		else:
			
			return render(request,'addofferspage.html',{})
	else:
		return render(request,'addofferspage.html')

@login_required(login_url=('renderloginpage'))	
def load_postpage(request):
	message="No Records Found..!"
	postsobj=Posts.objects.all()
	count=len(postsobj)

	if count>0:
		return render(request,'posts_page.html',{'postss':postsobj})
	else:
		return render(request,'posts_page.html',{'msg':message})

@login_required(login_url=('renderloginpage'))
def add_postspage(request):
	if request.method=="POST":
		if request.POST.get('title'):
			form=FileFormPost(request.POST,request.FILES)
			if form.is_valid():
				post=Posts()
				post.title=request.POST.get('title')
				post.description=request.POST.get('description')
				post.image=request.FILES['image']
				post.save()
				message="New Post Added Successfully..!"
				return render(request,'add_postspage.html',{'msg':message})

		else:
			return render(request,'add_postspage.html')
	else:
		return render(request,'add_postspage.html')

@login_required(login_url=('renderloginpage'))
def load_pointspage(request):
	objpoints=Points.objects.all()
	count=len(objpoints)
	if count>0:
		return render(request,'pointspage.html',{'pointss':objpoints})
	else:
		msg="No Records Found"
		return render(request,'pointspage.html',{'message':msg})

@login_required(login_url=('renderloginpage'))
def load_addpointspage(request):
	if request.method=="POST":
		if request.POST.get('name'):
			post=Points()
			id=request.POST.get('name')
			namesobj=Login.objects.get(id=id)
			post.name_id=id
			post.name=namesobj.firstname+namesobj.secondname
			post.title=request.POST.get('title')
			post.point=request.POST.get('point')
			post.save()
			message="New Point Added Successfully"
			return render(request,'add_pointspage.html',{'msg':message})

	else:
		objname=Login.objects.all()
		return render(request,'add_pointspage.html',{'names':objname})

	