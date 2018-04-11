import unittest

from problem2.main import Processor, Reader, ProcessorBuffer


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        processor = Processor(reader=Reader('test.info'), buffer=ProcessorBuffer())
        processor.process()
        self.assertAlmostEqual(0.54, processor.get_mean('/index'))
        self.assertAlmostEqual(0.7155, processor.get_mean('/home'))
        self.assertAlmostEqual(0.03, processor.get_mean('/test'))
