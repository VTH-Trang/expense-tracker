from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class MyWindow(Screen):
    def __init__(self, **kwargs):
        super(MyWindow, self).__init__(**kwargs)


        # Thiết lập background là hình ảnh gradient
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)


        # Thêm nút vào giao diện
        button1 = Button(text='Button 1', size_hint=(None, None), size=(253, 80),
                         pos_hint={'right': 1 - 465/1440, 'top': 1 - 406/1024},
                         background_normal='but.png', background_down='but.png')
        button1.bind(on_press=self.on_button1_press)
        self.add_widget(button1)


        # Thêm nút thứ hai vào giao diện
        button2 = Button(text='Button 2', size_hint=(None, None), size=(253, 80),
                         pos_hint={'right': 1 - 465/1440, 'top': 1 - 606/1024},
                         background_normal='but.png', background_down='but.png')
        button2.bind(on_press=self.on_button2_press)
        self.add_widget(button2)


        # Thêm nút thứ ba vào giao diện
        button3 = Button(text='Button 3', size_hint=(None, None), size=(253, 80),
                         pos_hint={'right': 1 - 465/1440, 'top': 1 - 806/1024},
                         background_normal='but.png', background_down='but.png')
        button3.bind(on_press=self.on_button3_press)
        self.add_widget(button3)


    def on_button1_press(self, instance):
        self.manager.current = 'screen2'


    def on_button2_press(self, instance):
        self.manager.current = 'screen3'


    def on_button3_press(self, instance):
        self.manager.current = 'screen4'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)


        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)


        # Thêm label hiển thị giá trị từ TextInput của Screen1
        self.label = Label(text='', font_size=20)
        self.add_widget(self.label)


        # Thêm TextInput cho ô nhập chi tiêu
        self.input_chitieu = TextInput(hint_text='Nhập chi tiêu', font_size=20, size_hint=(None, None), size=(300, 50),
                                 pos_hint={'center_x': 0.5, 'top': 0.7},
                                 background_normal='tb.png',
                                 background_active='tb.png')
        self.add_widget(self.input_chitieu)


        # Thêm TextInput cho ô nhập thu nhập
        self.input_thunhap = TextInput(hint_text='Nhập thu nhập', font_size=20, size_hint=(None, None), size=(300, 50),
                                 pos_hint={'center_x': 0.5, 'top': 0.5},
                                 background_normal='tb.png',
                                 background_active='tb.png')
        self.add_widget(self.input_thunhap)


class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)


        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)


class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)


        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyWindow(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))
        return sm


if __name__ == '__main__':
    MyApp().run()
