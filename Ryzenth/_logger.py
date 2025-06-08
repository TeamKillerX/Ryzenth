import logging

def logging_message_check():
    logger = logging.getLogger("[Ryzenth]")
    logger.setLevel(logging.DEBUG)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('httpcore').setLevel(logging.WARNING)
    return logger
