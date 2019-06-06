from itertools import islice

test = [{"question": "Найбiльш iнформативним методом дiагностики дiафрагмальної кили є11111:",
         "answers": [
             {"percent": "0%",
              "text": "Езофаготонокiмографiя"},
             {"percent": "0%",
              "text": "Езофагоскопiя"},
             {"percent": "0%",
              "text": "Ультразвукове дослідження"},
             {"percent": "0%",
              "text": "Комп'ютерна томографiя"},
             {"percent": "100%",
              "text": "Рентгенограма шлунка в горизонтальному та вертикальному положеннi хворого із застосуванням барію"},
         ]},
        {"question": "Найбiльш iнформативним методом дiагностики дiафрагмальної кили є22222:",
         "answers": [
             {"percent": "0%",
              "text": "Езофаготонокiмографiя"},
             {"percent": "0%",
              "text": "Езофагоскопiя"},
             {"percent": "0%",
              "text": "Ультразвукове дослідження"},
             {"percent": "0%",
              "text": "Комп'ютерна томографiя"},
             {"percent": "100%",
              "text": "Рентгенограма шлунка в горизонтальному та вертикальному положеннi хворого із застосуванням барію"},
         ]}
        ]

for i in test:
    i['first_letters'] = ''.join(k.lower()[0] for k in islice(i['question'].split(' '), 0, 4))
print(test)



#
#
#
# answers = "".join("%s - %s \n"%(i['percent'],i['text']) for i in test[0]['answers'])
# print(answers)

