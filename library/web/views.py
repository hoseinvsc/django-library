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


from .models import Book, Category, Writer

def add_book(request):
    message = ""
    categories = Category.objects.all()
    writers = Writer.objects.all()

    if 'title' in request.GET:
        title = request.GET.get('title', "نامشخص")
        category_id = request.GET.get('category')
        writer_id = request.GET.get('writer')
        number_of_pages = request.GET.get('number_of_pages')
        cover_type = request.GET.get('cover_type')
        printing_time = request.GET.get('printing_time')
        avaliable = request.GET.get('avaliable') == 'on'

        if title and category_id and writer_id and cover_type:
            try:
                category = Category.objects.get(id=category_id)
                writer = Writer.objects.get(id=writer_id)

                Book.objects.create(title=title,category=category,writer=writer,number_of_pages=number_of_pages,cover_type=cover_type,printing_time=printing_time,avaliable=avaliable)
                message = "کتاب اضافه شد!"
            except (Category.DoesNotExist, Writer.DoesNotExist):
                message = "دسته‌بندی یا نویسنده نامعتبر است."
        else:
            message = "لطفاً تمام فیلدها را پر کنید."
    return render(request, 'add_book.html', {'message': message, 'categories': categories, 'writers': writers})
