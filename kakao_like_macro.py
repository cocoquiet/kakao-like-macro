from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.messagebox as msgbox

import pyautogui as pag
import keyboard

window = Tk()
window.title('kakao_like_macro')
window.geometry('400x250+100+100')
window.resizable(False, False)

def check_mode():
    if mode_value.get() == 1:
        count_entry.config(state='disabled')
        progress_label.config(text='0/∞')
        progress_bar.config(value=100)
    else:
        count_entry.config(state='normal')
        progress_label.config(text='0/0')
        progress_bar.config(value=0)
    
def execute():
    if mode_value.get() == 1:
        response = msgbox.askokcancel(title='kakao_like_macro', message='무한모드를 선택하셨습니다! \n컴퓨터가 터~질수도 있으니 조심하세요! \nq를 눌러 중간에 종료할 수 있습니다. \n<스페이스바>를 눌러 사랑을 표현하세요!')

        if response:
            while True:
                if keyboard.is_pressed('space'):
                    i = 1
                    while True:
                        if keyboard.is_pressed('q'):
                            break
                        pag.click()
                        progress_label.config(text=f'{i}/∞')
                        window.update()
                        
                        i += 1
                        
                    msgbox.showinfo(title='kakao_like_macro', message='사랑을 다 표현했습니다!')
                    break
                    
    elif mode_value.get() == 0:
        cnt = int(count_entry.get())
        response = msgbox.askokcancel(title='kakao_like_macro', message=f'{cnt}번 클릭합니다. \nq를 눌러 중간에 종료할 수 있습니다. \n<스페이스바>를 눌러 사랑을 표현하세요!')

        if response:
            while True:
                if keyboard.is_pressed('space'):
                    for i in range(cnt):
                        if keyboard.is_pressed('q'):
                            break
                        
                        pag.click()
                        progress_bar.config(value=(i+1)/cnt*100)
                        progress_label.config(text=f'{i+1}/{cnt}')
                        window.update()
                        
                    msgbox.showinfo(title='kakao_like_macro', message='사랑을 다 표현했습니다!')
                    break



mode_frame = LabelFrame(window, text='모드 선택')
mode_frame.pack(expand=True, fill='both', side='top')

mode_value = IntVar()

finite_mode_buttton = Radiobutton(mode_frame, text='정해진 횟수만큼 클릭', variable=mode_value, value=0, command=check_mode)
finite_mode_buttton.pack()

infinite_mode_button = Radiobutton(mode_frame, text='무한모드', variable=mode_value, value=1, command=check_mode)
infinite_mode_button.pack()


progress_frame = LabelFrame(window, text='진행 상황')
progress_frame.pack(expand=True, side='bottom', fill='x')

progress_label = Label(progress_frame, text='0/0', width=5)
progress_label.pack(side='left')

progress_bar = Progressbar(progress_frame, maximum=100, value=0)
progress_bar.pack(expand=True, fill='both')


count_frame = LabelFrame(window, text='횟수 입력')
count_frame.pack(expand=True, side='left', fill='both')

count_entry = Entry(count_frame)
count_entry.pack(expand=True, fill='both')


execute_frame = LabelFrame(window, text='실행')
execute_frame.pack(expand=True, side='right', fill='both')

execute_button = Button(execute_frame, text='실행', command=execute)
execute_button.pack(expand=True, fill='both')


window.mainloop()