from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def registration_view(request):
  context = {}
  if request.POST:
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data.get('email')
      raw_password = form.cleaned_data.get('password1')
      account = authenticate(email = email, password = raw_password)
      login(request, account)
      return redirect('post_signup')
    else:
      context['registration_form'] = form
  else:
    form = RegistrationForm()
    context['registration_form'] = form
  return render(request, 'registration/signup.html', context)