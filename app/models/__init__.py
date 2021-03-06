from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Create extensions
db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()
