import time

from base.base_driver import BaseDriver


class ScenarioDetails(BaseDriver):
    # Constructor
    def __init__(self, driver, wait):
        # To Initiate Basedriver
        super().__init__(driver)
        self.driver = driver
        self.wait = wait


    def add_dataset(self):
        addDatasetBtn = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios-details/div/div[2]/capacity-parameters/div[1]/app-datasets/form/div[1]/div/button")
        addDatasetBtn.click()
        time.sleep(1)

    def change_scenario(self):
        click_scenario_dropdown = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios-details/div/div[1]/div/div/div[2]/div/div[1]/div/div/div/app-mpl-list-dropdown")
        click_scenario_dropdown.click()
        time.sleep(1)
        select_scenario_list = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios-details/div/div[1]/div/div/div[2]/div/div[1]/div/div/div/app-mpl-list-dropdown/div/div[2]/ul/li[2]")
        select_scenario_list.click()
        time.sleep(1)

    def purity_check(self):
        click_purity = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios-details/div/div[1]/div/div/div[2]/div/div[2]/div/app-mpl-list-dropdown")
        click_purity.click()
        time.sleep(1)
        click_purity_select = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios-details/div/div[1]/div/div/div[2]/div/div[2]/div/app-mpl-list-dropdown/div/div[2]/ul/li[2]")
        click_purity_select.click()
        time.sleep(1)

        dataset_text_check = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios-details/div/div[2]/capacity-parameters/div[1]/app-datasets/form/div[2]/mpl-table/div/table/tbody/tr[1]/td[3]/div/app-input/div/input")
        print("ajgsavjd",dataset_text_check.get_attribute("value"))
