# Auth Service

Small FastAPI-based authentication service used by the Expense Tracker project.  
Provides user sign-up, sign-in, JWT issuance (access + refresh), and simple DB migrations.

## Repo layout (important files)
- [server.py](server.py) — application entrypoint and router registration  
- [src/config/db.py](src/config/db.py) — DB engine, `SessionLocal`, [`src.config.db.get_db`](src/config/db.py), [`src.config.db.Base`](src/config/db.py), [`src.config.db.engine`](src/config/db.py)  
- [src/users/user_model.py](src/users/user_model.py) — SQLAlchemy `User` model (`src.users.user_model.User`)  
- [src/users/user_schema.py](src/users/user_schema.py) — Pydantic schemas: `src.users.user_schema.UserCreate`, `src.users.user_schema.UserLogin`, `src.users.user_schema.AuthResponse`, `src.users.user_schema.UserResponse`  
- [src/users/services/user_auth.py](src/users/services/user_auth.py) — auth logic: `src.users.services.user_auth.sign_up`, `src.users.services.user_auth.sign_in`  
- [src/users/user_routes.py](src/users/user_routes.py) — API routes (signup / signin)  
- [src/users/core/jwt_token.py](src/users/core/jwt_token.py) — JWT helpers: `src.users.core.jwt_token.create_access_token`, `src.users.core.jwt_token.create_refresh_token`  
- [src/users/core/user_password_hash.py](src/users/core/user_password_hash.py) — password hashing and validation: `src.users.core.user_password_hash.get_password_hash`, `src.users.core.user_password_hash.verify_password`, `src.users.core.user_password_hash.is_password_valid`  
- [src/users/core/error_handler.py](src/users/core/error_handler.py) — response formatting helpers: `src.users.core.error_handler.format_error_response`, `src.users.core.error_handler.format_validation_error_response`  
- [src/users/migrations/runner.py](src/users/migrations/runner.py) — migration runner class: `src.users.migrations.runner.MigrationRunner`  
- [src/users/migrations/001_create_users_table.py](src/users/migrations/001_create_users_table.py)  
- [src/users/migrations/002_add_timestamps.py](src/users/migrations/002_add_timestamps.py)

## Requirements
See [requirements.txt](requirements.txt). Install with:

```sh
pip install -r [requirements.txt](http://_vscodecontentref_/0)

Environment variables
Create a .env file at the project root containing DB and JWT settings. The code expects the following variables (names used in src/config/db.py and src/users/core/jwt_token.py):

DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
DB_NAME
JWT_SECRET_KEY
JWT_ALGORITHM (optional, default HS256)
JWT_ACCESS_TOKEN_EXPIRE_MINUTES (optional)
JWT_REFRESH_TOKEN_EXPIRE_DAYS (optional)
Example .env snippet:
DB_USER=postgres
DB_PASSWORD=secret
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=expense_tracker
JWT_SECRET_KEY=supersecretkey
