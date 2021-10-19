from flask import session
from flask_restx import Namespace, Resource, fields

from src.catalog.repo.product_repo import ProductRepo
from src.purchase.repo.coupon_repo import CouponRepo
from src.purchase.services.cart_services import CartServices
from src.purchase.services.checkout_services import CheckoutServices
from src.purchase.services.coupon_services import CouponServices
from src.catalog.services.product_services import ProductServices

checkout_endpoints = Namespace('checkout', description='Endpoints para operações do checkout', path='/checkout')

checkout_totals_model = checkout_endpoints.model('CheckoutTotals', {
    'subTotal': fields.Integer(description='Sub-total dos produtos no carrinho em centavos', min=0, attribute='sub_total', example=1000),
    'total': fields.Integer(description='Total dos produtos do carrinho, aplicando descontos/frete', min=0, example=1500),
    'subTotalText': fields.String(description='Sub-total dos produtos formatado em reais', example='R$ 10,00', attribute='sub_total_text'),
    'totalText': fields.String(description='Total dos produtos formatado em reais', example='R$ 15,00', attribute='total_text')

})

checkout_coupon_model = checkout_endpoints.model('CheckoutCoupon', {
    'coupon': fields.String(description='Código do coupon de desconto')
})


class DefaultEndpoint(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._coupon_services = CouponServices(
            CouponRepo(),
            session
        )
        self._checkout_services = CheckoutServices(
            CartServices(
                ProductServices(ProductRepo()),
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
