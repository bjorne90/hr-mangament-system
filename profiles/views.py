from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.urls import reverse
from .models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator

@login_required
def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
        booked_workshifts = profile.booked_workshifts.all()
        return render(request, 'profiles/profile_detail.html', {'profile': profile, 'booked_workshifts': booked_workshifts})
    except Profile.DoesNotExist:
        return render(request, 'profiles/create_profile.html')


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Update the profile with the form data
        profile.phone_number = request.POST.get('phone_number')
        profile.email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if the password and confirm_password match
        if password == confirm_password:
            profile.user.set_password(password)
            profile.user.save()
        else:
            return render(request, 'profiles/edit_profile.html', {'profile': profile, 'error': 'Passwords do not match'})

        profile.about_me = request.POST.get('about_me')
        profile.profile_image = request.FILES.get('profile_image')

        # Save the updated profile
        profile.save()

        # Redirect to the profile detail page
        return redirect('profiles:profile_detail')
    else:
        return render(request, 'profiles/edit_profile.html', {'profile': profile})


def user_login(request):
    # Login logic
    # ...

    return redirect(reverse('profiles:profile_detail'))

@login_required
def profile(request):
    user_profile = request.user.profile
    booked_workshifts = user_profile.booked_workshifts.all()
    return render(request, 'profiles/profile.html', {'booked_workshifts': booked_workshifts})

@login_required
def work_shifts(request):
    user_profile = request.user.profile
    booked_workshifts = Booking.objects.filter(user=user_profile.user)
    return render(request, 'profiles/profile_detail.html', {'booked_workshifts': booked_workshifts})

def links(request):
    employees = Profile.objects.all()
    return render(request, 'profiles/links.html', {'employees': employees})

@login_required
def employees(request):
    users = User.objects.order_by('first_name')

    # Pagination
    paginator = Paginator(users, 5)  # Show 5 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees.html', {'page_obj': page_obj, 'users': page_obj.object_list})