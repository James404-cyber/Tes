import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Meta32")._site_view_()
elif 'aarch' in arc:
	__import__("Filpp").ninex()
else:
	exit(f' Unknow device machine {arc}')
