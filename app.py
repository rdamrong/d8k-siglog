import signal
import os
import sys
import time
import logging

def readConfiguration(signalNumber, frame):
    logging.warning ('(SIGHUP) reading configuration')
    return

def terminateProcess(signalNumber, frame):
    logging.warning('(SIGTERM) terminating the process')
    logging.warning ('Action#1')
    logging.warning ('Action#2')
    logging.warning ('Bye')
    sys.exit()
def receiveSignal(signalNumber, frame):
    logging.warning ('Received SIGNAL: %d', signalNumber)
    return

if __name__ == '__main__':
    # register the signals to be caught
    signal.signal(signal.SIGHUP, readConfiguration)
    signal.signal(signal.SIGTERM, terminateProcess)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)

    # output current process id
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    print('My PID is:', os.getpid())
    logging.warning('Staring app')

    # wait in an endless loop for signals
    while True:
        logging.warning('Working...')
        time.sleep(30)
