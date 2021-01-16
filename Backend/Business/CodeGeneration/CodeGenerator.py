import os
import re
import string

from IntelligentModels.ModelHelper import ModelHelper
from Business.Wordnet.WordnetRelationFinder import WordnetRelationFinder
from Business.Wikipedia.WikipediaInformationExtractor import WikipediaInformationExtractor


class CodeGenerator:
    def __init__(self, language="Python"):
        self.lang_file = {"Python": ".py"}
        self.type_default = {"int": 0, "string": "\"\"", "float": 0.0, "double": 0.0, "None": None, "bool": False}

        self.language = language
        self.file_type = self.lang_file[language]
        self.model_helper = ModelHelper()

        self.wordnet = WordnetRelationFinder()
        self.wiki = WikipediaInformationExtractor()

        self.printable = set(string.printable)

        self.repo_template = open("./Business/CodeGeneration/Utils/Templates/Repository.txt", "r").read()
        self.service_template = open("./Business/CodeGeneration/Utils/Templates/Service.txt", "r").read()
        self.class_template = open("./Business/CodeGeneration/Utils/Templates/Class.txt", "r").read()
        self.function_template = open("./Business/CodeGeneration/Utils/Templates/Function.txt", "r").read()
        self.import_template = open("./Business/CodeGeneration/Utils/Templates/Import.txt", "r").read()
        self.flask_app_template = open("./Business/CodeGeneration/Utils/Templates/Flask_app.txt", "r").read()
        self.flask_crud_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD.txt", "r").read()
        self.flask_routes_template = open("./Business/CodeGeneration/Utils/Templates/Flask_routes.txt", "r").read()
        self.init_template = open("./Business/CodeGeneration/Utils/Templates/Init.txt", "r").read()
        self.serializer_template = open("./Business/CodeGeneration/Utils/Templates/Serializer.txt", "r").read()
        self.getter_template = open("./Business/CodeGeneration/Utils/Templates/Getter.txt", "r").read()
        self.setter_template = open("./Business/CodeGeneration/Utils/Templates/Setter.txt", "r").read()
        self.add_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD_add.txt", "r").read()
        self.delete_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD_delete.txt", "r").read()
        self.update_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD_update.txt", "r").read()
        self.find_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD_find.txt", "r").read()
        self.size_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD_size.txt", "r").read()
        self.get_template = open("./Business/CodeGeneration/Utils/Templates/Flask_CRUD_get.txt", "r").read()
        self.param_check_template = open("./Business/CodeGeneration/Utils/Templates/Flask_param_check.txt", "r").read()
        self.instantiate_template = open("./Business/CodeGeneration/Utils/Templates/Instantiation.txt", "r").read()

    def get_row_type(self, row):
        if re.search(".+\(.*\).*", row):
            return "fun"

        return "par"

    def generate_code(self, classes, output_folder):
        output_folder, import_folder, flask_folder = self.create_output_folder(output_folder)

        correct = True
        error = ""

        for doodle in classes:
            print(doodle)
            doodle = doodle.capitalize()

            extra_classes = self.wordnet.get_hyponyms(doodle)

            rows = ["description:String"]

            (correct, error), (domain_folder, extra_extra_classes, info) = \
                self.create_domain(doodle, "", rows, output_folder, import_folder)

            self.generate_json(doodle, info, output_folder)

            if not correct:
                break

            extra_classes += extra_extra_classes

            import_path = import_folder + ".Domain"

            classes = {"Domain": [(doodle, info)]}

            repo, repo_folder = self.generate_repository(doodle, output_folder, import_path)

            classes["Repository"] = [repo]

            for extraa in extra_classes:
                extra = self.get_class_name_from_wn(extraa)
                (correct, error), (domain_folder, extra_extra_classes, info) = \
                    self.create_domain(extra, doodle, rows, output_folder, import_folder)
                self.generate_json(extraa, info, output_folder)
                repo, _ = self.generate_repository(extra, output_folder, import_path)
                classes["Repository"].append(repo)
                classes["Domain"].append((extra, []))

            service, service_folder = self.generate_service(doodle, info, output_folder, import_path)

            classes["Service"] = [service]

            for extra in extra_classes:
                service, _ = self.generate_service(self.get_class_name_from_wn(extra), [], output_folder, import_path)
                classes["Service"].append(service)

            folders = {"Repository": "Classes.Repository", "Service": "Classes.Service",
                       "Domain": "Classes.Domain", "Flask": flask_folder}

            self.create_flask_files(folders, classes)

        return correct, error

    def get_class_name_from_wn(self, name):
        split = re.split("_|-| ", name)
        split = [x.capitalize() for x in split]
        name = "".join(split)
        return name

    def create_json_folder(self, output_folder):
        json_folder = output_folder + "/Data/"
        if not os.path.exists(json_folder):
            os.mkdir(json_folder)

        json_folder += "JSON/"

        if not os.path.exists(json_folder):
            os.mkdir(json_folder)

        return json_folder

    def generate_json(self, name, info, output_folder):
        json_folder = self.create_json_folder(output_folder)

        output_file = open(json_folder + name + "_test_json.json", "w+")
        json_string = "[\n\t"
        for desc in [''.join(filter(lambda x: x in self.printable,
                                    self.wordnet.get_definition(name).replace("\n", " "))),
                     ''.join(filter(lambda x: x in self.printable,
                                    self.wiki.get_page_summary(name).replace("\n", " "))), ""]:
            json_string += self.get_json_for_object(info, desc)
            json_string += ",\n\t"

        json_string = json_string[:-3] + "\n]"
        output_file.write(json_string)
        output_file.close()

    def get_json_for_object(self, param_info, desc):
        try:
            json_string = "{\n\t\t"
            json_string += self.get_json_for_params(param_info, desc)
            json_string = json_string[:-5] + "\n\t}"
            return json_string
        except:
            return ""

    def get_json_for_params(self, info, desc):
        json_string = ""
        for (access, name, param_type) in info:
            json_string = json_string + "\"" + name + "\": \""
            if param_type == "string":
                json_string += desc
            else:
                json_string += self.type_default[param_type]
            json_string += "\",\n\t\t\t"
        return json_string

    def create_flask_files(self, folders, classes):
        self.create_flask_init(folders, classes)
        self.create_flask_routes(folders, classes)

    def create_flask_init(self, folders, classes):
        service_folder = folders["Service"]
        repo_folder = folders["Repository"]
        flask_folder = folders["Flask"]

        import_text = ""
        create_text = ""

        for repo in classes["Repository"]:
            import_text = import_text + self.import_template.format(repo_folder + "." + repo, repo) + '\n'

        for service in classes["Service"]:
            import_text = import_text + self.import_template.format(service_folder + "." + service, service) + '\n'

        for (domain, params) in classes["Domain"]:
            repo_name = domain.lower() + "Repo"
            create_text = create_text + repo_name + " = " + domain.capitalize() + "Repository()\n"
            create_text = create_text + domain.lower() + "Service = " + \
                          domain.capitalize() + "Service(" + repo_name + ")\n"

        init_text = self.flask_app_template.format(import_text, create_text)
        init_file = open(flask_folder + "/__init__.py", "w+")
        init_file.write(init_text)
        init_file.close()

    def create_flask_routes(self, folders, classes):
        # service_folder = folders["Service"]
        # repo_folder = folders["Repository"]
        domain_folder = folders["Domain"]
        flask_folder = folders["Flask"]

        domain_import_text = ""
        imported = ""
        crud_text = ""

        for (domain, params) in classes["Domain"]:
            lowered = domain.lower()
            service = lowered + "Service"
            imported = imported + service + ", "

            domain_import_text = domain_import_text + \
                                 self.import_template.format(domain_folder + "." + domain, domain) + '\n'

            params_check = ""
            params_call = ""

            for par in params:
                param_name = "\"" + par[1] + "\""
                if par[2] in self.type_default:
                    param_type = self.type_default[par[2]]
                else:
                    param_type = par[2].capitalize() + "()"
                params_check = params_check + \
                               "\n    " + self.param_check_template.format(param_name, par[1],
                                                                           param_name, par[1], param_type) + '\n'
                params_call = params_call + par[1] + ", "

            params_call = params_call[:-2]

            add_text = self.add_template.format(lowered, lowered, params_check, service, params_call)
            delete_text = self.delete_template.format(lowered, lowered, params_check, service, params_call)
            update_text = self.update_template.format(lowered, lowered, params_check, service, params_call)
            get_text = self.get_template.format(lowered, lowered, service)
            size_text = self.size_template.format(lowered, lowered, service)
            find_text = self.find_template.format(lowered, lowered, params_check, service, params_call)

            crud_text = crud_text + \
                        self.flask_crud_template.format(add_text, update_text,
                                                        delete_text, find_text, get_text, size_text) + '\n\n\n'

        init_import_text = self.import_template.format("app", imported[:-2])

        crud_text = crud_text[:-2]

        routes_text = self.flask_routes_template.format(init_import_text, domain_import_text, crud_text)
        routes_file = open(flask_folder + "/routes.py", "w+")
        routes_file.write(routes_text)
        routes_file.close()

    def create_output_folder(self, output_folder):
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        flask_folder = output_folder + "/app"

        if not os.path.exists(flask_folder):
            os.mkdir(flask_folder)

        output_folder += "/Classes"

        import_folder = "Classes"

        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        return output_folder, import_folder, flask_folder

    def create_domain(self, doodle, parent_class, rows, output_folder, import_folder):
        domain_folder = output_folder + "/Domain"

        if not os.path.exists(domain_folder):
            os.mkdir(domain_folder)

        doodle_file_path = domain_folder + "/" + doodle + ".py"

        parameters = []
        functions = []
        classes = []

        for row in rows:
            row_type = self.get_row_type(row)
            if row_type == "par":
                parameters.append(row)
            elif row_type == "fun":
                functions.append(row)
            else:
                return (False, "Row type could not be inferred - " + row + " - not parameter nor function"), \
                       ("", [], [])

        functions_text = ""
        getters_and_setters_text = ""

        if len(parameters) == 0:
            init_text = self.init_template.format("", "    pass")
            info = []
            extra_classes = []
        else:
            init_text, info, extra_classes = self.get_parameter_text_and_info(parameters)

        classes += extra_classes

        text = self.get_getters_setters_text(info)
        if text:
            getters_and_setters_text = text

        text, extra_classes = self.get_function_text(functions)
        if text:
            functions_text = text

        classes += extra_classes

        extra_text = ""

        for extra_class in classes:
            extra_text = extra_text + self.import_template.format(import_folder + ".Domain." +
                                                                  extra_class, extra_class) + '\n'

            self.create_extra_class(extra_class, domain_folder)

        if parent_class != "":
            extra_text += self.import_template.format(import_folder + ".Domain." +
                                                      parent_class, parent_class) + '\n'

        serializer_text = self.get_serializer_text(info)

        doodle_file_text = self.class_template.format(extra_text, doodle.capitalize(), parent_class, init_text,
                                                      getters_and_setters_text, functions_text, serializer_text)

        doodle_file = open(doodle_file_path, "w+")
        doodle_file.write(doodle_file_text)
        doodle_file.close()

        return (True, "Everything is ok"), (domain_folder, classes, info)

    def create_extra_class(self, extra_class, domain_folder):
        name = extra_class.strip().capitalize()
        file_path = domain_folder + "/" + name + ".py"
        text = self.class_template.format("", name, "pass", "", "", self.serializer_template.format("{}"))
        file = open(file_path, "w+")
        file.write(text)
        file.close()

    def get_parameter_text_and_info(self, parameters):
        param = ""
        initial = "    "

        params = []
        classes = []
        for par in parameters:
            correct, access, name, param_type = self.get_parameter_info(par)
            if not correct:
                return False
            params.append((access, name, param_type))
            param += ", "
            param += name
            param += "="
            if param_type in self.type_default:
                param += str(self.type_default[param_type])
            else:
                extra_class = param_type.strip().capitalize()
                param += extra_class + "()"
                classes.append(extra_class)

        for (access, name, param_type) in params:
            initial = initial + "self." + access + name + " = " + name + '\n        '

        initial = initial[:-9]

        result = self.init_template.format(param, initial)
        return result, params, classes

    def get_getters_setters_text(self, parameters):
        result = ""
        for param in parameters:
            result += self.get_getter(param)
            result += "\n\n    "
            result += self.get_setter(param)
            result += "\n\n    "

        result = result[:-6]

        return result

    def get_getter(self, parameter):
        result = self.getter_template.format(parameter[1], parameter[0] + parameter[1])
        return result

    def get_setter(self, parameter):
        result = self.setter_template.format(parameter[1], parameter[1], parameter[0] + parameter[1], parameter[1])
        return result

    def get_function_text(self, functions):
        result = ""
        for fun in functions:
            param_text = ""
            correct, access, name, parameters, param_type = self.get_function_info(fun)
            if not correct:
                return False
            for param in parameters:
                param_text = param_text + ", " + param[0] + "=" + str(self.type_default[param[1]])

            fun_text = self.function_template.format(access, name, param_text, self.type_default[param_type])
            result = result + fun_text + "\n\n    "

        result = result[:-5]

        return result, []

    def get_function_info(self, function):
        access_modifier = ""
        if function[0] == "-":
            access_modifier = "__"
            function = function[1:]
        elif function[0] == "*":
            access_modifier = "_"
            function = function[1:]
        elif function[0] == "+":
            function = function[1:]

        return_type = "None"

        parameters = []

        paranth1 = function.find("(")
        paranth2 = function.find(")")

        name = function[:paranth1].strip()
        param_text = function[paranth1 + 1:paranth2].strip()
        return_text = function[paranth2 + 1:].strip()

        if param_text != "":
            if "," in param_text:
                split_params = param_text.split(",")
                for par in split_params:
                    split_par = par.split(":")
                    parameters.append((split_par[0].strip(), split_par[1].strip().lower()))
            else:
                split_par = param_text.split(":")
                parameters.append((split_par[0].strip(), split_par[1].strip().lower()))

        if return_text != "":
            return_type = return_text[1:]

        return True, access_modifier, name, parameters, return_type

    def get_parameter_info(self, parameter):
        access_modifier = ""
        if parameter[0] == "-":
            access_modifier = "__"
            parameter = parameter[1:]
        elif parameter[0] == "*":
            access_modifier = "_"
            parameter = parameter[1:]
        elif parameter[0] == "+":
            parameter = parameter[1:]

        param_type = "None"

        if ":" in parameter:
            split_param = parameter.split(":")
            if len(split_param) != 2:
                return False, False, False, False

            name = split_param[0]
            param_type = split_param[1].strip().lower()
        else:
            name = parameter.strip()

        return True, access_modifier, name, param_type

    def generate_repository(self, name, output_folder, domain_folder):
        repo_text = self.repo_template.format(domain_folder, name, name, name)

        repo_folder_path = output_folder + "/Repository"
        if not os.path.exists(repo_folder_path):
            os.mkdir(repo_folder_path)

        repo_name = name.capitalize() + "Repository"

        repo_file_path = repo_folder_path + "/" + repo_name + ".py"
        repo_file = open(repo_file_path, "w+")
        repo_file.write(repo_text)
        repo_file.close()

        return repo_name, repo_folder_path

    def generate_service(self, name, parameters, output_folder, domain_folder):
        service_name = name.capitalize() + "Service"
        imports = self.import_template.format(domain_folder + "." + name, name)
        params = ""
        constructor = name.capitalize() + "("
        nr_cons = 0

        for param in parameters:
            params = params + ", " + param[1] + "="
            if param[2] in self.type_default:
                params += str(self.type_default[param[2]])
            else:
                extra = param[2].capitalize()
                params = params + extra + "()"
                imports = imports + '\n' + self.import_template.format(domain_folder + "." + extra, extra)

            if nr_cons == 0:
                constructor += param[1]
            else:
                constructor = constructor + ", " + param[1]

            nr_cons += 1

        constructor += ")"

        service_text = self.service_template.format(imports, name,
                                                    params, constructor, params, constructor,
                                                    params, constructor, params, constructor)

        service_folder_path = output_folder + "/Service"
        if not os.path.exists(service_folder_path):
            os.mkdir(service_folder_path)

        service_file_path = service_folder_path + "/" + service_name + ".py"
        service_file = open(service_file_path, "w+")
        service_file.write(service_text)
        service_file.close()

        return service_name, service_folder_path

    def get_serializer_text(self, params):
        param_text = "{"
        for param in params:
            if param[2] in self.type_default:
                param_text = param_text + "\"" + \
                             param[1] + "\"" + ": " + "self." + param[0] + param[1] + ", "
            else:
                param_text = param_text + "\"" + \
                             param[1] + "\"" + ": " + "self." + param[0] + param[1] + ".serialize(), "

        if param_text != "{":
            param_text = param_text[:-2]
        param_text += "}"

        serializer_text = self.serializer_template.format(param_text)
        return serializer_text
