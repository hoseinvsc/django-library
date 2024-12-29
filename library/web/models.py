from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="نام")
    last_name = models.CharField(max_length=30, verbose_name="نام خانوادگی")
    id_card = models.IntegerField(null=True, verbose_name="شماره کارت")
    phone_number = models.IntegerField(null=True, verbose_name="شماره تلفن")
    add_time = models.DateTimeField(verbose_name="زمان اضافه شدن", null=True, default=None)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "دانش آموز"
        verbose_name_plural = "دانش آموزان"


class Writer(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="نام")
    last_name = models.CharField(max_length=40, verbose_name="نام خانوادگی")
    birth_year = models.IntegerField(null=True, verbose_name="سال تولد")
    living_place = models.CharField(max_length=40, verbose_name="محل زندگی")
    is_dead = models.BooleanField(verbose_name="زنده میباشد")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"


class Book(models.Model):
    title = models.CharField(max_length=40, verbose_name="عنوان", default="نامشخص")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null= True , verbose_name= 'دسته بندی' )
    writer = models.ForeignKey('Writer', on_delete=models.CASCADE, verbose_name="نویسنده")
    number_of_pages = models.IntegerField(null=True, verbose_name="تعداد صفحات")
    cover_type = models.CharField(max_length=40, verbose_name="نوع جلد")
    printing_time = models.TimeField(verbose_name="ساعت چاپ", null=True)
    avaliable = models.BooleanField(verbose_name="موجود در کتابخانه")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
        ordering = ('-number_of_pages',)




class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    description = models.TextField(verbose_name="توضیحات", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class Borrow(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE, verbose_name="دانش‌آموز")
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name="کتاب")
    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ قرض گرفتن")
    return_date = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ بازگشت")
    is_returned = models.BooleanField(default=False, verbose_name="کتاب بازگشت داده شده؟")
    
    def __str__(self):
        return f"{self.student.first_name} - {self.book.title}"

    class Meta:
        verbose_name = "قرض گرفتن کتاب"
        verbose_name_plural = "قرض گرفتن کتاب‌ها"



class Review(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE, verbose_name="دانش‌آموز")
    book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name="کتاب")
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name="امتیاز")
    
    def __str__(self):
        return f"نظر {self.student.first_name} درباره {self.book.title}"

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
