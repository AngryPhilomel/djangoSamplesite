from django.urls import path

from .views import index, by_rubric, BbCreateView, BbDetailView, BbByRubricView, BbAddView, BbEditView, BbDeleteView, rubricform

urlpatterns = [
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('rubrics/', rubricform, name='rubrics'),
    path('add/', BbAddView.as_view(), name='add'),
    path('detail/<int:pk>', BbDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BbEditView.as_view(), name='update'),
    path('delele/<int:pk>', BbDeleteView.as_view(), name='delete'),
    path('', index, name='index'),
]