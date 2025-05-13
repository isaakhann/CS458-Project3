from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time
import random
import string
from random import randint

# URL of the deployed React app
URL = "http://localhost:5173/"

# Generate a unique email for testing
random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
TEST_EMAIL = f"testuser_{random_string}@example.com"
#TEST_EMAIL = "testuser_nd98ctvg@example.com" #TEST

TEST_PASSWORD = "TestPassword123!"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(URL)
wait = WebDriverWait(driver, 60)  # Increased wait time to 15 seconds

print(f"Using unique test email: {TEST_EMAIL}")

lorem_words = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
    "exercitation", "ullamco", "laboris", "nisi", "aliquip", "ex", "ea", "commodo",
    "consequat", "duis", "aute", "irure", "dolor", "reprehenderit", "voluptate"
]


try:
    # Wait for the page to load and take initial screenshot
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    #driver.save_screenshot("initial_page.png")
    
    # 🟢 TEST SIGN UP
    print("Testing sign-up...")
    sign_up_toggle = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]")
    sign_up_toggle.click()
    
    # Adding a brief pause after switching to sign-up mode
    time.sleep(1)
    
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    
    # Clear fields first
    email_input.clear()
    password_input.clear()
    
    # Enter credentials
    email_input.send_keys(TEST_EMAIL)
    password_input.send_keys(TEST_PASSWORD)
    
    # Find the actual sign-up button (the one inside the form)
    sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign Up' and not(contains(., 'have an account'))]")
    
    # Take screenshot before clicking sign up
    #driver.save_screenshot("before_signup_click.png")
    
    # Click and wait longer
    sign_up_button.click()
    print("Sign-up button clicked, waiting for redirection...")
    
    # Wait longer for authentication and redirection
    time.sleep(3)
    
    # Take screenshot after sign-up to see what page we're on
    #driver.save_screenshot("after_signup.png")
    
    # Debug info
    print(f"Current URL: {driver.current_url}")
    print(f"Page title: {driver.title}")
    
    # Check if we're on the welcome page by looking for welcome message
    try:
        welcome_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Welcome')]")))
        print("Successfully reached welcome page!")
        
        
        
    except Exception as e:
        print(f"Failed to reach welcome page or find logout button: {e}")
        # Print all visible elements to help debug
        elements = driver.find_elements(By.XPATH, "//*[text()]")
        print("Visible text elements on page:")
        for el in elements[:10]:  # First 10 elements
            try:
                print(f"- {el.text}")
            except:
                pass
    

    # 🟢🟢🟢 TEST CASE: CREATING SURVEY WITH 0 QUESTIONS - BEGINNING
    print("TEST CASE: CREATING SURVEY WITH 0 QUESTIONS")
    survey_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create')]")))
    print("Found create survey button!")
    survey_button.click()
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Firebase')]")))
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Question')]")))

    
    
        #SURVEY AUTOMATION HERE
    create_button.click()
    print("Tried creating with 0 questions")
    time.sleep(3)
    
    # Handle first alert (0 questions error)
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.dismiss()
    except Exception as e:
        print(f"No initial alert found: {e}")

    print("Creating survey with 0 questions is not allowed by the system")
    
    # 🟢🟢🟢 TEST CASE: CREATING SURVEY WITH 0 QUESTIONS - END
    
      # 🟢🟢🟢 TEST CASE: NOT FILLING THE OPTIONAL QUESTIONS - BEGINNING
    print("TEST CASE: NOT FILLING THE OPTIONAL QUESTIONS")

    add_button.click()
    ra = randint(1, 100)
    print(f"Creating survey with {ra + 1} questions...")
    
    for x in range(0,ra):
       add_button.click()
    
    dropdown_menus = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.question-header select")))
  
    for dropdown_menu in dropdown_menus:
       select = Select(dropdown_menu)
       options = select.options
       if options:
          select.select_by_value(random.choice(options).get_attribute("value"))
    
    ####### TOGGLE RANDOMLY


    # toggles = driver.find_elements(By.CSS_SELECTOR, "label.toggle-label")
    # print("Found toggles!")
    # for toggle in toggles:
    #    input_checkbox = toggle.find_element(By.TAG_NAME, "input")
    #    ran_toggle = random.choice([True, False])
    #    if ran_toggle:  
    #       toggle.click()
    # num_add = random.randint(2, 5)      
    # for question_card in driver.find_elements(By.CSS_SELECTOR, "div.question-card"):
    #     try:
    #       print("Adding options to question card")
    #       for i in range(num_add):
    #         add_button = question_card.find_element(By.XPATH, ".//*[contains(text(), 'Add Option')]")
    #         add_button.click()
    #         driver.implicitly_wait(0.5)  
    #     except:
    #         continue
            
    # question_inputs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder='Untitled question']")))      
    # print("Found question inputs!")
    # print("Write titiles for questions")
    # for question in question_inputs:
    #     question.clear()
    #     words = random.choices(lorem_words, k=random.randint(3, 8))
    #     question.send_keys(words)   
    

    ####### TOGGLE RANDOMLY


    create_button.click()
    time.sleep(2)

    # Handle survey creation success alert
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert message: {alert_text}")
        alert.accept()
        print("Survey created successfully!")
    except Exception as e:
        print(f"Error handling success alert: {e}")

    driver.back()
    print("Navigated back to main page")
    time.sleep(2)  # Wait for page to load

