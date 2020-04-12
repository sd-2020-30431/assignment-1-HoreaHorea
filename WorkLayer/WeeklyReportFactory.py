from abc import ABC

from WorkLayer.AbstractReportFactory import AbstractReportFactory
from WorkLayer.Verifier import Verifier


class WeeklyReportFactory(AbstractReportFactory, ABC):

    def __init__(self, dateStart, dateEnd, fidb):
        # super(WeeklyReportFactory, self).__init__()  # still got some questions^*
        self.report = []
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.datasource = fidb

    v = Verifier

    def createReport(self):
        if self.v.weekVerifier(self.dateStart, self.dateEnd):
            self.report = self.datasource.getWeeklyReport(self.dateStart, self.dateEnd)
        else:
            self.report = "Incorrect dates chosen!"
