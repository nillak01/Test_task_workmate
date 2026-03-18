import logging


logging.basicConfig(
    level=logging.INFO,
    # было '%(levelname)s:%(name)s:%(message)s'
    format='%(levelname)s: %(message)s'
)
