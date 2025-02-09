from plyer import notification
import time

# Constants
NOTIFICATION_TITLE = '*** Take Rest ***'
NOTIFICATION_MESSAGE = "Hey there! It's time for a break. 🌈 Stand up, stretch, and take a few moments to relax. Your health and well-being are important, so make the most of this break. Remember, a refreshed mind is a productive mind! 💆‍♂️💻 #TakeABreak #Refresh #SelfCare"
APP_ICON_PATH = "Image/break-time-icon.png"
NOTIFICATION_TIMEOUT = 5
NOTIFICATION_INTERVAL_SECONDS = 20

def send_notification():
    notification.notify(
        title=NOTIFICATION_TITLE,
        message=NOTIFICATION_MESSAGE,
        app_icon=APP_ICON_PATH,
        timeout=NOTIFICATION_TIMEOUT
    )

if __name__ == '__main__':
    while True:
        send_notification()
        time.sleep(NOTIFICATION_INTERVAL_SECONDS)