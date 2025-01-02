from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
import jdatetime


from .models import Book

def test(request):
    return HttpResponse("hello world!")

def web_test(request):
    return render(request,'index.html')

def css_test(request):
    return render(request, 'css_test.html')

def home(request):
    return HttpResponse()
def book_list(request):
    b = Book.objects.all()
    return render(request, 'book_list.html', {'books': b})


def checker(request):
    age = request.GET.get('age')
    gender = request.GET.get('gender')
    message=''

    if age and gender:
        age = int(age)
        
        if (gender == 'female' and age < 9) or (gender == 'male' and age < 15):
            message = 'شما مجوز ندارید.'
        else:
            message = 'شما مجوز دارید.'
    
    return render(request, 'checker.html',{'message': message})




def days_calculator(request):
    input = request.GET.get('birth')
    if input :
        try:
            year, month, day = input.split('-')
            year = int(year)
            month = int(month)
            day = int(day)
        
            birth_date = date(year, month, day)
            today = date.today()
            days_lived = (today - birth_date).days
            return render(request, 'days_calculator.html', {'days': days_lived})

        except :
            return render(request, 'days_calculator.html', {'error': 'Please enter date in YYYY-MM-DD format!'})

    return render(request, 'days_calculator.html')



def days_jcal(request):
    input_date = request.GET.get('birth')
    if input_date:
        try:
            year, month, day = input_date.split('-')
            year = int(year)
            month = int(month)
            day = int(day)
            birth_date = jdatetime.date(year, month, day)
            today = jdatetime.date.today()
            delta = today - birth_date
            return render(request, 'days_jcal.html', {'days': delta.days})
        except ValueError:
            return render(request, 'days_jcal.html', {'error': 'Please enter date in YYYY-MM-DD format!'})

    return render(request, 'days_jcal.html')



def convert_date(request):
    if request.method == 'POST':
        input = request.POST.get('persian_date')
        if input:
            try:
                persian_date = jdatetime.datetime.strptime(input, '%Y-%m-%d')
                converted_date = persian_date.togregorian().strftime('%Y-%m-%d')
                return render(request, 'convert_date.html', {'converted_date': converted_date,'persian_date': persian_date.date})
            except:
                message = "تاریخ درست وارد نشده"
                return render(request, 'convert_date.html', {'message': message})
    return render(request, 'convert_date.html')




from .models import Book

def search_book(request):
    books = None
    message = None
    
    if request.method == "GET":
        book_name = request.GET.get('book_name')
        printing_time = request.GET.get('printing_time')
        if book_name and printing_time:
            books = Book.objects.filter(title__icontains=book_name)
            books = books.filter(printing_time=printing_time)

            if books:
                message = f"کتاب‌هایی که با '{book_name}' پیدا شدند:"
            else:
                message = "کتابی پیدا نشد"
    return render(request, 'book_search.html', {'message': message, 'books': books})




# ایجاد یک فرم در فرانت برای ایجاد یک کتاب از سمت فرانت