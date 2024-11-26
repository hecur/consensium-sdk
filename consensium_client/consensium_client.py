import requests

base_url = 'https://consensium-service-725186917460.europe-west2.run.app'

class ModeratorClient:
    def __init__(self, base_url=base_url):
        pass

    def get_next(self, project_id):
        pass

    def feedback(self, project_id, instance_id, feedback):
        pass


class OwnerClient:
    _owner_token: str
    _base_url: str
    _headers: dict

    def __init__(self, owner_token, base_url=base_url):
        self._owner_token = owner_token
        self._base_url = base_url
        self._headers = {"Authorization": f"Bearer {self._owner_token}"}

    def create_project(self, policy):
        return requests.post(f"{self._base_url}/projects", headers=self._headers, json={"policy": policy}).json()

    def update_policy(self, project_id, policy):
        return requests.put(f"{self._base_url}/projects/{project_id}/policy", headers=self._headers, json={"policy": policy}).json()
    
    def 

    def put_instance(self, project_id, features):
        return requests.post(f"{self._base_url}/projects/{project_id}/instances", headers=self._headers, json={"features": features}).json()


class PredictorClient:
    _predictor_token: str
    _base_url: str
    _headers: dict
    
    def __init__(self, predictor_token, base_url=base_url):
        self._predictor_token = predictor_token
        self._base_url = base_url
        self._headers = {"Authorization": f"Bearer {self._predictor_token}"}

    def list_projects(self):
        return requests.get(f"{self._base_url}/projects", headers=self._headers).json()

    def get_project(self, project_id):
        return requests.get(f"{self._base_url}/projects/{project_id}", headers=self._headers).json()

    def get_instance_batch(self, project_id, last_instance_id, batch_size):
        return requests.get(f"{self._base_url}/projects/{project_id}/instances?last_instance_id={last_instance_id}&batch_size={batch_size}", headers=self._headers).json()

    def put_prediction(self, project_id, instance_id, prediction):
        return requests.post(f"{self._base_url}/projects/{project_id}/instances/{instance_id}/predictions", headers=self._headers, json={"prediction": prediction})
