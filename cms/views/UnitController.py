from django.urls import path, include



def index(request):
    pass


def create_unit(request):
    pass    



def update_unit(request, id:int):
    pass



def delete_unit(request, id:int):
    pass



def get_unit(request, id:int):
    pass






urlpatterns = [
    path('', index, name='units'),
    path('create', create_unit, name='create_unit'),
    path('update/<int:id>', update_unit, name='update_unit'),
    path('delete/<int:id>', delete_unit, name='delete_unit'),
    path('<int:id>', get_unit, name='get_unit'),
]