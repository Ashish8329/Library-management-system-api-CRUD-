from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet, basename = 'book')
router.register(r'user', UserViewSet, basename = 'user') 
router.register(r'borrowingbook', BorrowingBookViewSet, basename = 'borrowingbook')
urlpatterns = router.urls

#for generic viewset
# urlpatterns = [ 
#     path('book/',Booklist_create_view.as_view(),name='book-list'),
#     path('book/<int:pk>/',Book_details_view.as_view(),name='book-details'),
#     path('user/',User_list.as_view(),name='book-list'),
#     path('user/<int:pk>/',User_details.as_view(),name='User_details'),
#     path('BorrowingBook/',BorrowingBook_list.as_view(),name='book-list'),
#     path('BorrowingBook/<int:pk>/',BorrowingBook_details.as_view(),name='book-details'),
# ]

