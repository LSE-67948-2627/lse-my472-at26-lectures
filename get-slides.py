# Step 1: Import packages
import os
from urllib.request import urlretrieve

## The only two lines to change in later weeks
week = "week04"
pdf_file_name = "my472-w04-tabular.pdf"

## Where the file should go
lecture_repo = os.path.expanduser("~/LSE-MY472-AT26/lse-my472-at26-lectures")
week_dir = os.path.join(lecture_repo, week)

if not os.path.exists(week_dir):
  os.mkdir(week_dir)

## Where the file comes from
base_url = "https://raw.githubusercontent.com/lse-my472/at26-lectures/main"
url = base_url + "/" + week + "/" + pdf_file_name
destination = os.path.join(week_dir, pdf_file_name)

## Download only if we do not already have it
if not os.path.exists(destination):
  urlretrieve(url, destination)
  print("Downloaded " + pdf_file_name + " to " + week_dir)
else:
  print(pdf_file_name + " is already in " + week_dir)