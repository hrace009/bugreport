#!/usr/bin/python
import templates.i
import smtplib
import os
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os import system
from getpass import getpass

'''
CODED BY MARIO YEHEZKIEL

INSTAGRAM : https://www.instagram.com/zcybercru/
	    https://www.instagram.com/mario.yhzkiell/
official website : https://www.zcybercru.zone.id
GITHUB : https://github.com/marioyhzkiell
hackerone : https://hackerone.com/marioyhzkiell

'''
merah	= ("\033[91m")
kuning	= ("\033[93m")
ungu	= ("\033[95m")
nila	= ("\033[94m")
hijau	= ("\033[92m")
system('clear')
print (kuning)
templates.i.item()
print (hijau)
print ('PENTING !!! , Harap Dibaca!!\n')
print ('note : tools ini hanya di khususkan bagi pengguna akun gmail dan yahoo!')
print ('note : aktifkan (less secure apps) di pengaturan akun agar tools ini work!')
print ('note : jika anda tidak percaya tools ini, pastikan anda mengirim email ke email anda sendiri\n',kuning)
print ('Pilih jenis vulnerable website yang ingin anda laporkan!\n')
print ('    1.SQL Injection')
print ('    2.LFI/Local File Inclusion')
print ('    3.RFI/Remote File Inclusion')
print ('    4.RCE/Remote Code Execution')
print ('    5.CSRF/Cross Site Request Forgery ')
print ('    6.XSS/Cross Site Scripting')
print ('    7.Server Side Injection')
print ('    8.CSV Injection')
print ('    9.parameter tampering')
print ('    10.bypass admin')
print ('    99.keluar/Ga Minat\n')
print ('    Example (1/2/3/4/5)')
inputbug	= input('masukan nomer pilihan : ')
msg = MIMEMultipart()
if inputbug == '1':
  msg.attach(MIMEText(open('templates/sqli.html',).read(),'html'))
  stringweb = 'url vuln SQL Injection : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/berita/index.php?id=12 ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '2':
  msg.attach(MIMEText(open('templates/lfi.html',).read(),'html'))
  stringweb = 'url vuln LFI : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/berita/index.php?page= ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '3':
  msg.attach(MIMEText(open('templates/rfi.html',).read(),'html'))
  stringweb = 'url vuln RFI : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/index.php?file=http://www.[remote].com/evil.txt ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '4':
  msg.attach(MIMEText(open('templates/rce.html',).read(),'html'))
  stringweb = 'url vuln RCE : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/cgi_bin/main.cgi?board=FREE_BOARD ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug =='5':
  msg.attach(MIMEText(open('templates/csrf.html',).read(),'html'))
  stringweb = 'url vuln CSRF : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/content/uploader.php ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '6':
  msg.attach(MIMEText(open('templates/xss.html',).read(),'html'))
  stringweb = 'url vuln XSS : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/search/?=\n[ Example : http://www.situsbokep.com/ on bukutamu ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '7':
  msg.attach(MIMEText(open('templates/ssi.html',).read(),'html'))
  stringweb = 'url vuln SSI Injection : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/login.shtml?page= ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '8':
  msg.attach(MIMEText(open('templates/csv.html',).read(),'html'))
  stringweb = 'url vuln CSV Injection : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/index.php?option= ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '9':
  msg.attach(MIMEText(open('templates/paramtemper.html',).read(),'html'))
  stringweb = 'url vuln Parameter tempering : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/product.php?cid=88&price=1000000 ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '10':
  msg.attach(MIMEText(open('templates/bypassadmin.html',).read(),'html'))
  stringweb = 'url vuln bypass admin : '
  penutup = '<br><br>dengan laporan ini semoga bug report saya dapat diterima dengan baik, terimakasih.'
  print ('\n[ Example : http://www.situsbokep.com/webadmin/login.php ]')
  namaweb = input('Masukan URL Website : ')
  msg.attach(MIMEText(stringweb,'html'))
  msg.attach(MIMEText(namaweb,'html'))
  msg.attach(MIMEText(penutup,'html'))
  print (hijau)
  print ('Example : /storage/sdcard0/recorder/bugreport.pdf')
  print ('Example : /storage/sdcard0/recorder/bugreport.mp4')
  print ('Example : /storage/sdcard0/recorder/bugreport.docx')
  print ('Example : /storage/sdcard0/recorder/bugreport.jpg\n')
  file_location = input('input letak dokumen (wajib) : ')
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
elif inputbug == '99':
    print ('semoga hari anda menyenangkan!')
    exit()
else:
    print ('input salah!')
    exit()
system('clear')
templates.i.item()
print (kuning)
print ('Pilih server email akun yang anda gunakan!')
print ('    1.gmail')
print ('    2.yahoo')
print ('    99.Keluar/Ga Minat\n')
choice = input("masukan pilihan(1/2/99): ")
if choice == '1':
        server = smtplib.SMTP('smtp.gmail.com', 587)
elif choice == '2':
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
elif choice == '99':
        print ('semoga hari anda menyenangkan!')
        exit()
else:
        print ('input salah! anda di kick!')
        exit()
print (hijau)
email           = input("masukan email anda : ")
password        =  getpass("masukan password email anda : ")
print (kuning)
toaddr          = input("masukan email tujuan anda : ")
print (hijau)
print ('Example : [BUG BOUNTY TOKOPEDIA] Reflected XSS on Search Product')
print ('Example : [www.namaweb.go.id] SQL Injection on /berita.php?id= ',kuning)
judul           = input("masukan judul email anda : ")

msg['From'] = email
msg['To'] = toaddr
msg['Subject'] = judul
server.starttls()
text = msg.as_string()
server.login(email,password)
server.sendmail(email, toaddr, text)
print('\nBerhasil Mengirim! , cek kotak keluar di email anda!')
server.quit()