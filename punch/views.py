from django.shortcuts import render,redirect
from django.http import HttpResponse
from punch.models import contactus
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    # return HttpResponse("this is home page")
    return render(request,"home.html")
def aboutus(request):
    return render(request,"aboutus.html")
def contactusx(request):
    return render(request,"contactus.html")
def services(request):
    data=contactus.objects.all().order_by("-id")
    context={"mydata": data}
    return render(request,"services.html",context)

def savethis(request):
    if request.method=="POST":
        Fullname=request.POST.get("fname")
        email=request.POST.get("email")
        phone__number=request.POST.get("number")
        message=request.POST.get("msg")
        myimg=request.FILES.get('img')
        myemail=f"""
        this is user contactus form data 
        user name : {Fullname}
        user email : {email}
        phone number : {phone__number}
        message : {message}
        image : {myimg}
         dhnyawaad...!
        """
        mail=EmailMessage("this email comming from django file",myemail,"shanuchoudharyvikas@gmail.com",["shanuchoudharyvikas@gmail.com","preetkaurskhp2002@gmail.com"])
        mail.send()
        # data=contactus("contact")
        mydata=contactus(username=Fullname,useremail=email,phonenumber=phone__number,message=message,myimage=myimg)
        mydata.save()
        messages.success(request,"your data saved successfully")
        
    return redirect("services")

def deletethisdata(request,myid):
    data=contactus.objects.get(id=myid)
    data.delete()
    return redirect("services")

def updatethisdata(request,zxc):
    my_data=contactus.objects.get(id=zxc)
    return render(request,"contactusupdate.html",{"yourdata":my_data})

def nowupdatedata(request,updateid):
    if request.method=="POST":
        fullname=request.POST.get("fname")
        email=request.POST.get("email")
        phone_number=request.POST.get("number")
        message=request.POST.get("msg")
        myimg=request.FILES.get('img')
        my__data=contactus.objects.get(id = updateid)
        my__data.username=fullname
        my__data.useremail=email
        my__data.phonenumber=phone_number
        my__data.message=message
        my__data.myimage=myimg
        my__data.save()
    return redirect("services") 
  
def searchdata(request):
    abc=request.GET['srch']
    searchthis=contactus.objects.filter(username=abc) or contactus.objects.filter(phonenumber=abc)
    context={"mydata": searchthis}
    return render(request,"services.html",context)

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        mypass=request.POST.get("mypass")
        fullname=request.POST.get("fullname")

        saveuser=User.objects.create_user(username=username,email=email,password=mypass,first_name=fullname)
        saveuser.save()
        messages.success(request,"useradded successfully")
    return render(request,"signup.html")

def mylogin(request):
    if request.method=="POST":
        myname=request.POST.get("username")
        passw=request.POST.get("password")
        checkuser=authenticate(username=myname,password=passw)
        if checkuser is not None:
            login(request,checkuser)
            messages.success(request,"login successfulllyyy....done....")
            return redirect("contactus")
        else:
            messages.warning(request,"pls enter valid info")
        
    return render(request,"login.html")

def mylogout(request):
    logout(request)
    return render("login")
