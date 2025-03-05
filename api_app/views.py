from http import HTTPStatus

from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_app.models import Student
from api_app.serializer import StudentSerializer

# Create your views here.

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

@api_view(['GET'])
def single_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return Response(status=HTTPStatus.NO_CONTENT)




# 200 -- OK
# 300 -- Redirect
# 400 -- Bad
# 500 -- Bad on Server Side