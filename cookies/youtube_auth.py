import os
import time
import logging
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
import warnings

from .cookie_manager import CookieManager

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

class YouTubeAuth:
    def __init__(self):
        self.cookie_manager = CookieManager()
        self.driver = None
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging for the authentication process"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('youtube_auth.log'),
                logging.StreamHandler()
            ]
        )

    def setup_driver(self) -> None:
        """Setup Chrome driver with appropriate options"""
        try:
            options = Options()
            
            # Set user data directory
            user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
            options.add_argument(f"user-data-dir={user_data_dir}")
            
            # Set user agent
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
            
            # Add other options
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            
            # Disable various features
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-background-networking")
            options.add_argument("--disable-component-update")
            options.add_argument("--disable-features=BraveRewards,Shields")
            options.add_argument("--process-per-site")
            options.add_argument("--enable-low-end-device-mode")
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-sync")
            options.add_argument("--disable-dev-shm-usage")
            
            # Additional options to handle errors
            options.add_argument("--disable-logging")
            options.add_argument("--log-level=3")
            options.add_argument("--silent")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            
            # Set up service
            service = Service()
            service.log_path = 'NUL'  # Disable service logging
            
            self.driver = webdriver.Chrome(service=service, options=options)
            logging.info("Chrome driver initialized successfully")
            
        except Exception as e:
            logging.error(f"Failed to initialize Chrome driver: {str(e)}")
            raise

    def wait_for_login(self) -> bool:
        """Wait for user to complete login and verify"""
        try:
            # Wait for YouTube home page to load
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "logo-icon"))
            )
            
            # Check if we're logged in by looking for the avatar
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-masthead #avatar-btn"))
                )
                return True
            except:
                return False
                
        except Exception as e:
            logging.error(f"Error waiting for login: {str(e)}")
            return False

    def authenticate(self, filename: Optional[str] = None) -> str:
        """
        Authenticate with YouTube and save cookies
        
        Args:
            filename: Optional filename to save cookies to
            
        Returns:
            Path to the saved cookie file
        """
        try:
            if not self.driver:
                self.setup_driver()
                
            print(Fore.GREEN + "\n✅ Step 1: Go to the loaded browser page")
            print("✅ Step 2: Log in to your Google account")
            print("✅ Step 3: Return to the terminal\n" + Style.RESET_ALL)
            
            # Navigate to YouTube
            self.driver.get("https://youtube.com")
            
            # Wait for user to log in
            print(Fore.CYAN + "\nWaiting for login... (Press Enter when done)" + Style.RESET_ALL)
            input()
            
            # Verify login
            if not self.wait_for_login():
                raise ValueError("Login verification failed. Please make sure you're properly logged in.")
            
            # Get cookies
            cookies = self.driver.get_cookies()
            
            # Validate cookies
            if not self.cookie_manager.validate_cookies(cookies):
                raise ValueError("Invalid cookies received")
                
            # Save cookies
            cookie_file = self.cookie_manager.save_cookies(cookies, filename)
            
            print(f"\n✅ Cookies saved to: {cookie_file}")
            return cookie_file
            
        except Exception as e:
            logging.error(f"Authentication error: {str(e)}")
            print(f"\n❌ Error: {str(e)}")
            raise
            
        finally:
            if self.driver:
                try:
                    self.driver.quit()
                    logging.info("Chrome driver closed successfully")
                except Exception as e:
                    logging.error(f"Error closing Chrome driver: {str(e)}")

def main():
    auth = YouTubeAuth()
    try:
        filename = input(Fore.CYAN + "\n💾 Enter cookies file name (without .txt extension): " + Style.RESET_ALL)
        if not filename:
            filename = f"youtube_cookies_{int(time.time())}"
            
        cookie_file = auth.authenticate(f"{filename}.txt")
        print(f"\n✅ Authentication successful! Cookies saved to: {cookie_file}")
        
    except Exception as e:
        print(f"\n❌ Authentication failed: {str(e)}")
        logging.error(f"Main process error: {str(e)}")

if __name__ == "__main__":
    main() 