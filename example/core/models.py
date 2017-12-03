from django.db import models
from djiiif import IIIFField
# Create your models here.



# --------------------------------------------------
# Archive classes
# --------------------------------------------------

class Asset(models.Model, ):
    """
    Represents an sample Asset.
    """

    original = IIIFField(null=True, blank=True, )
