# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import hmac
import json
from base64 import urlsafe_b64encode
from odoo import fields, models, _
from odoo.exceptions import ValidationError


class AbstractBackendMixin(models.AbstractModel):
    _name = "abstract.backend.mixin"
    _description = "Abstract Backend Mixin"

    jwt_secret_token = fields.Char()

    def _get_signature(self, header, payload):
        to_hash = "{}.{}".format(header, payload)
        return hmac.digest(self.jwt_secret_token, to_hash, "sha256")

    def verify_token_validity(self, token):
        split = token.split(".")
        if len(split) != 3:
            raise ValidationError(_("Bad JWT token: incorrect parts lengths"))
        signature = self._get_signature(split[0], split[1])
        if signature != split[2]:
            raise ValidationError(_("Bad JWT token: could not verify signature"))
        return True

    def generate_token(self, tenant):
        backend = "{}{}".format(self._name, self.id)
        login = getattr(tenant, tenant._login_field)
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {"backend": backend, "login": login}
        header_encoded = urlsafe_b64encode(json.dumps(header))
        payload_encoded = urlsafe_b64encode(json.dumps(payload))
        signature = self._get_signature(header_encoded, payload_encoded)
        token = "{}.{}.{}".format(header_encoded, payload_encoded, signature)
        return token
