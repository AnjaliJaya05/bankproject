from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import os
from django.core.mail import send_mail
from django.contrib.auth import logout

# Create your views here.


def index(request):
    return render(request,'index.html')

def Register(request):
    if request.method=='POST':
        a=Registform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['firstname']
            ln=a.cleaned_data['lastname']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            phn=a.cleaned_data['phone']
            ac=int("15"+str(phn))
            img=a.cleaned_data['file']
            p=a.cleaned_data['pin']
            rp=a.cleaned_data['repin']
            if p==rp:
                b=Registmodel(firstname=fn,lastname=ln,username=un,email=em,phone=phn,file=img,pin=p,balance=0,ac=ac)
                b.save()
                subject="your account has been created"
                message=f"your new account number is {ac}"
                email_from='anjalijo543@gmail.com'  #from
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(Login)
            else:
                return HttpResponse("pin doesnot match")
        else:
            return HttpResponse("registration failed")
    return render(request,'indexreg.html')

def Login(request):
    if request.method=='POST':
        a=Logform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            p=a.cleaned_data['pin']
            b=Registmodel.objects.all()
            for i in b:
                if i.username==un and i.pin==p:
                    request.session['id']=i.id
                    return redirect(profile)
            else:
                return HttpResponse("login failed")
    return render(request,'indexlog.html')

def profile(request):
    try:
        id1=request.session['id']
        a=Registmodel.objects.get(id=id1)
        img=str(a.file).split('/')[-1]
        return render(request,'profile.html',{'a':a,'img':img})
    except:
        return redirect(Login)


def edit(request,id):
    a=Registmodel.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.save()
        return redirect(profile)
    return render(request,'edit_profile.html',{'a':a})


def editimage(request):
    id1=request.session['id']
    a=Registmodel.objects.get(id=id1)
    img=str(a.file).split('/')[-1]
    if request.method=='POST':
        a.username=request.POST.get('username')
        if len(request.FILES)!=0:
            if len(a.file)>0:
                os.remove(a.file.path)
            a.file=request.FILES['file']
        a.save()
        return redirect(profile)
    return render(request,'editimage.html',{'a':a,'img':img})



def addamount(request,id):
    a=Registmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am #global
        request.session['ac']=a.ac
        a.balance+=int(am)
        a.save()
        b=addmoney(amount=am,uid=request.session['id'])
        b.save()
        pin=request.POST.get('pin')
        # print(a.pin)
        if int(pin)==a.pin:
            return redirect(success)
        else:
            return HttpResponse(' amount added failed')
    return render(request,'add_amount.html')

def success(request):
    am=request.session['am']
    ac=request.session['ac']
    return render(request,'success.html',{'am':am,'ac':ac})


def amountwithdraw(request,id):
    id1=request.session['id']
    a=Registmodel.objects.get(id=id1)
    if request.method=='POST':
        am=request.POST.get('amount')
        request.session['am']=am
        request.session['ac']=a.ac
        if (a.balance>=int(am)):
            a.balance-=int(am)
            a.save()
            b=withdrawmoney(amount=am,uid=request.session['id'])
            b.save()
            pin=request.POST.get('pin')
            if int(pin)==a.pin:
                return redirect(withdraw)
            else:
                return HttpResponse("Withdraw failed")
        else:
            return HttpResponse("insufficient balance")
    return render(request,'amount_withdraw.html')

def withdraw(request):
    am=request.session['am']
    ac=request.session['ac']
    return render(request,'withdraw.html',{'am':am,'ac':ac})


def checkbal(request):
    id=request.session['id']
    a=Registmodel.objects.get(id=id)
    if request.method=='POST':
        pin=request.POST.get('pin')
        if int(pin)==a.pin:
            return redirect(checkbal1)
        else:
            return HttpResponse('failed')
    return render(request,'checkbal.html')

def checkbal1(request):
    id=request.session['id']
    a=Registmodel.objects.get(id=id)
    return render(request,'checkbal1.html',{'bal':a.balance,'ac':a.ac})

