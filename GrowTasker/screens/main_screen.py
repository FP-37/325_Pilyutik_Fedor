from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from datetime import datetime
from api import get_fruit_count, get_tasks


class IconButton(ButtonBehavior, BoxLayout):
    def __init__(self, icon_source, text, on_press_callback, **kwargs):
        super().__init__(orientation='vertical', padding=4, spacing=2, **kwargs)
        self.icon = Image(source=icon_source, size_hint=(1, 0.7))
        self.label = Label(text=text, font_size='10sp', font_name='assets/fonts/CyrillicPixel7-LPeg.ttf', size_hint=(1, 0.3))
        self.add_widget(self.icon)
        self.add_widget(self.label)
        self.on_press_callback = on_press_callback

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.on_press_callback()
        return super().on_touch_up(touch)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.fruit_count = 0
        self.start_x = None
        self.clock_label = None
        self.task_labels = []
        self.tree_layout = None
        self.build_ui()
        Clock.schedule_interval(self.update_time, 1)

    def build_ui(self):
        layout = BoxLayout(orientation='vertical')

        self.tree_layout = RelativeLayout(size_hint=(1, 0.8))
        self.tree = Image(source="assets/tree.png", allow_stretch=True, keep_ratio=False)
        self.tree_layout.add_widget(self.tree)

        self.clock_label = Label(
            text="00:00",
            font_size='16sp',
            font_name='assets/fonts/CyrillicPixel7-LPeg.ttf',
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'y': 0.278},
            halign='center',
            valign='middle'
        )
        self.clock_label.bind(size=self._update_text_size)
        self.tree_layout.add_widget(self.clock_label)

        layout.add_widget(self.tree_layout)

        tab_bar = BoxLayout(size_hint=(1, 0.1), spacing=10, padding=10)
        calendar_tab = IconButton("assets/icon_calendar.png", "Планер", self.open_calendar)
        alarm_tab = IconButton("assets/icon_alarm.png", "Будильник", self.open_alarm)
        tab_bar.add_widget(calendar_tab)
        tab_bar.add_widget(alarm_tab)
        layout.add_widget(tab_bar)

        bottom = BoxLayout(size_hint=(1, 0.1))
        self.fruit_label = Label(text="🍎: 0", font_size='12sp', font_name='assets/fonts/CyrillicPixel7-LPeg.ttf')
        bottom.add_widget(self.fruit_label)
        layout.add_widget(bottom)

        self.add_widget(layout)

    def on_pre_enter(self):
        self.update_fruit_count()
        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.task_labels:
            self.tree_layout.remove_widget(widget)
        self.task_labels.clear()

        task_positions = [
            {'center_x': 0.5, 'y': 0.825},
            {'center_x': 0.228, 'y': 0.682},
            {'center_x': 0.775, 'y': 0.682},
            {'center_x': 0.5, 'y': 0.525},
            {'center_x': 0.175, 'y': 0.477},
            {'center_x': 0.826, 'y': 0.477},
        ]

        tasks = []
        for task_id, task in get_tasks().items():
            try:
                if not task.get("completed"):
                    date_part = task.get('date', '2099-01-01')
                    time_part = task.get('time') or "00:00"
                    dt_str = f"{date_part} {time_part}"
                    task["dt"] = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
                    task["id"] = task_id
                    tasks.append(task)
            except Exception:
                continue

        tasks.sort(key=lambda x: x["dt"])
        closest_tasks = tasks[:6]

        for i, pos in enumerate(task_positions):
            text = closest_tasks[i]['text'] if i < len(closest_tasks) else ""
            task_label = Label(
                text=text,
                font_size='10sp',
                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf',
                color=(0, 0, 0, 1),
                size_hint=(None, None),
                size=(160, 40),
                pos_hint=pos,
                halign='center',
                valign='middle'
            )
            task_label.bind(size=self._update_text_size)
            self.tree_layout.add_widget(task_label)
            self.task_labels.append(task_label)

    def _update_text_size(self, instance, value):
        instance.text_size = instance.size

    def update_time(self, *args):
        now = datetime.now()
        self.clock_label.text = now.strftime('%H:%M')

    def update_fruit_count(self):
        self.fruit_count = get_fruit_count()
        self.fruit_label.text = f"🍎: {self.fruit_count}"

    def open_calendar(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'calendar'

    def open_alarm(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'alarm'

    def on_touch_down(self, touch):
        self.start_x = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.start_x is None:
            return super().on_touch_up(touch)

        delta_x = touch.x - self.start_x
        if abs(delta_x) > 50 and delta_x < 0:
            self.open_calendar()

        self.start_x = None
        return super().on_touch_up(touch)
