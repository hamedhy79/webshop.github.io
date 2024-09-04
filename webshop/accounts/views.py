from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForms, UserLoginForms


# Create your views here.


class UserRegisterView(View):
    form_class = UserRegisterForms
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shop:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['password'])
            return redirect('shop:home')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('shop:home')


class UserLoginView(View):
    form_class = UserLoginForms
    template_name = 'registration/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shop:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                if self.next:
                    return redirect(self.next)
                return redirect('shop:home')
        return render(request, self.template_name, {'form': form})


# from django.contrib.auth import login, authenticate
# from django.contrib.auth import logout
# from django.shortcuts import render, redirect
# from .forms import SignUp
#
#
# def signup(request):
#     form_class = SignUp
#     template_name = 'accounts/signup.html'
#
#     if request.method == 'POST':
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('shop:home')
#     else:
#         form = SignUp()
#     return render(request, 'accounts/signup.html', {'form': form})
#

#
# def login_view(request):
#     def get(request)
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('shop:home')  # redirect to home page
#     return render(request, 'accounts/login.html')
# #
#
# # def signup(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             password = form.cleaned_data.get('password')
# #             user = authenticate(username=username, password=password)
# #             login(request, user)
# #             return redirect('shop')
# #         form = UserCreationForm()
# #     return render(request, 'signup.html', {'form': form})
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('shop:home')
