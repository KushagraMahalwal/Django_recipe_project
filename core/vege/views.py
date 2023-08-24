from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def Receipes(request):
    if request.method=='POST':
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        # recipe_image is a variable
        # 'recipe_image' is coming from the models.py the database file
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
       
    #    creating the object which was feed in the frontend and saving it to database
        Receipe.objects.create(receipe_image=receipe_image,
        receipe_name=receipe_name,
        receipe_description=receipe_description)
    
    # using this so the page won't refesh again
        return redirect('/receipes/')

    query_set=Receipe.objects.all()

    # passing the search key here
    if request.GET.get('search'):
        query_set=query_set.filter(receipe_name__icontains=request.GET.get('search'))


    # Here Receipe is coming from the models.py file which is database file
    # We are using context here to send the data from backend to frontend
    # query_set is the variable which stored the all the value of Recipes using object all method of django
    context={'Receipe':query_set}
    return render(request,"receipes.html",context)


def update_receipe(request,id):
    query_set=Receipe.objects.get(id=id)

    if request.method=='POST':
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")

        query_set.receipe_name=receipe_name
        query_set.receipe_description=receipe_description


        if receipe_image:
            query_set.receipe_image=receipe_image
        
        query_set.save()
        return redirect('/receipes/')

    context={'Receipes':query_set}   
    return render(request,"update.html",context)





def delete_receipe(request,id):

    query_set=Receipe.objects.get(id=id)
    query_set.delete()
    return redirect('/receipes/')


def login_page(request):
    
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect('/login/')
        
        user=authenticate(username=username, password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login')
        else:
            # login used to provide access to  store session of a particular user
            login(request, user)        
            return redirect('/receipes/')
    
    return render(request,'login.html')


def logout_page(request):

    logout(request)
    return redirect('/login/')



def register_page(request):

# here we sending data from frontend to backend
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

# creating/posting it in database after getting it from frontend using post method
#


        user=User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, messages.INFO, "Username already exists Please try a different one")
            return redirect('/register/')

# here we are using return redirect that is why program stopped there 

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
# if we pass password in the above it will give the string
# To encript the password  we are using inbuilt user methods to set password 

        user.set_password(password)
        user.save()

        #messages in the backend which can be pass in front end 
        messages.add_message(request, messages.INFO, "Account Created Successfully.")


        return redirect('/register/')
    return render(request,'register.html')

