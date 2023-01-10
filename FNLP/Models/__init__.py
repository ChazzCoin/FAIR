from F import LIST
from F.CLASS import FairClass
from FNLP.Engines import Merge


class BaseModel(FairClass):
    input_models = []
    webpage_models = []

    def add_input_models(self, input_models:list):
        self.input_models = input_models

    def get_content(self, model):
        return self.get_dict("content", model, None)

    def get_date(self, model):
        return self.get_dict("date", model, None)

    def absorb_content_model(self, model):
        cm = model
        for var in cm.get_list_of_variables():
            cm_value = cm.get_attribute(var)
            if var in self.get_list_of_variables():
                self_value = self.get_attribute(var)
                result = None
                # create ignore list, like pid.
                if not cm_value or var in ['pid']:
                    continue
                if str(var).startswith("original_"):
                    continue
                if str(var).startswith("_"):
                    continue
                if str(var).startswith("input"):
                    continue
                if type(cm_value) in [int]:
                    result = int(cm_value) + int(self_value)
                elif type(cm_value) in [list]:
                    result = LIST.flatten(cm_value, self_value)
                elif type(cm_value) in [dict]:
                    result = Merge.add_word_counts(self_value, cm_value)
                self.set_variable(var, result)
            else:
                self.set_variable(var, cm_value)

    """ Import/Export """
    def import_model(self, obj:dict):
        """ Load JSON Model """
        self.fromJson(obj)

    def export_model(self):
        """ Export Model as JSON"""
        return self.toJson(removeNone=True)

    def print_model(self):
        print(self.toJson())