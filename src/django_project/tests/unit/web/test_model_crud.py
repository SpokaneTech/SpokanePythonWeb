import os
import random
from pathlib import Path

import django
from django.apps import apps
from django.test import TestCase

BASE_DIR = Path(__file__).parents[4]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from model_bakery import baker  # noqa: E402


class EventTests(TestCase):
    """test CRUD operations on Event"""

    def setUp(self):
        self.model = apps.get_model("web", "event")
        self.to_bake = "web.Event"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_description(self):
        """verify description (TextField) can be updated"""
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=["description"]).description
        setattr(row, "description", updated_value)
        row.save()
        self.assertEqual(getattr(row, "description"), updated_value)
        self.assertNotEqual(getattr(row, "description"), original_value)

    def test_update_location(self):
        """verify location (CharField) can be updated"""
        row = self.bake()
        original_value = row.location
        updated_value = baker.prepare(self.to_bake, _fill_optional=["location"]).location
        setattr(row, "location", updated_value)
        row.save()
        self.assertEqual(getattr(row, "location"), updated_value)
        self.assertNotEqual(getattr(row, "location"), original_value)

    def test_update_name(self):
        """verify name (CharField) can be updated"""
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["name"]).name
        setattr(row, "name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "name"), updated_value)
        self.assertNotEqual(getattr(row, "name"), original_value)

    def test_update_url(self):
        """verify url (CharField) can be updated"""
        row = self.bake()
        original_value = row.url
        updated_value = baker.prepare(self.to_bake, _fill_optional=["url"]).url
        setattr(row, "url", updated_value)
        row.save()
        self.assertEqual(getattr(row, "url"), updated_value)
        self.assertNotEqual(getattr(row, "url"), original_value)


class PresentationRequestTests(TestCase):
    """test CRUD operations on PresentationRequest"""

    def setUp(self):
        self.model = apps.get_model("web", "presentationrequest")
        self.to_bake = "web.PresentationRequest"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_description(self):
        """verify description (TextField) can be updated"""
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=["description"]).description
        setattr(row, "description", updated_value)
        row.save()
        self.assertEqual(getattr(row, "description"), updated_value)
        self.assertNotEqual(getattr(row, "description"), original_value)

    def test_update_email(self):
        """verify email (CharField) can be updated"""
        row = self.bake()
        original_value = row.email
        updated_value = baker.prepare(self.to_bake, _fill_optional=["email"]).email
        setattr(row, "email", updated_value)
        row.save()
        self.assertEqual(getattr(row, "email"), updated_value)
        self.assertNotEqual(getattr(row, "email"), original_value)

    def test_update_presenter(self):
        """verify presenter (CharField) can be updated"""
        row = self.bake()
        original_value = row.presenter
        updated_value = baker.prepare(self.to_bake, _fill_optional=["presenter"]).presenter
        setattr(row, "presenter", updated_value)
        row.save()
        self.assertEqual(getattr(row, "presenter"), updated_value)
        self.assertNotEqual(getattr(row, "presenter"), original_value)

    def test_update_skill_level(self):
        """verify skill_level (CharField) can be updated"""
        row = self.bake()
        original_value = row.skill_level
        choices = getattr(self.model.skill_level.field, "choices", None)
        updated_value = random.choice([i[0] for i in choices if original_value not in i])
        setattr(row, "skill_level", updated_value)
        row.save()
        self.assertEqual(getattr(row, "skill_level"), updated_value)
        self.assertNotEqual(getattr(row, "skill_level"), original_value)

    def test_update_title(self):
        """verify title (CharField) can be updated"""
        row = self.bake()
        original_value = row.title
        updated_value = baker.prepare(self.to_bake, _fill_optional=["title"]).title
        setattr(row, "title", updated_value)
        row.save()
        self.assertEqual(getattr(row, "title"), updated_value)
        self.assertNotEqual(getattr(row, "title"), original_value)


class ResourceTests(TestCase):
    """test CRUD operations on Resource"""

    def setUp(self):
        self.model = apps.get_model("web", "resource")
        self.to_bake = "web.Resource"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_category(self):
        """verify category (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.category
        baker.make(self.model.category.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.category.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.category.field.related_model.objects.all())
        setattr(row, "category", updated_value)
        row.save()
        self.assertEqual(getattr(row, "category"), updated_value)
        self.assertNotEqual(getattr(row, "category"), original_value)

    def test_update_description(self):
        """verify description (TextField) can be updated"""
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=["description"]).description
        setattr(row, "description", updated_value)
        row.save()
        self.assertEqual(getattr(row, "description"), updated_value)
        self.assertNotEqual(getattr(row, "description"), original_value)

    def test_update_name(self):
        """verify name (CharField) can be updated"""
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["name"]).name
        setattr(row, "name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "name"), updated_value)
        self.assertNotEqual(getattr(row, "name"), original_value)

    def test_update_url(self):
        """verify url (CharField) can be updated"""
        row = self.bake()
        original_value = row.url
        updated_value = baker.prepare(self.to_bake, _fill_optional=["url"]).url
        setattr(row, "url", updated_value)
        row.save()
        self.assertEqual(getattr(row, "url"), updated_value)
        self.assertNotEqual(getattr(row, "url"), original_value)


class ResourceCategoryTests(TestCase):
    """test CRUD operations on ResourceCategory"""

    def setUp(self):
        self.model = apps.get_model("web", "resourcecategory")
        self.to_bake = "web.ResourceCategory"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_name(self):
        """verify name (CharField) can be updated"""
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["name"]).name
        setattr(row, "name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "name"), updated_value)
        self.assertNotEqual(getattr(row, "name"), original_value)


class TopicSuggestionTests(TestCase):
    """test CRUD operations on TopicSuggestion"""

    def setUp(self):
        self.model = apps.get_model("web", "topicsuggestion")
        self.to_bake = "web.TopicSuggestion"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_description(self):
        """verify description (TextField) can be updated"""
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=["description"]).description
        setattr(row, "description", updated_value)
        row.save()
        self.assertEqual(getattr(row, "description"), updated_value)
        self.assertNotEqual(getattr(row, "description"), original_value)

    def test_update_email(self):
        """verify email (CharField) can be updated"""
        row = self.bake()
        original_value = row.email
        updated_value = baker.prepare(self.to_bake, _fill_optional=["email"]).email
        setattr(row, "email", updated_value)
        row.save()
        self.assertEqual(getattr(row, "email"), updated_value)
        self.assertNotEqual(getattr(row, "email"), original_value)

    def test_update_skill_level(self):
        """verify skill_level (CharField) can be updated"""
        row = self.bake()
        original_value = row.skill_level
        choices = getattr(self.model.skill_level.field, "choices", None)
        updated_value = random.choice([i[0] for i in choices if original_value not in i])
        setattr(row, "skill_level", updated_value)
        row.save()
        self.assertEqual(getattr(row, "skill_level"), updated_value)
        self.assertNotEqual(getattr(row, "skill_level"), original_value)

    def test_update_title(self):
        """verify title (CharField) can be updated"""
        row = self.bake()
        original_value = row.title
        updated_value = baker.prepare(self.to_bake, _fill_optional=["title"]).title
        setattr(row, "title", updated_value)
        row.save()
        self.assertEqual(getattr(row, "title"), updated_value)
        self.assertNotEqual(getattr(row, "title"), original_value)
