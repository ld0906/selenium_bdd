from selenium import webdriver

'''
def before_feature(context,feature):
    context.driver = webdriver.Firefox()


def after_feature(context,feature):
    context.driver.quit()
    
'''



def before_all(context):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
