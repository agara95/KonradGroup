import page
from selenium import webdriver 
import unittest
from time import sleep
from HTMLTestRunner import HTMLTestRunner
import os



class AmazonCaseStudy(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome("chromedriver\\chromedriver.exe")
		self.driver.get("http://www.amazon.com")
	
	#Check the selected currency displayed for the product price
	def test_scenario3(self):
		amazonPage = page.AmazonHomePage(self.driver)
		amazonPage.click_language_button()
		amazonPage.currency_setting()


	#Check Product Detail Page 
	def test_scenario4(self):
		homePage = page.AmazonHomePage(self.driver)
		productPage = page.ProductPage(self.driver)
		homePage.searchElectronics_apple()
		productPage.price()
		productPage.stockStatus()
		productPage.shippingDetails()
		productPage.customer_rating()
		productPage.addToCart()

	def tearDown(self):
		self.driver.close()
	
if __name__ == "__main__":
	cwd = os.getcwd()
	directory = cwd +'\\Test Execution Report'
	unittest.main(testRunner=HTMLTestRunner(output= directory))

