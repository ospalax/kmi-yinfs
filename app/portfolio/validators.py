from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_skill_level(value):
    if (value < 0) or (value > 100):
        raise ValidationError(
            _('%(value) does not hold valid percentage number (0-100)'),
            params={'value': value},
        )

