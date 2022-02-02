import time

import pytest
from pages.scenario_list import ScenarioList
from pages.scenario_details import ScenarioDetails
# pytest in action – test_pytest_example_1.py


@pytest.mark.usefixtures("setup")
class TestDemo():
    # def function_1(self):
    #     print('self', self)
    #     time.sleep(1)
    #     tiles = self.driver.find_element_by_xpath("/html/body/app-root/div/div/app-landing/div/div[2]/div[2]/div")
    #     tiles.click()
    #     time.sleep(1)
    #     # print(tiles)

    #     # return var + 1

    def test_success(self):
        tiles = self.driver.find_element_by_xpath("/html/body/app-root/div/div/app-landing/div/div[2]/div[2]/div")
        tiles.click()
        time.sleep(1)
        # assert function_1(4) == 5

    def test_accordian(self):
        print('Test accordian')
        acc_accordian = []
        acc_accordian = self.driver.find_elements_by_xpath("//*[@id='headingThree']/div/a")
        print(len(acc_accordian))
        sl = ScenarioList(self.driver, self.wait)
        if len(acc_accordian) > 0:
            sl.account_select(acc_accordian, 'Account: 1acc')
            time.sleep(1)
            opp_accordian = []
            opp_accordian = self.driver.find_elements_by_xpath("//*[@id='headingThree']/div/a")
            if len(opp_accordian) > 0:
                sl.opportunity_select(opp_accordian, "Opportunity: 112")
                time.sleep(1)
            scenario_list = []
            scenario_list = self.driver.find_elements_by_xpath("//*[@role='tabpanel']/div/tr/td/div")
            print('scneario',len(scenario_list))
            noScenario = False
            # if self.driver.find_element_by_xpath("//*[@id='noScenario']").get_attribute('value'):
            #     noScenario = self.driver.find_element_by_xpath("//*[@id='noScenario']").text == 'No Scenario Found'
            print(noScenario)
            print(len(scenario_list))
            if noScenario == False:
                sl.scenario_select(scenario_list, "Scenario12")
                time.sleep(1)
            else:
                sl.add_scenario('sc1')
                time.sleep(1)
        else:
            sl.add_oppotunity("opp_1", "acc_1")
            time.sleep(1)

    def test_details(self):
        sd = ScenarioDetails(self.driver, self.wait)
        sd.change_scenario()
        time.sleep(1)
        sd.purity_check()
        time.sleep(1)
        sd.add_dataset()
        time.sleep(2)
