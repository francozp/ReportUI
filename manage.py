#correr XAMPP sudo /opt/lampp/manager-linux-x64.run
#sudo ln -s /opt/lampp/var/mysql/mysql.sock /var/run/mysqld/mysqld.sock --- sudo mkdir -p /var/run/mysqld
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PaReport.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)