import logging

logging.basicConfig(
    filename='logs/intrusion_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


def log_intrusion(message):
    logging.info(message)