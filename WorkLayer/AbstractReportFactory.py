from abc import ABC, abstractmethod

class AbstractReportFactory(ABC):

    def __init__(self,dateStart,dateEnd):
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.report= []
        super().__init__()

    @abstractmethod
    def createReport(self):
        pass
