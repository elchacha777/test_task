from rest_framework.test import APIRequestFactory, APITestCase
from .models import Logger
from .views import check_formula_view

class LoggerTest(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_post_formula(self):
        formula = {'formula': '((A + B) * [C / D])/{W + K}'}
        request = self.factory.post('math-formula/', data=formula, format='json')
        response = check_formula_view(request)
        assert response.data.get('formula') == True
        assert response.status_code == 200


        
