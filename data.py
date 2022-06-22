import requests
import html


def get_questions():
    endpoint = "https://opentdb.com/api.php?amount=20&type=boolean"
    response = requests.get(url=endpoint)
    response.raise_for_status()

    questions = []
    for item in response.json()["results"]:
        item["question"] = html.unescape(item["question"])
        questions.append(item)
    return questions


question_data = get_questions()
