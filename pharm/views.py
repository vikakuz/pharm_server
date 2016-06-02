from django.shortcuts import render
from django.http import HttpResponse
from .models import Manual
import json
from django.shortcuts import get_list_or_404


def index(request):
    return HttpResponse("Вы находитесь на стартовой странице сервера базы данных лекарственных препаратов.")


def search_detail(request, drug_name):
    # manual = []
    # drug_form = ['Maz', 'Poroshok']
    # manual.append({'one': 1, 'two': 2, 'three': 3, "drug_form": drug_form})
    # print json.dumps(manual)
    # drugs = get_list_or_404(Manual.objects.values(), name=drug_name)
    drugs = Manual.objects.filter(name__startswith=drug_name).select_related('indication_for_use', 'pharmacokinetics', 'pharmacy_conditions').\
        prefetch_related('drug_form__manual_set')
    #result = get_list_or_404(drugs)  # Manual.objects.filter(name__istartswith=drug_name).order_by('name').values())

    manuals = list(drugs.values())
    json_context = dict()

    result = []
    forms = list(drugs.values('drug_form__value'))
    groups = list(drugs.values('pharmacotherapeutic_group__value'))

    # for i in range(len(manuals)):
    #     result.append({'drug': manuals[i], 'drug_form': forms[i], 'groups': groups[i]})
    # for e in Manual.objects.filter(name__startswith=drug_name).values():
    #     json_context.append(e)
    #
    # for e in DrugForm.objects.all().values():
    #     json_context.append(e)

    json_context['manual'] = [d for d in drugs.values()]
    json_context['drug_form'] = [f for f in drugs.values('drug_form__value')]
    json_context['pharmacotherapeutic_group'] = [g for g in drugs.values('pharmacotherapeutic_group__value')]
    result.append({'drugs': json_context})
    return render(request, 'api/search_detail.html', {'drugs': json.dumps(result)})
    # return render(request, 'server_api/search_detail.html', {'drugs': json.dumps(result)})

    # response = "Вы ищете лекарство под названием '%s'.\n"
    # drugs = Manual.objects.values()
    # output = ''  # , '.join([p['value'] for p in drug])
    # drug_form_id = 0
    # for drug in drugs:
    #     if drug['name'] == drug_name:
    #         # output = str(drug)
    #         output.join(str(1))
    #         return HttpResponse(json.dumps(drug), content_type="application/json; encoding=utf-8")  # , ensure_ascii="False")
    #         # drug_form_id = drug[]
    #
    # if output == '':
    #     output = "Данного лекарства не найдено."
    #     return HttpResponse(output)  # response % drug_name)

