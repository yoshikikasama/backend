import os


def get_env():
    os.environ["SENDGRID_API_KEY"] = os.environ.get("SENDGRID_API_KEY", "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")
    return os.environ

