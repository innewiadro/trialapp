from django.contrib.auth.models import User
from django.db.models import CASCADE, Model, OneToOneField, TextField, IntegerField, CharField


COMMENT_AUTHOR = ((0, 'Shipowner'),
                  (1, 'Contractor'))

class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, max_length=5)
    
    contact_number = CharField(max_length=9, blank=True)  
    department = CharField(max_length=200, blank=True)
    title = CharField(max_length=200, blank=True)

    """class Meta:
        permissions = (("designer_field_edit", "Can edit designer comment fields"),
                       ("contractor_field_edit", "Can edit contractor comment fields"),
                       ("shipowner_field_edit", "Can edit shipowner comment fields"),
                       )"""
        
    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)
    
    def __str__(self):
        return self.user.username

    
