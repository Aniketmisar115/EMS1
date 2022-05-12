from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    name="Aniket"
    student_details=[
        {"name":"Aniket",
        "branch":"Mechanical",
        "year":"Final Year",
        "mobile_number":"9309820033",
        "email_id":"aniketmisar115@gmail.com"
        },
        {"name":"Rohit",
        "branch":"Electrical",
        "year":"Final Year",
        "mobile_number":"9325736002",
        "email_id":"rohittike89@gmail.com"
        },
        {"name":"Shubham",
        "branch":"Electrical",
        "year":"Final Year",
        "mobile_number":"9435544633",
        "email_id":"shubhamvaidya@gmail.com"
        },
        {"name":"Saloni",
        "branch":"Computer",
        "year":"Final Year",
        "mobile_number":"9685326475",
        "email_id":"saloniwadalkar@gmail.com"
        },
        {"name":"Payal",
        "branch":"Computer",
        "year":"Final Year",
        "mobile_number":"9823467525",
        "email_id":"payalshinde@gmail.com"
        }
    ]

    context={"display_name":name,"student_details":student_details}
    return render(request,"StudentDetails.html",context)
    #return HttpResponse(" Welcome to our student details page ")
    
def about(request):
    return HttpResponse("About student details page ")