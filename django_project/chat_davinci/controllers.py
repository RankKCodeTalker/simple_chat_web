import json
from django.http import HttpResponse, HttpRequest


def log(question, answer):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.writelines("Q:"+question+"\n")
        f.writelines("A:"+answer+"\n")

def ask(request):
    # request.encoding = 'utf-8'
    print(request.body)
    print(request.POST)
    request_dict = json.loads(request.body)
    question = request_dict['prompt']
    response = {}
    try:
        response['code'] = 0
        response['text'] = "你好！"
        return HttpResponse(json.dumps(response, ensure_ascii=False))
    except Exception as e:
        response['code'] = 1
        response['text'] = str(e)
        return HttpResponse(json.dumps(response, ensure_ascii=False))

