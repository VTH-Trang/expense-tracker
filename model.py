from datetime import date, timedelta, datetime
from matplotlib import pyplot as plt
import csv
import os
from matplotlib.figure import Figure

class ChiTieu:

  def __init__(self, strngay, muc_dich, so_tien):
    self.strngay = strngay
    self.muc_dich = muc_dich
    self.so_tien = float(so_tien)
    self.ngay = datetime.strptime(self.strngay, '%d/%m/%Y')

  def xuat(self):
    return self.ngay, self.muc_dich, self.so_tien

  def xuatrachuoi(self):
    S = str(self.ngay.strftime("%d/%m/%Y")) + ',' + self.muc_dich + ',' + str(
      self.so_tien)
    return S


class ChiTieuList:

  def __init__(self):
    self.dschitieu = []

  def them_chi_tieu(self, chi_tieu):
    self.chi_tieu = chi_tieu
    self.dschitieu.append(chi_tieu)

  def nhaptufile(self):
    if os.path.exists("quanlychitieu.csv"):
      with open("quanlychitieu.csv", mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
                if len(row) >= 3:
                    chitieu = ChiTieu(row[0], row[1], row[2])
                    self.dschitieu.append(chitieu)
  
  def tao_bao_cao(self):
    with open("bao_cao_chi_tieu.txt", mode= "+a", encoding="utf-8") as f:
      for chi_tieu in  self.dschitieu:
        f.write("Ngày {}: chi {}VND cho {}".format(chi_tieu.ngay.strftime("%d/%m/%Y"), chi_tieu.so_tien, chi_tieu.muc_dich, ) + "\n")
    
    
  def tong_chi_tieu(self):
    tong_chi_tieu = 0
    for chi_tieu in self.dschitieu:
      tong_chi_tieu += float(chi_tieu.so_tien)
    return tong_chi_tieu

  def tong_chi_tieu_trong_khoang_thoi_gian(self, strbat_dau, strket_thuc):
    tong_chi_tieu_trong_khoang = 0
    batdau = datetime.strptime(strbat_dau, '%d/%m/%Y')
    ketthuc = datetime.strptime(strket_thuc, '%d/%m/%Y')
    for chi_tieu in self.dschitieu:
      if batdau <= chi_tieu.ngay <= ketthuc:
        tong_chi_tieu_trong_khoang += chi_tieu.so_tien
    return tong_chi_tieu_trong_khoang

  def tong_chi_tieu_trong_thang_hien_tai(self):
    ngay_hom_nay = date.today()
    ngay_dau_thang = date(ngay_hom_nay.year, ngay_hom_nay.month, 1)
    ngay_cuoi_thang = date(ngay_hom_nay.year, ngay_hom_nay.month + 1, 1) - timedelta(days=1)
    
    ngay_dau_thang_str = ngay_dau_thang.strftime('%d/%m/%Y')
    ngay_cuoi_thang_str = ngay_cuoi_thang.strftime('%d/%m/%Y')
    
    tong_chi_tieu_thang = self.tong_chi_tieu_trong_khoang_thoi_gian(ngay_dau_thang_str, ngay_cuoi_thang_str)
    
    return tong_chi_tieu_thang


  def ve_bieu_do_chi_tieu(self, ax):
            muc_dich = []
            so_tien = []
            for chi_tieu in self.dschitieu:
                if chi_tieu.ngay.month == date.today().month:
                    if chi_tieu.muc_dich not in muc_dich:
                        muc_dich.append(chi_tieu.muc_dich)
                        so_tien.append(chi_tieu.so_tien)
                    else: 
                      for i in range( len(muc_dich)):
                        if chi_tieu.muc_dich == muc_dich[i]:
                          so_tien[i]+=chi_tieu.so_tien
            ax.pie(so_tien, labels=muc_dich, autopct='%1.1f%%')
            ax.set_title(f"Expenses for {date.today().strftime('%B, %Y')}")

  def xuat(self):
    S = ''
    for chi_tieu in self.dschitieu:
      S += chi_tieu.xuatrachuoi() + '\n'
    return S

  def xuattofile(self):
    with open("quanlychitieu.csv",newline= "", mode='w', encoding='utf-8') as f:
      for chi_tieu in self.dschitieu:
        csv.writer(f).writerow([
          chi_tieu.ngay.strftime("%d/%m/%Y"), chi_tieu.muc_dich,
          chi_tieu.so_tien
	        ])
      f.close()


class ThuNhap:

  def __init__(self, strngay, the_loai, so_tien):
    self.strngay = strngay
    self.the_loai= the_loai
    self.so_tien = float(so_tien)
    self.ngay = datetime.strptime(self.strngay, '%d/%m/%Y')


  def xuat(self):
    return self.ngay,self.the_loai, self.so_tien

  def xuatrachuoi(self):
    S = str(self.ngay.strftime("%d/%m/%Y")) + ',' + self.the_loai + ',' + str(
      self.so_tien)
    return S


class ThuNhapList:

  def __init__(self):
    self.dsthunhap = []
  
  def nhaptufile(self):
    if os.path.exists("quanlythunhap.csv"):
      with open("quanlythunhap.csv", mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
                if len(row) >= 3:
                    thunhap = ThuNhap(row[0], row[1], row[2])
                    self.dsthunhap.append(thunhap)

  def them_thu_nhap(self, thu_nhap):
    self.thu_nhap = thu_nhap
    self.dsthunhap.append(thu_nhap)
  
  def tao_bao_cao(self):
    with open("bao_cao_thu_nhap.txt", mode= "+a", encoding="utf-8") as f:
      for thu_nhap in  self.dsthunhap:
        f.write("Ngày {}: thu {}VND từ {}".format(thu_nhap.ngay.strftime("%d/%m/%Y"), thu_nhap.so_tien, thu_nhap.the_loai ) + "\n")
  
  def tong_thu_nhap(self):
    tong_thu_nhap = 0
    for thu_nhap in self.dsthunhap:
      tong_thu_nhap += thu_nhap.so_tien
    return tong_thu_nhap

  def tong_thu_nhap_trong_khoang_thoi_gian(self, strbat_dau, strket_thuc):
    tong_thu_nhap_trong_khoang = 0
    batdau = datetime.strptime(strbat_dau, '%d/%m/%Y')
    ketthuc = datetime.strptime(strket_thuc, '%d/%m/%Y')
    for thu_nhap in self.dsthunhap:
      if batdau <= thu_nhap.ngay <= ketthuc:
        tong_thu_nhap_trong_khoang += thu_nhap.so_tien
    return tong_thu_nhap_trong_khoang

  def tong_thu_nhap_trong_thang_hien_tai(self):
    ngay_hom_nay = date.today()
    ngay_dau_thang = date(ngay_hom_nay.year, ngay_hom_nay.month, 1)
    ngay_cuoi_thang = date(ngay_hom_nay.year, ngay_hom_nay.month + 1, 1) - timedelta(days=1)
    
    ngay_dau_thang_str = ngay_dau_thang.strftime('%d/%m/%Y')
    ngay_cuoi_thang_str = ngay_cuoi_thang.strftime('%d/%m/%Y')
    
    tong_thu_nhap_thang = self.tong_thu_nhap_trong_khoang_thoi_gian(ngay_dau_thang_str, ngay_cuoi_thang_str)
    
    return tong_thu_nhap_thang

  def ve_bieu_do_thu_nhap(self, ax):
            the_loai = []
            so_tien = []
            for thu_nhap in self.dsthunhap:
                if thu_nhap.ngay.month == date.today().month:
                    if thu_nhap.the_loai not in the_loai:
                        the_loai.append(thu_nhap.the_loai)
                        so_tien.append(thu_nhap.so_tien)
                    else: 
                      for i in range( len(the_loai)):
                        if thu_nhap.the_loai == the_loai[i]:
                          so_tien[i]+=thu_nhap.so_tien
            ax.pie(so_tien, labels=the_loai, autopct='%1.1f%%')
            ax.set_title(f"Expenses for {date.today().strftime('%B, %Y')}")
  
  def xuat(self):
    S = ''
    for thu_nhap in self.dsthunhap:
      S += thu_nhap.xuatrachuoi() + '\n'
    return S

  def xuattofile(self):
    with open("quanlythunhap.csv",newline= "", mode='w', encoding='utf-8') as f:
      for thu_nhap in self.dsthunhap:
        csv.writer(f).writerow([thu_nhap.ngay.strftime("%d/%m/%Y"),thu_nhap.the_loai,  thu_nhap.so_tien])
    f.close()


class TaiKhoan:
  def __init__(self, so_tien):
    self.so_tien = so_tien

  def tinh_so_du(self, tong_thu_nhap, tong_chi_tieu):
    so_du = tong_thu_nhap - tong_chi_tieu
    return so_du

"""if __name__ == "__main__":
  # Tạo tài khoản
  taikhoan= TaiKhoan(5000000)
  
  # Tạo chi tiêu và list chi tiêu
  listchitieu = ChiTieuList()
  listchitieu.nhaptufile()
  chitieu1 = ChiTieu("22/04/2023", "milk", "50")
  chitieu2 = ChiTieu("15/04/2023", 'snack', "40")

  # Thêm chi tiêu
  listchitieu.them_chi_tieu(chitieu1)
  listchitieu.them_chi_tieu(chitieu2)

  # Lưu vào file
  listchitieu.xuattofile()

  # In từng chuỗi chi tiêu
  print(chitieu1.xuatrachuoi())
  print(chitieu2.xuatrachuoi())
  
  #In tổng chi tiêu
  print("Tổng tất cả các chi tiêu:", listchitieu.tong_chi_tieu())
  
  #In tổng chi tiêu trong tháng
  print("Tổng chi tiêu trong tháng:", listchitieu.tong_chi_tieu_trong_thang_hien_tai())

  # In tổng chi tiêu trong khoảng thời gian
  print(
    "Tổng chi tiêu trong khoảng thời gian là: ",
    listchitieu.tong_chi_tieu_trong_khoang_thoi_gian("22/1/2023", "26/5/2023"))

  # Vẽ biểu đồ chi tiêu
  

  
  # Tạo list thu nhập và thu nhập
  listthunhap= ThuNhapList()
  listthunhap.nhaptufile()
  thunhap1 = ThuNhap("25/04/2023","online", "200")
  thunhap2 = ThuNhap("10/04/2023", "fulltime","300")
 
  # Thêm thu nhập
  listthunhap.them_thu_nhap(thunhap1)
  listthunhap.them_thu_nhap(thunhap2)
  
  # Lưu vào file
  listthunhap.xuattofile()
  
  # In chuỗi thu nhập
  print(thunhap1.xuatrachuoi())
  print(thunhap2.xuatrachuoi())
  
  #In tổng thu nhập
  print("Tổng tất cả các thu nhập:", listthunhap.tong_thu_nhap())
  
  #In tổng thu nhập trong tháng
  print("Tổng thu nhập trong tháng:", listthunhap.tong_thu_nhap_trong_thang_hien_tai())

  # In tổng thu nhập trong khoảng thời gian
  print("Tổng thu nhập trong khoảng thời gian là: ",listthunhap.tong_thu_nhap_trong_khoang_thoi_gian("22/1/2023", "26/5/2023"))
  
  # Tính số dư tài khoản
  tong_thu_nhap= listthunhap.tong_thu_nhap()
  tong_chi_tieu= listchitieu.tong_chi_tieu()
  print("Số dư tài khoản là:", taikhoan.tinh_so_du(tong_thu_nhap, tong_chi_tieu))
  listchitieu.tao_bao_cao()
  listthunhap.tao_bao_cao()"""
