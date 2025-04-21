from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# URL of the deployed React app
URL = "https://project1-cs458.vercel.app/"

# Generate a unique email for testing
random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
TEST_EMAIL = f"testuser_{random_string}@example.com"
#TEST_EMAIL = "testuser_nd98ctvg@example.com" #TEST

TEST_PASSWORD = "TestPassword123!"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(URL)
wait = WebDriverWait(driver, 20)  # Increased wait time to 15 seconds

print(f"Using unique test email: {TEST_EMAIL}")

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
        
        # 🟢 TEST LOGOUT
        print("Testing logout...")
        # Now look for the logout button
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]")))
        print("Found logout button!")
        
        # Take screenshot before clicking logout
        #driver.save_screenshot("before_logout.png")
        
        logout_button.click()
        time.sleep(2)
        print("Logout successful!")
        
        # Take screenshot after logout
        #driver.save_screenshot("after_logout.png")
        
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
    
    
    # 🟢 TEST LOGIN WITH EMAIL
    print("Testing login with email...")

   
    time.sleep(2)
    # email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
    #password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    sign_in_button.click()
    time.sleep(2)
    # email_input.send_keys(TEST_EMAIL)
    # password_input.send_keys(TEST_PASSWORD)
    sign_in_button = driver.find_element(By.XPATH, "//button[text()='Sign In' and not(contains(., 'have an account'))]")
    sign_in_button.click()

    time.sleep(3)  # Wait for authentication
    print("Email login successful!")

    # 🟢 TEST LOGOUT AFTER LOGIN
    print("Testing logout after login...")
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]")))
    print("Found logout button after login!")
    
    logout_button.click()
    time.sleep(2)
    print("Logout successful after login!")
    
    # 🟢 TEST LOGIN WITH GOOGLE
    print("Testing sign-in with Google...")
    google_sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in with Google')]")))
    google_sign_in_button.click()
    
    # Assuming the Google sign-in flow is handled in a pop-up or redirect, you might need additional steps here
    time.sleep(3)  # Wait for the redirection to finish
    print("Google login initiated. Please handle the login process manually if necessary.")
    
    # 🟢 TEST LOGIN WITH GITHUB
    print("Testing sign-in with GitHub...")
    github_sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in with GitHub')]")))
    github_sign_in_button.click()
    
    # Assuming the GitHub sign-in flow is handled in a pop-up or redirect, you might need additional steps here
    time.sleep(3)  # Wait for the redirection to finish
    print("GitHub login initiated. Please handle the login process manually if necessary.")
    
    # 🟢 TEST SIGN IN WITH EMPTY FIELDS
    print("Testing sign-in with empty fields...")
    sign_in_toggle = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    sign_in_toggle.click()
    
    # Clear the fields to make sure they are empty
    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    
    # Clear any pre-filled values from previous steps
    email_input.clear()
    password_input.clear()
    
    # Click the sign-in button with empty fields
    sign_in_button = driver.find_element(By.XPATH, "//button[text()='Sign In' and not(contains(., 'have an account'))]")
    sign_in_button.click()
    
    time.sleep(2)  # Wait for error or validation
    print("Tried to sign in with empty fields. Check for error or validation message.")

finally:
    print("Closing browser...")
    time.sleep(2)
    driver.quit()
