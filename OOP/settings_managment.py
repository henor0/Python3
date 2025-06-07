from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int = 50

# Create an instance of Settings
settings = Settings(app_name="MyApp", admin_email="admin@example.com")
print(settings)
