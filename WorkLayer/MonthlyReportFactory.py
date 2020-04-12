from abc import ABC

from WorkLayer.AbstractReportFactory import AbstractReportFactory
from WorkLayer.Verifier import Verifier


class MonthlyReportFactory(AbstractReportFactory, ABC):

    def __init__(self, dateStart, dateEnd, fidb):
        #super(MonthlyReportFactory, self).__init__()  # still got some questions^*
        self.report = []
        self.dateEnd = dateEnd
        self.dateStart = dateStart
        self.datasource = fidb

    v = Verifier

    def createReport(self):
        if self.v.monthVerifier(self.dateStart, self.dateEnd):
            self.report = self.datasource.getMonthlyReport(self.dateStart)
        else:
            self.report = "Incorrect dates chosen!"