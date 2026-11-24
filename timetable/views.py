from django.shortcuts import render

def timetable_view(request):
    timetable = {
        'Monday': ['Maths', 'Physics', 'English'],
        'Tuesday': ['Chemistry', 'Maths', 'Sports'],
        'Wednesday': ['English', 'Physics', 'Maths'],
        'Thursday': ['Maths', 'Chemistry', 'English'],
        'Friday': ['Physics', 'Sports', 'Maths'],
    }
    return render(request, 'timetable.html', {'timetable': timetable})