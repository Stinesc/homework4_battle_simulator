import sys
import logging
import logging.config

LOGGING = {
   'version': 1,
   'disable_existing_loggers': True,
   'formatters': {
       'verbose': {
           'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
       },
       'simple': {
           'format': '%(levelname)s %(message)s'
       },
   },
   'handlers': {
       'null': {
           'level':'DEBUG',
           'class':'logging.NullHandler',
       },
       'console':{
           'level':'DEBUG',
           'class':'logging.StreamHandler',
           'formatter': 'verbose'
       },
       'consoleError':{
           'level':'ERROR',
           'class':'logging.StreamHandler',
           'formatter': 'simple'
       }
   },
   'loggers': {
       'A': {
           'handlers': ['null'],
           'propagate': True,
           'level': 'INFO',
       },
       'A.B': {
           'handlers': ['consoleError'],
           'level': 'DEBUG',
           'propagate': False,
       },
       'A.B.X': {
           'handlers': ['console'],
           'level': 'DEBUG',
           'propagate': True,
       },
       'C': {
           'handlers': ['console'],
           'level': 'INFO'
       }
   }
}


logging.config.dictConfig(LOGGING)
logA = logging.getLogger('A')
logAB = logging.getLogger('A.B')
logABX = logging.getLogger('A.B.X')
logC = logging.getLogger('C')
logA.error('A_asdasddasdasdasdas')
logAB.error('AB_asdasddasdasdasdas')
logABX.error('ABX_asdasddasdasdasdas')
logC.error('C_asdasddasdasdasdas')
