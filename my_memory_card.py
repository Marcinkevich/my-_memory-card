from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton, 
        QPushButton, QLabel)
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Как называется активная оболочка Земли, которая населена живыми организмами?', 'Биосфера', 'Криосфера', 'Гидросфера', 'Тропосфера'))
questions_list.append(Question('Что означает выражение "Вскрыть ящик пандоры?"', 'Сделать действие с необратимыми последствиями, которое нельзя отменить', 'Умереть', 'Ничего', 'Посмореть в ящик'))
questions_list.append(Question('Кто такие фрики?', 'Необычные люди ', 'Эксцентричные люди', 'Животные', 'Рыбы'))
questions_list.append(Question('Кто такие друиды?','жрецы у древних кельтских народов','мифические существа','Люди ','НЕ ведаю!'))
questions_list.append(Question('Кто такие драконы?','ряд мифологических и фантастических существ','Кролики','Люди ','НЕ ведаю!'))
questions_list.append(Question('Кто такие энты','в легендариуме Дж. Р. Р. Толкина один из народов, населяющих Средиземье','Деревья','Листья', 'Ветки'))
questions_list.append(Question('СКОЛЬКО книг написал Дж. Р. Р. Толкин?','2','4','1','3'))
questions_list.append(Question('Что такое на языке древних эльфов БРИСИНГР?','огонь', 'вода', 'эль', 'ром'))
questions_list.append(Question('Кто такой Эрагон?','главный герой тетралогии Кристофера Паолини «Наследие»', 'слон', 'эльф', 'мяч'))
questions_list.append(Question('Какое растение называют «живым светофором»?','Медуница', 'Ромашка', 'Подорожник', 'Колокольчик'))



app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('ОСЕНЬ селёзны ваплос !!!!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout() 
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет? Вот в чём вопрос!?')
lb_Correct = QLabel('ответ тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox) 
layout_line2.addWidget(AnsGroupBox) 
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('НУ ТЫ КРУТ, ПРАВИЛЬНО!!!!!')
        window.score += 1
        print('Статистика/n-всего вопросов', window.total, '/n-Правильных ответов', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('НЕТ НЕТ НЕТ И ЕЩЁ РАЗ НЕТ!!!!!')
            print('Рейтинг:', (window.score/window.total*100), '%')


def next_question():
    window.total += 1
    print('Статистика/n-всего вопросов', window.total, '/n-Правильных ответов', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')



btn_OK.clicked.connect(click_OK)

window.total = 0
window.score = 0

next_question()
window.resize(400, 300)
window.show()
app.exec()