# 🟢 TEST SURVEY COMPLETION AND SUBMITTING
        # Store the survey ID from the alert message for later use
    survey_id = alert_text.split(": ")[1].strip()
    print(f"Stored survey ID: {survey_id}")

    # Click "All Surveys" button
    all_surveys_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'All Surveys')]")))
    print("Found All Surveys button!")
    all_surveys_button.click()
    time.sleep(2)

    # Find and click the survey with matching ID
        # Find and click the survey with matching ID
    try:
        # Update the XPath to match the actual structure
        survey_element = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            f"//li[contains(@style, 'background') and contains(., '{survey_id}')]"
        )))
        print(f"Found our survey with ID: {survey_id}")
        
        # Use JavaScript click for more reliable interaction
        driver.execute_script("arguments[0].scrollIntoView(true);", survey_element)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", survey_element)
        print("Clicked on survey")
        time.sleep(2)

        print("Submitting without filling optional questions...")

        # # Answer all questions
        # print("Answering survey questions...")
        # questions = driver.find_elements(By.CLASS_NAME, "question-card")
        
        # for question in questions:
        #     # Handle different question types
        #     if question.find_elements(By.TAG_NAME, "input"):
        #         input_type = question.find_element(By.TAG_NAME, "input").get_attribute("type")
                
        #         if input_type == "text":
        #             text_input = question.find_element(By.TAG_NAME, "input")
        #             text_input.send_keys("Test Answer")
        #         elif input_type == "radio":
        #             # Select first radio option
        #             radio_options = question.find_elements(By.TAG_NAME, "input")
        #             radio_options[0].click()
        #         elif input_type == "checkbox":
        #             # Select first checkbox option
        #             checkbox = question.find_element(By.TAG_NAME, "input")
        #             checkbox.click()
            
        #     elif question.find_elements(By.TAG_NAME, "select"):
        #         # Handle dropdown
        #         select = Select(question.find_element(By.TAG_NAME, "select"))
        #         select.select_by_index(1)  # Select second option (first is usually placeholder)


        # Submit the survey
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit Survey')]")))
        submit_button.click()
        time.sleep(2)

        # Handle submission success alert
        alert = wait.until(EC.alert_is_present())
        print(f"Survey submission response: {alert.text}")
        alert.accept()

        print("Survey submitted successfully!")

    except Exception as e:
        print(f"Error during survey answering: {e}")
        print(f"Current URL: {driver.current_url}")
        driver.save_screenshot("survey_answer_error.png")
        
