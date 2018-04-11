from enum import Enum
import numpy as np
import scipy.stats as st


class ProcessorBufferKey(Enum):
    STEP = 0
    SUM = 1
    SQUARE_SUM = 2


class ProcessorBuffer:
    def __init__(self):
        self.__buffer = {}

    def __getitem__(self, key):
        if key not in self.__buffer:
            return {
                ProcessorBufferKey.SUM: 0,
                ProcessorBufferKey.STEP: 0,
                ProcessorBufferKey.SQUARE_SUM: 0,
            }
        else:
            return self.__buffer[key]

    def __setitem__(self, key, value):
        self.__buffer[key] = {
            ProcessorBufferKey.SUM: value[ProcessorBufferKey.SUM],
            ProcessorBufferKey.STEP: value[ProcessorBufferKey.STEP],
            ProcessorBufferKey.SQUARE_SUM: value[ProcessorBufferKey.SQUARE_SUM],
        }


class Processor:
    def __init__(self, reader, buffer):
        self.__reader = reader
        self.__buffer = buffer

    def get_count_lines(self, type_):
        return self.__buffer[type_][ProcessorBufferKey.STEP]

    def get_variance(self, type_):
        buf = self.__buffer[type_]
        square_sum = buf[ProcessorBufferKey.SQUARE_SUM]
        n = buf[ProcessorBufferKey.STEP]
        sum_ = buf[ProcessorBufferKey.SUM]
        return (n * square_sum - sum_ ** 2) / float(n * (n - 1))

    def get_std_err(self, type_):
        sum_ = self.__buffer[type_][ProcessorBufferKey.SUM]
        return np.sqrt(self.get_variance(type_) / float(sum_))

    def get_mean(self, type_):
        buf = self.__buffer[type_]
        n = buf[ProcessorBufferKey.STEP]
        sum_ = buf[ProcessorBufferKey.SUM]
        return sum_ / float(n)

    def get_conf_interval(self, type_, level=0.95):
        sem = self.get_std_err(type_)
        mean = self.get_mean(type_)
        n = self.__buffer[type_][ProcessorBufferKey]
        return st.t.interval(level, n, loc=mean, scale=sem)

    def process(self):
        while True:
            status, _, type_, time_ = self.__reader.read()
            if status is ReaderStatus.FINISH:
                return
            else:
                buf = self.__buffer[type_]
                buf[ProcessorBufferKey.SUM] = buf[ProcessorBufferKey.SUM] + time_
                buf[ProcessorBufferKey.STEP] = buf[ProcessorBufferKey.STEP] + 1
                buf[ProcessorBufferKey.SQUARE_SUM] = buf[ProcessorBufferKey.SQUARE_SUM] + time_ ** 2
                self.__buffer[type_] = buf


class ReaderStatus(Enum):
    OK = 0
    FINISH = 1


class Reader:

    def __init__(self, path):
        self.file = open(path)

    def read(self):
        line = self.file.readline().split(',')
        if len(line[0]) == 0:
            return ReaderStatus.FINISH, None, None, None
        else:
            return ReaderStatus.OK, int(line[0]), line[1], float(line[2])

    def close(self):
        self.file.close()
