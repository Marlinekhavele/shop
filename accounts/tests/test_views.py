import pytest
import json
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Customer

@pytest.mark.django_db
def test_customer_create(api_client):
    user = User.objects.create_user('michal', 'test@scvconsultants.com', "michalpassword")
    assert User.objects.count() == 1