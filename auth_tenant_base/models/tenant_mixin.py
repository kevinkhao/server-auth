# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _, fields


class TenantMixin(models.AbstractModel):
    _name = 'tenant.mixin'
    _description = 'Tenant'
    _login_field = None
    _password_hash_field = None
    _backend_name = None

    def sign_in(self, login, pwd_hash):
        tenant = self.search([
            (self._login_field, '=', login),
            (self._password_hash_field, '=', pwd_hash)
        ])
        return tenant

    def sign_up(self, login, pwd_hash, backend_id):
        already_exists = self.search([
            (self._login_field, '=', login)
        ])
        if already_exists:
            raise ValidationError(_("Username already exists"))
        else:
            new_tenant = self.create({
                self._login_field: login,
                self._password_hash_field: pwd_hash,
                "backend_id": backend_id
            })
        return new_tenant
