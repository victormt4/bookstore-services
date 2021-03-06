from typing import Dict, List
from flask import session
import pickle

from src.purchase.entities import Coupon
from src.purchase.errors import CouponAlreadyActiveError, CouponLimitError
from src.errors import NotFoundError
from src.shared.contracts.repository import Repository


class CouponServices:
    __active_coupons: Dict[str, Coupon]

    def __init__(self, coupon_repo: Repository[Coupon], session_object: session, coupon_limit: int = 1):
        """
        :param Repository[Coupon] coupon_repo: Repo dos coupons
        :param session|dict session_object: objeto da sessão
        :param int coupon_limit: quantidade de coupons ativados ao mesmo tempo
        """
        self.__repo = coupon_repo
        self.__session_object = session_object
        self.__active_coupons = {}
        self.__coupon_limit = coupon_limit
        if 'active_coupons' in session_object:
            self.__active_coupons = pickle.loads(session_object['active_coupons'])

    def get_coupons(self) -> List[Coupon]:
        """
        Retorna uma lista de coupons
        :rtype: List[Coupon]
        """
        return self.__repo.get_all()

    def get_coupon(self, code: str) -> Coupon:
        """
        Busca um coupon pelo código
        :rtype: Coupon
        :raises NotFoundError
        """
        coupons = self.get_coupons()

        for coupon in coupons:
            if coupon.code == code:
                return coupon

        raise NotFoundError(f'Coupon "{code}" not found')

    def activate_coupon(self, code: str):
        """
        Ativa um cupom
        :param code: str Código do cupom
        :raises CouponAlreadyActiveError: Quando o cupom já foi ativo
        :raises NotFoundError
        """
        coupon = self.get_coupon(code)

        if coupon.code in self.__active_coupons:
            raise CouponAlreadyActiveError(f'Coupon "{code}" is already active')

        if len(self.__active_coupons) == self.__coupon_limit:
            raise CouponLimitError(f"Coupon limit exceeded. Max coupons: {self.__coupon_limit}")

        self.__active_coupons[coupon.code] = coupon
        self.__session_object['active_coupons'] = pickle.dumps(self.__active_coupons)

    def get_active_coupons(self):
        """
        Retorna um dicinário de coupons, indexado pelo código do coupon
        :return: Dict[str, Coupon]
        """
        return self.__active_coupons

    def deactivate_coupons(self):
        """
        Desativa todos os coupons ativos
        """
        self.__active_coupons = {}
        self.__session_object['active_coupons'] = pickle.dumps(self.__active_coupons)
