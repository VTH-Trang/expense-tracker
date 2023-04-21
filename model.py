from datetime import date, timedelta, datetime
import csv
import os
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

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
    with open("bao_cao_chi_tieu.txt", mode= "w", encoding="utf-8") as f:
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
    with open("bao_cao_thu_nhap.txt", mode= "w", encoding="utf-8") as f:
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
            ax.set_title(f"Incoms in {date.today().strftime('%B, %Y')}")
  
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
