import easygui
import random

name=easygui.enterbox("What is your name?")
easygui.msgbox("Ok, "+name+"!\nLet's play 21 game")
answer=random.randint(1,21)
prediction1=0
prediction2=0

prediction1=random.randint(1,13)
choice=easygui.buttonbox("Your first card is "+str(prediction1)+"\nDo you want more?"
                                                            ,choices=['Yes','No'])


if choice=='Yes':
    prediction2=random.randint(1,13)
    end_result=prediction1+prediction2
    easygui.msgbox("Your second card is "+str(prediction2)+"\nCheck your result")
    
    if end_result>=answer and end_result<=21:
        easygui.msgbox("Your final result is "+str(end_result)+"\nComputer's card was "+
                       str(answer)+'\nYou win!')
    elif end_result<answer:
        easygui.msgbox("Your final result is "+str(end_result)+"\nComputer's card was "+
                       str(answer)+'\nYou lose!')               
                         
    else:
         easygui.msgbox("Your final result is "+str(end_result)+"It is over 21, so you lose."
                        "Computer's card was "+str(answer))
                                        
if choice=="No":
    easygui.msgbox("Ok, check your result")

    if prediction1<answer:
        easygui.msgbox("Your final result is "+str(prediction1)+"\nComputer's card was "+
                       str(answer)+"\nYou lose!")
    else:
        easygui.msgbox("Your final result is "+str(prediction)+"\nComputer's card was "+
                        str(answer)+"\nYou win!")
