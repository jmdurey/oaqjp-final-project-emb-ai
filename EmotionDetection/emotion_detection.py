import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    
    # 1. Turn the response text into a dictionary (like a real Python list)
    formatted_response = json.loads(response.text)
    
    # 2. Dig into the dictionary to find the emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # 3. Get the specific scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 4. Find the emotion with the biggest number
    dominant_emotion = max(emotions, key=emotions.get)
    
    # 5. Put it all in the neat package the lab asked for
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result
