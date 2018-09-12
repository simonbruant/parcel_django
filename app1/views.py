# -*- coding: utf-8 -*-

import os

from django.conf import settings
from django.views.generic import TemplateView

APP1_APP_FILE = ""
app_path = os.path.join(settings.ROOT_DIR, 'app1', 'static', 'app1', 'app')
if os.path.exists(app_path):
    app_static_files = os.listdir(app_path)
    if app_static_files:
        APP1_APP_FILE = [i for i in app_static_files if i.startswith('main.')][0]
        print(APP1_APP_FILE, 'APP FILE')
        

class IndexView(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        app_static_url = 'app1/{}'.format('app')
        context['app_url'] = '{}/{}'.format(app_static_url, APP1_APP_FILE)
        return context
