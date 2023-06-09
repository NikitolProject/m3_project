from django.contrib.auth.models import Group

from objectpack.ui import ModelEditWindow
from objectpack.actions import ObjectPack


class GroupPack(ObjectPack):

    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True

