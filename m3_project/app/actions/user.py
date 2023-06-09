from json import loads

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from m3.actions.context import ActionContext
from m3_ext.ui import all_components as ext

from objectpack.ui import BaseEditWindow

from objectpack.actions import ObjectPack


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            input_type='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'active status',
            name='is_active',
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            anchor='100%')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'

class UserPack(ObjectPack):

    model = get_user_model()
    add_window = edit_window = UserAddWindow
    add_to_menu = True

    @atomic
    def post_run(
        self: "UserPack",
        _: HttpRequest, 
        context: ActionContext, 
        __: HttpResponse
    ) -> None:
        """
        Пост обработчик действия UserPack, отвечающий за правильное 
        сохранение паролей пользователей.

        TODO:
        - Возможно, избавиться от этого обработчика в угоду более правильного
        подхода к изменению логики сохранения данных о пользователе.
        """
        data: dict = loads(context.json())

        if all((data.get("app.actions.user.UserPack_id", None) is not None, data.get("password"))):
            user = get_user_model().objects.get(username=data["username"])
            
            if not data['password'].startswith("pbkdf2_sha256"):
                user.set_password(data["password"])
                user.save()

