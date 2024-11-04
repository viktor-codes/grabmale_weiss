from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, TextBlock, RichTextBlock
from django.utils.translation import gettext as _

from wagtail.models import Page


class HomePage(Page):

    # Hero Section
    main_title = models.CharField(
        max_length=255, default="", verbose_name=_("Main Title")
    )
    description = RichTextField(default="", verbose_name=_("Description"))
    call_to_action = models.CharField(
        default="", max_length=255, verbose_name=_("Call to Action")
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Image"),
    )

    # Our Services Section
    services = StreamField(
        [
            (
                "service",
                StructBlock(
                    [
                        (
                            "title",
                            TextBlock(required=True, verbose_name=_("Service Title")),
                        ),
                        (
                            "description",
                            RichTextBlock(
                                required=True, verbose_name=_("Service Description")
                            ),
                        ),
                        (
                            "image",
                            ImageChooserBlock(
                                required=False, verbose_name=_("Service Image")
                            ),
                        ),
                    ]
                ),
            )
        ],
        blank=True,
        verbose_name=_("Services"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("main_title", heading=_("Main Title")),
                FieldPanel("description", heading=_("Description")),
                FieldPanel("call_to_action", heading=_("Call to Action")),
                FieldPanel("image", heading=_("Image")),
            ],
            heading=_("Hero Section"),
        ),
        FieldPanel("services", heading=_("Services")),
    ]
