from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.views import View


class Tasks(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                "tasks": Task.objects.filter(user=request.user)
            }
            return render(request, "index.html", context)
        return redirect('login')

    def post(self, request):
        Task.objects.create(
            user=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST['deadline'],
        )
        return redirect('/tasks/')


def ochir(request, pk):
    if request.user.is_authenticated:
        Task.objects.get(id=pk).delete()
        return redirect('/tasks/')
    return redirect('login')


def edit(request, pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            tahrirlash = Task.objects.get(id=pk)
            if tahrirlash.user == request.user:
                tahrirlash.title = request.POST['title']
                tahrirlash.description = request.POST['description']
                tahrirlash.status = request.POST['status']
                tahrirlash.save()
                return redirect('/tasks/')
            return redirect('login')

    context = {
        "tasks": Task.objects.get(id=pk)
    }
    return render(request, 'edit.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect('/tasks/')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
