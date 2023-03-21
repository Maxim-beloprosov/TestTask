from fw.application_manager import ApplicationManager


class WebBase():

    APP = ApplicationManager()

    def setup_class(self):
        self.APP.web_base.open_main_page()

    def setup_method(self):
        self.APP.web_base.open_main_page()

    def teardown_method(self):
        self.APP.driver_instance.stop_driver()

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

