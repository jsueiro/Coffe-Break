import content_crawler
import webbrowser
import time
import sys
from win10toast_click import ToastNotifier
from content_crawler import update_file


def launch_page():
    webbrowser.open('index.html')


def show_notification():
    toast = ToastNotifier()
    toast.show_toast('Time for a break?', 'You should go and get some coffee.',
                     duration=30, callback_on_click=launch_page)


seconds = (int(sys.argv[1]) * 60) if int(sys.argv[1]) > 0 else 2700


while True:
    time.sleep(seconds)  # 2700
    update_file()
    show_notification()
    time.sleep(600)
