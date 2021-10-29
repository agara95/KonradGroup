import selenium
from locator import *
from selenium.webdriver.support.ui import *
from selenium.common.exceptions import NoSuchElementException
import unittest
from time import sleep
import sys




class BasePage(object):
	def __init__(self, driver):
		self.driver = driver

class AmazonHomePage(BasePage):

	def click_language_button(self):
		element = self.driver.find_element(*AmazonPageLocators.LANGUAGE_BUTTON)
		element.click()

	def currency_setting(self):
		image_path = "Photo"
		currecnyDD = Select(self.driver.find_element(*AmazonPageLocators.CURRENCY_DROPDOWN))
		currency ='CAD'
		try:
			currecnyDD.select_by_value(currency)
			save_button = self.driver.find_element(*AmazonPageLocators.SAVE_BUTTON)
			save_button.click()
			#finding item on page to confirm price 
			item = self.driver.find_element(*AmazonPageLocators.ITEM_SELECT)
			item.click()
			price_item = self.driver.find_element(*AmazonPageLocators.PRICE)
			if currency in price_item.text:
				return True
			else:
				return False
		except NoSuchElementException:
			self.driver.save_screenshot(f"{image_path}/NoCAD.png")
			assert False, ("CAD validation Error")
			return False
		return True

	#search for apple products in electronics and select a product
	def searchElectronics_apple(self):		
		textBox = self.driver.find_element(*AmazonPageLocators.SEARCH_BAR)
		textBox.send_keys("Apple")
		select = Select(self.driver.find_element(*AmazonPageLocators.SELECT_DD))
		select.select_by_value('search-alias=electronics-intl-ship')
		searchButton = self.driver.find_element(*AmazonPageLocators.SEARCH_BUTTON)
		searchButton.click()
		product = self.driver.find_element(*AmazonPageLocators.ITEM)	
		product.click()
		
#Tests run after searching for a product on Amazon Page			
class ProductPage(BasePage):
	def price(self):
		image_path = "Photo"
		try:
			price = self.driver.find_element(*AmazonPageLocators.PRICE)
		except NoSuchElementException:
			self.driver.save_screenshot(f"{image_path}/price.png")
			assert False,("Price validation Error")
			return False
		return True

	def stockStatus(self):
		image_path = "Photo"
		try:
			stock = self.driver.find_element(*AmazonPageLocators.STOCK_STATUS)
		except NoSuchElementException:
			self.driver.save_screenshot(f"{image_path}/stockStatus.png")
			assert False,("Stock status validation Error")
			return False
		return True
	
	def shippingDetails(self):
		image_path = "Photo"
		try:
			shipping = self.driver.find_element(*AmazonPageLocators.SHIPPING_DETAILS)
		except NoSuchElementException:
			self.driver.save_screenshot(f"{image_path}/shipping.png")
			assert False,("Shipping validation Error")
			return False
		return True
	
	
	def customer_rating(self):
		image_path = "Photo"
		try:
			rating = self.driver.find_element(*AmazonPageLocators.RATING)
		except NoSuchElementException:
			self.driver.save_screenshot(f"{image_path}/rating.png")
			assert False,("Rating validation Error")
			return False
		return True

	def addToCart(self):
		image_path = "Photo"
		try:
			addToCartButton = self.driver.find_element(*AmazonPageLocators.ADD_TO_CART)
			addToCartButton.click()
			sleep(5)
			cart = self.driver.find_element(*AmazonPageLocators.CART_TOTAL)
			assert cart.text == '1'
		except NoSuchElementException:
			self.driver.save_screenshot(f"{image_path}/rating.png")
			assert False,("Add to Cart Validation Error")
			return False
		return True