from selenium import webdriver
import csv
import time
import configparser

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://shub.edu.vn/login')

def start(username, password, class_code, test_number):
    #Enter username
    input_username = driver.find_element_by_xpath('//*[@id="__next"]/div/form/div[1]/div/input')
    input_username.send_keys(username)
    #Enter password
    input_password = driver.find_element_by_xpath('//*[@id="__next"]/div/form/div[2]/div/input')
    input_password.send_keys(password)
    #Submit
    submit_button = driver.find_element_by_xpath('//*[@id="__next"]/div/form/button')
    driver.execute_script("arguments[0].click();", submit_button)
    #Navigate to test page
    time.sleep(sleep_time)
    driver.get(f'https://shub.edu.vn/class/{class_code}/homework/{test_number}/test') 
    time.sleep(sleep_time)
    list_by_class = driver.find_elements_by_class_name('MuiTypography-body1')
    return count_questions(list_by_class)

def count_questions(list_by_class):
    count = 0
    for element in list_by_class:
        val = element.get_attribute('innerHTML')
        try:
            int(val)
            count += 1
        except:
            pass
    print(f'Questions found: {count}')
    return brute_force(count)

def refresh_page(idx, count, answer):
    driver.get(f'https://shub.edu.vn/class/{class_code}/homework/{test_number}/test')
    time.sleep(sleep_time)
    #Click number box
    number_box = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[3]/div[{idx}]/div')
    driver.execute_script("arguments[0].click();", number_box)
    #Input answer
    answer_input = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[3]/div[{count + 1}]/div[2]/input')
    answer_input.send_keys(answer)
    #Send answer
    handin_button = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/button[1]')
    driver.execute_script("arguments[0].click();", handin_button)

    time.sleep(sleep_time)

    #Agree to send
    agree_button = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/button[2]')
    driver.execute_script("arguments[0].click();", agree_button)

    time.sleep(sleep_time)
    return driver

def brute_force(count):
    for idx in range(1, count + 1):
        attempt = 0
        for answer in ['A', 'B', 'C']:
            attempt += 1

            driver = refresh_page(idx, count, answer)

            num_of_right_answers = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/p[2]').get_attribute('innerHTML')

            if num_of_right_answers == '1':
                print(f'#{idx} : {answer}')
                write_to_csv(idx, answer, file_name)
                break
            elif attempt == 3:
                print(f'#{idx} : D')
                write_to_csv(idx, 'D', file_name)
                break
            time.sleep(sleep_time)
    driver.quit() 

def write_to_csv(idx, answer, file_name):
    with open(file_name, 'a+', newline='') as file:
        csvwriter = csv.writer(file, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([idx,answer])

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config['ACCOUNT']['Username']
    password = config['ACCOUNT']['Password']
    class_code = config['TEST']['ClassCode']
    test_number = config['TEST']['TestNumber']
    file_name = config['SETTINGS']['KeyFileName']
    sleep_time = float(config['SETTINGS']['SleepTime'])
    return username, password, class_code, test_number, file_name, sleep_time

username, password, class_code, test_number, file_name, sleep_time = read_config()
print('='*30)
print(f'Username : {username}')
print(f'Password : {password}')
print(f'Class Code : {class_code}')
print(f'Test Number : {test_number}')
print(f'CSV File Name : {file_name}')
print(f'sleep_time = {sleep_time}')
print('='*30)
start(username, password, class_code, test_number)
print('='*30)
print('Done')
input()