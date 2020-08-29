# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from hashlib import sha256

from odoo import models, _
from odoo.exceptions import ValidationError


class TenantMixin(models.AbstractModel):
    _name = 'tenant.mixin'
    _description = 'Tenant'

    _login_field = None
    _password_hash_field = None

    def sign_in(self, login, password):
        pwd_hash = sha256(password)
        tenant = self.search([(self._login_field, '=', login), (self._login_password_field, '=', pwd_hash)])
        return tenant

    def sign_up(self, login, password):
        already_exists = self.search([(self._login_field, '=', login)])
        if already_exists:
            raise ValidationError(_("Username already exists"))
        else:
            new_tenant = self.create({
                self._login_field: login,
                self._password_hash_field: sha256(password),
            })
        return new_tenant

    def reset_password(self, tenant):
        setattr(tenant, tenant._password_hash_field, "")
