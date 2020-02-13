"""Goes through all usernames and collects their information"""
import sys

from util.account import login
from util.chromedriver import SetupBrowserEnvironment
from util.cli_helper import get_all_user_names
from util.datasaver import Datasaver
from util.extractor import extract_information
from util.extractor_posts import InstagramPost
from util.settings import Settings
from post_getter import di_csv_kan
from tqdm import tqdm


Settings.chromedriver_location = '/Users/svmihar/Documents/chromedriver'
Settings.scrape_posts_infos = True
Settings.log_output_toconsole = True

with SetupBrowserEnvironment() as browser:
    usernames = get_all_user_names()
    for username in tqdm(usernames):
        print('Extracting information from ' + username)
        information, user_commented_list = extract_information(browser, username, Settings.limit_amount)
        Datasaver.save_profile_json(username, information.to_dict())
        # print ("Number of users who commented on their profile is ", len(user_commented_list),"\n")

print('convert to csv')
di_csv_kan()
