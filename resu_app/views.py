from django.shortcuts import render
from django.http import HttpResponse
from .models import ResuModel
from django.core.exceptions import ValidationError

def resu_views(request):
    return HttpResponse("Hi!")

def resu_model_view(request):
    resu = None
    if request.method == 'POST':
        user_name = request.POST.get('input_name')
        user_email = request.POST.get('input_email')
        user_resume = request.FILES.get('input_resume')
        user_transcript = request.FILES.get('input_transcript')

        try:
            resu = ResuModel.objects.create(
                name= user_name,
                email= user_email,
                resume= user_resume,
                transcript= user_transcript
            )
            return HttpResponse("🟢 SUCCESS: Your documents have been securely processed and written to the database!")
        except ValidationError as e:
            return HttpResponse(f"Registration error {e.message}")
    return render (request, 'index.html', {'items': resu})