from django.db import migrations
from django.contrib.auth.models import User

def configurar_superusuario(apps, schema_editor):
    username = 'kikeconk'
    email = 'bhaktivan@yahoo.com'
    # 👇 PON AQUÍ LA CONTRASEÑA QUE QUIERAS USAR (Anota bien las mayúsculas o signos)
    nueva_password = 'Miclavei32janer$' 

    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    user.set_password(nueva_password)
    user.is_superuser = True
    user.is_staff = True
    user.save()

def eliminar_superusuario(apps, schema_editor):
    User.objects.filter(username='kikeconk').delete()

class Migration(migrations.Migration):

    dependencies = [
        # Depende directamente de tu última migración registrada
        ('mapas', '0003_alter_mapasocial_coautores'), 
    ]

    operations = [
        migrations.RunPython(configurar_superusuario, reverse_code=eliminar_superusuario),
    ]