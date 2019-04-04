from django.shortcuts import render


# 아래 test 버전은 구동확인을 위해 임시로 만든 것이니 삭제하지 마시고 새로 추가해서 작성하시기 바랍니다.
# 규칙 약속하기 : 함수명과 template HTML 파일명 일치 시키기
def js_test(request):
    context = {

    }
    return render(request, 'jsapp/js_test.html', context)

def lesson(request):
    context = {

    }
    return render(request, 'jsapp/lesson1.html', context)



def js_study_list(request):
    context = {

    }
    return render(request, 'jsapp/_js_study_list.html', context)