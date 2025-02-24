import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lib.pages.basepage import BasePage
from lib.pages.homepage import HomePage
from lib.constants import Constants

def before_all(context):
    driver = set_selenium_driver(context)
    driver.set_page_load_timeout(60)  # Increase the timeout to 60 seconds
    driver.maximize_window()

    context.web_driver = driver
    context.browser = driver  # Ensure context.browser is set correctly
    context.home = HomePage(context)

    contexts = {
        'home': context.home,
    }

    context.all_contexts = contexts

def after_scenario(context, scenario):
    sep = '\n'
    steps = []
    for step in scenario.steps:
        steps.append(str(step).replace('<', '').replace('>', '').capitalize())
    if test_rail_report(context) == 'True':
        validate_scenario(scenario, context, sep.join(steps))
    pass

def after_all(context):
    context.browser.quit()
    return print("===== That's all folks =====")

def after_step(context, step):
    if step.exception is not None:
        context.step_error = step.exception
        context.failed_step = step.name
    if step.status == 'failed':
        context.failed_step = step.name

def validate_scenario(scenario, context, steps):
    if scenario.status.name == 'failed':
        return print('Failed Step: ' + context.failed_step + '\n' + str(context.step_error))

def set_selenium_driver(context):
    env = context.config.userdata.get("driver", "local")
    if env == 'aws':
        driver = set_docker_driver()
    else:
        driver = set_local_driver()
    return driver

def set_local_driver() -> webdriver:
    chromedriver_path = "chromedriver/chromedriver-win64/chromedriver.exe"
    chrome_binary_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Update this path to your Chrome binary

    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"Chromedriver not found: {chromedriver_path}")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.binary_location = chrome_binary_path  # Set the Chrome binary location

    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=chrome_options)

def set_docker_driver() -> webdriver:
    selenium_url = os.environ.get("SELENIUM_URL", "http://0.0.0.0:4444/wd/hub")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('useAutomationExtension', False)

    return webdriver.Remote(
        command_executor=selenium_url,
        desired_capabilities=chrome_options.to_capabilities()
    )

def test_rail_report(context):
    return context.config.userdata["testrail"]
