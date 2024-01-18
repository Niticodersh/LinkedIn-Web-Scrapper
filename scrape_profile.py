from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

def scrape_linkedin_profiles(driver, link):

    driver.get(link)
    scroll_pause_time = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(3):
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # ## Extracting Page Source
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')

    # ## Scraping details: Profile Picture URL, Name, Connections, About, Education and Skills

    # In[ ]:


    img_tag = soup.find('img', class_='presence-entity__image')
    profile_picture_url = img_tag['src']
    name_loc = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})
    name = name_loc.get_text().strip()

    connection_div = driver.find_element(By.CLASS_NAME, 'ph5')
    connection_loc = connection_div.find_element(By.CLASS_NAME, 'pv-top-card--list-bullet')
    span_elements = connection_loc.find_elements(By.TAG_NAME, 'span')
    connections_data = "".join(" ".join([span.text for span in span_elements][1]).split())

    sections = driver.find_elements(By.CSS_SELECTOR, '[data-view-name="profile-card"]')
    output = {}
    output["Profile Picture URL"] = profile_picture_url
    output["Name"] = name
    output["Connections"] = connections_data
    for section in sections:
        extract_div = section.find_element(By.CSS_SELECTOR, ':nth-child(1)')
        required = ["education", "about", "skills"]
        if (extract_div.get_attribute("id") not in required):
            continue

        extract_id = extract_div.get_attribute("id")
        if (extract_id == 'about'):
            elements = section.find_elements(By.TAG_NAME, 'span')
            summary = ""
            for element in elements[1:]:
                if element.get_attribute('class') == 'visually-hidden':
                    summary += element.get_attribute("innerText")
            output['Summary'] = summary

        elif (extract_id == 'education'):
            output['Education'] = []
            elements = section.find_elements(By.TAG_NAME, 'span')
            filtered_elements = []
            for element in elements[1:]:
                if element.get_attribute('class') == 'visually-hidden':
                    filtered_elements.append(element)

            for i in range(len(filtered_elements)):
                span = filtered_elements[i]
                temp = {}
                span_parent = span.find_element(By.XPATH, "..")
                class_attr = span_parent.get_attribute('class')
                class_list = class_attr.split()
                if ('mr1' in class_list):
                    temp['Institution'] = span.get_attribute('innerText')
                    if ((i + 1) < len(filtered_elements)):
                        temp['Degree'] = filtered_elements[i + 1].get_attribute('innerText')
                    if ((i + 2) < len(filtered_elements)):
                        temp['Time Period'] = filtered_elements[i + 2].get_attribute('innerText')
                    output['Education'].append(temp)
        else:

            footerlinkcontainer = section.find_element(By.CLASS_NAME, 'pvs-list__footer-wrapper')
            if footerlinkcontainer:
                footerlink = footerlinkcontainer.find_element(By.TAG_NAME, 'a').get_attribute('href')
                driver.get(footerlink)
                sleep(3)
                list_container = driver.find_element(By.CLASS_NAME, 'pvs-list__container')
                list_container = list_container.find_element(By.CLASS_NAME, 'pvs-list')
                output['Skills'] = []
                lis = list_container.find_elements(By.TAG_NAME, 'span')
                lis = [x for x in lis if (x.get_attribute('class') == 'visually-hidden')]

                for span in lis:
                    span_parent = span.find_element(By.XPATH, "..")
                    class_attr = span_parent.get_attribute('class')
                    class_list = class_attr.split()

                    if 'mr1' in class_list:
                        output['Skills'].append(span.get_attribute('innerText'))

                sleep(3)
                break

            output['Skills'] = []
            lis = section.find_elements(By.TAG_NAME, 'span')
            lis = [x for x in lis if x.get_attribute('class') == 'visually-hidden'][1:]
            for span in lis:
                span_parent = span.find_element(By.XPATH, "..")
                class_attr = span_parent.get_attribute('class')
                class_list = class_attr.split()
                if 'mr1' in class_list:
                    output['Skills'].append(span.get_attribute('innerText'))
            output['Skills'] = set(output['Skills'])
    return output