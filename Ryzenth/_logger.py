import logging


def setting_loggings():
    LOGGING_CONFIG = {
        "version": 1,
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "formatter": "http",
                "stream": "ext://sys.stderr"
            }
        },
        "formatters": {
            "http": {
                "format": "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        'loggers': {
            'httpx': {
                'handlers': ['default'],
                'level': 'WARNING',
            },
            'httpcore': {
                'handlers': ['default'],
                'level': 'WARNING',
            },
        }
    }
    logging.config.dictConfig(LOGGING_CONFIG)

def logging_message_check():
    logger = logging.getLogger("[Ryzenth]")
    logger.setLevel(logging.DEBUG)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('httpcore').setLevel(logging.WARNING)
    return logger
