
Module auth_base

class AuthentificableMixin()
    _login_field = None
    _password_field = None

    def sign_in(login, password):
        encrypted_password = enrypt(password)
        record = self.search[(self._login_field, "=", login), (self._password_field, "=", encrypted_password)]


    def sign_up():


    def reset_password():

    def set_password():



Module auth_password_rotation check pas d'ancien hash'


Module auth_password_constraint
  - 12 char
  - majus/minus
  - char speciaux
  - chiffre

voir si y à un module qui te calcule la sécurité du mdp

Module auth_password_expiration

 valide 3 mois


Module auth_jwt


class AbstractBackendMixin()

    jwt_secret_token = fields.Char()

    def verify_token_validity(self):
        return "user-account"

    def generate_token(self, account):
       backend: shopinvader.backend,1
       login: email@example.org

 + route renovellement e tokeb

class AuthService():
    _model_name = None

    def _sign_in()
        return self.collection.generate_token()


    def _sign_out():
        supprimer
        la
        session

    def _reset_password()

    def _sign_up()


class ir_http()

        https: // github.com / OCA / server - auth / blob / 12.0 / auth_api_key / models / ir_http.py





Module shopinvader_jwt

class ShopivaderSignService
    _inherit = "auth.jwt.service"

    @route(/sign_in)
    def sign_in(self):
        self._sign_in

surcharger le controler pour utiliser l'auth_jwt et appeler la method verifify_token_validity

