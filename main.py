from deeppavlov import build_model

model = build_model('squad_ru_bert', download=True, install=True)
questions = ["Что приготовить на ужин?"]
answer, answer_score, answer_place = model(questions)
print(answer)