from django.shortcuts import render
from django.http import HttpResponse
from .models import user,trlist,contact,complaint
from .forms import login,complaintForm
import random
import datetime
# Create your views here.
def first(request):
    return render(request,'front.html')

def logi(request):
    logfm=login()
    return render(request,'login.html',{'form':logfm})

def logver(request):
    global responscedic
    logfm=login()
    try:
        if request.method=='POST':
            uid=request.POST['userid']
            pw=request.POST['pasu']
            person=user.objects.all()
            for man in person:
                if uid==man.userid and pw==man.password:
                    responscedic={"client":man}
                    return render(request,'dash.html',responscedic)
            else:
                return render(request,'login.html',{'note':'password or user id is incorrect','form':logfm})
                
    except:
        return HttpResponse('error')
                
                
def adduserfm(request):
    return render(request,'register.html')

def addnuser(request):
    if request.method=="POST":
        def genaccno():
            return random.randrange(11111111111,99999999999)
        def uid():
            return random.randrange(111111,999999)
        def ifsc():
            value=random.randrange(1222222,9999999)
            return "RB"+str(value)
        acc=genaccno()
        uid=uid()
        ifsc=ifsc()
        fn=request.POST['fname']
        ln=request.POST['lname']
        dob=request.POST['dateob'] 
        ph=request.POST['phone']
        em=request.POST['email']
        lc=request.POST['location']
        acty=request.POST['actype']
        gen=request.POST['GEN']
        bnlist=user(acc_no=acc,first_name=fn,last_name=ln,dob=dob,phone=ph,email=em,location=lc,acc_type=acty,userid=uid,ifsc=ifsc,gender=gen) 
        bnlist.save()
    return render(request,'password.html',{'msg':acc,'msg1':uid})

def passet(request):
    if request.method=="POST":
        inus=request.POST["inus"]
        Udet=user.objects.all()
        for i in Udet:
            if inus in i.userid:
                        pas1=request.POST["inpass"]
                        pas2=request.POST["cnpass"]
                        if pas2==pas1:
                            i.password=pas1
                            i.save()
                            return render(request,'password.html',{'msg': "password set successfully"})
                        else:
                            return render(request,'password.html',{'msg': "password doesn't match"})
def pro(request):
    return render(request,'dash.html',responscedic)

def account(request):
    return render(request,'accounts/savings.html',responscedic)

def loan(request):
    return render(request,'accounts/loan.html')
def deppage(request):
    return render(request,'transaction.html',responscedic)

def deposite(request):
    if request.method=="POST":
        acc=request.POST['accno']
        am=int(request.POST['amount'])
        Udet=user.objects.all()
        for i in Udet:
            if acc in i.acc_no:
                i.balan=i.balan+am
                i.save()
                return render(request,'transaction.html',{'depmsg':"Amount deposited successfully"})
            
def transfer(request):
    try:
        if request.method=='POST':
            acc=request.POST['facc']
            tacc=request.POST['tacc']
            am=int(request.POST['amount'])
            base=user.objects.all()
            for num in base:
                if acc in num.acc_no:
                    num.balan=num.balan-am
                    aftertr=num.balan
                    num.save()
            for numb in base:
                if tacc in numb.acc_no:
                    numb.balan=numb.balan+am
                    numb.save()
                    now=datetime.datetime.now()
                    tran=trlist(acc_no=acc,tr_amount=am,to_acc=tacc,d_t=now,balan=aftertr)
                    tran.save()
                    return render(request,'transaction.html',{'depmsg2':'Amount transfered successfully'})        
        else:
            return render(request,'dash.html')
    except:
        pass
def resetpg(request):
    return render(request,'reset.html')
def reset(request):
    logfm=login()
    try:
        if request.method=='POST':
            opass=request.POST['opass']
            npass=request.POST['npass']
            cnpass=request.POST['cnpass']
            base=user.objects.all()
            for i in base:
                if opass==i.password and npass==cnpass:
                        i.password=npass
                        i.save()
                        return render(request,'login.html',{'msg2':'password reset','form':logfm})
    except:
        pass
    
def logout(request):
    logfm=login()
    return render(request,'login.html',{'msg1':'session expired-- please login again','form':logfm})

def statementpg(request):
    return render(request,'accounts/statement.html',responscedic)

def statement(request):
    try:
        if request.method=='POST':
            acc=request.POST['acc']
            tr=trlist.objects.all()
            nlist=[]
            for i in tr:
                if acc in i.acc_no or acc in i.to_acc:
                    nlist.append(i)
            demodic = {'tr':nlist,
                       'account':acc,
                       'msg':'Transaction of this account:'}
            print(nlist)
            print(demodic)
            return render(request,'accounts/statementdis.html',demodic)
    except:
        return HttpResponse('error')
    
def calu(request):
    return render(request,'calculator/cal.html')
def intro(request):
    return render(request,'front.html')
def about(request):
    return render(request,'about.html')
def complaint(request):
    comp=complaintForm()
    return render(request,'complaint.html',{'form':comp})
def contact1(request):
    clist=contact.objects.all()
    rdic={
        'key':clist
    }
    print(rdic)
    return render(request,'contact.html',rdic)

def post_comp(request):
    
    if request.method=='POST':
        comp=complaintForm(request.POST)
        comp.save()
        return render(request,'complaint.html')
    
    
