from django.shortcuts import render
from django.http import HttpResponse

from awsapp.login import LoginForm, SignUpForm, KeyForm, AwsInstance, UnknownForm

from awsapp.models import Employee, Credentials
from django.template import RequestContext

import boto3


def hello(request):
   return render(request,"awsapp/home.html",{})


def login(request):
   message = ""
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'awsapp/config.html', {'username':username})
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         username = form.cleaned_data['email']
         password = form.cleaned_data['password']
         if Employee.objects.filter(email=username, password=password).exists():
            request.session['username']=username
            return render(request, 'awsapp/config.html', {"username" : username})
         message = "Invalid Email-ID or Password!!! Please Try Again."
         return render(request,'awsapp/home.html',{'form':form, 'message':message})
   else:
      form = LoginForm()
   return render(request,'awsapp/home.html',{'form':form})


def signup(request):
   message = ""
   if request.method == 'POST':
      sform = SignUpForm(request.POST)
      if sform.is_valid():
         #Employee.objects.filter(fname = "ayush").delete()
         fname = sform.cleaned_data['fname']
         mobile = sform.cleaned_data['mobile']
         email = sform.cleaned_data['email']
         password = sform.cleaned_data['password']
         if Employee.objects.filter(email = sform.cleaned_data['email']).count()>0:
            message = "You have already registered. Please Login with your credentials"
            sform = LoginForm()
            return render(request,'awsapp/home.html',{'sform':sform, 'message':message})
         
         Employee.objects.create(fname = fname , email= email, password = password, mobile = mobile )
         message = "Cogratulation!!! You have been registered.Please Login with your credentials."
         return render(request,'awsapp/home.html',{'sform':sform, 'message':message})
   else:
      sform = LoginForm()
   return render(request,'awsapp/home.html',{'sform':sform,})


def home(request):
   try:
      username = request.session['username']
      Credentials.objects.filter(email=username).delete()
      del request.session['username']
   except:
      pass
   return hello(request)


def dashboard(request):
   try:
      if request.session['username']:
         username = request.session['username']
         if request.method == 'POST':
            try:
               kform = KeyForm(request.POST)
               if kform.is_valid():
                  accountid = kform.cleaned_data['accountid']
                  accesskey = kform.cleaned_data['accesskey']
                  Credentials.objects.create(email = username, accountid = accountid, accesskey = accesskey)
                  try:
                     ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
                     instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped', 'stopping']}])
                     return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})
                  except:
                     pass
                  return render(request,'awsapp/dashboard.html',{'username':username})
            except:
               pass
            
            try:
               uform = UnknownForm(request.POST)
               if 'start' in request.POST:
                  ids = request.POST.getlist('iid[]')
                  user = Credentials.objects.filter(email=username)
                  account = user.values_list("accountid",flat=True)
                  accountid = account[0]
                  access = user.values_list("accesskey",flat=True)
                  accesskey = access[0]
                  ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
                  ec2.instances.filter(InstanceIds=ids).start()
                  instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped', 'stopping']}])
                  return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})
               
               if 'stop' in request.POST:
                  ids = request.POST.getlist('iid[]')
                  user = Credentials.objects.filter(email=username)
                  account = user.values_list("accountid",flat=True)
                  accountid = account[0]
                  access = user.values_list("accesskey",flat=True)
                  accesskey = access[0]
                  ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
                  ec2.instances.filter(InstanceIds=ids).stop()
                  instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped','stopping']}])
                  return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})

               if 'reboot' in request.POST:
                  ids = request.POST.getlist('iid[]')
                  user = Credentials.objects.filter(email=username)
                  account = user.values_list("accountid",flat=True)
                  accountid = account[0]
                  access = user.values_list("accesskey",flat=True)
                  accesskey = access[0]
                  ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
                  ec2.instances.filter(InstanceIds=ids).reboot()
                  instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped', 'stopping']}])
                  return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})
               
               if 'terminate' in request.POST:
                  ids = request.POST.getlist('iid[]')
                  user = Credentials.objects.filter(email=username)
                  account = user.values_list("accountid",flat=True)
                  accountid = account[0]
                  access = user.values_list("accesskey",flat=True)
                  accesskey = access[0]
                  ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
                  ec2.instances.filter(InstanceIds=ids).terminate()
                  instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped', 'stopping']}])
                  return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})
            except:
               pass
            
            aform = AwsInstance(request.POST)
            if aform.is_valid():
               amitype = aform.cleaned_data['amitype']
               instancetype = aform.cleaned_data['instancetype']
               instanceno = aform.cleaned_data['instanceno']
               user = Credentials.objects.filter(email=username)
               account = user.values_list("accountid",flat=True)
               accountid = account[0]
               access = user.values_list("accesskey",flat=True)
               accesskey = access[0]
               ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
               instances = ec2.create_instances(ImageId=amitype, MinCount=instanceno, MaxCount=instanceno, InstanceType=instancetype)
               instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped', 'stopping']}])
               return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})
            
         else:
            try:
               user = Credentials.objects.filter(email=username)
               account = user.values_list("accountid",flat=True)
               accountid = account[0]
               access = user.values_list("accesskey",flat=True)
               accesskey = access[0]
               ec2 = boto3.resource('ec2', region_name="us-east-1", aws_access_key_id=accountid, aws_secret_access_key=accesskey)
               instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','pending','stopped', 'stopping']}])
               return render(request, 'awsapp/dashboard.html',{'username':username, 'instance':instance})
            except:
               pass
            return render(request,'awsapp/config.html',{'username':username})
   except:
      pass
   return render(request, 'awsapp/home.html',)

