from django.contrib.auth.models import Permission

from m3_ext.ui import all_components as ext

from objectpack.ui import BaseEditWindow
from objectpack.actions import ObjectPack

from .content_type import ContentTypePack


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = ext.ExtDictSelectField(
            label=u'content-type',
            name='content_type_id',
            anchor='100%',
            pack=ContentTypePack
        )

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__codename,
            self.field__content_type,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionPack(ObjectPack):

    model = Permission
    add_window = edit_window = PermissionAddWindow
    add_to_menu = True
    add_to_desktop = True

