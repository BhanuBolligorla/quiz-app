import os
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SECURITY
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-fallback-key")

    # DATABASE URL (SQLite default or external DB)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(basedir, "quiz.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # S3 URL
    S3_BASE_URL = os.environ.get(
        "S3_BASE_URL",
        "https://your-bucket-name.s3.amazonaws.com/"
    )
