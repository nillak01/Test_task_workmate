import logging


logging.basicConfig(
    level=logging.WARNING,
    # было '%(levelname)s:%(name)s:%(message)s'
    format='%(levelname)s: %(message)s'
)
