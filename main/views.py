from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    # Portfolio Data
    skills = [
        {'name': 'HTML'},
        {'name': 'CSS'},
        {'name': 'JavaScript'},
        {'name': 'Python'},
        {'name': 'SQL'},
        {'name': 'Django'},
        {'name': 'Data Structures'},
    ]

    projects = [
        {'title': 'Pykart - E-commerce Platform', 'description': 'Developed an e-commerce platform similar to Flipkart using Django, enabling users to browse products, manage a shopping cart, and complete purchases.', 'tech_stack': 'Python, Django, HTML, CSS, JavaScript', 'link': 'https://github.com/ANTHONYALEX55/ecommerce'},
        {'title': 'Fruit Quality Monitoring System', 'description': 'Developed a Fruit Quality Monitoring System using image processing techniques (OpenCV, scikit-image) to extract key features like color and texture from fruit images. Implemented and trained an SVM model (scikit-learn) to classify fruit quality into different grades, achieving high accuracy.', 'tech_stack': 'Python, OpenCV, scikit-image, scikit-learn', 'link': 'https://github.com/Sankaranarayanan47/Fruit-Quality-Monitoring'},
    ]

    education = [
        {'institution': 'S.K.P Engineering College, Tiruvannamalai', 'degree': 'B.E - Computer Science Engineering', 'duration': '2021 - 2024'},
        {'institution': 'Kumaran Polytechnic College, Tiruvannamalai', 'degree': 'Diploma in Computer Engineering', 'duration': '2019 - 2021'},
        {'institution': 'Mary Immaculate School, Tiruvannamalai', 'degree': 'Class XII', 'duration': 'March 2019'},
    ]

    # Contact Form Handling
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send an email or save to the database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # You can integrate email or save the data as per your requirement
            return redirect('success')  # Redirect to a success page after form submission
    else:
        form = ContactForm()

    # Context Data for Template Rendering
    context = {
        'skills': skills,
        'projects': projects,
        'education': education,
        'form': form,
        "projects": projects,
    }

    return render(request, 'home.html', context)

# Success page view
def success(request):
    return render(request, 'success.html')
