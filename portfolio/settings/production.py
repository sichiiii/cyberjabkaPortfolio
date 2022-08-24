from split_settings.tools import include
z

settings = []

base_settings = [
    'components/common.py',
    'components/database_production.py',
    'components/smtp.py'
]
settings.extend(base_settings)
include(*settings)
