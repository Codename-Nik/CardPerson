class MyMixin(object):
    mixin_group = ""

    def get_prop(self):
        return self.mixin_group.upper()

    def get_upper(self, s):
        return s.upper()