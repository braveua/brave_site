class RootRouter:
    def db_for_read(self, model, **hints):
        print(f"[db_for_read] model={model.__name__}, app_label={model._meta.app_label}")
        if model._meta.app_label in ('nbu'):
            return 'ora23'
        if model._meta.model_name in ('nbucurrency', 'nburate'):
            return 'ora23'
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
