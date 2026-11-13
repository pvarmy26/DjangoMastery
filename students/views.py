from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import StudentForm, RegisterForm, LoginForm
from .models import Student
from .forms import DocumentUploadForm
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import StudentPermission

@login_required
def home(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            Student.objects.create(
                name=form.cleaned_data["name"],
                age=form.cleaned_data["age"],
                course=form.cleaned_data["course"],
                marks=form.cleaned_data["marks"]
            )

            return redirect("home")

    else:
        form = StudentForm()

    return render(
        request,
        "students/home.html",
        {"form": form}
    )


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "students/register.html",
        {"form": form}
    )


def user_login(request):

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect("home")

    else:
        form = LoginForm()

    return render(
        request,
        "students/login.html",
        {"form": form}
    )


def user_logout(request):

    logout(request)

    return redirect("login")

@login_required
def upload_document(request):
    if request.method == "POST":
        form = DocumentUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("upload_document")
    else:
        form = DocumentUploadForm()

    return render(
        request,
        "students/upload_document.html",
        {"form": form}
    )

@api_view(["GET", "POST"])
@permission_classes([StudentPermission])
def student_api(request):

    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )

@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([StudentPermission])
def student_detail_api(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(
            student,
            data=request.data
        )

    elif request.method == "PATCH":
        serializer = StudentSerializer(
            student,
            data=request.data,
            partial=True
        )

    elif request.method == "DELETE":
        student.delete()
        return Response(status=204)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_api(request):
    return Response({
        "message": "Welcome Admin!"
    })