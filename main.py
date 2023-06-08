import json

def calculate_normalized_emotion_scores(file_path):
    # Read the JSON file.
    with open(file_path, 'r') as f:
        data = json.load(f)

    emotion_scores = {}

    # Iterate through the file to get to emotions + scores.
    for item in data:
        for prediction in item["results"]["predictions"]:
            for grouped_prediction in prediction["models"]["prosody"]["grouped_predictions"]:
                for prediction in grouped_prediction["predictions"]:
                    for emotion in prediction["emotions"]:
                        name = emotion["name"]
                        score = emotion["score"]

                        # Add score to the appropriate list in the dictionary.
                        if name not in emotion_scores:
                            emotion_scores[name] = [score]
                        else:
                            emotion_scores[name].append(score)

    # calculate the sum of scores for each emotion
    sum_scores = {emotion: sum(scores) for emotion, scores in emotion_scores.items()}
    
    # Normalize the sum of scores
    min_sum_score = min(sum_scores.values())
    max_sum_score = max(sum_scores.values())
    range_sum_scores = max_sum_score - min_sum_score

    normalized_scores = {}
    for emotion, sum_score in sum_scores.items():
        if range_sum_scores != 0:
            normalized_scores[emotion] = (sum_score - min_sum_score) / range_sum_scores
        else:
            normalized_scores[emotion] = 1  # if all sums are the same, normalize to 1

    return normalized_scores

# Run
normalized_emotion_scores = calculate_normalized_emotion_scores('./data.json')
print(normalized_emotion_scores)



""" THIS JUST SUMS SCORES, NO NORMALIZE
def calculate_average_emotion_scores(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)


    emotion_scores = {}

    for item in data:
        for prediction in item["results"]["predictions"]:
            for grouped_prediction in prediction["models"]["prosody"]["grouped_predictions"]:
                for prediction in grouped_prediction["predictions"]:
                    for emotion in prediction["emotions"]:
                        name = emotion["name"]
                        score = emotion["score"]

                        # Add score to the appropriate list in the dictionary.
                        if name not in emotion_scores:
                            emotion_scores[name] = [score]
                        else:
                            emotion_scores[name].append(score)

    average_scores = {}
    for emotion, scores in emotion_scores.items():
        average_scores[emotion] = sum(scores) / len(scores)
    
    return average_scores

average_emotion_scores = calculate_average_emotion_scores('./data.json')
print(average_emotion_scores)
"""