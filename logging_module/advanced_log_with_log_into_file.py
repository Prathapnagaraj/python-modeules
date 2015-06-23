import logging
from mylib import do_something

log=logging.getLogger(__file__)
log.setLevel(logging.DEBUG) #logging.info will ignore DEBUG msg
			   

# create a file handler
handler=logging.FileHandler(__file__.replace('py','log'))
handler.setLevel(logging.DEBUG) #logging.DEBUG will log all msg

# create a logging format

format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(format)
log.addHandler(handler)

log.info('hey info')
log.debug('hey debug')
log.error('hello error')
log.warning('hello warn')
do_something()
do_something()
log.critical('hello critical')

def do_nothing():
	print "Doing nothing"

