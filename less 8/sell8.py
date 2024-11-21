import logging

logging.basicConfig(level=logging.DEBUG, filename='logs.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

try:
    print(10/0)
except ZeroDivisionError:
    logging.exception('Division by zero')