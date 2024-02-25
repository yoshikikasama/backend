# Role Back処理の例

from django.db import migrations


def migrate_address_data(apps, schema_editor):
    """
    user.addressをaddress.addressにデータ移行する
    """
    User = apps.get_model("account", "User")
    Address = apps.get_model("account", "Address")
    for user in User.objects.all():
        Address.objects.create(
            user=user,
            address=user.address,
        )


def reverse_address_data(apps, schema_editor):
    """
    address.addressをuser.addressに戻す
    """
    Address = apps.get_model("account", "Address")
    for address in Address.objects.all():
        user = address.user
        user.address = address.address
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_address"),
    ]
    operations = [
        # データマイグレーション
        migrations.RunPython(
            migrate_address_data, reverse_code=reverse_address_data
        ),
    ]
