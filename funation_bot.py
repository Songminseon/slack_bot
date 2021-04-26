import json
import requests
import slack
import time 
import schedule
import datetime

def post_to_slack(message):
    my_webhook = "https://hooks.slack.com/services/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"
    slack_data = json.dumps({'text':message})
    response = requests.post(
        my_webhook,
        data=slack_data,
        headers={'Content-Type':'application/json'}
        )
    
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' %(response.status_code, response.text))

def search_api():
    data=requests.get('https://do.funation.io/function/getSubmitList')
    my_data = data.json()['info']
    if len(my_data) == 0:
        pass
    for i in range(0, len(my_data)):
        giv_data= str(my_data[i]['submit_giv'])
        account_data = str(my_data[i]['submit_accountOwner'])
        date_data = str(my_data[i]['submit_date'])
        message = account_data + "의 예금주명으로 " + giv_data + "기브 충전 왔습니다. 확인해주세요. 기브신청시간 : "+ date_data
        post_to_slack(message)
        
def post_to_slack2(message):
    my_webhook = "https://hooks.slack.com/services/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"
    slack_data = json.dumps({'text': message})
    response = requests.post(
        my_webhook,
        data=slack_data,
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))


def search_api2():
    data = requests.get('https://do.funation.io/api/SearchResult')
    my_data = data.json()['data']
    if len(my_data) == 0:
        pass
    else:
        message = "✨✨응모완료 나왔어요✨✨"
        post_to_slack2(message)

while True:     
        search_api()
        search_api2()
        now = time.localtime()
        print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
        print("다음 알림 %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min+5, now.tm_sec))
        time.sleep(299)
