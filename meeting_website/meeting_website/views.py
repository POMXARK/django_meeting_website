from django.views.generic.base import TemplateResponseMixin, ContextMixin, View


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """

    def get(self, request, *args, **kwargs):
        data = {
            "title_page": "Api",
            "title": "Django Api Docs",
            "table_title": ["#", "Description", "Link"],
            "table_content":
                (
                    ("Регистрация нового участника", "/api/clients/create"),
                    ("Заполнить информацию о пользователе (Включая аватар)", "/admin/members/person/"),
                    ("Авторизация пользователя", "/auth/token/login"),
                    ("Оценить участника (GET запрос , с токеном)", "/api/clients/1/match", "prdfyi4w"),

                    ("Список участников (GET запрос , с токеном)", "/api/list",
                     "vfqr9jvd"),
                    ("Фильтрация по полу", "/api/list/?gender=M",
                     "egxpr1jm"),
                    ("Фильтрация по имени", "/api/list/?last_name=Роман",
                     "w2rqijsy"),
                    ("Фильтрация по фамилии", "/api/list/?last_name=Бушуев",
                     "jt5g4mp6"),
                    ("Люди рядом", "/api/list/?distance=1500",
                     "us9vudl1"),
                    ("Админ панель admin:admin", "/admin/"),

                )

        }
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context=data)


