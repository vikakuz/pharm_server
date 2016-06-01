from __future__ import unicode_literals
from django.db import models


# drug form dictionary
class DrugForm(models.Model):
    value = models.TextField(max_length=50, unique=True)

    def __str__(self):
        return self.value


# pharmacotherapeutic group dictionary
class PharmacotherapeuticGroup(models.Model):
    value = models.TextField(max_length=150, unique=True)

    def __str__(self):
        return self.value


# pharmacy conditions dictionary
class PharmacyConditions(models.Model):
    value = models.TextField(max_length=150, unique=True)

    def __str__(self):
        return self.value


# indicatIndicationsForUseions for use table
class IndicationsForUse(models.Model):
    common_information = models.TextField(null=True)
    for_children = models.TextField()
    for_elderly_people = models.TextField()
    for_pregnant_women = models.TextField()
    for_lactating_mothers = models.TextField()

    def __str__(self):
        return self.common_information + "\nДля детей:\n" + self.for_children \
               + "\nДля пожилых людей:\n" + self.for_elderly_people \
               + "\nДля беременных:\n" + self.for_pregnant_women \
               + "\nДля Кормящих матерей:\n" + self.for_lactating_mothers


# pharmacokinetics table
class Pharmacokinetics(models.Model):
    common_information = models.TextField()
    absorption = models.TextField()
    distribution = models.TextField()
    metabolism = models.TextField()
    breeding = models.TextField()

    def __str__(self):
        return self.common_information + "\nВсасывание:\n" + self.absorption \
               + "\nРаспределение:\n" + self.distribution \
               + "\nМетаболизм:\n" + self.metabolism \
               + "\nВыведение:\n" + self.breeding


# manual table
class Manual(models.Model):
    registration_number = models.TextField(primary_key=True)
    name = models.TextField()
    drug_form = models.ManyToManyField(DrugForm)
    composition = models.TextField()
    description = models.TextField()
    pharmacotherapeutic_group = models.ManyToManyField(PharmacotherapeuticGroup)
    code_ATH = models.TextField(unique=True)
    pharmacodynemics = models.TextField(null=True)
    pharmacokinetics = models.ForeignKey(Pharmacokinetics, null=True)
    indication_for_use = models.ForeignKey(IndicationsForUse)
    contra = models.TextField()
    carefully = models.TextField()
    use_for_pregnancy_lactating = models.TextField()
    dosing = models.TextField()
    extra_effects = models.TextField()
    overdose = models.TextField(null=True)
    with_other_drugs = models.TextField(null=True)
    special_instructions = models.TextField()
    form_edition = models.TextField()
    conditions_saving = models.TextField()
    experation_date = models.TextField(max_length=30)
    pharmacy_conditions = models.ForeignKey(PharmacyConditions)
    owner_of_registration_number = models.TextField()
    manufacturer = models.TextField()
    barcode = models.TextField()

    # def __str__(self):
    #     return "Регистрационный номер:" + self.registration_number \
    #            + "\nНазвание:\n" + self.name \
    #            + "\nЛекарственная форма:\n" + self.drug_form \
    #            + "\nСостав:\n" + self.composition \
    #            + "\nОписание:\n" + self.description \
    #            + "\nФармакотеерапевтическая группа:\n" + self.pharmacotherapeutic_group \
    #            + "\nКод АТХ:\n" + self.code_ATH \
    #            + "\nФармакодинамика:\n" + self.pharmacodynemics \
    #            + "\nФармакокинетика:\n" + self.pharmacokinetics \
    #            + "\nПоказания к применению:\n" + self.indication_for_use \
    #            + "\nПротивопоказания:\n" + self.contra \
    #            + "\nС осторожностью:\n" + self.carefully \
    #            + "\nПрименение при беременности и в перид грудного вскармливания:\n" + self.use_for_pregnancy_lactating \
    #            + "\nСпособ применения и дозы:\n" + self.dosing \
    #            + "\nПобочные действия:\n" + self.extra_effects \
    #            + "\nПередозировка:\n" + self.overdose \
    #            + "\nВзаимодействие с другими лекарственными препаратами:\n" + self.with_other_drugs \
    #            + "\nОсобые указания:\n" + self.special_instructions \
    #            + "\nФорма выпуска:\n" + self.form_edition\
    #            + "\nУсловия хранения:\n" + self.conditions_saving \
    #            + "\nСрок годности:\n" + self.experation_date \
    #            + "\nУсловия отпуска из аптек:\n" + self.pharmacy_conditions \
    #            + "\nВладелец регистрационного удостоверения:\n" + self.owner_of_registration_number \
    #            + "\nПроизводитель:\n" + self.manufacturer
