from entitygraph.api_response import ApiResponse
from entitygraph.base_client import BaseApiClient


class QueryAPI(BaseApiClient):
    def select(self, query: str, repository: str = 'entities', application_label: str = 'default',
               response_mimetype: str = 'text/csv') -> ApiResponse | Exception:
        """
        :param query: SPARQL query. For example: 'SELECT ?entity  ?type WHERE { ?entity a ?type } LIMIT 100'
        :param repository: The repository type in which the query should search: entities, schema, transactions or application
        :param application_label: The application label for which the query should be executed
        :param response_mimetype: text/csv or application/sparql-results+json
        """
        endpoint = "api/query/select"
        params = {'repository': repository}
        headers = {'X-Application': application_label, 'Content-Type': 'text/plain', 'Accept': response_mimetype}
        return self._make_request('POST', endpoint, headers=headers, params=params, data=query)

    def construct(self, query: str, repository: str = 'entities', application_label: str = 'default',
                  response_mimetype: str = 'text/turtle') -> ApiResponse | Exception:
        """
        :param query: SPARQL query. For example: 'CONSTRUCT WHERE { ?s ?p ?o . } LIMIT 100'
        :param repository: The repository type in which the query should search: entities, schema, transactions or application
        :param application_label: The application label for which the query should be executed
        :param response_mimetype: text/turtle or application/ld+json
        """
        endpoint = "api/query/construct"
        params = {'repository': repository}
        headers = {'X-Application': application_label, 'Content-Type': 'text/plain', 'Accept': response_mimetype}
        return self._make_request('POST', endpoint, headers=headers, params=params, data=query)