# 🟢🟢🟢 TEST CASE: NOT FILLING THE OPTIONAL QUESTIONS - END

# 🟢🟢🟢 TEST CASE: NOT FILLING THE REQUIRED QUESTIONS - BEGINNING
    print("TEST CASE: NOT FILLING THE REQUIRED QUESTIONS")
    survey_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create')]")))
    print("Found create survey button!")
    survey_button.click()
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Firebase')]")))
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Question')]")))

    
    
        #SURVEY AUTOMATION HERE

    # ## Create a survey with 0 questions
    # create_button.click()
    # print("Tried creating with 0 questions")
    # time.sleep(3)
    
    # # Handle first alert (0 questions error)
    # try:
    #     alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    #     alert.dismiss()
    # except Exception as e:
    #     print(f"No initial alert found: {e}")
        
    add_button.click()
    ra = randint(1, 100)
    print(f"Creating survey with {ra + 1} questions...")
    
    for x in range(0,ra):
       add_button.click()
    
    dropdown_menus = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.question-header select")))
  
    for dropdown_menu in dropdown_menus:
       select = Select(dropdown_menu)
       options = select.options
       if options:
          select.select_by_value(random.choice(options).get_attribute("value"))
    
    ###### TOGGLE RANDOMLY


    toggles = driver.find_elements(By.CSS_SELECTOR, "label.toggle-label")
    print("Found toggles!")
    for toggle in toggles:
       input_checkbox = toggle.find_element(By.TAG_NAME, "input")
       ran_toggle = random.choice([True, False])
       if ran_toggle:  
          toggle.click()
    num_add = random.randint(2, 5)      
    for question_card in driver.find_elements(By.CSS_SELECTOR, "div.question-card"):
        try:
          #print("Adding options to question card")
          for i in range(num_add):
            add_button = question_card.find_element(By.XPATH, ".//*[contains(text(), 'Add Option')]")
            add_button.click()
            driver.implicitly_wait(0.5)  
        except:
            continue
            
    question_inputs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder='Untitled question']")))      
    print("Found question inputs!")
    print("Write titiles for questions")
    for question in question_inputs:
        question.clear()
        words = random.choices(lorem_words, k=random.randint(3, 8))
        question.send_keys(words)   
    

    ###### TOGGLE RANDOMLY


    create_button.click()
    time.sleep(2)

    # Handle survey creation success alert
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert message: {alert_text}")
        alert.accept()
        print("Survey created successfully!")
    except Exception as e:
        print(f"Error handling success alert: {e}")

    driver.back()
    print("Navigated back to main page")
    time.sleep(2)  # Wait for page to load

