from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver
driver = webdriver.Chrome('path/to/chromedriver')

# Navigate to LinkedIn jobs page
driver.get('https://www.linkedin.com/jobs/')

# Handle any pop-ups or cookie notifications
try:
    close_button = driver.find_element_by_class_name('artdeco-toaster-close-button')
    close_button.click()
except:
    pass

# Find the search bar and enter the job title
search_bar = driver.find_element_by_name('keywords')
search_bar.send_keys('Cientista de Dados' or 'Ciência de Dados')
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(5)

# Extract the company, job title, and any other relevant data
job_listings = driver.find_elements_by_class_name('job-search-card')
for job in job_listings:
    company = job.find_element_by_class_name('company').text
    title = job.find_element_by_class_name('title').text
    print(f'Company: {company}\nTitle: {title}\n')

# Close the browser
driver.quit()
