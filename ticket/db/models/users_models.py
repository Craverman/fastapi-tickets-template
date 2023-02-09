from tortoise import fields, models


class User(models.Model):
    """Model for user."""

    id = fields.IntField(pk=True)
    name = fields.TextField(null=True)

    class Meta:
        table = "users"

    def __str__(self) -> str:
        return str(self.id)
