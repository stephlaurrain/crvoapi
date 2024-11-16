# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arrow(models.Model):
    visua_org_id = models.IntegerField(blank=True, null=True)
    visua_dest_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    y_org = models.IntegerField(blank=True, null=True)
    y_dest = models.IntegerField(blank=True, null=True)
    x_org = models.IntegerField(blank=True, null=True)
    x_dest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arrow'


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    type_category = models.CharField(max_length=1, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryObject(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_object'


class Contact(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address_work = models.TextField(blank=True, null=True)
    zip_code_work = models.CharField(max_length=50, blank=True, null=True)
    city_work = models.CharField(max_length=50, blank=True, null=True)
    code_building = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    email_work = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    phone_work = models.CharField(max_length=50, blank=True, null=True)
    phone_cel = models.CharField(max_length=50, blank=True, null=True)
    phone_cel_work = models.CharField(max_length=50, blank=True, null=True)
    phone_fax_work = models.CharField(max_length=50, blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    date_nameday = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=50, blank=True, null=True)
    responsable = models.TextField(blank=True, null=True)
    associate = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    site_web = models.CharField(max_length=250, blank=True, null=True)
    site_web_work = models.CharField(max_length=50, blank=True, null=True)
    schedules_work = models.CharField(max_length=50, blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    is_visua = models.IntegerField(blank=True, null=True)
    is_synch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class ContactProject(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_project'


class Decisional(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    type_decisional = models.CharField(max_length=255, blank=True, null=True)
    scoring = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    solution = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decisional'


class Goal(models.Model):
    abscon = models.TextField(blank=True, null=True)
    formulation = models.TextField(blank=True, null=True)
    measurable = models.TextField(blank=True, null=True)
    resource = models.TextField(blank=True, null=True)
    ecological = models.TextField(blank=True, null=True)
    circumstantial = models.TextField(blank=True, null=True)
    realistic = models.TextField(blank=True, null=True)
    exciting = models.TextField(blank=True, null=True)
    reward = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal'


class Link(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    is_ged = models.IntegerField(blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    is_visua = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link'


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    contain = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    is_visua = models.IntegerField(blank=True, null=True)
    color_back = models.CharField(max_length=255, blank=True, null=True)
    type_note = models.CharField(max_length=255, blank=True, null=True)
    is_rich = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note'


class Param(models.Model):
    node = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    second_key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'param'


class Picture(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    color_back = models.CharField(max_length=255, blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picture'


class Project(models.Model):
    type_projet = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    price_projected = models.FloatField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    is_done = models.IntegerField(blank=True, null=True)
    font = models.CharField(max_length=50, blank=True, null=True)
    color_visua = models.CharField(max_length=255, blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_begin = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    note = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=8, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    is_visua = models.IntegerField(blank=True, null=True)
    is_synch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class Reminder(models.Model):
    reminder = models.IntegerField(blank=True, null=True)
    unit_reminder = models.CharField(max_length=10, blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reminder'


class Sticker(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    contain = models.TextField(blank=True, null=True)
    color_back = models.CharField(max_length=255, blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    color_write = models.CharField(max_length=255, blank=True, null=True)
    font = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sticker'


class TypeCategory(models.Model):
    type_category = models.CharField(max_length=3, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_category'


class TypeProject(models.Model):
    type_project = models.CharField(max_length=2, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_project'


class Visua(models.Model):
    position_x = models.IntegerField(blank=True, null=True)
    position_y = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    note_id = models.IntegerField(blank=True, null=True)
    link_id = models.IntegerField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    sticker_id = models.IntegerField(blank=True, null=True)
    picture_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visua'
