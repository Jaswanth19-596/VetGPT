from selenium import webdriver
from selenium.webdriver.common.by import By
import time
listOfURLS = []

fewURLs = [
    # 'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102888&ind=1',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102887&ind=676',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102890&ind=1161'
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102889&ind=1733',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102892&ind=1782',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102891&ind=1842',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102893&ind=1912',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=110705&ind=1930',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102894&ind=2047',
           'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102895&ind=2220',
        #    'https://veterinarypartner.vin.com/default.aspx?pid=19239&catId=102896&ind=2354'
           ]
# Initialize the WebDriver
driver = webdriver.Chrome()
for url in fewURLs:

    # Open the target webpage
    driver.get(url)

    # Wait for the page to load completely
    driver.implicitly_wait(10)  # Implicit wait, adjust time as needed

    # Find all elements with the class 'tree-leaf'
    tree_leaf_elements = driver.find_elements(By.CLASS_NAME, 'tree-leaf')

    # Print the number of elements found
    print(f"Number of elements with class 'tree-leaf': {len(tree_leaf_elements)}")



    # Optionally, print each element or its text content
    for element in tree_leaf_elements:
        listOfURLS.append(f'https://veterinarypartner.vin.com{element.get_attribute('data-nextnodeurl')}')
    # Close the driver

count = 0

for url in listOfURLS:
    try:

        driver.get(url)
        count+=1
        time.sleep(3)
        headingElement = driver.find_element(By.ID, 'ctl00_DocumentTitlePanel')
        content = driver.find_element(By.ID, 'ctl00_DocumentMainContentPanel')

        with open('content.txt', 'a') as f:
            f.write(headingElement.text)
            f.write(content.text)
    except Exception as e:
        print(url)
        print('Something went wrong', e)


print(count)

driver.quit()
