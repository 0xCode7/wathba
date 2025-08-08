from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student, Feedback


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

            # عدل درجات الطلبة الأقل من 10
            students.filter(grade__lt=10).update(grade=10)

            if students.count() == 1:
                student = students.first()
                try:
                    grade_value = float(student.grade)
                except (ValueError, TypeError):
                    grade_value = 0.0

                if grade_value < 10:
                    student.grade = 10
                    student.save()

                context['search_result'] = student
                context['view'] = 'none'


            elif students.count() > 1:
                context['error'] = '⚠ الاسم غير فريد، يرجى تحديد اسم أكثر دقة'

            else:
                context['error'] = '❌ الطالب غير مسجل بالبرنامج'
                context['suggestions'] = Student.objects.filter(
                    name__startswith=name[:2]
                )[:5]

    # اقرأ المتغير من الجلسة وأرسله للسياق ثم احذفه من الجلسة
    hide_feedback = request.session.pop('hide_feedback_form', False)
    context['hide_feedback_form'] = hide_feedback

    return render(request, 'grade.html', context)



def feedback_view(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text', '').strip()
        if feedback_text:
            Feedback.objects.create(text=feedback_text)
            request.session['feedback_success'] = True
            return redirect('thanks')
        else:
            return render(request, 'grade.html', {'error': 'الرجاء كتابة ملاحظتك.'})
    return redirect('get_students')


def thanks_view(request):
    if request.session.get('feedback_success'):
        del request.session['feedback_success']
        request.session['hide_feedback_form'] = True  # إخفاء الفورم عند العودة
        return render(request, 'thanks.html', {'message': 'شكرًا لانضمامك لرحلة وثبة.. دعمك يلهمنا للاستمرار❤️'})
    else:
        return redirect('get_students')
