"""
This program uses python turtle to write a formal letter.
This is an easy way to teach kids letter writing and Python
in an integrated learning approach.
"""

from turtle import Turtle, Screen
from datetime import date


t = Turtle()
screen = Screen()
width, height = 800, 800
screen.setup(width, height)
screen.title('Letter with Python Turtle written by Uchenna Wealth')
screen.bgcolor('#33d7ff')
t.penup()
t.shape('turtle')
t.pencolor('#a533ff')
t.speed(3)
t.left(90)
spaces = ' '*30
sender_and_date = f'''
                {spaces} Plot 167F Ushafa Expansion Scheme
                {spaces} Abuja, Nigeria\n
                {spaces} {date.today().strftime('%d' + ' ' + '%B' + ' ' + '%Y')}
                '''
receiver = f'''
The Manager\n
Google Inc.\n
Silicon Valley\n
U.S.A
'''
greeting = 'Dear Sir/Ma,\n'
title = '\tAPPLICATION FOR THE ROLE OF SOFTWARE ENGINEER\n'
body = f'''
I wish to apply for the role of senior software engineer at Google. I believe that my experience and skills

are suitable for this role. I look forward to hearing from you.

Thank you.\n
'''
closing = '''
\nYours faithfully\n

Signature: U.C.A\n

Uchenna Wealth
'''
t.setpos(-50, height/3)
t.write(sender_and_date, True, font=('Comic Sans MS', 10, 'normal'))
t.setpos(-300, height/5)
t.write(receiver, True, font=('Comic Sans MS', 10, 'normal'))
t.setpos(-300, height/7)
t.write(greeting, True, font=('Comic Sans MS', 10, 'normal'))
t.setpos(-230, height/9)
t.write(title, True, font=('Comic Sans MS', 10, 'bold'))
t.setpos(-300, -(height/20))
t.write(body, True, font=('Comic Sans MS', 10, 'normal'))
t.setpos(-300, -200)
t.write(closing, True, font=('Comic Sans MS', 10, 'normal'))
t.hideturtle()
screen.mainloop()
