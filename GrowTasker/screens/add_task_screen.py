from datetime import datetime
from calendar import monthrange
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import uuid
from api import add_task


RU_WEEKDAYS = {
    0: "Понедельник", 1: "Вторник", 2: "Среда",
    3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"
}


class ScrollSelector(BoxLayout):
    def __init__(self, values, default_value, callback, **kwargs):
        super().__init__(orientation='vertical', size_hint=(None, 1), width=80, **kwargs)
        self.callback = callback
        self.scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        self.grid = GridLayout(cols=1, size_hint_y=None, spacing=5, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.add_widget(self.scroll)
        self.values = values
        self.value_buttons = []
        self.selected_value = default_value
        self.selected_btn = None

        for value in values:
            btn = Button(
                text=value,
                size_hint_y=None,
                height=40,
                background_color=(0.4, 0.25, 0.1, 1),
                color=(1, 1, 1, 1),
                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf',
            )
            btn.bind(on_release=self.on_select)
            self.grid.add_widget(btn)
            self.value_buttons.append(btn)

        Clock.schedule_once(lambda dt: self.scroll_to_value(default_value), 0.1)

    def on_select(self, instance):
        self.selected_value = instance.text
        self._highlight_selected(instance)
        if self.callback:
            self.callback()

    def scroll_to_value(self, value):
        for i, btn in enumerate(self.value_buttons):
            if btn.text == value:
                self._highlight_selected(btn)
                target = btn.y
                self.scroll.scroll_y = 1 - (target / self.grid.height)
                break

    def set_values(self, new_values, default_value=None):
        current = self.selected_value
        self.grid.clear_widgets()
        self.value_buttons.clear()
        self.selected_btn = None

        for value in new_values:
            btn = Button(
                text=value,
                size_hint_y=None,
                height=40,
                background_color=(0.4, 0.25, 0.1, 1),
                color=(1, 1, 1, 1),
                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf',
            )
            btn.bind(on_release=self.on_select)
            self.grid.add_widget(btn)
            self.value_buttons.append(btn)

        if current in new_values:
            self.selected_value = current
            Clock.schedule_once(lambda dt: self.scroll_to_value(current), 0.1)
        elif default_value and default_value in new_values:
            self.selected_value = default_value
            Clock.schedule_once(lambda dt: self.scroll_to_value(default_value), 0.1)

    def _highlight_selected(self, selected_btn):
        for btn in self.value_buttons:
            btn.background_color = (0.4, 0.25, 0.1, 1)
        selected_btn.background_color = (0.5, 1, 0.5, 1)
        self.selected_btn = selected_btn


class AddTaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_input = None
        self.time_checkbox = None
        self.day_selector = None
        self.month_selector = None
        self.year_selector = None
        self.hour_selector = None
        self.minute_selector = None
        self.date_label = None
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        layout.add_widget(Label(text="Новая задача", font_size='20sp', size_hint_y=None, height=40,
                                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf'))

        self.text_input = TextInput(hint_text="Текст задачи", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.text_input)

        self.date_label = Label(text="", font_size='14sp', size_hint_y=None, height=30,
                                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf')
        layout.add_widget(self.date_label)

        now = datetime.now()
        layout.add_widget(Label(text="Дата задачи:", size_hint_y=None, height=30,
                                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf'))
        date_layout = BoxLayout(size_hint_y=None, height=150, spacing=10, padding=[40, 0], orientation='horizontal')

        self.day_selector = ScrollSelector([], str(now.day), self.on_date_change)
        self.month_selector = ScrollSelector([str(i) for i in range(now.month, 13)], str(now.month), self.on_date_change)
        self.year_selector = ScrollSelector([str(now.year + i) for i in range(5)], str(now.year), self.on_date_change)

        date_layout.add_widget(self.day_selector)
        date_layout.add_widget(self.month_selector)
        date_layout.add_widget(self.year_selector)
        layout.add_widget(date_layout)

        time_toggle = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.time_checkbox = CheckBox(size_hint=(None, None), size=(30, 30))
        time_toggle.add_widget(self.time_checkbox)
        time_toggle.add_widget(Label(text="Добавить время", size_hint_x=None, width=140,
                                     font_name='assets/fonts/CyrillicPixel7-LPeg.ttf'))
        layout.add_widget(time_toggle)

        layout.add_widget(Label(text="Время задачи:", size_hint_y=None, height=30,
                                font_name='assets/fonts/CyrillicPixel7-LPeg.ttf'))
        time_layout = BoxLayout(size_hint_y=None, height=150, spacing=10, padding=[40, 0])

        self.hour_selector = ScrollSelector([], "00", self.on_time_change)
        self.minute_selector = ScrollSelector([], "00", None)

        time_layout.add_widget(self.hour_selector)
        time_layout.add_widget(self.minute_selector)
        layout.add_widget(time_layout)

        button_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        save_button = Button(text="Сохранить", font_name='assets/fonts/CyrillicPixel7-LPeg.ttf')
        save_button.bind(on_release=self.save_task)
        cancel_button = Button(text="Отмена", font_name='assets/fonts/CyrillicPixel7-LPeg.ttf')
        cancel_button.bind(on_release=self.go_back)
        button_layout.add_widget(save_button)
        button_layout.add_widget(cancel_button)

        layout.add_widget(button_layout)
        self.add_widget(layout)

        Clock.schedule_once(lambda dt: self.update_day_selector())
        Clock.schedule_once(lambda dt: self.update_time_selectors())
        Clock.schedule_once(lambda dt: self.update_date_label())

    def on_date_change(self, *args):
        self.update_day_selector()
        self.update_time_selectors()
        self.update_date_label()

    def on_time_change(self, *args):
        self.update_time_selectors()

    def update_day_selector(self):
        try:
            year = int(self.year_selector.selected_value)
            month = int(self.month_selector.selected_value)
            now = datetime.now()
            current_day = now.day if year == now.year and month == now.month else 1
            days = monthrange(year, month)[1]
            values = [str(i) for i in range(current_day, days + 1)]
            default = values[0]
            self.day_selector.set_values(values, default)
        except:
            pass

    def update_time_selectors(self):
        now = datetime.now()
        try:
            day = int(self.day_selector.selected_value)
            month = int(self.month_selector.selected_value)
            year = int(self.year_selector.selected_value)
        except:
            return

        selected_date = datetime(year, month, day).date()
        is_today = selected_date == now.date()

        start_hour = now.hour if is_today else 0
        hour_values = [f"{i:02d}" for i in range(start_hour, 24)]
        default_hour = hour_values[0]
        self.hour_selector.set_values(hour_values, default_hour)

        try:
            hour = int(self.hour_selector.selected_value)
        except:
            hour = start_hour

        start_minute = now.minute if is_today and hour == now.hour else 0
        minute_values = [f"{i:02d}" for i in range(start_minute, 60)]
        default_minute = minute_values[0]
        self.minute_selector.set_values(minute_values, default_minute)

    def update_date_label(self):
        try:
            day = int(self.day_selector.selected_value)
            month = int(self.month_selector.selected_value)
            year = int(self.year_selector.selected_value)
            dt = datetime(year, month, day)
            date_str = dt.strftime('%d.%m.%y') + f", {RU_WEEKDAYS[dt.weekday()]}"
            self.date_label.text = date_str
        except:
            self.date_label.text = ""

    def save_task(self, instance):
        text = self.text_input.text.strip()
        if not text:
            return

        try:
            day = int(self.day_selector.selected_value)
            month = int(self.month_selector.selected_value)
            year = int(self.year_selector.selected_value)
            date = datetime(year, month, day).strftime('%Y-%m-%d')
        except:
            return

        time = ""
        if self.time_checkbox.active:
            time = f"{self.hour_selector.selected_value}:{self.minute_selector.selected_value}"

        task_id = str(uuid.uuid4())
        task_data = {
            "id": task_id,
            "text": text,
            "completed": False,
            "date": date,
            "time": time
        }

        add_task(task_data)
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'calendar'

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'calendar'
