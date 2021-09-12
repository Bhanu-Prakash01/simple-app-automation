from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

desire_cap={
  "platformName": "Android",
  "platformVersion": "9.0",
  "deviceName": "R8UOW84SNZ7HNRQG",
  "app": "C:/Users/kingk/Desktop/app.apk"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desire_cap)

touch =TouchAction(driver)
tokens=['DFB38DAA2D4E3B1FE81D5A94B95A1CA38D796C76','053ADBC286576AAC05442CDCBDF14112AA0E42CD','15A86DF3431E1AE801664628966B4DE6BE026511']


def opening():
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.Button').click()
  driver.implicitly_wait(10)

  # for i in range(2):
  touch.press(x=303,y=104).move_to(x=400,y=1330).release().perform()
  print('swipe')
  driver.swipe(300,1330,300,500)
  # print('swipe')
  driver.find_element_by_id('com.example.implementingapp:id/btAddPaymentMethod').click()



def Debit_card(crd_nbr,cvv,name):

  print('debit')
  debit_card = driver.find_element_by_xpath( '//android.view.ViewGroup[@content-desc="Add Payment Method"]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.RelativeLayout')

  debit_card.click()
  driver.implicitly_wait(10)
  card_number=driver.find_element_by_id('com.example.implementingapp:id/textInputCardNumber')
  cvv_number=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
  expire_date=driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')


  card_number.send_keys(crd_nbr)
  cvv_number.send_keys(cvv)

  expire_date.click()

  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
  driver.find_element_by_id('com.example.implementingapp:id/textInputCardHolderName').send_keys(name)

  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()

  driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
  driver.implicitly_wait(50)



