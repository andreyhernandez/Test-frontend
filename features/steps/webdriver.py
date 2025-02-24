from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

class WebDriver(RemoteWebDriver):
    def are_element_presents(self, table, context):
        for row in table:
            name = row['name']
            element_type = row['type']
            if not self.find_elements_by_name(name):
                return False
        return True
