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
            message = "Thanks for Submitting"
            solution = ""

            if query == "1":
                query="What is Talent Serve?"
                solution = "We are an IIT, IIM and Symbiosis alumni, engaging with Millions of Students around the world to give a 360-degree solution to all the Career, Education, Work and Corporate needs."
            elif query == "2":
                query="What is the major work done by the company?"
                solution = "The major work done by the company includes sourcing , matching qualified candidates with job openings and providing various courses to the users."
            elif query == "3":
                query="Is there any app available?"
                solution = "No, But Talent Serve is coming with mobile app available for download very shortly. You will be able to find it on the app stores for both iOS and Android platforms."

            try:
                email_body = """
                <html>
                    <head></head>
                    <body>
                        <p>Hello {name},</p>
                        <p>We have successfully received your query:</p>
                        <p><strong>Query:</strong> {query}</p>
                        <p><strong>Solution:</strong></p>
                        <div style="border: 1px solid #ccc; padding: 10px;">
                            <p>{solution}</p>
                        </div>
                    </body>
                </html>
                """.format(name=name, query=query, solution=solution)

                send_mail(
                    "Query Response from Talent Serve",
                    "",
                    "", #write the mail-id here
                    [email],  # Use recipient's email from the form
                    fail_silently=False,
                    html_message=email_body
                )
            except Exception as e:
                error_msg = "An error occurred: {}".format(str(e))
                print(error_msg)

            return render(
                request,
                "mails/success.html",
                {"message": message, "query": query, "solution": solution},
            )

        except Exception as e:
            error_msg = "An error occurred: {}".format(str(e))
            return render(
                request, "mails/contact_us.html", {"message": error_msg}
            )
    else:
        return render(request, "mails/contact_us.html", {})


def success(request):
    return render(request, "mails/success.html")


def contact_us(request):
    return render(request, "mails/contact_us.html")
