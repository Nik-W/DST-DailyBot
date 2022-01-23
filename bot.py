import subprocess
import pyautogui
import os

def load_not_end(pictures):
    for pic in pictures:
        if (pyautogui.locateCenterOnScreen(pic) != None):
            return False
    return True

def get_logo():
    pictures = []
    for root, dirs, files in os.walk("Logo"):  
        for filename in files:
            pictures.append('Logo/' + filename)
    return pictures

def main():
    args = [r"E:/Games/Steam/steamapps/common/Don't Starve Together/bin/dontstarve_steam"]
    #pathLogoImg = 'DST DailyBot/Logo1.png'
    #pathExitImg = 'DST DailyBot/X.png'
    pictures = get_logo()
    exitImg = 'X.png'

    subprocess.run(args)
    print("Запуск Don't Starve Together.")
    pyautogui.sleep(5)
    while (load_not_end(pictures)):
        pyautogui.sleep(1)
        print("Загрузка...")
    else:
        print("Загрузка завершена.\nИдёт получение бонуса...")
        pyautogui.sleep(1)
        savePos = pyautogui.position()
        pyautogui.click(exitImg)
        pyautogui.moveTo(savePos)
        print("Бонус получен! Скрипт завершён.")

if __name__ == "__main__":
    main()