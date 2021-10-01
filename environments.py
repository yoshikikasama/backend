import os


def get_env():
    os.environ["SENDGRID_API_KEY"] = os.environ.get("SENDGRID_API_KEY", "test")
    return os.environ
