from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from app.models import Course, Student
import csv
def construct_csv_from_model(request):
    courses=Course.objects.all()
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="courses_data.csv"'
    writer=csv.writer(response)
    writer.writerow(["Course Name","Course Code","Credits"])
    for course in courses:
        writer.writerow([course.course_name,course.course_code,course.course_credits])
    return response
def construct_pdf_from_model(request):
    courses=Course.objects.all()
    response=HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="courses_data.pdf"'
    c=canvas.Canvas(response)

    c.drawString(70,720,"Course Name")
    c.drawString(170,720,"Course Code")
    c.drawString(270,720,"Credits")
    y=660
    for course in courses:
        c.drawString(70,y,course.course_name)
        c.drawString(170,y,course.course_code)
        c.drawString(270,y,str(course.course_credits))
        y=y-60
    c.showPage()
    c.save() 
    return response