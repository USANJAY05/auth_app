from uvicorn import run
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    run("app:app",host='0.0.0.0',port=os.getenv("PORT"))

if __name__ == '__main__':
    main()