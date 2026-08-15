import json

social_posts_catalog_backup = dict()

print("\n")
try:
    with open("social_posts_catalog_backup.JSON","w") as file:
        json.dump(social_posts_catalog_backup, file, indent=4, ensure_ascii=False)
except FileExistsError:
    print("\"social_posts_catalog_backup.JSON\" already exists")
except TypeError:
    print("\"social_posts_catalog_backup.JSON\" is not in a JSON format")
else:
    print("\"social_posts_catalog_backup.JSON\" saved successfully")


print("\n")
try:
    with open("files_log.JSON","w") as file:
        json.dump(social_posts_catalog_backup, file, indent=4, ensure_ascii=False)
except FileExistsError:
    print("\"files_log.JSON\" already exists")
except TypeError:
    print("\"files_log.JSON\" is not in a JSON format")
else:
    print("\"files_log.JSON\" saved successfully")