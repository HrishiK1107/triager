from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count, Avg
import random

from .forms import BugReportForm
from .models import BugReport


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('dashboard')
        else:
            messages.error(request, "There was an error during registration.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST, request.FILES)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.submitted_by = request.user
            bug.save()

            messages.success(request, "Bug report submitted successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Error in submitting the report. Please check the form.")
    else:
        form = BugReportForm()
    return render(request, 'submit.html', {'form': form})

@login_required
def user_dashboard(request):
    reports = BugReport.objects.filter(submitted_by=request.user)
    return render(request, 'dashboard.html', {'reports': reports})

def leaderboard(request):
    users = User.objects.annotate(
        report_count=Count('bugreport'),
        avg_cvss=Avg('bugreport__cvss_score')
    ).order_by('-report_count', '-avg_cvss')
    
    return render(request, 'leaderboard.html', {'users': users})

@login_required
def homepage(request):
    top_reports = BugReport.objects.order_by('-cvss_score')[:3]

    security_facts = [
        "The first computer bug was an actual moth.",
        "SQL injection is one of the oldest and still most common vulnerabilities.",
        "The term 'zero-day' refers to exploits that have no patch yet.",
        "Social engineering is more dangerous than most technical exploits.",
        "Passwords like 'admin' and '123456' are still among the most used globally.",
    ]

    random_fact = random.choice(security_facts)

    return render(request, 'home.html', {
        'top_reports': top_reports,
        'random_fact': random_fact
    })

@login_required
def bug_detail(request, report_id):
    report = get_object_or_404(BugReport, id=report_id)
    return render(request, 'bug_detail.html', {'report': report})
