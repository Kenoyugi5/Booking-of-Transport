from django.shortcuts import render, get_object_or_404
from .models import Class, Student

# Create your views here.
def classes(request):
	class_list = [
		{'id': 1, 'name': 'Grade 1'},
		{'id': 2, 'name': 'Grade 2'},
		{'id': 3, 'name': 'Grade 3'},
		{'id': 4, 'name': 'Grade 4'},
		{'id': 5, 'name': 'Grade 5'},
		{'id': 6, 'name': 'Grade 6'},
		{'id': 7, 'name': 'Grade 7A'},
		{'id': 8, 'name': 'Grade 7&'},
		{'id': 19, 'name': 'Grade 8A'},
		{'id': 20, 'name': 'Grade 8&'},
		{'id': 11, 'name': 'Form 1A'},
		{'id': 12, 'name': 'Form 1&'},
		{'id': 13, 'name': 'Form 2A'},
		{'id': 14, 'name': 'Form 2&'},
		{'id': 15, 'name': 'Form 3A'},
		{'id': 16, 'name': 'Form 3&'},
		{'id': 17, 'name': 'Form 4A'},
		{'id': 18, 'name': 'Form 4&'},
	]

	primary_classes = [cls for cls in class_list if 1 <= cls['id'] <= 6]
	jss_classes = [cls for cls in class_list if cls['id'] in [7, 8, 19, 20]]
	highschool_classes = [cls for cls in class_list if 11 <= cls['id'] <= 18]

	context = {
		'primary_classes': primary_classes,
		'jss_classes': jss_classes,
		'highschool_classes': highschool_classes
	}

	return render(request, 'classes.html', context)

def student_list_view(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    students = class_obj.students.all()
    return render(request, 'student_list.html', {'class_obj': class_obj, 'students': students})