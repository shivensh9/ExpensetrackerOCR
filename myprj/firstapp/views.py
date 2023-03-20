from django.shortcuts import render
from .forms import InputForm
from django.http import HttpResponse,HttpResponseRedirect
from .functions import handle_uploaded_file
# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST,request.FILES)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # roll_number = form.cleaned_data['roll_number']
            msg=handle_uploaded_file(request.FILES['file'])
            # msg=first_name+"   "+last_name+"   "+(str)(roll_number)
            return HttpResponse(msg)
    else:
        context = {}
        context['form'] = InputForm()
        return render(request, "home.html", context)


