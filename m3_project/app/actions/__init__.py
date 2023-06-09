from .user import UserPack
from .content_type import ContentTypePack
from .permission import PermissionPack
from .group import GroupPack

action_packs = (UserPack(), ContentTypePack(), PermissionPack(), GroupPack())

__all__ = ('action_packs',)

