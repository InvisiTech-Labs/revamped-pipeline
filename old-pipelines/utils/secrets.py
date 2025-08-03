import os

def get_secret():
    return os.getenv("CLIENT_SECRET", "no-secret-found")

if __name__ == "__main__":
    print("v1 secret loaded:", get_secret())
