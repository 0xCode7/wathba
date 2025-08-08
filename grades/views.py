from django.shortcuts import render
from .models import Student



def index(request):
    return render(request, 'base.html')
def students_view(request):
    context = {}

    if request.method == 'GET':
        # لو فيه gender → عرض الأوائل
        gender = request.GET.get('gender')
        if gender:
            context['top_students'] = Student.objects.filter(
                is_best=True,
                gender=gender
            ).order_by('-grade')

    elif request.method == 'POST':
        # بحث عن طالب
        name = request.POST.get('name', '').strip()

        if not name:
            context['error'] = '⚠ الاسم مطلوب'
        else:
            students = Student.objects.filter(name__icontains=name)

            if students.count() == 1:
                context['search_result'] = students.first()

            elif students.count() > 1:
                context['error'] = '⚠ الاسم غير فريد، يرجى تحديد اسم أكثر دقة'

            else:
                context['error'] = '❌ الطالب غير مسجل بالبرنامج'
                context['suggestions'] = Student.objects.filter(
                    name__startswith=name[:2]
                )[:5]

    return render(request, 'grade.html', context)
