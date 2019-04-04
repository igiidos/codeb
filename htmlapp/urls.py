from django.urls import path
from . import views


# 아래 test 버전은 구동확인을 위해 임시로 만든 것이니 삭제하지 마시고 새로 추가해서 작성하시기 바랍니다.
# 규칙 약속하기 : path값과 name값은 항상 view 함수명과 일치 시키기(테스트 버전 참조)
urlpatterns = [
    path('html_study_list/', views.html_study_list, name='html_study_list'),
    path('html_test/', views.html_test, name='html_test'),
    path('html_editor1/', views.html_editor1, name='html_editor1'),
    path('html_editor_include/', views.html_editor_include, name='html_editor_include'),
    path('add_text_json/', views.add_text_json, name='add_text_json'),
]
