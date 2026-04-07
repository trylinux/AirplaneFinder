"""Application configuration."""

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")

    # MySQL connection
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_DB = os.environ.get("MYSQL_DB", "airplane_museum_tracker")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination
    RESULTS_PER_PAGE = 20
