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
       'battle_success': {
           'handlers': ['consoleError'],
           'level': 'INFO'
       },
       'no_config_file': {
           'handlers': ['console'],
           'level': 'DEBUG',
           'propagate': True
       }
   }
}
