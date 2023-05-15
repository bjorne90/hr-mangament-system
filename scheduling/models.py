from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class WorkShift(models.Model):
    name = models.CharField(max_length=100, default='Location')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    role = models.CharField(max_length=100, blank=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

@login_required
def workshift_list(request):
    from .models import WorkShift
    workshifts = WorkShift.objects.exclude(booking__isnull=False)
    return render(request, 'scheduling/workshift_list.html', {'workshifts': workshifts})

@login_required
def book_workshift(request, workshift_id):
    from booking.models import Booking
    workshift = WorkShift.objects.get(id=workshift_id)

    if request.method == 'POST':
        # Handle the booking logic
        # ...

        # Update the user's profile with the booked workshift
        user_profile = request.user.profile
        user_profile.booked_workshifts.add(workshift)
        user_profile.save()

        # Render a success message
        success_message = 'Du är bokad på detta pass.'
        return render(request, 'scheduling/book_workshift.html', {'workshift': workshift, 'success_message': success_message})

    return render(request, 'scheduling/book_workshift.html', {'workshift': workshift})

@login_required
def work_shifts(request):
    from booking.models import Booking
    user_profile = request.user.profile
    booked_workshifts = Booking.objects.filter(user=user_profile)
    return render(request, 'scheduling/work_shifts.html', {'booked_workshifts': booked_workshifts})

@login_required
def add_event(request):
    # Handle adding event logic
    return render(request, 'scheduling/add_event.html')

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workshift = models.ForeignKey(WorkShift, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return f"Booking: {self.user} - {self.workshift}"
