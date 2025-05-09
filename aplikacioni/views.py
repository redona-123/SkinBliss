from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    products= Product.objects.all() #tek html duhet cikel
    categories= Category.objects.all()
    context={"products": products, "categories": categories}
    return render(request, "home.html", context)

# ki kujdes emrat dhe filet si i ke krijuar
def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")


def contact(request):
    if request.method == "POST":
        infoFirstName = request.POST["firstName"]
        infoLastName = request.POST["lastName"]
        infoEmail = request.POST["email"]
        infoComment = request.POST["comment"]
        if infoFirstName != "" and  infoLastName != "" and infoEmail != ""  and infoComment != "" :
            Contact(
                Contact_firstName = infoFirstName,
                Contact_lastName = infoLastName,
                Contact_email = infoEmail,
                Contact_comment = infoComment,
                    
                ) .save()
            messages.success(request, "Message sent!")
        else:
            messages.error(request, "Message not sent! Please fill the form")
            

    return render(request, "contact.html")       # metode per te lexuar html



# footer, index, navbar nk duhet te kene funksion, se jane ne cdo faqe
