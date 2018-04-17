from django.views.generic import TemplateView


class DevTestView(TemplateView):
    '''A view that simply tests whether Jinja2 is working.'''

    template_name = 'devtestview.html'

    def get_context_data(self, **kwargs):
        context = super(DevTestView, self).get_context_data(**kwargs)
        context['title'] = 'Dev Test View'
        return context
