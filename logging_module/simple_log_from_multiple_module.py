import logging
import mylib

def main():
	logging.basicConfig(filename='myapp.log',level=logging.INFO)
	logging.info('welcome to main')
	mylib.do_something()
	logging.info('Fininshed')


if __name__=='__main__':
	main()
