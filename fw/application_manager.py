from fw.driverInstance import DriverInstance
from data.settings import Settings

from fw.fw_base import FWBase

from fw.web.test.test_fw import TestFW
from fw.web.web_base import WebBase
from fw.work_with_time import work_with_time


class ApplicationManager:

    settings = Settings()

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.fw_base = FWBase(self)
        self.web_base = WebBase(self)
        self.time = work_with_time()
        self.test_fw = TestFW(self)