import math

from django.db.models import Avg
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

from .forms import All_knifesForm_step1, All_knifesForm_step2, Grinding_dataForm, Honing_dataForm, RegisterUserForm
from .models import All_knifes


class CalculationView(View):
    def get(self, request):
        return render(request, 'Calculation.html')

    def post(self, request):
        form_grinding = Grinding_dataForm(request.POST)
        form_honing = Honing_dataForm(request.POST)

        if form_honing.is_valid():
            KJ = form_honing.cleaned_data['KJ']
            GA = form_honing.cleaned_data['GA']
            RWH = form_honing.cleaned_data['RW']
            honing_add = form_honing.cleaned_data['honing_add']
            FVB_S = form_honing.cleaned_data['FVB_S']
            C3_C4 = form_honing.cleaned_data['C3_C4']
            C5_C6 = form_honing.cleaned_data['C5_C6']

            AC = math.sqrt((KJ - 6) ** 2 + 11.9 ** 2)
            BAC = math.atan(11.9 / (KJ - 6))
            DC = math.sqrt(RWH ** 2 + AC ** 2 - 2 * RWH * AC * math.cos(math.radians(90 + GA + honing_add) - BAC))
            FC = math.sqrt(DC ** 2 - (C3_C4 + FVB_S) ** 2)
            FVB_H = FC - C5_C6 + 6

            return render(request, 'Calculation.html',
                          context={'KJ': KJ, 'GA': GA, 'RWH': RWH, 'honing_add': honing_add, 'FVB_S': FVB_S,
                                   'C3_C4': C3_C4, 'C5_C6': C5_C6, 'FVB_H': FVB_H})

        elif form_grinding.is_valid():
            KJ = form_grinding.cleaned_data['KJ']
            GA = form_grinding.cleaned_data['GA']
            RWG = form_grinding.cleaned_data['RW']
            C1 = form_grinding.cleaned_data['C1']
            C2 = form_grinding.cleaned_data['C2']

            AC = math.sqrt((KJ - 6) ** 2 + 11.9 ** 2)
            BAC = math.atan(11.9 / (KJ - 6))
            DC = math.sqrt(RWG ** 2 + AC ** 2 - 2 * RWG * AC * math.cos(math.radians(90 + GA) - BAC))
            EC = math.sqrt(DC ** 2 - C1 ** 2)
            USH = EC - C2 + 6

            return render(request, 'Calculation.html',
                          context={'KJ': KJ, 'GA': GA, 'RWG': RWG, 'C1': C1, 'C2': C2, 'USH': USH})

        return render(request, 'Calculation.html')


def main(request):
    return render(request, 'Main.html')


def feedback(request):
    return render(request, 'Calculation.html')


