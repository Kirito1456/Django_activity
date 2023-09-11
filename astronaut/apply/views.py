from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'apply/index.html')

def result(request):
    message = 'Aside: If you are not the right height to be an astronaut, that is fine! Space is dangerous anyways. But still, most people found a happy alternative job here on earth anyways. 🌱.'
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name', '')
        height_cm = float(request.POST.get('height_cm', 0))
        if 160 < height_cm < 190:
            result_msg = f'Congratulations {applicant_name}! You have the correct height to be an astronaut.'
            message = ''
        elif height_cm <= 160:
            result_msg = f'Sorry, {applicant_name}. Your height is below the minimum height to be an astronaut.'
        else:
            result_msg = f'Sorry, {applicant_name}. Your height is above the maximum height to be an astronaut.'
        return render(request, 'apply/result.html', {'result_msg': result_msg, 'message': message})
    else:
        return render(request, 'apply/index.html')
