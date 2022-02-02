import time

from base.base_driver import BaseDriver


class ScenarioList(BaseDriver):
    # Constructor
    def __init__(self, driver, wait):
        # To Initiate Basedriver
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def account_select(self, accountnames, selectedaccount):
        print(selectedaccount)
        for account in accountnames:
            if (account.text == selectedaccount):
                account.click()
                time.sleep(2)
                break

    def opportunity_select(self, opportunitynames, selectedopportunity):
        print(selectedopportunity)
        for opportunity in opportunitynames:
            if opportunity.text == selectedopportunity:
                opportunity.click()
                time.sleep(2)
                break

    def scenario_select(self, scenarionames, selectedscenario):
        print(selectedscenario)
        for scenario in scenarionames:
            if scenario.text == selectedscenario:
                print(scenario.text)
                scenario.click()
                time.sleep(2)
                break

    def add_oppotunity(self, oppname, accname):
        addOpportunity = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-scenarios/div[2]/div[1]/div/div/div[2]/input")
        addOpportunity.click()
        time.sleep(2)

        OppName = self.driver.find_element_by_xpath(
            "/html/body/modal-container/div/div/app-add-scenario-modal/div/div[2]/form/div/div[1]/input")
        OppName.clear()
        OppName.send_keys(oppname)
        time.sleep(1)

        accName = self.driver.find_element_by_xpath(
            "/html/body/modal-container/div/div/app-add-scenario-modal/div/div[2]/form/div/div[2]/input")
        accName.clear()
        accName.send_keys(accname)
        time.sleep(1)

        addButton = self.driver.find_element_by_xpath(
            "/html/body/modal-container/div/div/app-add-scenario-modal/div/div[3]/button[2]")
        addButton.click()
        time.sleep(1)

        time.sleep(1)

    def add_scenario(self, scenarioname):
        print('Add Scenario', scenarioname)
        time.sleep(1)
        #Add Scenario Option
        add_scenario = self.driver.find_element_by_xpath("//*[@id='accordion']/div/div[1]/div[2]/div/img")
        add_scenario.click()
        time.sleep(1)

        #Enter Scenario Name
        enter_scenario = self.driver.find_element_by_xpath("/html/body/modal-container/div/div/app-add-scenario-modal/div/div[2]/form/div/div/input")
        enter_scenario.send_keys(scenarioname)
        time.sleep(1)

        #Add Button
        submit_btn = self.driver.find_element_by_xpath("/html/body/modal-container/div/div/app-add-scenario-modal/div/div[3]/button[2]")
        submit_btn.click()
        time.sleep(1)

