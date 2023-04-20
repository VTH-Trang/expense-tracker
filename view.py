#in báo cáo
#import các thư viện
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import io
from kivy.uix.boxlayout import BoxLayout
from model import *
from model import ChiTieuList, ThuNhapList


from kivy.config import Config
Config.set('graphics', 'window_state', 'visible')


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
        screen4 = self.manager.get_screen('screen4')
        screen4.reset()
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
        listthunhap.tao_bao_cao()
 
        
    def store_data2(self, instance):
        # Lưu dữ liệu của 3 ô textinput
        chi_tieu = self.input_chitieu.text
        the_loai_chi = self.input_theloaichi.text
        date = self.input_date.text
        chitieu= ChiTieu(date, the_loai_chi, chi_tieu)
        listchitieu= ChiTieuList()
        listchitieu.nhaptufile()
        listchitieu.them_chi_tieu(chitieu)
        listchitieu.xuattofile()
        listchitieu.tao_bao_cao()

    def on_back_button_press(self, instance):
        self.manager.current = 'screen1'


class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)

        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)

        # Nút quay lại vào giao diện
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(100, 50),
                             pos_hint={'center_x': 0.7 , 'top': 1 - 900/1024},
                             background_normal='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)

        # Tạo một nút để in file
        btn = Button(text='In file', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(100, 50),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 900/1024},
                             background_normal='but2.png',
                      on_press=self.print_file)

        # Tạo một Label để hiển thị nội dung file
        self.file_content_label = Label(text='', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf',
                                        font_size='20sp',
                                        halign='left',
                                        valign='top',
                                        size_hint_y=None,
                                        markup=True)
        self.file_content_label2 = Label(text='', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf',
                                        font_size='20sp',
                                        halign='left',
                                        valign='top',
                                        size_hint_y=None,
                                        markup=True)
        # Tạo hai ScrollView và đặt các Label vào trong ScrollView
        self.scroll_view = ScrollView(size_hint=(0.5, None),
                                       size=(Window.width/2, Window.height - 100),
                                       pos_hint={'center_x': .25, 'center_y': .72},
                                       do_scroll_x=False,
                                       do_scroll_y = 1.0)
        self.scroll_view.add_widget(self.file_content_label)
        self.scroll_view2 = ScrollView(size_hint=(0.5, None),
                                       size=(Window.width/2, Window.height - 100),
                                       pos_hint={'center_x': .75, 'center_y': .5},
                                       do_scroll_x=False)
        self.scroll_view2.add_widget(self.file_content_label2)

        # Tạo một BoxLayout và đặt hai ScrollView vào trong BoxLayout
        box_layout = BoxLayout(orientation='horizontal')
        box_layout.add_widget(self.scroll_view)
        box_layout.add_widget(self.scroll_view2)

        # Đặt BoxLayout vào layout của màn hình
        self.add_widget(btn)
        self.add_widget(box_layout)
    
    def on_back_button_press(self, instance):
        self.manager.current = 'screen1'

    def print_file(self, instance):
        # Mở file 'bao_cao_thu_nhap.txt' để đọc
        with io.open('bao_cao_thu_nhap.txt', 'r', encoding='utf-8') as f1:
            # Đọc nội dung của file vào một biến
            file_content1 = f1.read()
        # Mở file 'bao_cao_chi_tieu.txt' để đọc
        with io.open('bao_cao_chi_tieu.txt', 'r', encoding='utf-8') as f2:
            # Đọc nội dung của file vào một biến
            file_content2 = f2.read()
        # Đặt nội dung file vào Label
        self.file_content_label.text = file_content1
        self.file_content_label2.text = file_content2
        # Cập nhật kích thước của ScrollView để hiển thị đầy đủ nội dung
        self.file_content_label.texture_update()
        self.file_content_label2.texture_update()
        self.scroll_view.scroll_y = 1.0
        self.scroll_view.height = self.file_content_label.texture_size[1]
        self.scroll_view.height = self.file_content_label2.texture_size[1]

