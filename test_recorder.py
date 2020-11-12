#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:12
# @Author  : Menzel3
# @Site    : 
# @File    : test_recorder.py
# @Software: PyCharm
# @version : 0.0.1
import unittest
from sunflower.internal.recorder import Recorder, HA, DEC
from sunflower.internal.model.offset import HAOffset, DECOffset
from sunflower.internal.model.target import Target
from PyQt5.QtCore import QDateTime


class TestStringMethods(unittest.TestCase):

    def test_write(self):
        localTime = QDateTime.currentDateTime()
        recorder = Recorder()
        target = Target(name='test')
        ha = [23.76153215391256, 31.168754830018017, 31.853349116583416, 36.26792003332821, 38.68135271905504,
              41.260941232476746, 43.448195137480454, 45.61301352630765, 48.27885959218019, 50.34754611973788]
        offset_ha = [19.0, 19.0, 19.5, 19.25, 19.1, 18.9, 18.9, 18.9, 18.85, 18.85]

        dec = [-3.3922330810514882, -3.4001945563262996, -3.4009302916765476, -3.4056743106063454, -3.408267613265428,
               -3.4110392743056757, -3.413389245283975, -3.4157149860054545, -3.4185788314731047, -3.4208010416085095]
        offset_dec = [7.5, 8.5, 8.8, 9.0, 9.3, 9.5, 9.7, 9.8, 10.05, 10.15]
        for i in range(10):
            target.hourAngle, target.declination = ha[i], dec[i]
            haOffset = HAOffset(ha[i], offset_ha[i], localTime, -1, target)
            decOffset = DECOffset(dec[i], offset_dec[i], localTime, -1, target)
            self.assertEqual(None, recorder.writeData(haOffset=haOffset, decOffset=decOffset))

    def test_read(self):
        recorder = Recorder()
        self.assertTrue(([23.76153215391256, ], [19.0,]), recorder.readData(scale=[23, 25], kind=HA))
        self.assertTrue(([-3.3922330810514882, ], [7.5, ]), recorder.readData(scale=[-3, -3.4], kind=DEC))


if __name__ == '__main__':
    unittest.main()