from django.shortcuts import render, redirect
from .forms import DonorForm
from .models import Donor
from django.http import HttpResponse
from django.urls import reverse

def home(request):
    return render(request, 'donation/home.html')

def donar(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            blood_group = form.cleaned_data['blood_group']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            diseases = form.cleaned_data['diseases']
            donor_organ = form.cleaned_data['donor_organ']
            description = form.cleaned_data['description']
            
            # Create and save the Donor object
            donor = Donor(
                name=name,
                age=age,
                sex=sex,
                blood_group=blood_group,
                mobile_number=mobile_number,
                email=email,
                diseases=diseases,
                donor_organ=donor_organ,
                description=description
            )
            donor.save()
            
            # Get the URL for the home page
            home_url = reverse('home')
            
            # Build the HTML response with the success message and a link to the home page
            response = """
            <html>
            <head>
                <title>Success</title>
                <div class="success-message">
                <h1>Form Submitted Successfully!</h1><h2>Thank you for your donation!</h1>
    <p>Your generous contribution means a lot to us.</p>
    <p>Please consider donating again to support our cause further.</p>
                <a href="{0}" class="btn btn-primary">Go back to the home</a>
                </div>
                <style>
                    .success-message {{
                        text-align: center;
                        margin-top: 50px;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #007bff;
                        color: #fff;
                        text-decoration: none;
                        border-radius: 5px;
                    }}
                    .btn:hover {{
                        background-color: #0056b3;
                    }}
                </style>
                
                </body>
            </html>
            """.format(home_url)
            
            # Return the HTML response
            return HttpResponse(response)
    else:
        form = DonorForm()
    
    return render(request, 'donation/donar.html', {'form': form})
def success_page(request):
    return render(request, 'donation/success.html')

def admin(request):
    donors = Donor.objects.all()
    return render(request, 'donation/admin.html', {'donors': donors})

def receiver(request):
    return render(request, 'donation/receiver.html')
