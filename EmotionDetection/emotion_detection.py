def emotion_detector(text_to_analyze):
    # We are bypassing the internet call because it's broken
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }