from selenium.webdriver.common.by import By

class AmazonPageLocators(object):

	LANGUAGE_BUTTON = (By.ID, "icp-nav-flyout")
	CURRENCY_DROPDOWN = (By.NAME, "COP")
	SEARCH_BAR = (By.ID,"twotabsearchtextbox")
	SEARCH_BUTTON = (By.ID,"nav-search-submit-button")
	SELECT_DD = (By.ID,'searchDropdownBox')
	ITEM = (By.CLASS_NAME,'a-price-whole')
	PRICE = (By.ID, 'exports_desktop_qualifiedBuybox_priceInsideBuyBox')
	STOCK_STATUS = (By.ID, 'availability')
	SHIPPING_DETAILS = (By.ID, 'exports_desktop_qualifiedBuybox_tlc_feature_div')
	RATING = (By.ID,'averageCustomerReviews')
	ADD_TO_CART = (By.ID,'add-to-cart-button')
	CART_TOTAL = (By.ID,'nav-cart-count')
	CAD_OPTION = (By.CSS_SELECTOR, "[data-value='{'stringVal':'CNY'}'']")
	SAVE_BUTTON = (By.ID,'icp-btn-save')
	ITEM_SELECT = (By.CLASS_NAME,'a-list-item');

 