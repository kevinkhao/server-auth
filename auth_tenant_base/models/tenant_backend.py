# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import hmac
import json
from hashlib import sha256

from base64 import urlsafe_b64encode
from odoo import fields, models, _
from odoo.exceptions import ValidationError


class TenantBackendMixin(models.AbstractModel):
    _name = "tenant.backend.mixin"
    _description = "Tenant Backend"

    def sign_in(self, login, password, tenant_model):
        pwd_hash = sha256(password)
        tenant = self.env[tenant_model].sign_in(login, pwd_hash)
        if tenant:
            return tenant
        raise ValidationError(_("Tenant credentials invalid"))

    def sign_up(self, login, password, tenant_model):
        pwd_hash = sha256(password)
        return self.env[tenant_model].sign_up(login, pwd_hash, self.id)

    def reset_password(self, tenant):
        setattr(tenant, tenant._password_hash_field, "")


