import json
from datetime import datetime
import os
from glob import glob

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


"""
ChatGPT에게 원하는 역할을 세부적으로 지정하여 
원하는 쿼리를 날립니다.
"""

def get_sentencecs():
    global predictions
    prediction_files = glob(r'C:\Users\JeongSeongYun\Desktop\OpenHands\OHTest\word_outputs\*.json')
    target_file = prediction_files[-1]
    with open(f'{target_file}', 'r') as f:
        predictions = json.load(f)

    system_msg = """
                You are a translator that transforms words into sentences. 
                You consider the order of the words in the incoming list to create an accurate sentence. 

                For instance, if the incoming list is ['if', 'you', 'have', 'student', 'licence', 'can', 'get', 'discount'], 
                your translation should be, "If you have a student license, you can get a discount."

                However, the sentence must be very natural.
                Also, you must not invent other words outside of those given for use in your translation.

                """

    query = """
            Please create a sentence composed of elements from the incoming word list.
            However, you must consider the order of the words in the list. 
            Also, you must not invent other words outside of those given for use in your translation.
            """



    user_msg = str(predictions) + "\n\n" + query

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", #TODO: 어떤 모델이 적합할지 테스트 해보기 
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )

    return response.choices[0].message.content

def get_result_json():
    result={}
    try:
        sentence = get_sentencecs()
        result['status'] = "success"
    except :
        result['status'] = "error"
        print("Something is Wrong!! Do Something")
        return
    
    result['predicted_sentence'] = sentence

    now =  datetime.now()
    log_time = now.strftime("%y%m%d_%H%M")  # Format as "yymmdd_HHMM"

    result_log_file_name = f"{log_time}.json"

    file_path = fr"C:\Users\JeongSeongYun\Desktop\OpenHands\OHTest\sentence_ouptuts\{result_log_file_name}"
    with open(file_path, "w", encoding="utf-8") as output:
        json.dump(result, output, ensure_ascii=False, indent=4)

    print(f"✅ Input Word List : {predictions}")
    print(f"🤖 Output Sentence : {sentence}" )

    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    
    return data

if __name__ == "__main__":                          
    get_result_json()                