import logging
logger = logging.getLogger(__name__)

logger.info("hello!")
# There are other message types like:
# warning, error, critical, log, debug, exception,

logging.basicConfig(filename=args.logging_output, level=logging.DEBUG)
