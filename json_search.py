import re


class jsonsearch:
    __limit: int = 0

    def __init__(self, data_json: dict):
        try:
            # Initialize the JSON data and results list
            if not isinstance(data_json, dict):
                raise ValueError("Input data must be a dictionary")
            self.__json_data = data_json
            self.__results = []
        except Exception as e:
            # Handle initialization errors
            print(f"An error occurred during initialization: {str(e)}")

    def search_value(self, value, limit: int = 0):
        try:
            # Search for a specific value in the JSON data
            # with an optional limit on the number of results
            self.__limit = limit
            self.__results = []
            self.__search(self.__json_data, None, value)
            return self.__results
        except Exception as e:
            # Handle errors in search_value method
            print(f"An error occurred during search_value: {str(e)}")
            return []

    def search_key(self, key: str, limit: int = 0):
        try:
            # Search for a specific key in the JSON data
            # with an optional limit on the number of results
            self.__limit = limit
            self.__results = []
            self.__search(self.__json_data, key, None)
            return self.__results
        except Exception as e:
            # Handle errors in search_key method
            print(f"An error occurred during search_key: {str(e)}")
            return []

    def __search(self, obj, key, value, root: list = None):
        if root is None:
            root = []
        try:
            # Recursively search through the JSON data
            # to find the specified key or value
            if isinstance(obj, (list, dict)):
                for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
                    if self.__limit != 0 and self.__limit <= len(self.__results):
                        return
                    if (value is not None and value == v) or (key is not None and k == key):
                        self.__results.append({'key': k, 'value': v, 'link': root + [k]})
                    if not isinstance(v, str):
                        self.__search(v, key, value, root + [k])
        except Exception as e:
            # Handle errors in __search method
            print(f"An error occurred during search: {str(e)}")

    def find_all(self, regx, limit: int = 0):
        try:
            # Find all occurrences of a pattern in the JSON data
            # with an optional limit on the number of results
            self.__limit = limit
            self.__results = []
            compiled_regex = re.compile(regx)
            self.__findall(self.__json_data, compiled_regex, compiled_regex)
            return self.__results
        except Exception as e:
            # Handle errors in find_all method
            print(f"An error occurred during find_all: {str(e)}")
            return []

    def find_key(self, regx, limit: int = 0):
        try:
            # Find all keys matching a pattern in the JSON data
            # with an optional limit on the number of results
            self.__limit = limit
            self.__results = []
            compiled_regex = re.compile(regx)
            self.__findall(self.__json_data, compiled_regex, None)
            return self.__results
        except Exception as e:
            # Handle errors in find_key method
            print(f"An error occurred during find_key: {str(e)}")
            return []

    def find_value(self, regx, limit: int = 0):
        try:
            # Find all values matching a pattern in the JSON data
            # with an optional limit on the number of results
            self.__limit = limit
            self.__results = []
            compiled_regex = re.compile(regx)
            self.__findall(self.__json_data, None, compiled_regex)
            return self.__results
        except Exception as e:
            # Handle errors in find_value method
            print(f"An error occurred during find_value: {str(e)}")
            return []

    def __findall(self, obj, key, value, root: list = None):
        if root is None:
            root = []
        try:
            # Recursively find all occurrences of a pattern
            # in the keys or values of the JSON data
            if isinstance(obj, (list, dict)):
                for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
                    if self.__limit != 0 and self.__limit <= len(self.__results):
                        return
                    if (isinstance(v, str) and value is not None and value.match(v)) or \
                            (isinstance(k, str) and key is not None and key.match(k)):
                        self.__results.append({'key': k, 'value': v, 'link': root + [k]})
                    self.__findall(v, key, value, root + [k])
        except Exception as e:
            # Handle errors in __findall method
            print(f"An error occurred during findall: {str(e)}")
