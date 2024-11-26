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
    def __init__(self, base_url=base_url):
        pass

    def create_project(self, acceptance_policy):
        pass

    def update_project(self, project_id, acceptance_policy):
        pass

    def put_instance(self, project_id, features):
        pass


class PredictorClient:
    _predictor_token: str
    _base_url: str

    def __init__(self, predictor_token, base_url=base_url):
        self._predictor_token = predictor_token
        self._base_url = base_url

    def list_projects(self):
        return requests.get(f"{self._base_url}/projects", headers={"Authorization": f"Bearer {self._predictor_token}"}).json()

    def get_project(self, project_id):
        return requests.get(f"{self._base_url}/projects/{project_id}", headers={"Authorization": f"Bearer {self._predictor_token}"}).json()

    def get_instance_batch(self, project_id, last_instance_id, batch_size):
        return requests.get(f"{self._base_url}/projects/{project_id}/instances?last_instance_id={last_instance_id}&batch_size={batch_size}", headers={"Authorization": f"Bearer {self._predictor_token}"}).json()

    def put_prediction(self, project_id, instance_id, prediction):
        return requests.post(f"{self._base_url}/projects/{project_id}/instances/{instance_id}/predictions", headers={"Authorization": f"Bearer {self._predictor_token}"}, json={"prediction": prediction})
