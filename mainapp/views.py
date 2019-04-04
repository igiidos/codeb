from django.shortcuts import render
from .models import IndexMarkUp


# 아래 test 버전은 구동확인을 위해 임시로 만든 것이니 삭제하지 마시고 새로 추가해서 작성하시기 바랍니다.
# 규칙 약속하기 : 함수명과 template HTML 파일명 일치 시키기
def index(request):
    markup = IndexMarkUp.objects.get(markup_title=1)
    context = {
        'markup': markup,
    }
    return render(request, 'mainapp/index.html', context)

