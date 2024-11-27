import requests

base_url = 'https://consensium-service-725186917460.europe-west2.run.app'

class ModeratorClient:
    def __init__(self, moderator_token, base_url=base_url):
        self._moderator_token = moderator_token
        self._base_url = base_url
        self._headers = {"Authorization": f"Bearer {self._moderator_token}"}

    def get_next(self, project_id):
        response = requests.get(f"{self._base_url}/projects/{project_id}/predictions/next", headers=self._headers)
        return response.json(), response.status_code

    def feedback(self, project_id, prediction_id, feedback):
        response = requests.post(f"{self._base_url}/projects/{project_id}/predictions/{prediction_id}/feedback", headers=self._headers, json={"feedback": feedback})
        return response.json(), response.status_code


class OwnerClient:
    _owner_token: str
    _base_url: str
    _headers: dict

    def __init__(self, owner_token, base_url=base_url):
        self._owner_token = owner_token
        self._base_url = base_url
        self._headers = {"Authorization": f"Bearer {self._owner_token}"}

    def create_project(self, project: dict):
        response = requests.post(f"{self._base_url}/projects", headers=self._headers, json=project)
        return response.json(), response.status_code

    def update_policy(self, project_id: str, policy_document: str):
        response = requests.put(f"{self._base_url}/projects/{project_id}/policy", headers=self._headers, json={"policy_document": policy_document})
        return response.json(), response.status_code
    
    def add_predictor(self, project_id: str, predictor_ids: list[str]):
        response = requests.put(f"{self._base_url}/projects/{project_id}/predictors", headers=self._headers, json={"predictor_ids": predictor_ids})
        return response.json(), response.status_code
    
    def add_moderator(self, project_id: str, moderator_ids: list[str]):
        response = requests.put(f"{self._base_url}/projects/{project_id}/moderators", headers=self._headers, json={"moderator_ids": moderator_ids})
        return response.json(), response.status_code

    def put_instance(self, project_id: str, features: dict):
        response = requests.post(f"{self._base_url}/projects/{project_id}/instances", headers=self._headers, json={"features": features})
        return response.json(), response.status_code


class PredictorClient:
    _predictor_token: str
    _base_url: str
    _headers: dict
    
    def __init__(self, predictor_token, base_url=base_url):
        self._predictor_token = predictor_token
        self._base_url = base_url
        self._headers = {"Authorization": f"Bearer {self._predictor_token}"}

    def list_projects(self):
        response = requests.get(f"{self._base_url}/projects", headers=self._headers)
        return response.json(), response.status_code

    def get_project(self, project_id: str):
        response = requests.get(f"{self._base_url}/projects/{project_id}", headers=self._headers)
        return response.json(), response.status_code

    def get_instance_batch(self, project_id: str, last_instance_id=None, batch_size=None):
        url = f"{self._base_url}/projects/{project_id}/instances"
        params = {}
        if last_instance_id is not None:
            params['last_instance_id'] = last_instance_id
        if batch_size is not None:
            params['batch_size'] = batch_size
        response = requests.get(url, headers=self._headers, params=params)
        return response.json(), response.status_code

    def put_prediction(self, project_id: str, instance_id: str, prediction_yes: float):
        response = requests.post(f"{self._base_url}/projects/{project_id}/instances/{instance_id}/predictions", headers=self._headers, json={"prediction_yes": prediction_yes})
        return response.json(), response.status_code