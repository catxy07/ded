from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        if os.environ.get('RENDER'):  # Only on Render
            from django.contrib.auth import get_user_model

            def create_superuser(sender, **kwargs):
                User = get_user_model()
                # Use your actual superuser field
                if not User.objects.filter(is_superadmin=True).exists():
                    User.objects.create_superuser(
                        email="admin@admin.com",
                        username="admin",
                        password="admin123"
                    )
                    print("Superuser created: admin@admin.com / admin123")

            post_migrate.connect(create_superuser, sender=self)
