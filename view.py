#import các thư viện
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from model import *

class MyWindow(Screen):
    def __init__(self, **kwargs):
        super(MyWindow, self).__init__(**kwargs)

        # Thiết lập background là hình ảnh gradient
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)

        # Thêm label vào giao diện
        label = Label(text='SMART MONEY',font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', font_size=40, size_hint=(None, None), size=(100, 50), 
                      pos_hint={'center_x': 0.5 , 'center_y': 0.8})
        self.add_widget(label)

        # Thêm nút 1 vào giao diện
        button1 = Button(text='Ghi số liệu', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                         pos_hint={'center_x': 0.5 , 'top': 1 - 406/1024},
                         background_normal='but2.png', background_down='but2.png')
        button1.bind(on_press=self.on_button1_press)
        self.add_widget(button1)

        # Thêm nút 2 vào giao diện
        button2 = Button(text='Xem báo cáo', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80), 
                         pos_hint={'center_x': 0.5 , 'top': 1 - 606/1024},
                         background_normal='but2.png', background_down='but2.png',
                         border= [0, 0, 0, 0])
        button2.bind(on_press=self.on_button2_press)
        self.add_widget(button2)

        # Thêm nút 3 vào giao diện
        button3 = Button(text='Xem biểu đồ', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                         pos_hint={'center_x': 0.5 , 'top': 1 - 806/1024},
                         background_normal='but2.png', background_down='but2.png')
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

        """# Thêm ảnh
        anh1 = Image(source='big2.png', keep_ratio=False, allow_stretch=True,
                         pos_hint={'center_x': 0.5 , 'top': 1 - 406/1024})
        self.add_widget(anh1)"""

        # Thêm label vào giao diện
        label = Label(text='SMART MONEY',font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', font_size=40, size_hint=(None, None), size=(100, 50), 
                      pos_hint={'center_x': 0.5 , 'center_y': 0.8})
        self.add_widget(label)


        # Thêm label hiển thị giá trị từ TextInput của Screen1
        self.label = Label(text='', font_size=20)
        self.add_widget(self.label)

        #DATE
        self.input_date = TextInput(hint_text='Date', multiline=False, font_size=15, size_hint=(None, None), size=(144, 37),
                                 pos_hint={'center_x': 0.9, 'top': 0.9},
                                 background_normal='date2.png',
                                 background_active='date2.png')
        self.input_date.bind(on_text_validate=self.store_data1)
        self.input_date.bind(on_text_validate=self.store_data2)
        self.add_widget(self.input_date)

        # Thêm TextInput cho ô nhập thu nhập
        self.input_thunhap = TextInput(hint_text='Nhập thu nhập', multiline=False, font_size=20, size_hint=(None, None), size=(300, 50),
                                 pos_hint={'center_x': 0.2, 'top': 0.7},
                                 background_normal='tb2.png',
                                 background_active='tb2.png')
        self.input_thunhap.bind(on_text_validate=self.store_data1)
        self.add_widget(self.input_thunhap)
        self.input_theloaithu = TextInput(hint_text='Thể loại thu nhập',  multiline=False, font_size=15, size_hint=(None, None), size=(144, 37),
                                 pos_hint={'center_x': 0.5, 'top': 0.7},
                                 background_normal='type2.png',
                                 background_active='type2.png')
        self.input_theloaithu.bind(on_text_validate=self.store_data1)
        self.add_widget(self.input_theloaithu)

        # Thêm một button "ENTER 1"
        enter_button = Button(text='ENTER 1', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(153, 40),
                              pos_hint={'center_x': 0.8, 'top': 0.7},
                              background_normal='but2.png', background_down='but2.png')
        enter_button.bind(on_press=self.store_data1)
        self.add_widget(enter_button)

        # Thêm TextInput cho ô nhập chi tiêu
        self.input_chitieu = TextInput(hint_text='Nhập chi tiêu',  multiline=False, font_size=20, size_hint=(None, None), size=(300, 50),
                                 pos_hint={'center_x': 0.2, 'top': 0.5},
                                 background_normal='tb2.png',
                                 background_active='tb2.png')
        self.input_chitieu.bind(on_text_validate=self.store_data2)
        self.add_widget(self.input_chitieu)
        self.input_theloaichi = TextInput(hint_text='Thể loại chi tiêu',  multiline=False, font_size=15, size_hint=(None, None), size=(144, 37),
                                 pos_hint={'center_x': 0.5, 'top': 0.5},
                                 background_normal='type2.png',
                                 background_active='type2.png')
        self.input_theloaichi.bind(on_text_validate=self.store_data2)
        self.add_widget(self.input_theloaichi)
                # Thêm một button "ENTER 2"
        enter_button = Button(text='ENTER 2', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(153, 40),
                              pos_hint={'center_x': 0.8, 'top': 0.5},
                              background_normal='but2.png', background_down='but2.png')
        enter_button.bind(on_press=self.store_data2)
        self.add_widget(enter_button)

        # Nút quay lại vào giao diện
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 800/1024},
                             background_normal='but2.png', background_down='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)
    
    def store_data1(self, instance):
        # Lưu dữ liệu của 3 ô textinput
        thu_nhap = self.input_thunhap.text
        the_loai_thu = self.input_theloaithu.text
        date = self.input_date.text
        thunhap= ThuNhap(date,the_loai_thu, thu_nhap)
        listthunhap= ThuNhapList()
        listthunhap.nhaptufile()
        listthunhap.them_thu_nhap(thunhap)
        listthunhap.xuattofile()
        print(thunhap.xuatrachuoi())
        print("Tổng tất cả các thu nhập:", listthunhap.tong_thu_nhap())
        print("Tổng thu nhập trong tháng:", listthunhap.tong_thu_nhap_trong_thang_hien_tai())
        print("Tổng thu nhập trong khoảng thời gian là: ",listthunhap.tong_thu_nhap_trong_khoang_thoi_gian("22/1/2023", "26/5/2023"))
        
        
    def store_data2(self, instance):
        # Lưu dữ liệu của 3 ô textinput
        chi_tieu = self.input_chitieu.text
        the_loai_chi = self.input_theloaichi.text
        date = self.input_date.text

    def on_back_button_press(self, instance):
        self.manager.current = 'screen1'


class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)

        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)

        # Nút quay lại vào giao diện
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 900/1024},
                             background_normal='but2.png', background_down='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)

    def on_back_button_press(self, instance):
        self.manager.current = 'screen1'

class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)

        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)

        # Nút quay lại vào giao diện
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 900/1024},
                             background_normal='but2.png', background_down='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)

    def on_back_button_press(self, instance):
        self.manager.current = 'screen1'

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        # Tạo instance của MyScreenManager
        sm = MyScreenManager()

        # Thêm các màn hình vào MyScreenManager
        sm.add_widget(MyWindow(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))

        return sm

if __name__ == '__main__':
    MyApp().run()
