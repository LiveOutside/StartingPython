import random
way = '3'
print('Вы находитесь в комнате в которой имеется', way, 'прохода. Выберите куда пойти.')
if way == '3':
    answer1 = input()
    if answer1 == '1':
	      print('Вы входите в комнату в которой    имеется 2 прохода')
	      print('Выберите проход.')
	      answer = input()
	      if answer11 == '1':
	          print('Вы зашли в тупик.')
	      elif answer11 == '2':
	          print('Вы смогли пройти лабиринт. Поздравляю!')
    elif answer1 == '2':
        print('Вы входите в комнату, в ней нет проходов.')
        print('Вы видите тёмную фигуру в углу комнаты.')
        print('На вас напал Жак Фреско! Он даёт вам на решение загадки 30 секунд! ')
        print('"Сколько орехов в сумке у пожилого бобра?"')
        answers = ['1','500','76083221']
        answer = random.choice(answers)
        word = input()
        if word == answer:
            print('Смерть..?')
        elif word != answer:
            print('Вы ответили не верно.')
            print('От этих слов ваш персонаж впадает в депрессию')
            depression = ['1','0']
            depressiondeath = random.choice(depression)
            if depressiondeath == '1':
                print('Вы умерли от ужасной депрессии Жака фреско.')
            elif depressiondeath == '0':
                print('Вы выживаете и чудом спасаетесь из лабиринта.')
	  
	  