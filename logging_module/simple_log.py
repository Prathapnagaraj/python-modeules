import logging
'''
To use this logging you need to follow 2 step
                                              1: basic config (if not default conf is taken)
					      2: log the msg

'''

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug("hi im in debug")
logging.info('hi im in info')
logging.warning('im in warning')
print "hello world"

