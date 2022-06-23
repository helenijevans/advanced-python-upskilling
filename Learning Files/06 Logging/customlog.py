# Demonstrate how to customize logging output

import logging

extData = {'user': 'joem@example.com'}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    # asctime - Human readable date format when the log record was created
    # filename/functioname - file/function where the log message originated
    # levelname/levelno - String/Numeric representation of the message level (DEBUG, INFO etc.)
    # lineno - Source line number where the logging call was issued (if applicable)
    # message - The logged message string itself
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    # extData string passed in through below method to access data through the keys
    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    main()
