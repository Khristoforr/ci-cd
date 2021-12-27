import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_one_course(api_client, product_factory):
    product = product_factory()
    url = reverse('product-detail', args=[product.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == product.id