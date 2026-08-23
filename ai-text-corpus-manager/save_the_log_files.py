import json

social_posts_catalog_backup = dict()
files_log = dict()

print("\n")
try:
    with open("social_posts_catalog_backup.JSON", "w") as file:
        json.dump(social_posts_catalog_backup, file, indent=4, ensure_ascii=False)
except TypeError:
    print("\"social_posts_catalog_backup.JSON\" is not in a JSON format")
else:
    print("\"social_posts_catalog_backup.JSON\" saved successfully")

print("\n")
try:
    with open("files_log.JSON", "w") as file:
        json.dump(files_log, file, indent=4, ensure_ascii=False)
except TypeError:
    print("\"files_log.JSON\" is not in a JSON format")
else:
    print("\"files_log.JSON\" saved successfully")
