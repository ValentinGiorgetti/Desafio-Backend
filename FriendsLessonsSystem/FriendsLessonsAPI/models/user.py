from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField()
    friends = models.ManyToManyField("self")

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        for friend in self.friends.all():
            if friend.username == self.username:
                self.friends.remove(friend)
                super(User, self).save(*args, **kwargs)
                raise Exception("No puede agregarse a sí mismo a su lista de amigos")