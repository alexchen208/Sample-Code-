def registration_business(request):
  context = {}
  if request.POST:
    form = RegistrationBusinessForm(request.POST)
    if form.is_valid():
      form.save()
      user = request.user.id
      business_id = form.instance.id
      UserForm.objects.get(id=user).business.add(business_id)
      return redirect('construct_email')
    else:
      context['registration_business_form'] = form
  else:
    form = RegistrationBusinessForm()
    context['registration_business_form'] = form
  return render(request, 'registration/business1.html', context)