# from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
# from django.dispatch import receiver
# from django.conf import settings
# from .models import Subject, LinkWrapper, Link
#
#
#
# @receiver(post_save, sender=Subject)
# def subject_post_save(sender, **kwargs):
#     wrapper = LinkWrapper(title = "Last Year Paper", subject=kwargs['instance'])
#     wrapper.save()