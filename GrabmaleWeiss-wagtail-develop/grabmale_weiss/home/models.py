from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, TextBlock, RichTextBlock, CharBlock
from django.utils.translation import gettext_lazy as _
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
    services_section_title = models.CharField(
        max_length=255, default="", verbose_name=_("Services Title")
    )
    services_section_description = RichTextField(
        default="", verbose_name=_("Services Description")
    )
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

    # Features Section
    features_title = models.CharField(
        max_length=255, default="", verbose_name=_("Features Title")
    )
    features_footer_note = models.CharField(
        max_length=255, default="", verbose_name=_("Features Note")
    )

    features_items = StreamField(
        [
            (
                "features_item",
                StructBlock(
                    [
                        (
                            "subtitle",
                            CharBlock(
                                required=True, verbose_name=_("Features Subtitle")
                            ),
                        ),
                        (
                            "features_text",
                            RichTextBlock(
                                required=True, verbose_name=_("Features Text")
                            ),
                        ),
                    ],
                    verbose_name=_("Features Item"),
                ),
            )
        ],
        blank=True,
        verbose_name=_("Features Items"),
    )

    # About Us Section
    about_us_title = models.CharField(
        max_length=255, default="", verbose_name=_("About Us Title")
    )
    about_us_subtitle = models.CharField(
        default="", max_length=255, verbose_name=_("About Us Subtitle")
    )
    about_us_images = StreamField(
        [("image", ImageChooserBlock(required=False, label=_("About Us Image")))],
        blank=True,
        min_num=2,
        max_num=2,
        verbose_name=_("About Us Images"),
    )

    about_us_stories = StreamField(
        [
            (
                "story",
                StructBlock(
                    [
                        (
                            "timeline_date",
                            CharBlock(required=True, verbose_name=_("Timeline Date")),
                        ),
                        (
                            "story_text",
                            RichTextBlock(required=True, verbose_name=_("Story Text")),
                        ),
                    ],
                    verbose_name=_("Story"),
                ),
            )
        ],
        blank=True,
        verbose_name=_("About Us Stories"),
    )

    # Gallery Section
    gallery_title = models.CharField(
        max_length=255, default="", verbose_name=_("Gallery Title")
    )
    gallery_images = StreamField(
        [("image", ImageChooserBlock(required=False, label=_("Gallery Image")))],
        blank=True,
        verbose_name=_("Gallery Images"),
    )

    # Contact Us Section
    phone_number_1 = models.CharField(
        default="", max_length=255, verbose_name=_("Phone Number 1")
    )
    phone_number_2 = models.CharField(
        default="", max_length=255, verbose_name=_("Phone Number 2")
    )
    email = models.EmailField(default="", verbose_name=_("Email"))
    address = models.CharField(default="", max_length=255, verbose_name=_("Address"))

    # Footer Section
    footer_text = RichTextField(default="", verbose_name=_("Footer Text"))
    footer_links = StreamField(
        [
            (
                "link",
                StructBlock(
                    [
                        (
                            "link_text",
                            TextBlock(required=True, verbose_name=_("Link Text")),
                        ),
                    ]
                ),
            ),
        ],
        blank=True,
        verbose_name=_("Footer Links"),
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
        MultiFieldPanel(
            [
                FieldPanel(
                    "services_section_title", heading=_("Services Section Title")
                ),
                FieldPanel(
                    "services_section_description",
                    heading=_("Services Section Description"),
                ),
                FieldPanel("services", heading=_("Services")),
            ],
            heading=_("Our Services Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("features_title", heading=_("Features Title")),
                FieldPanel("features_items", heading=_("Features Items")),
                FieldPanel("features_footer_note", heading=_("Footer Note")),
            ],
            heading=_("Features Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("about_us_title", heading=_("About Us Title")),
                FieldPanel("about_us_subtitle", heading=_("About Us Subtitle")),
                FieldPanel("about_us_images", heading=_("About Us Images")),
                FieldPanel("about_us_stories", heading=_("About Us Stories")),
            ],
            heading=_("About Us Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("gallery_title", heading=_("Gallery Title")),
                FieldPanel("gallery_images", heading=_("Gallery Images")),
            ],
            heading=_("Gallery Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("phone_number_1", heading=_("Phone Number 1")),
                FieldPanel("phone_number_2", heading=_("Phone Number 2")),
                FieldPanel("email", heading=_("Email")),
                FieldPanel("address", heading=_("Address")),
            ],
            heading=_("Contact Us Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("footer_text", heading=_("Footer Text")),
                FieldPanel("footer_links", heading=_("Footer Links")),
            ],
            heading=_("Footer Section"),
        ),
    ]
