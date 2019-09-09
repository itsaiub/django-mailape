from django.conf import settings
from django.urls import reverse
from django.template import Context


class EmailTemplateContext(Context):
    @staticmethod
    def make_link(path):
        return settings.MAILING_LIST_LINK_DOMAIN + path

    def __init__(self, subscriber, dict_=None, **kwargs):
        if dict_ is None:
            dict_ = {}
        email_ctx = self.common_context(subscriber)
        email_ctx.update(dict_)
        super().__init__(email_ctx, **kwargs)

    def common_context(self, subscriber):
        subscriber_pk_kwargs = {'pk': subscriber.id}
        unsubscribe_path = reverse(
            'mailinglist:unsubscribe',
            kwargs=subscriber_pk_kwargs
        )
        return {
            'subscriber': subscriber,
            'mailing_list': subscriber.mailing_list,
            'unsubscriber_link': self.make_link(unsubscribe_path)
        }
