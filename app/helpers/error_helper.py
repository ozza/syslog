def error_logger(logfile, timestamp, errortype, exception, data):
    file = open(logfile, "a")

    file.write(
        str(timestamp) + " " + str(errortype) + " ERROR: " + str(exception) + " --- " + str(data)
        + "\n--------------------------------\n"
    )

    file.close()
