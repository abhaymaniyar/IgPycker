from distutils.core import setup


setup(
	name = "IgPycker",
	version = "1.0",
	py_modules = ['pycker'],


	#metadata
	author = 'Abhay Maniyar',
	author_email = 'abhaymaniyar@live.in',
	description = 'A module to get high resolution profile picture of Instagram users',
	license = 'Public domain',
	install_requires=['bs4'],
	keywords = 'example',
)
