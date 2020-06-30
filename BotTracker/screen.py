import pyautogui

path = r'D:\Programs\ProgramsPythonProjects\Trackeryt\screens\scr.png'

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(path)