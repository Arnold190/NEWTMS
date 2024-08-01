from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Attendance, Meetings
from django.contrib import messages
from .forms import TaskForm, UploadForm, DeadlineForm
from .models import Task, Uploads, Deadline
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

class CustomLoginView(LoginView):
    template_name = 'Checkpoint/login.html'  # Replace with your actual template path

    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('dashboard')  
    

@login_required
def dashboard(request):
    context = {
        'username': request.user.username,
        
    }
    return render(request, 'Checkpoint/userdashboard.html', context)


#@login_required
#def dashboard(request):
 #context = {
      #  'username': request.user.username,
    #}

    #return render(request, 'Checkpoint/userdashboard.html') 


#def LoginView(request):
  # return render(request, 'Checkpoint/login.html')

@csrf_protect
def LoginView(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'Checkpoint/login.html', {'login': form})


##########



@login_required
def clock_in(request):
    user = request.user
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(user=user, work_date=today)
    if not attendance.clock_in_time:
        attendance.clock_in_time = timezone.now()
        attendance.save()
    return redirect('attendance_status')

@login_required
def clock_out(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, work_date=today).first()
    if attendance and not attendance.clock_out_time:
        attendance.clock_out_time = timezone.now()
        attendance.save()
    return redirect('attendance_status')

@login_required
def attendance_status(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, work_date=today).first()
    return render(request, 'attendance_status.html', {'attendance': attendance})

def meeting_links(request):
    meetings = Meetings.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})


def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        upload_form = UploadForm(request.POST, request.FILES)
        if task_form.is_valid() and upload_form.is_valid():
            upload = upload_form.save()
            task = task_form.save(commit=False)
            task.uploads = upload
            task.save()
            return redirect('task_list')  # Redirect to a task list or another page
    else:
        task_form = TaskForm()
        upload_form = UploadForm()
    return render(request, 'create_task.html', {'task_form': task_form, 'upload_form': upload_form})


@login_required
def create_deadline(request):
    if request.method == 'POST':
        form = DeadlineForm(request.POST)
        if form.is_valid():
            deadline = form.save(commit=False)
            deadline.created_by = request.user
            deadline.save()
            return redirect('deadline_list')  # Change this to the name of your deadline list view
    else:
        form = DeadlineForm()
    return render(request, 'create_deadline.html', {'form': form})

@login_required
def deadline_list(request):
    deadlines = Deadline.objects.all()
    return render(request, 'deadline_list.html', {'deadlines': deadlines})


@login_required
def total_employees(request):
    total = User.objects.count()
    context = {'total': total}
    return render(request, 'total_employees.html', context)