def ministatement(request,id):
    a=Registmodel.objects.get(id=id)
    pin=request.POST.get('pin')
    if request.method=='POST':
        if int(pin)==a.pin:
            choice=request.POST.get('select')
            if choice=="deposit":
                return redirect(depositstatement)
            elif choice=="withdraw":
                return redirect(withdrawstatement)
        else:
            return HttpResponse('incorrect password')
    return render(request,'ministatement.html')

def depositstatement(request):
    a=addmoney.objects.all()
    id=request.session['id']
    return render(request,'deposit_statement.html',{'a':a,'id':id})

def withdrawstatement(request):
    a=withdrawmoney.objects.all()
    id=request.session['id']
    return render(request,'withdraw_statement.html',{'a':a,'id':id})

def newsupload(request):
    if request.method=='POST':
        a=newsform(request.POST,request.FILES)
        if a.is_valid():
            tp=a.cleaned_data['topic']
            c=a.cleaned_data['content']
            # i=a.cleaned_data['file']
            b=newsmodel(topic=tp,content=c)
            b.save()
            return redirect(newsdisplay)
        else:
            return HttpResponse("failed")
    return render(request,'newsfeed.html')

def newsdisplay(request):
    a=newsmodel.objects.all()
    id1=[]
    t=[]
    c=[]
    d=[]
    for i in a:
        id=i.id
        id1.append(id)
        to=i.topic
        t.append(to)
        co=i.content
        c.append(co)
        da=i.date
        d.append(da)
    pair=zip(t,c,d,id1)
    return render(request,'newsdisplay.html',{'a':pair})


def newsdelete(request,id):
    a=newsmodel.objects.get(id=id)
    a.delete()
    return redirect(newsdisplay)

def newsedit(request,id):
    a=newsmodel.objects.get(id=id)
    if request.method=='POST':
        a.topic=request.POST.get('topic')
        a.content=request.POST.get('content')
        a.save()
        return redirect(newsdisplay)
    return render(request,'newsedit.html',{'a':a})


def usernewsdisplay(request):
    a=newsmodel.objects.all()
    id1=[]
    t=[]
    c=[]
    d=[]
    for i in a:
        id=i.id
        id1.append(id)
        to=i.topic
        t.append(to)
        co=i.content
        c.append(co)
        da=i.date
        d.append(da)
    pair=zip(t,c,d,id1)
    return render(request,'usernewsdisp1.html',{'a':pair})

def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(alog)
            else:
                return HttpResponse("login failed")
    return render(request,'admin_login.html')

def alog(request):
    return render(request,'admin_login1.html')

def wish(request,id):
    a=newsmodel.objects.get(id=id)
    wish=wishlist.objects.all()
    for i in wish:
        if i.newsid==a.id and i.uid==request.session['id']:
            return HttpResponse("item already in wishlist")
    b=wishlist(topic=a.topic,content=a.content,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return redirect(wishdisplay)


def wishdisplay(request):
     a=wishlist.objects.all()
     id=request.session['id']
     return render(request,'wishlistdisplay.html',{'a':a,'id':id})

def wish_rem(request,id):
    a=wishlist.objects.get(id=id)
    a.delete()
    return redirect(wishdisplay)

def logout_view(request):
    logout(request)
    return redirect(Login)

def forgot_password(request):
    a=Registmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        ac=request.POST.get('ac')
        # request.session['em']=em
        for i in a:
            if (i.email==em and i.ac==int(ac)):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/bank_app/change/{id}"
                frm="anjalijo543@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("check mail")
        else:
            return  HttpResponse("sorry")
    return render(request,'forgot_password.html')

def change_password(request,id):
    a=Registmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('repin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse("password changed")
        else:
            return HttpResponse("sorry")
    return render(request,'change.html')


def moneytransfer(request,id):
    a=Registmodel.objects.get(id=id)
    b=Registmodel.objects.all()
    if request.method=='POST':
        nm=request.POST.get('name')
        ac=request.POST.get('ac')
        am=request.POST.get('amount')
        for i in b:
            if int(ac)==i.ac and nm==i.username:
                if a.balance>=int(am):
                    a.balance-=int(am)
                    i.balance+=int(am)
                    i.save()
                    a.save()
                    return HttpResponse("money transferred successfully")
                else:
                    return HttpResponse("insufficient balance")
        else:
            return HttpResponse("usernot found")
    return render(request,'moneytransfer.html')