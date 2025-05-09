 pip install dj-database-url
postgresql://test_db_z75q_user:CMgZ9CqEUbZRHnLX7xq5z06mz0KbdvRZ@dpg-d0epgj15pdvs73au8st0-a.oregon-postgres.render.com/test_db_z75q
 import dj-database-url
 import os
DATABASES ={
 "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
