import json

class json_helpers:
    # properties
    json_object = None

    def convert_to_json(v_json, format='False', print_json='False', skip_logging='False'):
        # json.loads() takes in a string and returns a json object.
        # json.dumps() takes in a json object and returns a string.

        if type(v_json) is not dict:
            if type(v_json) is tuple:
                if format.casefold() != 'True'.casefold():
                    print("Not beautifying json")
                    json_object = json.dumps(v_json)
                elif format.casefold() == 'True'.casefold():
                    json_object = json.dumps(v_json, indent=4)
                    type(json_object)
            elif type(v_json) is str:
                if format.casefold() != 'True'.casefold():
                    print("Not beautifying json")
                    json_object = json.dumps(json.loads(v_json))
                elif format.casefold() == 'True'.casefold():
                    json_object = json.dumps(json.loads(v_json), indent=4)
            elif type(v_json) is list:
                if format.casefold() != 'True'.casefold():
                    print("Not beautifying json")
                    json_object = json.dumps(v_json)
                elif format.casefold() == 'True'.casefold():
                    json_object = json.dumps(v_json, indent=4)
        if type(v_json) is dict:
                if format.casefold() != 'True'.casefold():
                    print("Not beautifying json")
                    json_object = json.dumps(v_json)
                elif format.casefold() == 'True'.casefold():
                    json_object = json.dumps(v_json, indent=4)

        if format.casefold() == 'False'.casefold():
            return json.loads(json_object)
        elif format.casefold() == 'True'.casefold():
            if skip_logging != 'True':
                print("##############################################################################################################################")
                print("# NOTE** if saving to variable and calling that variable without a print statement '\\n' will appear after each key and value #")
                print("# To print json with indents directly from function call, add [print_json='True'] as a parameter                             #")
                print("##############################################################################################################################")
            if print_json.casefold() == 'True'.casefold():
                if skip_logging != 'True':
                    print("Format and print_json were both passed as True, beautifying json\n")
                    input("Press enter to continue...")
                    print(json_object)
                    return json_object
                if skip_logging == 'True':
                    print(json_object)
            else:
                if skip_logging != 'True':
                    print('Format was passed as True while print_json was either not passed, or not passed as True.\n')
                return json.loads(json_object)
        elif format.casefold() not in ('False'.casefold(), 'True'.casefold()):
            if skip_logging != 'True':
                print('format not specified, defaulting to json not beautified\n')
            return json.loads(json_object)
            