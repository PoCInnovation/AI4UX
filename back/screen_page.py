import time
from typing import Tuple

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True

def screen_web_page(url: str, size: Tuple[int, int], output: str) -> None:
    """
    Screen a given page
    :param url: page
    :param size: (width, height) of the page
    :param output: file
    """
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    width, height = size

    driver.get(url)
    driver.set_window_size(width, height)  # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot(output)

    driver.close()
    driver.quit()


# Example
if __name__ == "__main__":
    screen_web_page('https://pythonbasics.org', (1920, 1080), 'output.png')
