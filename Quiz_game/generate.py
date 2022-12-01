import requests
import html

questions = []

def generateQ(n):
    cnt = 1
    for i in range(n):
        resp = requests.get(url='https://opentdb.com/api.php?amount=1&type=boolean')
        data = resp.json()
        resp_code = data['response_code']
        s = html.unescape(data['results'][0]['question'])
        question = 'Q.' + str(cnt) + '. ' + s
        correct_ans =  data['results'][0]['correct_answer']
        if(resp_code == 0):
            cnt += 1
            questions.append([question,correct_ans])
        else:
            n = n + 1
    
    return questions