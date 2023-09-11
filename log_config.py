import logging

def configure_logging() -> None:
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d: %(message)s')
    handler = logging.FileHandler('game.log')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.info('\n--- New Session ---')

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)