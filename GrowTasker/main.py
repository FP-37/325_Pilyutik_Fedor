import os
import subprocess
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition

from screens.main_screen import MainScreen
from screens.calendar_screen import CalendarScreen
from screens.add_task_screen import AddTaskScreen
from screens.alarm_screen import AlarmScreen


def start_redis():
    redis_exe = r"C:\Program Files\Redis\redis-server.exe"
    redis_conf = r"C:\Program Files\Redis\redis.windows.conf"

    if os.path.exists(redis_exe) and os.path.exists(redis_conf):
        try:
            subprocess.Popen([redis_exe, redis_conf], creationflags=subprocess.CREATE_NEW_CONSOLE)
        except Exception as e:
            print(f"[Redis Error] Не удалось запустить Redis: {e}")
    else:
        print("[Redis Warning] redis-server.exe или конфиг не найдены. Убедитесь в пути.")


class PlannerApp(App):
    def build(self):
        Window.size = (400, 700)  # Отладка на десктопе

        start_redis()  # Автозапуск Redis

        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CalendarScreen(name='calendar'))
        sm.add_widget(AddTaskScreen(name='add_task'))
        sm.add_widget(AlarmScreen(name='alarm'))
        return sm


if __name__ == '__main__':
    PlannerApp().run()
