from django.contrib import admin
from django.apps import apps
admin.site.site_header = "API Coran XEN-IT Sarl"
admin.site.site_title = "Administration API CORAN"
admin.site.index_title = "Bienvenue dans l administration "
class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)
models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class,)
    except admin.sites.AlreadyRegistered:
        pass
