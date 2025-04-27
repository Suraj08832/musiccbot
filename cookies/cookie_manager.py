import os
import json
import time
from typing import Optional
from pathlib import Path
import logging

class CookieManager:
    def __init__(self, cookies_dir: str = "cookies"):
        self.cookies_dir = Path(cookies_dir)
        self.cookies_dir.mkdir(exist_ok=True)
        self.log_file = self.cookies_dir / "logs.csv"
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging for cookie operations"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )

    def save_cookies(self, cookies: list, filename: Optional[str] = None) -> str:
        """
        Save cookies to a file in Netscape format
        
        Args:
            cookies: List of cookie dictionaries
            filename: Optional filename to save cookies to
            
        Returns:
            Path to the saved cookie file
        """
        if not filename:
            filename = f"cookies_{int(time.time())}.txt"
            
        cookie_file = self.cookies_dir / filename
        
        with open(cookie_file, 'w') as f:
            f.write("# Netscape HTTP Cookie File\n")
            f.write("# This is a generated file! Do not edit.\n\n")
            f.write("# domain  include_subdomains  path  secure  expiration_date  name  value\n")
            
            for cookie in cookies:
                expiry = cookie.get('expiry') or cookie.get('expires') or 0
                f.write(f"{cookie['domain']}\t")
                f.write("TRUE\t")
                f.write(f"{cookie['path']}\t")
                f.write("TRUE\t" if cookie.get('secure') else "FALSE\t")
                f.write(f"{int(expiry)}\t")
                f.write(f"{cookie['name']}\t{cookie['value']}\n")
                
        logging.info(f"Cookies saved to {cookie_file}")
        return str(cookie_file)

    def get_random_cookie_file(self) -> str:
        """
        Get a random cookie file from the cookies directory
        
        Returns:
            Path to a random cookie file
        """
        txt_files = list(self.cookies_dir.glob('*.txt'))
        if not txt_files:
            raise FileNotFoundError("No cookie files found in the cookies directory")
            
        cookie_file = str(txt_files[0])  # Just get the first file for now
        logging.info(f"Selected cookie file: {cookie_file}")
        return cookie_file

    def validate_cookies(self, cookies: list) -> bool:
        """
        Validate that cookies have required fields
        
        Args:
            cookies: List of cookie dictionaries
            
        Returns:
            True if cookies are valid, False otherwise
        """
        required_fields = {'domain', 'path', 'name', 'value'}
        
        for cookie in cookies:
            if not all(field in cookie for field in required_fields):
                return False
                
        return True 