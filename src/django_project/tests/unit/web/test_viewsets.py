import os
from pathlib import Path

import django

BASE_DIR = Path(__file__).parents[4]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
os.environ.setdefault("ENV_PATH", "../envs/.env.test")
django.setup()

from unittest.mock import patch

from django.apps import apps
from django.shortcuts import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


def create_custom_client(group_name):
    """create a client user in a specified group and return a client for object for that user"""
    user = baker.make("auth.User", username=f"{group_name}_user")
    group = baker.make("auth.Group", name=group_name)
    user.groups.add(group)
    token = baker.make("authtoken.Token", user=user)
    client = APIClient()
    client.credentials(**dict(HTTP_AUTHORIZATION=f"Token {token.key}"))
    return client


def create_client():
    """create a client without an attached user"""
    client = APIClient()
    return client


class UserSetupMixin:
    def setUp(self):
        self.user = baker.make("auth.User", username="tester_basic")
        self.token = baker.make("authtoken.Token", user=self.user)
        self.client = APIClient()
        self.client.credentials(**dict(HTTP_AUTHORIZATION=f"Token {self.token.key}"))
        self.unauthorized_client = APIClient()


class EventTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the EventViewSet viewset"""

    def setUp(self):
        super(EventTests, self).setUp()
        self.row = baker.make("web.Event")

    def test_event_list_authorized(self):
        """verify that a get request to the event-list endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:event-list")
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_event_list_unauthorized(self):
        """verify that a get request to the event-list endpoint for an unauthorized user returns a 401
        and the row content is not found"""
        url = reverse("rest:event-list")
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_event_post_authorized(self):
        """verify that a post request to the event-list endpoint returns a 200 and the row content is found"""
        url = reverse("rest:event-list")
        model = apps.get_model("web.Event")
        client = create_custom_client("default")
        prepare = baker.prepare("web.Event")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(model.objects.count(), pre_post_row_count)

    def test_event_post_unauthorized(self):
        """verify that a post request to the event-list endpoint returns a 403 and the row content is not found"""
        url = reverse("rest:event-list")
        model = apps.get_model("web.Event")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_event_retrieve_authorized(self):
        """verify that a get request to the event-detail endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:event-detail", args=[getattr(self.row, "pk")])
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], getattr(self.row, "pk"))

    def test_event_retrieve_unauthorized(self):
        """verify that a get request to the event-detail endpoint for an unauthorized user returns a 401 and
        the row content is not found"""
        url = reverse("rest:event-detail", args=[getattr(self.row, "pk")])
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_event_destroy_authorized(self):
        """verify that a delete request to the event-detail endpoint for an authorized user returns a 204 and the
        record is deleted"""
        model = apps.get_model("web.Event")
        url = reverse("rest:event-detail", args=[getattr(self.row, "id")])
        client = create_custom_client("default")
        response = client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.row, model.objects.all())

    def test_event_destroy_unauthorized(self):
        """verify that a delete request to the event-detail endpoint for an unauthorized user returns a 401 and the
        record is not deleted"""
        model = apps.get_model("web.Event")
        url = reverse("rest:event-detail", args=[getattr(self.row, "id")])
        response = self.unauthorized_client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(getattr(self.row, "id"), response.json())
        self.assertEqual(response.json()["detail"], "Authentication credentials were not provided.")
        self.assertIn(self.row, model.objects.all())

    def test_event_patch_authorized(self):
        """verify that a patch request to the event-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:event-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Event")
        client = create_custom_client("default")
        prepare = baker.prepare("web.Event", pk=self.row.pk)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_event_patch_unauthorized(self):
        """verify that a patch request to the event-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:event-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Event")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.patch(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_event_put_authorized(self):
        """verify that a put request to the event-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:event-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Event")
        client = create_custom_client("default")
        prepare = baker.prepare("web.Event")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.put(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_event_put_unauthorized(self):
        """verify that a put request to the event-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:event-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Event")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.put(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)


class PresentationRequestTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the PresentationRequestViewSet viewset"""

    def setUp(self):
        super(PresentationRequestTests, self).setUp()
        self.row = baker.make("web.PresentationRequest")

    def test_presentationrequest_list_authorized(self):
        """verify that a get request to the presentationrequest-list endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:presentationrequest-list")
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_presentationrequest_list_unauthorized(self):
        """verify that a get request to the presentationrequest-list endpoint for an unauthorized user returns a 401
        and the row content is not found"""
        url = reverse("rest:presentationrequest-list")
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_presentationrequest_post_authorized(self):
        """verify that a post request to the presentationrequest-list endpoint returns a 200 and the row content is found"""
        url = reverse("rest:presentationrequest-list")
        model = apps.get_model("web.PresentationRequest")
        client = create_custom_client("default")
        prepare = baker.prepare("web.PresentationRequest")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(model.objects.count(), pre_post_row_count)

    def test_presentationrequest_post_unauthorized(self):
        """verify that a post request to the presentationrequest-list endpoint returns a 403 and the row content is not found"""
        url = reverse("rest:presentationrequest-list")
        model = apps.get_model("web.PresentationRequest")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_presentationrequest_retrieve_authorized(self):
        """verify that a get request to the presentationrequest-detail endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "pk")])
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], getattr(self.row, "pk"))

    def test_presentationrequest_retrieve_unauthorized(self):
        """verify that a get request to the presentationrequest-detail endpoint for an unauthorized user returns a 401 and
        the row content is not found"""
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "pk")])
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_presentationrequest_destroy_authorized(self):
        """verify that a delete request to the presentationrequest-detail endpoint for an authorized user returns a 204 and the
        record is deleted"""
        model = apps.get_model("web.PresentationRequest")
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "id")])
        client = create_custom_client("default")
        response = client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.row, model.objects.all())

    def test_presentationrequest_destroy_unauthorized(self):
        """verify that a delete request to the presentationrequest-detail endpoint for an unauthorized user returns a 401 and the
        record is not deleted"""
        model = apps.get_model("web.PresentationRequest")
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "id")])
        response = self.unauthorized_client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(getattr(self.row, "id"), response.json())
        self.assertEqual(response.json()["detail"], "Authentication credentials were not provided.")
        self.assertIn(self.row, model.objects.all())

    def test_presentationrequest_patch_authorized(self):
        """verify that a patch request to the presentationrequest-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.PresentationRequest")
        client = create_custom_client("default")
        prepare = baker.prepare("web.PresentationRequest", pk=self.row.pk)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_presentationrequest_patch_unauthorized(self):
        """verify that a patch request to the presentationrequest-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.PresentationRequest")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.patch(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_presentationrequest_put_authorized(self):
        """verify that a put request to the presentationrequest-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.PresentationRequest")
        client = create_custom_client("default")
        prepare = baker.prepare("web.PresentationRequest")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.put(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_presentationrequest_put_unauthorized(self):
        """verify that a put request to the presentationrequest-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:presentationrequest-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.PresentationRequest")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.put(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)


class ResourceTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the ResourceViewSet viewset"""

    def setUp(self):
        super(ResourceTests, self).setUp()
        self.row = baker.make("web.Resource")

    def test_resource_list_authorized(self):
        """verify that a get request to the resource-list endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:resource-list")
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_resource_list_unauthorized(self):
        """verify that a get request to the resource-list endpoint for an unauthorized user returns a 401
        and the row content is not found"""
        url = reverse("rest:resource-list")
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_resource_post_authorized(self):
        """verify that a post request to the resource-list endpoint returns a 200 and the row content is found"""
        url = reverse("rest:resource-list")
        model = apps.get_model("web.Resource")
        client = create_custom_client("default")
        category = baker.make("web.ResourceCategory")
        prepare = baker.prepare("web.Resource", category=category, _fill_optional=True)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_")}
        data["category"] = category.pk
        pre_post_row_count = model.objects.count()
        response = client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(model.objects.count(), pre_post_row_count)

    def test_resource_post_unauthorized(self):
        """verify that a post request to the resource-list endpoint returns a 403 and the row content is not found"""
        url = reverse("rest:resource-list")
        model = apps.get_model("web.Resource")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resource_retrieve_authorized(self):
        """verify that a get request to the resource-detail endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:resource-detail", args=[getattr(self.row, "pk")])
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], getattr(self.row, "pk"))

    def test_resource_retrieve_unauthorized(self):
        """verify that a get request to the resource-detail endpoint for an unauthorized user returns a 401 and
        the row content is not found"""
        url = reverse("rest:resource-detail", args=[getattr(self.row, "pk")])
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_resource_destroy_authorized(self):
        """verify that a delete request to the resource-detail endpoint for an authorized user returns a 204 and the
        record is deleted"""
        model = apps.get_model("web.Resource")
        url = reverse("rest:resource-detail", args=[getattr(self.row, "id")])
        client = create_custom_client("default")
        response = client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.row, model.objects.all())

    def test_resource_destroy_unauthorized(self):
        """verify that a delete request to the resource-detail endpoint for an unauthorized user returns a 401 and the
        record is not deleted"""
        model = apps.get_model("web.Resource")
        url = reverse("rest:resource-detail", args=[getattr(self.row, "id")])
        response = self.unauthorized_client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(getattr(self.row, "id"), response.json())
        self.assertEqual(response.json()["detail"], "Authentication credentials were not provided.")
        self.assertIn(self.row, model.objects.all())

    def test_resource_patch_authorized(self):
        """verify that a patch request to the resource-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:resource-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Resource")
        client = create_custom_client("default")
        prepare = baker.prepare("web.Resource", pk=self.row.pk)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resource_patch_unauthorized(self):
        """verify that a patch request to the resource-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:resource-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Resource")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.patch(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resource_put_authorized(self):
        """verify that a put request to the resource-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:resource-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Resource")
        client = create_custom_client("default")
        category = baker.make("web.ResourceCategory")
        prepare = baker.prepare("web.Resource", category=category)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        data["category"] = category.pk
        pre_post_row_count = model.objects.count()
        response = client.put(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resource_put_unauthorized(self):
        """verify that a put request to the resource-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:resource-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.Resource")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.put(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)


class ResourceCategoryTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the ResourceCategoryViewSet viewset"""

    def setUp(self):
        super(ResourceCategoryTests, self).setUp()
        self.row = baker.make("web.ResourceCategory")

    def test_resourcecategory_list_authorized(self):
        """verify that a get request to the resourcecategory-list endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:resourcecategory-list")
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_resourcecategory_list_unauthorized(self):
        """verify that a get request to the resourcecategory-list endpoint for an unauthorized user returns a 401
        and the row content is not found"""
        url = reverse("rest:resourcecategory-list")
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_resourcecategory_post_authorized(self):
        """verify that a post request to the resourcecategory-list endpoint returns a 200 and the row content is found"""
        url = reverse("rest:resourcecategory-list")
        model = apps.get_model("web.ResourceCategory")
        client = create_custom_client("default")
        prepare = baker.prepare("web.ResourceCategory")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(model.objects.count(), pre_post_row_count)

    def test_resourcecategory_post_unauthorized(self):
        """verify that a post request to the resourcecategory-list endpoint returns a 403 and the row content is not found"""
        url = reverse("rest:resourcecategory-list")
        model = apps.get_model("web.ResourceCategory")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resourcecategory_retrieve_authorized(self):
        """verify that a get request to the resourcecategory-detail endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "pk")])
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], getattr(self.row, "pk"))

    def test_resourcecategory_retrieve_unauthorized(self):
        """verify that a get request to the resourcecategory-detail endpoint for an unauthorized user returns a 401 and
        the row content is not found"""
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "pk")])
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_resourcecategory_destroy_authorized(self):
        """verify that a delete request to the resourcecategory-detail endpoint for an authorized user returns a 204 and the
        record is deleted"""
        model = apps.get_model("web.ResourceCategory")
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "id")])
        client = create_custom_client("default")
        response = client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.row, model.objects.all())

    def test_test_resourcecategory_destroy_unauthorized(self):
        """verify that a delete request to the resourcecategory-detail endpoint for an unauthorized user returns a 401 and the
        record is not deleted"""
        model = apps.get_model("web.ResourceCategory")
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "id")])
        response = self.unauthorized_client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(getattr(self.row, "id"), response.json())
        self.assertEqual(response.json()["detail"], "Authentication credentials were not provided.")
        self.assertIn(self.row, model.objects.all())

    def test_resourcecategory_patch_authorized(self):
        """verify that a patch request to the resourcecategory-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.ResourceCategory")
        client = create_custom_client("default")
        prepare = baker.prepare("web.ResourceCategory", pk=self.row.pk)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resourcecategory_patch_unauthorized(self):
        """verify that a patch request to the resourcecategory-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.ResourceCategory")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.patch(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resourcecategory_put_authorized(self):
        """verify that a put request to the resourcecategory-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.ResourceCategory")
        client = create_custom_client("default")
        prepare = baker.prepare("web.ResourceCategory")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.put(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resourcecategory_put_unauthorized(self):
        """verify that a put request to the resourcecategory-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:resourcecategory-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.ResourceCategory")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.put(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_resourcecategory_resources_authorized(self):
        """verify the resourcecategory-resources endpoint returns a 200 and the row content is found"""
        resource = baker.make("web.Resource", category=self.row)
        url = reverse("rest:resourcecategory-resources", args=[getattr(self.row, "pk")])

        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)
        self.assertIn(str(resource), response.content.decode("utf-8"))

    def test_resourcecategory_resources_unauthorized(self):
        """verify the resourcecategory-resources endpoint returns a 403 and the row content is not found"""
        resource = baker.make("web.Resource", category=self.row)
        url = reverse("rest:resourcecategory-resources", args=[getattr(self.row, "pk")])
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(str(resource), response.content.decode("utf-8"))

    def test_resourcecategory_resources_exception(self):
        """verify the resourcecategory-resources endpoint returns a 500"""
        from web.serializers import ResourceSerializer

        with patch.object(ResourceSerializer.Meta, "fields", ["blah"]):
            baker.make("web.Resource", category=self.row)
            url = reverse("rest:resourcecategory-resources", args=[getattr(self.row, "pk")])

            client = create_custom_client("default")
            response = client.get(url, format="json")
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_resourcecategory_resources_no_data(self):
        """verify the resourcecategory-resources endpoint returns a 404 if related data is not available"""
        url = reverse("rest:resourcecategory-resources", args=[getattr(self.row, "pk")])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TopicSuggestionTests(UserSetupMixin, APITestCase):
    """test API endpoints provided by the TopicSuggestionViewSet viewset"""

    def setUp(self):
        super(TopicSuggestionTests, self).setUp()
        self.row = baker.make("web.TopicSuggestion")

    def test_topicsuggestion_list_authorized(self):
        """verify that a get request to the topicsuggestion-list endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:topicsuggestion-list")
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))
        self.assertGreater(len(response.json()["results"]), 0)

    def test_topicsuggestion_list_unauthorized(self):
        """verify that a get request to the topicsuggestion-list endpoint for an unauthorized user returns a 401
        and the row content is not found"""
        url = reverse("rest:topicsuggestion-list")
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_topicsuggestion_post_authorized(self):
        """verify that a post request to the topicsuggestion-list endpoint returns a 200 and the row content is found"""
        url = reverse("rest:topicsuggestion-list")
        model = apps.get_model("web.TopicSuggestion")
        client = create_custom_client("default")
        prepare = baker.prepare("web.TopicSuggestion")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(model.objects.count(), pre_post_row_count)

    def test_topicsuggestion_post_unauthorized(self):
        """verify that a post request to the topicsuggestion-list endpoint returns a 403 and the row content is not found"""
        url = reverse("rest:topicsuggestion-list")
        model = apps.get_model("web.TopicSuggestion")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_topicsuggestion_retrieve_authorized(self):
        """verify that a get request to the topicsuggestion-detail endpoint for an authorized user returns a 200 and
        the row content is found"""
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "pk")])
        client = create_custom_client("default")
        response = client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], getattr(self.row, "pk"))

    def test_topicsuggestion_retrieve_unauthorized(self):
        """verify that a get request to the topicsuggestion-detail endpoint for an unauthorized user returns a 401 and
        the row content is not found"""
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "pk")])
        response = self.unauthorized_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("results", response.json())
        self.assertNotIn(str(getattr(self.row, "pk")), response.content.decode("utf-8"))

    def test_topicsuggestion_destroy_authorized(self):
        """verify that a delete request to the topicsuggestion-detail endpoint for an authorized user returns a 204 and the
        record is deleted"""
        model = apps.get_model("web.TopicSuggestion")
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "id")])
        client = create_custom_client("default")
        response = client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.row, model.objects.all())

    def test_test_topicsuggestion_destroy_unauthorized(self):
        """verify that a delete request to the topicsuggestion-detail endpoint for an unauthorized user returns a 401 and the
        record is not deleted"""
        model = apps.get_model("web.TopicSuggestion")
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "id")])
        response = self.unauthorized_client.delete(url, pk=self.row.pk, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn(getattr(self.row, "id"), response.json())
        self.assertEqual(response.json()["detail"], "Authentication credentials were not provided.")
        self.assertIn(self.row, model.objects.all())

    def test_topicsuggestion_patch_authorized(self):
        """verify that a patch request to the topicsuggestion-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.TopicSuggestion")
        client = create_custom_client("default")
        prepare = baker.prepare("web.TopicSuggestion", pk=self.row.pk)
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_topicsuggestion_patch_unauthorized(self):
        """verify that a patch request to the topicsuggestion-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.TopicSuggestion")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.patch(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_topicsuggestion_put_authorized(self):
        """verify that a put request to the topicsuggestion-detail endpoint for an authorized user returns a 200 and
        the row content is updated"""
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.TopicSuggestion")
        client = create_custom_client("default")
        prepare = baker.prepare("web.TopicSuggestion")
        data = {k: v for k, v in prepare.__dict__.items() if not k.startswith("_") and v}
        pre_post_row_count = model.objects.count()
        response = client.put(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(model.objects.count(), pre_post_row_count)

    def test_topicsuggestion_put_unauthorized(self):
        """verify that a put request to the topicsuggestion-detail endpoint for an unauthorized user returns a 401 and
        the row content is not updated"""
        url = reverse("rest:topicsuggestion-detail", args=[getattr(self.row, "pk")])
        model = apps.get_model("web.TopicSuggestion")
        pre_post_row_count = model.objects.count()
        response = self.unauthorized_client.put(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(model.objects.count(), pre_post_row_count)
