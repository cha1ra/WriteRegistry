# -*- coding: utf-8 -*-
import winreg
print("-- レジストリ書き込み開始 --")
print('control panel\desktop の ScreenSaveActive値 を変更します')

path = r'control panel\desktop'

try:
	key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_READ)
	data, regtype = winreg.QueryValueEx(key, 'ScreenSaveActive')
	winreg.CloseKey(key)

	print('data = ' + data)

	if data == '1':
		data = '0'
	else:
		data = '1'

	print('値を ' + data + ' に変更します')

	key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_WRITE)
	winreg.SetValueEx(key, 'ScreenSaveActive', 0, winreg.REG_SZ, data)
	winreg.CloseKey(key)
except:
	print("読込、または書込時にエラーが発生しました")

print("-- 終了 --")
input('Press Enter...')