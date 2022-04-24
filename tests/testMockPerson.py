from unittest import TestCase
import pytest
from pytest_mysql import factories
from src.generator import Generator
from src.address import address
from src.person import person


class GeneratorTesting (TestCase):

    mysql_my_proc = factories.mysql_proc(
        port=8888)

    def test_getDate(self):
       gD = Generator.genFloor()
       assert gD.isdigit()

    def testGenerateBirthDate(self):
        gB = Generator.genBirthDate()
        assert(isinstance(gB,str))

    def testGenCprBirthday(self):
        firstPerson = Generator.genCPR('female', '12-05-2011')
        assert firstPerson[0:6] == '120511'

    def testGenCprGender(self):
        firstPerson = Generator.genCPR('male', '12-05-2011')
        assert int(firstPerson[10])%2 == 1

    def testGenCprMiddle(self):
        firstPerson = Generator.genCPR('male', '12-05-2011')
        assert int(firstPerson[7:10]) > 99 and int(firstPerson[6:9]) < 1000

    def testGenStreetNum(self):
        streetNr = Generator.genStreetNumber()
        assert(isinstance(streetNr,str))



