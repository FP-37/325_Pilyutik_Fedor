from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import StringProperty


class CenteredScrollSelector(BoxLayout):
    selected_value = StringProperty("")

    def __init__(self, values, **kwargs):
        kwargs.setdefault('orientation', 'vertical')
        super().__init__(**kwargs)

        self.values = values
        self.selected_value = values[0] if values else ""
        self._current_label = None
        self._auto_scrolling = False
        self._scroll_event = None
        self.item_height = 40
        self._deadzone_threshold = self.item_height * 0.4

        self.scroll_view = ScrollView(size_hint=(1, 1), bar_width=0, scroll_type=['content'])
        self.grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=[0, 100, 0, 100])
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.labels = []
        for value in values:
            label = Label(text=value, size_hint_y=None, height=self.item_height, font_size='16sp')
            self.labels.append(label)
            self.grid.add_widget(label)

        self.scroll_view.add_widget(self.grid)
        self.add_widget(self.scroll_view)

        Clock.schedule_once(self.center_nearest, 1)
        self.scroll_view.bind(scroll_y=self.on_scroll)

    def on_scroll(self, *args):
        if self._auto_scrolling:
            return
        if self._scroll_event:
            Clock.unschedule(self._scroll_event)
        self._scroll_event = Clock.schedule_once(self.center_nearest, 0.4)

    def center_nearest(self, *args):
        self._auto_scrolling = True

        scroll_y = self.scroll_view.scroll_y
        visible_height = self.scroll_view.height
        grid_height = self.grid.height
        scroll_top = scroll_y * (grid_height - visible_height)
        center_y = scroll_top + visible_height / 2

        nearest_label = None
        min_distance = float('inf')

        for label in self.labels:
            label_center = label.y + label.height / 2
            distance = abs(center_y - label_center)
            if distance < min_distance:
                min_distance = distance
                nearest_label = label

        if nearest_label and nearest_label != self._current_label and min_distance <= self._deadzone_threshold:
            self._current_label = nearest_label
            self.selected_value = nearest_label.text

            new_scroll_y = (grid_height - (nearest_label.y + nearest_label.height / 2) - visible_height / 2) / (grid_height - visible_height)
            new_scroll_y = max(0, min(1, new_scroll_y))

            def _end_scroll(*_):
                self._auto_scrolling = False

            anim = Animation(scroll_y=new_scroll_y, duration=0.2)
            anim.bind(on_complete=_end_scroll)
            anim.start(self.scroll_view)

        else:
            self._auto_scrolling = False

