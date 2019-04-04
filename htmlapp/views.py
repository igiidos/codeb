from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from .models import HtmlEditor


# 아래 test 버전은 구동확인을 위해 임시로 만든 것이니 삭제하지 마시고 새로 추가해서 작성하시기 바랍니다.
# 규칙 약속하기 : 함수명과 template HTML 파일명 일치 시키기
def html_editor1(request):
    context = {

    }
    return render(request, 'htmlapp/html_editor1.html', context)

def iframe_test(request):
    pass


def html_test(request):
    context = {

    }
    return render(request, 'htmlapp/html_test.html', context)


def add_text_json(request):
    if request.is_ajax():
        get_text = request.POST.get('edit')

        create_text = HtmlEditor.objects.create(
            text=get_text
        )
        create_text.save()

        html = {
            'contexts': get_text
        }
        return JsonResponse(html)
