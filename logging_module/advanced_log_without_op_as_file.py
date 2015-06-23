import logging

# create logger
logging.basicConfig(level=logging.DEBUG)
log=logging.getLogger(__file__)

def main():
	log.info('hello info')
	log.debug('hello debug')
	log.warn('hello warning')
	log.error('hello error')
	log.critical('hello critical')
	print "hello log"

if __name__=='__main__':
	main()