def Cerditcard(crd_nbr,cvv,name):
  print('credit card')
  driver.implicitly_wait(5)
  if(driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Add Payment Method"]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout')):
    driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Add Payment Method"]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout').click()
  else:
    driver.find_element_by_id('com.example.implementingapp:id/btAddPaymentMethod').click()
    driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Add Payment Method"]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout').click()

  card_number = driver.find_element_by_id('com.example.implementingapp:id/textInputCardNumber')
  cvv_number = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
  expire_date = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')


  card_number.send_keys(crd_nbr)
  cvv_number.send_keys(cvv)

  expire_date.click()

  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
  driver.find_element_by_id('com.example.implementingapp:id/textInputCardHolderName').send_keys(name)

  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()

  driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
  # driver.implicitly_wait(10)
  driver.implicitly_wait(50)



def saving(r_numb,bank_numb,bank_name,account_name):
  print('savings')
  driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Add Payment Method"]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout').click()
  driver.implicitly_wait(5)
  driver.find_element_by_id('com.example.implementingapp:id/textInputRoutingNumber').send_keys(r_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountNumber').send_keys(bank_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputBankName').send_keys(bank_name)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountHolderName').send_keys(account_name)
  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()
  driver.find_element_by_id('com.example.implementingapp:id/btDone').click()
  driver.implicitly_wait(50)


def check_amount(r_numb,bank_numb,bank_name,account_name):
  print('check amount')
  check_account = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Add Payment Method"]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout')
  check_account.click()
  driver.implicitly_wait(5)
  driver.find_element_by_id('com.example.implementingapp:id/textInputRoutingNumber').send_keys(r_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountNumber').send_keys(bank_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputBankName').send_keys(bank_name)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountHolderName').send_keys(account_name)
  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()
  driver.find_element_by_id('com.example.implementingapp:id/btDone').click()
  driver.implicitly_wait(50)








def Add_Checking_Account(r_numb,bank_numb,bank_name,account_name):
  driver.implicitly_wait(5)
  driver.find_element_by_id('com.example.implementingapp:id/textInputRoutingNumber').send_keys(r_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountNumber').send_keys(bank_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputBankName').send_keys(bank_name)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountHolderName').send_keys(account_name)
  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()
  driver.find_element_by_id('com.example.implementingapp:id/btDone').click()
  driver.implicitly_wait(50)

def Add_Saving_account(r_numb,bank_numb,bank_name,account_name):
  driver.implicitly_wait(5)
  driver.find_element_by_id('com.example.implementingapp:id/textInputRoutingNumber').send_keys(r_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountNumber').send_keys(bank_numb)
  driver.find_element_by_id('com.example.implementingapp:id/textInputBankName').send_keys(bank_name)
  driver.find_element_by_id('com.example.implementingapp:id/textInputAccountHolderName').send_keys(account_name)
  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()
  driver.find_element_by_id('com.example.implementingapp:id/btDone').click()
  driver.implicitly_wait(50)

def Add_Credit_Card(crd_nbr,cvv,name):
  card_number = driver.find_element_by_id('com.example.implementingapp:id/textInputCardNumber')
  cvv_number = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
  expire_date = driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')
  card_number.send_keys(crd_nbr)
  cvv_number.send_keys(cvv)
  expire_date.click()
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
  driver.find_element_by_id('com.example.implementingapp:id/textInputCardHolderName').send_keys(name)
  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()
  driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
  driver.implicitly_wait(50)

def Add_Debit_Card(crd_nbr,cvv,name):
  card_number = driver.find_element_by_id('com.example.implementingapp:id/textInputCardNumber')
  cvv_number = driver.find_element_by_xpath(
    '//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
  expire_date = driver.find_element_by_xpath(
    '//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')

  card_number.send_keys(crd_nbr)
  cvv_number.send_keys(cvv)

  expire_date.click()

  driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]').click()
  driver.find_element_by_id('com.example.implementingapp:id/textInputCardHolderName').send_keys(name)

  driver.find_element_by_id('com.example.implementingapp:id/cbAgreement').click()

  driver.find_element_by_xpath(
    '//android.view.ViewGroup[@content-desc="Card Details"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
  driver.implicitly_wait(50)

def Edit_A_Profile(token):
  driver.find_element_by_id('com.example.implementingapp:id/etToken').send_keys(token)
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button').click()
  driver.implicitly_wait(50)
  time.sleep(5)
  driver.find_element_by_id('com.example.implementingapp:id/etToken').clear()

def AddPaymentMethod():
  opening()
  time.sleep(10)
  try:
    driver.find_element_by_id('com.example.implementingapp:id/btAddPaymentMethod').click()
  except:
    pass
  check_amount(121000021,44455875474557545,'wepay','test')
  driver.find_element_by_id('com.example.implementingapp:id/btAddPaymentMethod').click()
  driver.implicitly_wait(30)

  time.sleep(10)
  saving(121000021,44455875474557545,'wepay','test')
  driver.implicitly_wait(30)
  driver.find_element_by_id('com.example.implementingapp:id/btAddPaymentMethod').click()

  time.sleep(10)
  Cerditcard(4204589280067016, 420,'Anthony')
  driver.implicitly_wait(30)

  time.sleep(10)
  driver.find_element_by_id('com.example.implementingapp:id/btAddPaymentMethod').click()
  Debit_card(4204589280067016, 420,'Anthony')

  # for i in range(3):
  time.sleep(10)
  driver.implicitly_wait(50)
  touch.press(x=303, y=504).move_to(x=400, y=900).release().perform()
  print('swipe')
  driver.swipe(300, 900, 300, 500)
  driver.implicitly_wait(50)
  touch.press(x=303, y=504).move_to(x=400, y=630).release().perform()
  print('swipe')
  driver.swipe(300, 630, 300, 500)

#   other payment options
  time.sleep(5)
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[3]').click()
  Add_Saving_account(121000021,44455875474557545,'wepay','test')

  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
  Add_Checking_Account(121000021,44455875474557545,'wepay','test')



  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[5]').click()
  Add_Credit_Card(4204589280067016, 420,'Anthony')

  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[6]').click()
  Add_Debit_Card(4204589280067016, 420,'Anthony')

  # time.sleep(30)
  driver.implicitly_wait(50)
  # for i in range(3):
  time.sleep(10)
  touch.press(x=303, y=104).move_to(x=400, y=1330).release().perform()
  print('swipe')
  driver.swipe(300, 1330, 300, 500)
  touch.press(x=303, y=104).move_to(x=400, y=1330).release().perform()
  print('swipe')
  driver.swipe(300, 1330, 300, 500)
    # touch.press(x=303, y=104).move_to(x=400, y=1330).release().perform()
    # print('swipe')
    # driver.swipe(300, 1330, 300, 500)
    # touch.press(x=303, y=504).move_to(x=400, y=1330).release().perform()
    # print('swipe')
    # driver.swipe(300, 1330, 300, 500)
  for token in tokens:
    Edit_A_Profile(token)

  time.sleep(5)
  print('over.....')
AddPaymentMethod()