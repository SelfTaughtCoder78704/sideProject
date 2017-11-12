from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from django.views import generic
from contractor.forms import (
    RegistrationForm,
    EditProfileForm,

)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from .models import work, worker


class IndexView(generic.ListView):
    template_name = 'contractor/index.html'

    def get_queryset(self):
        return work.objects.all()


class DetailView(generic.DetailView):
    model = work
    template_name = 'contractor/detail.html'

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contractor/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'contractor/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'contractor/profile.html', args)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('contractor:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form }
        return render(request, 'contractor/edit_profile.html', args)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():

            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('contractor:view_profile'))
        else:
            return redirect(reverse('contractor:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form }
        return render(request, 'contractor/change_password.html', args)