class Choose_the_angleView(View):

    def get(self, request):
        model = All_knifes.objects.all()
        form1 = All_knifesForm_step1()
        form2 = All_knifesForm_step2()

        angle = 0
        honing_add = 0
        return render(request, 'Choose-the-angle.html',
                      context={'model': model, 'form1': form1, 'form2': form2, 'angle': angle, 'honing_add': honing_add,
                               'message_step1': 'make a choose'})

    def post(self, request):

        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        print(num_visits)

        angle = 0
        honing_add = 0

        # проверка на step1

        if request.POST['step'] == 'step1':
            model = All_knifes.objects.all()
            form = All_knifesForm_step1(request.POST)
            if form.is_valid():
                brend = form.cleaned_data['brend']
                series = form.cleaned_data['series']
                steel = form.cleaned_data['steel']

                if All_knifes.objects.filter(brend=brend, series=series, steel=steel):
                    knife = All_knifes.objects.filter(brend=brend, series=series, steel=steel)[
                        0]  # отображаем первый элемент из выбранных
                    return render(request, 'Choose-the-angle.html',
                                  context={'model': model, 'knife': knife, 'angle': angle, 'honing_add': honing_add,
                                           'message_step1': 'look our suggestion or'})

                elif All_knifes.objects.filter(brend=brend, brend__isnull=False):
                    angle = All_knifes.objects.filter(brend=brend).aggregate(Avg('angle'))[
                        'angle__avg']  # среднее значение из выбранных
                    honing_add = All_knifes.objects.filter(brend=brend).aggregate(Avg('honing_add'))[
                        'honing_add__avg']  # среднее значение из выбранных
                    knife = All_knifes.objects.filter(brend=brend)[0]  # отображаем первый элемент из выбранных
                    return render(request, 'Choose-the-angle.html',
                                  context={'model': model, 'knife': knife, 'angle': angle, 'honing_add': honing_add,
                                           'message_step1': 'look our suggestion or'})

                elif All_knifes.objects.filter(steel=steel, steel__isnull=False):
                    angle = All_knifes.objects.filter(steel=steel).aggregate(Avg('angle'))[
                        'angle__avg']  # среднее значение из выбранных
                    honing_add = All_knifes.objects.filter(steel=steel).aggregate(Avg('honing_add'))[
                        'honing_add__avg']  # среднее значение из выбранных
                    knife = All_knifes.objects.filter(steel=steel)[0]  # отображаем первый элемент из выбранных
                    return render(request, 'Choose-the-angle.html',
                                  context={'model': model, 'knife': knife, 'angle': angle, 'honing_add': honing_add,
                                           'message_step1': 'look our suggestion or'})

            return render(request, 'Choose-the-angle.html',
                          context={'model': model, 'angle': angle, 'honing_add': honing_add,
                                   'message_step1': 'Not found, try next step'})

        # проверка step2

        elif request.POST['step'] == 'step2':
            model = All_knifes.objects.all()
            form = All_knifesForm_step2(request.POST)
            angle = 0
            honing_add = 0
            if form.is_valid():
                carbon = form.cleaned_data['carbon']
                add = form.cleaned_data['CrMoV']
                for knife in All_knifes.objects.all():  # если есть 'carbon' и 'CrMoV' - проверка на точное совпадение
                    if knife.carbon == carbon and knife.CrMoV == add:
                        return render(request, 'Choose-the-angle.html',
                                      context={'model': model, 'knife': knife, 'add': add, 'carbon': carbon,
                                               'angle': angle, 'honing_add': honing_add,
                                               'message_step2': 'look our suggestion or'})

                if All_knifes.objects.filter(carbon__exact=carbon):  # проверка на точное совпадение по 'carbon'
                    angle = All_knifes.objects.filter(carbon__exact=carbon).aggregate(Avg('angle'))[
                        'angle__avg']  # среднее значение из выбранных
                    honing_add = All_knifes.objects.filter(carbon__exact=carbon).aggregate(Avg('honing_add'))[
                        'honing_add__avg']  # среднее значение из выбранных
                    return render(request, 'Choose-the-angle.html',
                                  context={'model': model, 'angle': angle, 'honing_add': honing_add,
                                           'carbon': carbon, 'message_step2': 'look our suggestion or'})

                elif All_knifes.objects.filter(carbon__lt=carbon + 0.08,
                                               carbon__gt=carbon - 0.08):  # если не точное совпадение выбирается из интервала
                    angle = All_knifes.objects.filter(carbon__lt=carbon + 0.08, carbon__gt=carbon - 0.08).aggregate(
                        Avg('angle'))['angle__avg']  # среднее значение из выбранных
                    honing_add = \
                        All_knifes.objects.filter(carbon__lt=carbon + 0.08, carbon__gt=carbon - 0.08).aggregate(
                            Avg('honing_add'))['honing_add__avg']  # среднее значение из выбранных
                    return render(request, 'Choose-the-angle.html',
                                  context={'model': model, 'angle': angle, 'honing_add': honing_add, 'carbon': carbon,
                                           'message_step2': 'look our suggestion or'})

                return render(request, 'Choose-the-angle.html',
                              context={'model': model, 'angle': angle, 'honing_add': honing_add, 'add': add,
                                       'carbon': carbon,
                                       'message_step2': 'Not found, try next step'})
        # проверка step3

        elif request.POST['step'] == 'step3':
            model = All_knifes.objects.all()
            if request.POST['category'] == 'low_quality':
                angle = All_knifes.objects.filter(category='low_quality').aggregate(Avg('angle'))[
                    'angle__avg']  # среднее значение из имеющихсях
                honing_add = All_knifes.objects.filter(category='low_quality').aggregate(Avg('honing_add'))[
                    'honing_add__avg']
                return render(request, 'Choose-the-angle.html',
                              context={'model': model, 'low_quality': True, 'angle': angle, 'honing_add': honing_add,
                                       'message_step3': 'look our suggestion'})

            elif request.POST['category'] == 'medium_quality':
                angle = All_knifes.objects.filter(category='medium_quality').aggregate(Avg('angle'))[
                    'angle__avg']  # среднее значение из имеющихсях
                honing_add = All_knifes.objects.filter(category='medium_quality').aggregate(Avg('honing_add'))[
                    'honing_add__avg']
                return render(request, 'Choose-the-angle.html',
                              context={'model': model, 'medium_quality': True, 'angle': angle, 'honing_add': honing_add,
                                       'message_step3': 'look our suggestion'})

            elif request.POST['category'] == 'high_quality':
                angle = All_knifes.objects.filter(category='high_quality').aggregate(Avg('angle'))[
                    'angle__avg']  # среднее значение из имеющихсях
                honing_add = All_knifes.objects.filter(category='high_quality').aggregate(Avg('honing_add'))[
                    'honing_add__avg']
                return render(request, 'Choose-the-angle.html',
                              context={'model': model, 'high_quality': True, 'angle': angle, 'honing_add': honing_add,
                                       'message_step3': 'look our suggestion'})

            elif request.POST['category'] == 'premium_quality':
                angle = All_knifes.objects.filter(category='premium_quality').aggregate(Avg('angle'))[
                    'angle__avg']  # среднее значение из имеющихсях
                honing_add = All_knifes.objects.filter(category='premium_quality').aggregate(Avg('honing_add'))[
                    'honing_add__avg']
                return render(request, 'Choose-the-angle.html',
                              context={'model': model, 'premium_quality': True, 'angle': angle,
                                       'honing_add': honing_add,
                                       'message_step3': 'look our suggestion'})

        return render(request, 'Choose-the-angle.html', context={'model': model})


# class User_loginView(View):
#     def get(self, request):
#         return render(request, 'Login.html')
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['email'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, 'Account-table.html')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#         else:
#             form = LoginForm()
#         return render(request, 'Login.html', {'form': form})


class RegisterFormView(CreateView):
    form_class = RegisterUserForm
    success_url = 'account_table'
    template_name = 'registration/Login.html'

    # def form_valid(self, form):
    #     form.save()
    #     return super(RegisterFormView, self).form_valid(form)
    #
    # def form_invalid(self, form):
    #     return print('not')

def account_table(request):
    return render(request, 'Account-table.html')



