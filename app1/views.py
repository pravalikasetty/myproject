from django.shortcuts import render,redirect
from .models import Register
from .models import Resume


def userhome(request):
    return render(request,"userhome.html")
def modify(request):
    operation=request.GET['operation']
    username=request.GET['username']
    email=request.GET['email']
    password=request.GET['password']
    phno=request.GET['phno']
    desig=request.GET['desig']
    print(email)
    # r=Register.objects.get(email=email)
    
    # if operation=="update":
    #     r.username=username
    #     r.email=email
    #     r.password=password
    #     r.phno=phno
    #     r.desig=desig
    #     r.save()
    # else:
    #     Register.delete(r)
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})




def adminhome(request):
    return render(request,"adminhome.html")
def viewusers(request):
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})

def about(request):
    return render(request,"about.html")
def register(request):
    return render(request,"register.html")
def doregister(request):
    username=request.GET['username']
    email=request.GET['email']
    password=request.GET['password']
    phno=request.GET['phno']
    r=Register()
    r.username=username
    r.email=email
    r.password=password
    r.phno=phno
    r.save()
    #return render(request,"register.html",{"msg":"register successfully"})
    return render(request,"login.html",{"email":email})


def login(request):
    return render(request,"login.html")
def logincheck(request):
    email1=request.GET['email']
    password1=request.GET['password']
    r=None
    try:
        r=Register.objects.get(email=email1,password=password1)
        print("r=",r)
    except Exception as ex:
        print(ex)
        return render(request,"login.html",{"msg":"invalid email/password"})
    if(r!=None):
        if(r.desig=='user'):
            return redirect('/userhome/')
        if(r.desig=='admin'):
            return redirect('/adminhome/')
    else:
        return render(request,"login.html",{"msg":"invalid"})
    
def resume(request):
    return render(request,"resume.html")
def doresume(request):
    fullname=request.GET.get('Fullname')
    email=request.GET.get('email')
    phone=request.GET.get('phone')
    dob=request.GET.get('dob')
    linkedIn=request.GET.get('linkedIn')
    careerobjective=request.GET.get('careerobjective')
    education=request.GET.get('education')
    skills=request.GET.get('skills')
    projects=request.GET.get('projects')
    certifications=request.GET.get('certifications')
    
    
    if fullname and email and phone:
        r=Resume()
        r.fullname=fullname
        r.email=email
        r.phone=phone
        r.dob=dob
        r.linkedin=linkedin
        r.addres=address
        r.CareerObjective=careerobjective
        r.Education= education
        r.Skills=skills
        r.Projects=projects
        r.Certifications= certifications
        r.save()
        return render(request,"one.html")
    else:
        return render(request,"one.html",{"error":"Required fields are missing"})
def one(request):
    return render(request,"one.html")
#def doone(request):
    #fullname=request.GET['Fullname']
    #email=request.GET['Email']
    #phone=request.GET['Phone']
    #dob=request.GET['dd-mm-yyyy']
    #linkedin=request.GET['LinkedIn']
    #address=request.GET['Address']
    #careerobjective=request.GET['CareerObjective']
    #education=request.GET['Education']
    #skills=request.GET['Skills']
    #projects=request.GET['Projects']
    #certifications=request.GET['Certifications']
    #s=Submit()
    #s.fullname=fullname
    #s.email=email
    #s.phone=phone
    #s.dob=dob
    #s.linkedin=linkedin
    #s.addres=address
    #s.CareerObjective=careerobjective
    #s.Education= education
    #s.Skills=skills
    #s.Projects=projects
    #s.Certifications= certifications
    #s.save()
    #return render(request,"one.html")







  