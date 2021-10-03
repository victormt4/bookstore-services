from flask import session
from flask_restx import Namespace, Resource, fields

from src.cart.services.cart_services import CartServices
from src.cart.services.checkout_services import CheckoutServices
from src.cart.services.coupon_services import CouponServices
from src.product.services.product_services import ProductServices

checkout_endpoints = Namespace('checkout', description='Endpoints para operações do checkout', path='/checkout')

checkout_totals_model = checkout_endpoints.model('CheckoutTotals', {
    'subTotal': fields.Float(description='Sub-total dos produtos no carrinho', min=0, attribute='sub_total'),
    'total': fields.Float(description='Total dos produtos do carrinho, aplicando descontos/frete', min=0)
})

checkout_coupon_model = checkout_endpoints.model('CheckoutCoupon', {
    'coupon': fields.String(description='Código do coupon de desconto')
})


class DefaultEndpoint(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._coupon_services = CouponServices(
            session
        )
        self._checkout_services = CheckoutServices(
            CartServices(
                ProductServices(),
                session
            ),
            self._coupon_services
        )


@checkout_endpoints.route('/total')
class CheckoutTotal(DefaultEndpoint):
    @checkout_endpoints.doc(description='Calcula os totais do carrinho de compras')
    @checkout_endpoints.marshal_with(checkout_totals_model, description='Objeto com os totais calculados')
    def get(self):
        return self._checkout_services.get_totals()


@checkout_endpoints.route('/coupon')
class CheckoutActivateDiscount(DefaultEndpoint):
    @checkout_endpoints.doc(description='Aplica um coupon de desconto', body=checkout_coupon_model)
    def post(self):
        parser = checkout_endpoints.parser()
        parser.add_argument('coupon', type=str, required=True, location='json')
        args = parser.parse_args()
        self._coupon_services.activate_coupon(args.get('coupon'))
        return {'message': 'Coupon has been activated'}

    @checkout_endpoints.doc(description='Desativa todos os coupons de desconto')
    def delete(self):
        self._coupon_services.deactivate_coupons()
        return {'message': 'All coupons have been deactivated'}
