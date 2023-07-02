from dataAdapters.jsonAdapter import JsonAdapter


class AdapterFactory:
    @staticmethod
    def get_adapter(type):
        if type == "json":
            return JsonAdapter()
        else:
            raise NotImplementedError("[Adapter Factory] Adapter not found.")