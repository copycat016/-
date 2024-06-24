import pyautogui
import time
def CheckWord():
    word_path = './pic/word.png'
    region=(0, 0, 2560, 1000)
    matches = list(pyautogui.locateAllOnScreen(word_path, confidence=0.95,region=region))
    print("本页扫描到位置")
    print(matches)
    #"""
    if matches:
        for match in matches:
            # 获取每个匹配项的中心点位置
            center_x1, center_y1 = pyautogui.center(match)
            # 移动鼠标并点击
            pyautogui.moveTo(center_x1, center_y1, duration=0.1)
            pyautogui.click()

            # 等待一段时间以防止点击过快
            time.sleep(3)
            try:
                DownloadAndClose()
            except Exception as e:
                print("Worry:Not Find Download Button")
                try:
                    download_path = './pic/download_alraedy.png'
                    match = list(pyautogui.locateAllOnScreen(download_path, confidence=0.8))
                    close_path = './pic/close_2.png'
                    match = list(pyautogui.locateAllOnScreen(close_path, confidence=0.8))
                    center_x, center_y = pyautogui.center(match[0])
                    # 移动鼠标并点击
                    pyautogui.moveTo(center_x, center_y, duration=0.1)
                    pyautogui.click()
                except Exception as e:
                    exit(1)
            pyautogui.moveTo(center_x1, center_y1, duration=0.1)
    #"""
    pyautogui.scroll(-400)
def DownloadAndClose():
    download_path = './pic/download.png'
    match = list(pyautogui.locateAllOnScreen(download_path, confidence=0.8))
    center_x, center_y = pyautogui.center(match[0])
    # 移动鼠标并点击
    pyautogui.moveTo(center_x, center_y, duration=0.1)
    pyautogui.click()
    time.sleep(1)

    save_path='./pic/save.png'
    match = list(pyautogui.locateAllOnScreen(save_path, confidence=0.8))
    center_x, center_y = pyautogui.center(match[0])
    # 移动鼠标并点击
    pyautogui.moveTo(center_x, center_y, duration=0.1)
    pyautogui.click()
    time.sleep(1)

    close_path = './pic/close_2.png'
    match = list(pyautogui.locateAllOnScreen(close_path, confidence=0.8))
    center_x, center_y = pyautogui.center(match[0])
    # 移动鼠标并点击
    pyautogui.moveTo(center_x, center_y, duration=0.1)
    pyautogui.click()



time.sleep(5)
while(1):
    CheckWord()





