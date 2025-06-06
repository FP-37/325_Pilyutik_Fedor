from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from datetime import datetime
from api import get_tasks, update_task, delete_task
import calendar


class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_date = None
        self.day_buttons = []
        self.tasks_layout = None
        self.month_spinner = None
        self.year_spinner = None
        self.days_layout = None
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        top_bar = BoxLayout(size_hint_y=None, height=40, spacing=10)
        top_bar.add_widget(Label(text="Предстоящее", font_size='20sp', font_name='assets/fonts/CyrillicPixel7-LPeg.ttf'))

        now = datetime.now()
        self.month_spinner = Spinner(
            text=str(now.month),
            values=[str(i) for i in range(1, 13)],
            size_hint=(None, None),
            size=(80, 40)
        )
        self.year_spinner = Spinner(
            text=str(now.year),
            values=[str(now.year + i) for i in range(5)],
            size_hint=(None, None),
            size=(80, 40)
        )
        self.month_spinner.bind(text=self.on_month_year_change)
        self.year_spinner.bind(text=self.on_month_year_change)

        top_bar.add_widget(self.month_spinner)
        top_bar.add_widget(self.year_spinner)
        layout.add_widget(top_bar)

        scroll_days = ScrollView(size_hint_y=None, height=50, do_scroll_y=False, bar_width=0)
        self.days_layout = GridLayout(cols=1000, spacing=5, size_hint_x=None, height=50)
        self.days_layout.bind(minimum_width=self.days_layout.setter('width'))
        scroll_days.add_widget(self.days_layout)
        layout.add_widget(scroll_days)

        self.tasks_scroll = ScrollView()
        self.tasks_layout = GridLayout(cols=1, spacing=10, padding=5, size_hint_y=None)
        self.tasks_layout.bind(minimum_height=self.tasks_layout.setter('height'))
        self.tasks_scroll.add_widget(self.tasks_layout)
        layout.add_widget(self.tasks_scroll)

        button_bar = BoxLayout(size_hint_y=None, height=40, spacing=10)
        add_btn = Button(text="Добавить задачу")
        add_btn.bind(on_release=self.go_to_add_task)
        back_btn = Button(text="Назад")
        back_btn.bind(on_release=self.go_back)
        button_bar.add_widget(add_btn)
        button_bar.add_widget(back_btn)

        layout.add_widget(button_bar)
        self.add_widget(layout)

    def refresh_days(self):
        self.days_layout.clear_widgets()
        self.day_buttons.clear()

        try:
            year = int(self.year_spinner.text)
            month = int(self.month_spinner.text)
            num_days = calendar.monthrange(year, month)[1]
            today = datetime.today().strftime('%Y-%m-%d')

            for day in range(1, num_days + 1):
                date_str = f"{year:04d}-{month:02d}-{day:02d}"
                btn = Button(text=str(day), size_hint_x=None, width=50)

                if date_str == today:
                    btn.background_color = (0.7, 0.9, 1, 1)  # подсветка сегодняшнего дня

                btn.bind(on_release=self.select_day)
                self.day_buttons.append((btn, date_str))
                self.days_layout.add_widget(btn)

        except Exception:
            pass

    def highlight_selected_day(self):
        for btn, date_str in self.day_buttons:
            if date_str == self.selected_date:
                btn.background_color = (0.5, 1, 0.5, 1)
            elif date_str == datetime.today().strftime('%Y-%m-%d'):
                btn.background_color = (0.7, 0.9, 1, 1)
            else:
                btn.background_color = (1, 1, 1, 1)

    def on_month_year_change(self, *args):
        self.refresh_days()
        # автоселект сегодняшней даты, если она входит в месяц
        today = datetime.today()
        y, m = int(self.year_spinner.text), int(self.month_spinner.text)
        if today.year == y and today.month == m:
            self.selected_date = today.strftime('%Y-%m-%d')
        else:
            self.selected_date = f"{y:04d}-{m:02d}-01"

        self.highlight_selected_day()
        self.load_tasks()

    def select_day(self, instance):
        for btn, date_str in self.day_buttons:
            if btn == instance:
                self.selected_date = date_str
                self.highlight_selected_day()
                self.load_tasks()
                break

    def load_tasks(self):
        self.tasks_layout.clear_widgets()
        tasks = get_tasks()

        for task_id, task_data in tasks.items():
            if not isinstance(task_data, dict):
                continue
            if task_data.get("date") != self.selected_date:
                continue

            task_layout = BoxLayout(size_hint_y=None, height=40)
            checkbox = CheckBox(size_hint=(None, None), size=(30, 30), active=task_data.get('completed', False))
            checkbox.bind(active=lambda cb, val, tid=task_id: self.update_task_status(tid, val))

            task_label = Label(text=task_data.get('text', ''), font_size='16sp',
                               font_name='assets/fonts/CyrillicPixel7-LPeg.ttf')
            delete_btn = Button(text="Удалить", size_hint_x=None, width=80)
            delete_btn.bind(on_release=lambda btn, tid=task_id, w=task_layout: self.remove_task(tid, w))

            task_layout.add_widget(checkbox)
            task_layout.add_widget(task_label)
            task_layout.add_widget(delete_btn)

            self.tasks_layout.add_widget(task_layout)

    def update_task_status(self, task_id, completed):
        update_task(task_id, completed)

    def remove_task(self, task_id, widget):
        delete_task(task_id)
        self.tasks_layout.remove_widget(widget)

    def go_to_add_task(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'add_task'

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main'

    def on_pre_enter(self):
        self.refresh_days()
        today = datetime.today()
        self.month_spinner.text = str(today.month)
        self.year_spinner.text = str(today.year)
        self.selected_date = today.strftime('%Y-%m-%d')
        self.highlight_selected_day()
        self.load_tasks()
