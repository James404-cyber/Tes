import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Meta32").James()
elif 'aarch' in arc:
	__import__("Meta").James()
else:
	exit(f' Unknow device machine {arc}')
