from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import regform,LoginForm,regform1
from.models import registration



# Create your views here.



def greetings(request):
    return render(request,"greetings.html")

def submitform(request):
      if request.method=='POST':
            if (request.POST.get('first_name')) and request.POST.get('last_name') and request.POST.get('age') and request.POST.get('adress') and request.POST.get('emailid') and request.POST.get('phone') and request.POST.get('password') and request.POST.get('confirm_password'):
                  email = request.POST.get('emailid')
                  if registration.objects.filter(emailid=email).exists():
                        return render(request,"login//invalidem.html")
                  registered_number = request.POST.get('phone')
                  if registration.objects.filter(phonenumber=registered_number).exists():
                        return render(request,'login//invalidph.html')


                  reg=registration()
                  reg.first_name=request.POST.get('first_name')
                  reg.last_name=request.POST.get('last_name')
                  reg.age=request.POST.get('age')
                  reg.adress=request.POST.get('adress')
                  reg.emailid=request.POST.get('emailid')
                  reg.phonenumber=request.POST.get('phone')
                  reg.password=request.POST.get('password')
                  y=request.POST.get('confirm_password')

                  if reg.password==y:
                    reg.save()
                    return redirect('/table')


                  else:
                        return render(request,'login//invalidpw.html')

            else:
                  return HttpResponse ("<h1> some fields are misssing </h1>")
      form=regform()
      return render(request,"login/register.html",context={'form':form})


def login(request):

        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['emailid']
                password = form.cleaned_data['password']
                user = registration.objects.filter(emailid=email, password=password).first()

                if user is not None:
                    LoginForm(request,user)
                    c=registration
                    return redirect('/table')
                else:
                    return render(request,"login/empwer.html")
            else:
                return HttpResponse("Form is not valid")
        else:
            form = LoginForm()

            return render(request, "login/login.html", context={'form': form})

def table(request):
    emp=registration.objects.all()
    return render(request,'registration/table.html',context={"emp":emp})

def delete(request, id):
        emp = registration.objects.get(id=id)
        emp.delete()
        return redirect('/table')

def update(request,id):
        emp = registration.objects.get(id=id)
        if request.method == 'POST':
            form = regform1(request.POST, instance=emp)
            if form.is_valid():
                form.save()
                return HttpResponse("""<h1> employ data updated suceesfully </h1>

                         <h1> <a href="/table"> click here </a>view employ details</h2>
                       """)
        return render(request, "registration//update.html", context={"emp": emp})


def part2(request):
    return render(request,'greetings2.html')
