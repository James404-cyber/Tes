import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Ran32").James()
elif 'aarch' in arc:
	__import__("Ran").James()
else:
	exit(f' Unknow device machine {arc}')
