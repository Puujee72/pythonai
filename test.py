from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# ChatBot үүсгэх
chatbot = ChatBot('TeacherBot')

# Dataset: Багш-Сурагч сэдэвтэй
training_data = [
    "Сайн уу", "Сайн байна уу!",
    "Багш аа, өнөөдрийн хичээл юу вэ?", "Өнөөдөр Python програмчлалын хичээл орно.",
    "Гит гэж юу вэ?", "Git бол хувилбар хянах систем юм.",
    "GitHub гэж юу вэ?", "GitHub бол код хадгалах, хуваалцах онлайн платформ.",
    "Python гэж юу вэ?", "Python бол хялбар, хүчирхэг програмчлалын хэл юм.",
    "Та миний гэрийн даалгаврыг шалгасан уу?", "Тийм ээ, би шалгасан.",
    "Яаж AI сурах вэ?", "AI сурахын тулд Python хэл, ML, Data Science-ийн үндсийг судлаарай.",
    "Багш аа, та сайн уу?", "Баярлалаа, сайн байна.",
    "Талархлаа", "Зүгээр ээ, амжилт хүсье!",
    "Баяртай", "Баяртай!"
]

# Сургах
trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Вэб хуудас
@app.route("/")
def index():
    return render_template("index.html")

# Чат асуултад хариу өгөх route
@app.route("/get")
def get_response():
    user_text = request.args.get("msg")
    response = chatbot.get_response(user_text)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
