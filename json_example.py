import json
# We can load our JSON file into a variable called "data”
with open("json_example.json") as f:
  data = f.read()
# json_dict is a dictionary, and json.loads takes care of
# placing our JSON data into it.
json_dict = json.loads(data)
#print(json_dict)
for i in range(1):
  for key, value in json_dict["interface"]["ipv4"]["address"][i].items():
    print("{0}:{1}".format(str(key),str(value)))
