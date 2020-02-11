import csv
import errno
import json
import datetime
import os
import re
import random
import signal
import time

import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .settings import Settings
from .time_util import sleep
from .time_util import sleep_actual
from util.exceptions import PageNotFound404
from util.instalogger import InstaLogger


def web_adress_navigator(browser, link):
    """Checks and compares current URL of web page and the URL to be navigated and if it is different, it does navigate"""

    try:
        current_url = browser.current_url
    except WebDriverException:
        try:
            current_url = browser.execute_script("return window.location.href")
        except WebDriverException:
            current_url = None

    if current_url is None or current_url != link:
        response = browser.get(link)

        if check_page_title_notfound(browser):
            InstaLogger.logger().error("Failed to get page " + link)
            raise PageNotFound404("Failed to get page " + link)

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "viewport")))


def check_page_title_notfound(browser):
    title = browser.title
    return title.lower().startswith('page not found')


def check_folder(folder):
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return True
