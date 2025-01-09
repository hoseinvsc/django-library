from django.urls import path
from .views import test, web_test, css_test, home, book_list, checker, days_calculator, days_jcal, convert_date, add_book, BookDetailView,BookUpdateView
# from . import views
urlpatterns = [
    path('test/',test),
    path('web/test/',web_test),
    path('css/test',css_test),
    path('', home),
    path('books/',book_list),
    path('checker/',checker),
    path('days_calculator/',days_calculator),
    path('days_jcal/', days_jcal),
    path('convert/',convert_date),
    path('add-book/',add_book),
    # path('book/<int:book_id>/',book_detail, name='book_detail'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),

]