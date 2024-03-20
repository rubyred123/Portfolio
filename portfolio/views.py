from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs

# Create your views here.

def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')


def contact(request):

    if not request.user.is_authenticated:
        messages.warning(request,"Please Login to contact....")
        return redirect("/auth/login")
     
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phn_num = request.POST.get("num")
        description = request.POST.get("desc")

        query = Contact(name=name,email=email,phn_num=phn_num,description=description)
        query.save()
        messages.success(request,"Thanks for contacting, will get by you soon!")

        #messages.info(request, f'The name is {name} & the email is {email} your number is {phn_num} & message is {description}')
        
        return redirect('/contact')
    
    return render(request,'contact.html')



def resume(request):
    return render(request,'resume.html')



def blog(request):

    posts = Blogs.objects.all()
    context = {
        "posts":posts
    }
    return render(request,'blog.html', context)

