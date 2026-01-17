# NOTE: This script downloads icons from the Satisfactory Wiki and organizes them into folders.
#
# - The downloaded images remain the copyrighted property of Coffee Stain Studios.
#
# - The use of these images in this community tool is
#   protected under the international convention(s)
#   of fair use for non-commercial purposes.
#
# - This script is intended for personal use only and this script specifically is licensed under the MIT License below.
#
# - Images downloaded by this script very likely should:
#     - Not be included in its repository. (By default are excluded in the .gitignore file.)
#     - Not be redistributed further.
#     - Only be used in local development/personal use.

# MIT LICENSE FOR THIS SCRIPT || https://opensource.org/license/mit/ || download_icons.py
# Copyright (c) 2026 https://github.com/NerArth/SatisfactoryOutputCalculator
# - Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#   associated documentation (the "Software"), to deal in the Software without restriction, including
#   without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#   sell copies of the Software, and to permit persons to whom the Software is furnished to do so.
#
# - The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#   INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
#   AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import requests
import time
import shutil
from tqdm import tqdm

# MediaWiki API endpoint for Satisfactory Wiki
API_URL = "https://satisfactory.wiki.gg/api.php"
CATEGORY_MAP = {
    "Category:Item_icons": "item",
    "Category:Building_icons": "building",
    "Category:Vehicle_icons": "vehicle",
    "Category:Fluid_icons": "fluid",
    "Category:Milestone_icons": "milestone"
}
OUTPUT_DIR = "icons"
HEADERS = {
    "User-Agent": "SatisfactoryIconDownloader/1.0 (Contact: your-email@example.com)"
}

def get_category_members(category):
    """
    Fetches all members (files) of a given category using the MediaWiki API.
    """
    members = []
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": category,
        "cmlimit": "max",
        "format": "json"
    }
    
    while True:
        try:
            response = requests.get(API_URL, params=params, headers=HEADERS).json()
            query = response.get("query", {})
            members.extend(query.get("categorymembers", []))
            
            if "continue" in response:
                params.update(response["continue"])
            else:
                break
        except Exception as e:
            print(f"Error fetching members for {category}: {e}")
            break
            
    return members

def get_image_urls(file_titles):
    """
    Fetches the actual direct URLs for a list of File: titles.
    Queries in batches of 50 for efficiency.
    """
    urls = {}
    for i in range(0, len(file_titles), 50):
        batch = file_titles[i:i+50]
        params = {
            "action": "query",
            "titles": "|".join(batch),
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json"
        }
        try:
            response = requests.get(API_URL, params=params, headers=HEADERS).json()
            pages = response.get("query", {}).get("pages", {})
            for page_id in pages:
                page = pages[page_id]
                title = page.get("title")
                image_info = page.get("imageinfo", [])
                if image_info:
                    urls[title] = image_info[0].get("url")
        except Exception as e:
            print(f"Error fetching URLs for batch starting with {batch[0]}: {e}")
            
    return urls

def download_image(url, filename):
    """
    Downloads an image from a URL and saves it to a file.
    """
    try:
        response = requests.get(url, stream=True, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(4096):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return False

def sanitize_filename(title):
    filename = title.replace("File:", "")
    # Sanitize filename (basic)
    return filename.replace("/", "_").replace("\\", "_")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    # Ensure category folders exist
    for folder in CATEGORY_MAP.values():
        os.makedirs(os.path.join(OUTPUT_DIR, folder), exist_ok=True)

    file_to_category = {}
    
    print("Collecting file names from categories...")
    for category, folder in CATEGORY_MAP.items():
        print(f" - Scanning {category}...")
        members = get_category_members(category)
        for m in members:
            title = m['title']
            if title.startswith("File:"):
                # If a file is in multiple categories, it will stay in the folder of the LAST category scanned
                # or we could make it a list logic, but usually items are distinct enough.
                file_to_category[title] = folder
    
    print(f"Total unique icons found: {len(file_to_category)}")

    # Step 1: Move existing files from root to subfolders if they belong there
    print("Organizing existing files into category folders...")
    for title, folder in file_to_category.items():
        filename = sanitize_filename(title)
        root_path = os.path.join(OUTPUT_DIR, filename)
        target_path = os.path.join(OUTPUT_DIR, folder, filename)
        
        if os.path.exists(root_path):
            if not os.path.exists(target_path):
                shutil.move(root_path, target_path)
            else:
                os.remove(root_path) # Already exists in target, just clean up root

    # Convert to list for processing
    file_titles_list = list(file_to_category.keys())
    
    print("Fetching direct image URLs...")
    image_urls = get_image_urls(file_titles_list)
    
    successful = 0
    failed = 0
    skipped = 0

    pbar = tqdm(file_titles_list, desc="Downloading icons")
    for title in pbar:
        filename = sanitize_filename(title)
        folder = file_to_category[title]
        filepath = os.path.join(OUTPUT_DIR, folder, filename)
        
        # Check if already downloaded in the correct folder
        if os.path.exists(filepath):
            skipped += 1
            pbar.set_postfix({"skipped": skipped})
            continue

        url = image_urls.get(title)
        if url:
            if download_image(url, filepath):
                successful += 1
            else:
                failed += 1
        else:
            failed += 1
        
        pbar.set_postfix({"success": successful, "failed": failed, "skipped": skipped})
        
        # Polite delay
        time.sleep(0.02)

    print(f"\nIcons download process complete.")
    print(f"Success: {successful}")
    print(f"Failed:  {failed}")
    print(f"Skipped: {skipped}")
    print(f"Files are organized in: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()
