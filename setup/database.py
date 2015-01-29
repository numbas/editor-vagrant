# Copy this file to database.py and make the necessary changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'numbas_editor',                      # Or path to database file if using sqlite3.
        'USER': 'numbas',                      # Not used with sqlite3.
        'PASSWORD': 'db',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