class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)

        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)
        
        xuatbd_button = Button(text='Xuất biểu đồ', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 800/1024},
                             background_normal='but2.png', background_down='but2.png')
        xuatbd_button.bind(on_press=self.ve_bieu_do)
        
        self.add_widget(xuatbd_button)
       
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 900/1024},
                             background_normal='but2.png', background_down='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)
       
    def ve_bieu_do(self, instance):
         # Tạo box layout để chứa biểu đồ
        box_layout1 = BoxLayout(orientation='vertical', size_hint=(1, 0.5))
        self.add_widget(box_layout1)
        
        box_layout2 = BoxLayout(orientation='vertical', size_hint=(1, 0.5))
        self.add_widget(box_layout2)

        # Tạo scroll view để biểu đồ có thể cuộn được
        scroll_view1 = ScrollView(size_hint=(1, None), height=800)
        box_layout1.add_widget(scroll_view1)
        
        scroll_view2 = ScrollView(size_hint=(1, None), height=800)
        box_layout2.add_widget(scroll_view2)
        
         # Tạo box layout để chứa figure canvas
        canvas_box_layout1 = BoxLayout(orientation='vertical', size_hint=(0.5, None), height=500)
        scroll_view1.add_widget(canvas_box_layout1)
        
        canvas_box_layout2 = BoxLayout(orientation='vertical', size_hint=(0.5, None), height=500)
        scroll_view2.add_widget(canvas_box_layout2)
        
         # Vẽ biểu đồ thu nhập
        listthunhap= ThuNhapList()
        listthunhap.nhaptufile()
        fig1 = Figure()
        fig1 = plt.figure(figsize=(4, 2))
        ax1 = fig1.add_subplot(111)
        listthunhap.ve_bieu_do_thu_nhap(ax1)
        
        # Vẽ biểu đồ chi tiêu
        listchitieu= ChiTieuList()
        listchitieu.nhaptufile()
        fig2 = Figure()
        fig2 = plt.figure(figsize=(4, 2))
        ax2 = fig2.add_subplot(111)
        listchitieu.ve_bieu_do_chi_tieu(ax2)
   
        # Tạo widget FigureCanvasKivyAgg từ Figure
        canvas1 = FigureCanvasKivyAgg(fig1)
        canvas2 = FigureCanvasKivyAgg(fig2)

        # Thêm widget FigureCanvasKivyAgg vào Screen4
        canvas_box_layout1.add_widget(canvas1)
        canvas_box_layout2.add_widget(canvas2)
        
        canvas1.pos_hint= {'center_x': 0.5,  'center_y': 1, "top": 1}
        canvas2.pos_hint= {'center_x': 1.5, 'center_y': 1, "top": 1}
        
        xuatbd_button = Button(text='Xuất biểu đồ', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 800/1024},
                             background_normal='but2.png', background_down='but2.png')
        xuatbd_button.bind(on_press=self.ve_bieu_do)
        
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 900/1024},
                             background_normal='but2.png', background_down='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)
   
    def on_back_button_press(self, instance):
            self.manager.current = 'screen1'
            
    def reset(self):
        # Thiết lập background là hình ảnh "bg2.jpg"
        bg_image = Image(source='bg2.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(bg_image)
        
        xuatbd_button = Button(text='Xuất biểu đồ', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 800/1024},
                             background_normal='but2.png', background_down='but2.png')
        xuatbd_button.bind(on_press=self.ve_bieu_do)
        
        self.add_widget(xuatbd_button)
       
        back_button = Button(text='Back', font_name='#9Slide03 Montserrat Alternates SemiBold.ttf', size_hint=(None, None), size=(253, 80),
                             pos_hint={'center_x': 0.5 , 'top': 1 - 900/1024},
                             background_normal='but2.png', background_down='but2.png')
        back_button.bind(on_press=self.on_back_button_press)
        self.add_widget(back_button)
        

    
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