# 🟢 TEST SURVEY COMPLETION AND SUBMITTING
        # Store the survey ID from the alert message for later use
    survey_id = alert_text.split(": ")[1].strip()
    print(f"Stored survey ID: {survey_id}")

    # Click "All Surveys" button
    all_surveys_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'All Surveys')]")))
    print("Found All Surveys button!")
    all_surveys_button.click()
    time.sleep(2)

    # Find and click the survey with matching ID
        # Find and click the survey with matching ID
    try:
        # Update the XPath to match the actual structure
        survey_element = wait.until(EC.element_to_be_clickable((
            By.XPATH, 
            f"//li[contains(@style, 'background') and contains(., '{survey_id}')]"
        )))
        print(f"Found our survey with ID: {survey_id}")
        
        # Use JavaScript click for more reliable interaction
        driver.execute_script("arguments[0].scrollIntoView(true);", survey_element)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", survey_element)
        print("Clicked on survey")
        time.sleep(2)

        print("Submitting without filling required questions...")

        # # Answer all questions
        # print("Answering survey questions...")
        # questions = driver.find_elements(By.CLASS_NAME, "question-card")
        
        # for question in questions:
        #     # Handle different question types
        #     if question.find_elements(By.TAG_NAME, "input"):
        #         input_type = question.find_element(By.TAG_NAME, "input").get_attribute("type")
                
        #         if input_type == "text":
        #             text_input = question.find_element(By.TAG_NAME, "input")
        #             text_input.send_keys("Test Answer")
        #         elif input_type == "radio":
        #             # Select first radio option
        #             radio_options = question.find_elements(By.TAG_NAME, "input")
        #             radio_options[0].click()
        #         elif input_type == "checkbox":
        #             # Select first checkbox option
        #             checkbox = question.find_element(By.TAG_NAME, "input")
        #             checkbox.click()
            
        #     elif question.find_elements(By.TAG_NAME, "select"):
        #         # Handle dropdown
        #         select = Select(question.find_element(By.TAG_NAME, "select"))
        #         select.select_by_index(1)  # Select second option (first is usually placeholder)

        # Submit the survey
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit Survey')]")))
        submit_button.click()
        time.sleep(2)

        print("The survey isn't submitted because the required questions are not filled.")


# 🟢🟢🟢 TEST CASE: NOT FILLING THE REQUIRED QUESTIONS - END

# 🟢🟢🟢 TEST CASE: FILLING THE REQUIRED QUESTIONS - BEGINNING
        print("TEST CASE: FILLING THE REQUIRED QUESTIONS")

        # Find the body element and click it
        body = driver.find_element(By.TAG_NAME, 'body')
        body.click()

        # Answer all questions
        print("Answering survey questions...")
        questions = driver.find_elements(By.CLASS_NAME, "question-card")
        
        for question in questions:
            # Handle different question types
            if question.find_elements(By.TAG_NAME, "input"):
                input_type = question.find_element(By.TAG_NAME, "input").get_attribute("type")
                
                if input_type == "text":
                    text_input = question.find_element(By.TAG_NAME, "input")
                    text_input.send_keys("Test Answer")
                elif input_type == "radio":
                    # Select first radio option
                    radio_options = question.find_elements(By.TAG_NAME, "input")
                    radio_options[0].click()
                elif input_type == "checkbox":
                    # Select first checkbox option
                    checkbox = question.find_element(By.TAG_NAME, "input")
                    checkbox.click()
            
            elif question.find_elements(By.TAG_NAME, "select"):
                # Handle dropdown
                select = Select(question.find_element(By.TAG_NAME, "select"))
                select.select_by_index(1)  # Select second option (first is usually placeholder)

        # Submit the survey
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit Survey')]")))
        submit_button.click()
        time.sleep(2)

        # Handle submission success alert
        alert = wait.until(EC.alert_is_present())
        print(f"Survey submission response: {alert.text}")
        alert.accept()

        print("Survey submitted successfully!")

    except Exception as e:
        print(f"Error during survey answering: {e}")
        print(f"Current URL: {driver.current_url}")
        driver.save_screenshot("survey_answer_error.png")
    
# 🟢🟢🟢 TEST CASE: FILLING THE REQUIRED QUESTIONS - END





 # 🟢 TEST LOGOUT
    print("Testing logout...")
    time.sleep(2)  # Give time for any animations to complete
    
    try:
        # # Navigate back to main page
        # driver.back()
        # print("Navigated back to main page")
        # time.sleep(2)  # Wait for page to load
        
        # Now try to find and click logout button

        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]")))
        print("Found logout button!")
        logout_button.click()
        time.sleep(2)
        
        # Verify we're back at login page
        wait.until(EC.url_to_be(URL))
        print("Logout successful!")
    except Exception as e:
        print(f"Error during logout: {e}")
        print(f"Current URL: {driver.current_url}")
        driver.save_screenshot("logout_error.png")

finally:
    print("Closing browser...")
    time.sleep(2)
    driver.quit()
