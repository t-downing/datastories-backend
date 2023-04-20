from django.db import models


class Model(models.Model):
    label = models.CharField()
    default_layout = models.OneToOneField("layout", null=True, blank=True, on_delete=models.SET_NULL, related_name="model_default")

    def __str__(self):
        return f"{self.label} [{self.pk}]"


class Node(models.Model):
    label = models.CharField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.label} [{self.pk}]"


class QualElement(Node):
    pass


class QuantElement(Node):
    pass


class Layout(models.Model):
    label = models.CharField()
    model = models.ForeignKey("model", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.label} [{self.pk}]"


class QualElementPosition(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    element = models.ForeignKey("qualelement", on_delete=models.CASCADE)
    layout = models.ForeignKey("layout", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("element", "layout")


class QuantElementPosition(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    element = models.ForeignKey("quantelement", on_delete=models.CASCADE)
    layout = models.ForeignKey("layout", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("element", "layout")


class Connection(models.Model):
    from_element = models.ForeignKey("qualelement", on_delete=models.CASCADE, related_name="downstream_connections")
    to_element = models.ForeignKey("qualelement", on_delete=models.CASCADE, related_name="upstream_connections")

    class Meta:
        unique_together = ("from_element", "to_element")
