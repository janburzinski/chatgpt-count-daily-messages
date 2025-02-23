# the project name is wrong haha
# i wanted to count the messages per month

import json
import os
import datetime

script_dir = os.path.dirname(__file__)
c_rel_path = "data/conversations.json"
c_abs_file_path = os.path.join(script_dir,c_rel_path)

count_per_month = [0] * 12

def main():
  with open(c_abs_file_path, mode="r") as f:
    data = json.load(f)
    
  for record in data:
    date = datetime.datetime.fromtimestamp(record["create_time"])
    count_per_month[date.month - 1] += 1
  
  for i,r in enumerate(count_per_month):
    print(f"[{i + 1}] {r}")
 
# i just wanted to see how the conversations.json from the data dump actually looked
# because the downloaded dump looked horrendous
def prettify_json():
  cf_rel_path = "data/f_conversations.json"
  cf_abs_file_path = os.path.join(script_dir,cf_rel_path)
  print(cf_abs_file_path)
  
  with open(c_abs_file_path, mode="r") as file_from, \
       open(cf_abs_file_path, mode="w") as file_to:
         data=file_from.readlines()
         json.dump(data,file_to,indent=4,sort_keys=True)

if __name__ == "__main__":
  main()    