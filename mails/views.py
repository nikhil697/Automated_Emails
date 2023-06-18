import mysql.connector
from django.shortcuts import render
from .models import contact
from django.core.mail import send_mail
from django.conf import settings


# def contact_us(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         query = request.POST.get('query')

#         contact1 = contact(name=name, email=email, phone=phone, query=query)
#         contact1.save()

#         return render(request, 'success.html')


#     return render(request, 'contact_us.html')
def submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        query = request.POST.get("query")
        try:
            # Save the form data to the database
            Regis = contact(name=name, email=email, phone=phone, query=query)
            Regis.full_clean()
            Regis.save()
            message = "Thanks for submitting"
            try:
                send_mail(
                "Query Response from Talent Serve",
                "Hello {name}\n\n"
                "We have successfully received your query.\n\n"
                "Query: {query}\n"
                "Solution: Kindly visit www.talentserve.org for more information.".format(name=name, query=query),
                "", #enter email here
                [email],  # Use recipient's email from the form
                fail_silently=False,
                )
            except Exception as e:
                error_msg = "An error occurred: {}".format(str(e))
                print(error_msg)

            return render(request, "mails/success.html", {"message": message})
            
        except Exception as e:
            error_msg = "An error occurred: {}".format(str(e))
            return render(request, "mails/contact_us.html", {"message": error_msg})
    else:
        return render(request, "mails/contact_us.html", {})


def success(request):
    return render(request, "mails/success.html")


def contact_us(request):
    return render(request, "mails/contact_us.html")
