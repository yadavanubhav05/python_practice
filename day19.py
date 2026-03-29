# import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Script started")
# logging.info("Low memory")
# logging.info("Something failed")

# import logging

# logging.basicConfig(level=logging.INFO)

# values = [10, 20, "abc"]

# for v in values:
#     try:
#         num = int(v)
#         logging.info(f"Processed {num}")
#     except ValueError:
#         logging.error(f"Invalid value: {v}")

import logging
import requests

logging.basicConfig(level=logging.INFO)

res = requests.get("https://api.github.com")

logging.info(f"Status code: {res.status_code}")
