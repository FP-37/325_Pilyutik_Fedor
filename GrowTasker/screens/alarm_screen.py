from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.pickers import MDTimePickerInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from datetime import datetime


class AlarmScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alarms = []
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Заголовок
        self.layout.add_widget(Label(text="Будильники", font_size='20sp', size_hint=(1, 0.1)))

        # Прокручиваемый список будильников
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.alarms_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.alarms_layout.bind(minimum_height=self.alarms_layout.setter('height'))
        self.scroll_view.add_widget(self.alarms_layout)
        self.layout.add_widget(self.scroll_view)

        # Кнопка добавления
        self.add_button = Button(text="Добавить будильник", size_hint=(1, 0.1))
        self.add_button.bind(on_release=self.add_alarm)
        self.layout.add_widget(self.add_button)

        # Кнопка назад
        self.back_button = Button(text="Назад", size_hint=(1, 0.1))
        self.back_button.bind(on_release=self.go_back)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def add_alarm(self, instance):
        time_picker = MDTimePickerInput()
        time_picker.bind(on_save=self.save_alarm)
        time_picker.open()

    def save_alarm(self, instance, time):
        alarm_time = time.strftime('%H:%M')
        alarm_label = Label(text=f"Будильник на {alarm_time}", font_size='16sp', size_hint_y=None, height=40)
        edit_button = Button(text="Изменить", size_hint=(None, None), size=(100, 40))
        edit_button.bind(on_release=lambda x: self.edit_alarm(alarm_label))

        container = BoxLayout(size_hint_y=None, height=40)
        container.add_widget(alarm_label)
        container.add_widget(edit_button)

        self.alarms_layout.add_widget(container)
        self.alarms.append({'time': alarm_time, 'widget': container})

    def edit_alarm(self, label):
        time_picker = MDTimePickerInput()
        time_picker.bind(on_save=lambda instance, time: self.update_alarm(label, time))
        time_picker.open()

    def update_alarm(self, label, time):
        label.text = f"Будильник на {time.strftime('%H:%M')}"

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main'
