# Step 1: Import packages
import os
from urllib.request import urlretrieve

# Step 2: Create two variables
week = "week01"
pdf_file_name = "my472-w01-computation-core.pdf"

# Step 3: Build the path
repo_dir = os.path.join(os.path.expanduser("~"), "LSE-MY472-AT26","lse-my472-at26-lectures")
week_dir = os.path.join(repo_dir, week)

# Step 4: Create folder if it does not exist
os.makedirs(week_dir, exist_ok=True)

# Step 5: Build URL from variables
base_url = "https://raw.githubusercontent.com/lse-my472/at26-getting-started/main"
url = base_url + "/" + week + "/" + pdf_file_name

# Step 6: Conditional download
destination = os.path.join(week_dir, pdf_file_name)
if not os.path.exists(destination):
    urlretrieve(url, destination)
    print("Downloaded " + pdf_file_name + " to " + week_dir)
else:
    print(pdf_file_name + " is already in " + week_dir)