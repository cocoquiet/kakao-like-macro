import pyautogui as pag
import keyboard
import os

cnt = int(input('몇 번 클릭할까요?(-1 입력시 무한 반복) : '))
os.system('cls')

if cnt == -1:
    print('무한 모드를 선택하셨습니다! 컴퓨터가 터~질수도 있으니 조심하세요!')
    print('q를 눌러 중간에 종료할 수 있습니다.')
    print('<스페이스바>를 눌러 사랑을 표현하세요!')
    while True:
        if keyboard.is_pressed('space'):
            print('시작!\n')
            x = 0
            
            while True:
                if keyboard.is_pressed('q'):
                    break
                
                print(f'\r{x+1}번째 클릭', end='')
                pag.click()
                x += 1
                
            print('\n사랑을 다 표현했습니다!')
            os.system('pause')
    
else:
    print('q를 눌러 중간에 종료할 수 있습니다.')
    print('<스페이스바>를 눌러 사랑을 표현하세요!')
    while True:
        if keyboard.is_pressed('space'):
            print('시작!\n')
            
            for x in range(cnt):
                if keyboard.is_pressed('q'):
                    break
                
                print(f'\r{x+1}번째 클릭', end='')
                pag.click()
                
            print('\n사랑을 다 표현했습니다!')
            os.system('pause')
                