# import datetime
# from time import sleep
# 1

# class Clock:    
    
#     def time(self):
#         print(datetime.datetime.now())


# class Alarm:
#     alarm = None
#     def alarm_on(self):
#         Alarm.alarm = True

    
#     def alarm_off(self):
#         Alarm.alarm = False


# class AlarmClock(Alarm, Clock):
       
#     def alarm_set(self, day=0,hour=0,minutes=0):
#         while AlarmClock.alarm:
#             time_now = datetime.datetime.now()
#             print
#             if str(time_now.hour) == hour and str(time_now.minute) == minutes and str(time_now.day) == day:
#                 print('ALARM')
#                 break
#             sleep(1)



# alarm = AlarmClock()
# alarm.time()
# alarm.alarm_on()
# alarm.alarm_set(day="24",hour="1",minutes="44")

#2

# class Coder:
    
#     experience = ''
#     count_code_time = 0

#     def get_info(self):
#         pass

#     def coding(self):
#         pass


# class Backend(Coder):

#     def init(self, languages_backend):
#         self.experience = languages_backend

#     def get_info(self):
#         print(f'Ваш язык {self.experience} ваше время кода {self.count_code_time} часов ')

#     def coding(self, time):
#         self.count_code_time += time



# class Frontend(Coder):
#     """Класс для фронтенда"""

#     def init(self, languages_frontend):
#         self.experience = languages_frontend

#     def get_info(self):
#         print(f'Ваш язык {self.experience} ваше время кода {self.count_code_time} часов ')

#     def coding(self, time):
#         self.count_code_time += time


# class FullStack(Frontend, Backend, Coder):

#     def init(self, languages_frontend):
#         self.experience = languages_frontend


# be1 = Backend('Python')
# be1.coding(20)
# be1.get_info()

# fe1 = Frontend('JS')
# fe1.coding(50)
# fe1.get_info()

# fs1 = FullStack('Python, js')
# fs1.coding(200)
# fs1.get_info()




# list = [22, 16, 13, 7];
# random.shuffle(list)
# print ("Перемешанный список : ",  list)



#3
# import random

# class Deck:

#     cards = ['Aчервь', '2червь', '3червь', '4червь', '5червь', '6червь', '7червь', '8червь', '9червь', '10червь', 'Jчервь', 'Qчервь', 'Kчервь',
#              'Aбубн', '2бубн', '3бубн', '4бубн', '5бубн', '6бубн', '7бубн', '8бубн', '9бубн', '10бубн', 'Jбубн', 'Qбубн', 'Kбубн',
#              'Aтерф', '2терф', '3терф', '4терф', '5терф', '6терф', '7терф', '8терф', '9терф', '10терф', 'Jтерф', 'Qтерф', 'Kтерф',
#              'Aпики', '2пики', '3пики', '4пики', '5пики', '6пики', '7пики', '8пики', '10пики', 'Jпики', 'Qпики', 'Kпики']
    
    
#     class Card:
        
#         def deal(self):
#             card = random.choice(Deck.cards)
#             print(f"Ваша карта {card} и теперь в колоде карт её нету")
#             c = Deck.cards.index(card)
#             del(Deck.cards[c])

#         def mix(self):
            
#             Deck.cards = ['Aчервь', '2червь', '3червь', '4червь', '5червь', '6червь', '7червь', '8червь', '9червь', '10червь', 'Jчервь', 'Qчервь', 'Kчервь',
#                           'Aбубн', '2бубн', '3бубн', '4бубн', '5бубн', '6бубн', '7бубн', '8бубн', '9бубн', '10бубн', 'Jбубн', 'Qбубн', 'Kбубн',
#                           'Aтерф', '2терф', '3терф', '4терф', '5терф', '6терф', '7терф', '8терф', '9терф', '10терф', 'Jтерф', 'Qтерф', 'Kтерф',
#                           'Aпики', '2пики', '3пики', '4пики', '5пики', '6пики', '7пики', '8пики', '10пики', 'Jпики', 'Qпики', 'Kпики']

#             random.shuffle(Deck.cards)



# card = Deck.Card()
# card.deal()
# print(Deck.cards)
# card.mix()
# print(Deck.cards)



##4

# def hackerrankInString(s):
#     target = 'hackerrank'
#     n = len(target)
    
#     i = 0
    
#     for char in s:
#         if char == target[i]:
#             i += 1
#             if i == n:
#                 return "YES"
#     return "NO"