import requests
import json
def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Extract emotion scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        # Find dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }