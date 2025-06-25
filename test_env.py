from dotenv import load_dotenv
import os

load_dotenv()

print("API_KEY =", os.getenv("API_KEY"))
print("API_SECRET =", os.getenv("API_SECRET"))