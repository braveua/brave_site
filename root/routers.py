class RootRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('nbu'):
            return 'ORA_CR'
        return None

    # def db_for_write(self, model, **hints):
    #     if model._meta.app_label in ('root'):
    #         return 'ora23'
    #     # if model._meta.app_label in ('api'):
    #     #     return 'django'
    #     return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label == 'nbu_currency' or \
    #        obj2._meta.app_label == 'root':
    #        return True
    #     return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if app_label in ('root'):
    #         return db == 'ora23'
    #     # if app_label in ('api',):
    #     #     return db == 'django'
    #     return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'blogs':
            return db == 'default'
        # Добавьте условия для других приложений, если нужно
        return None
