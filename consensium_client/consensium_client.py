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
    def __init__(self, base_url=base_url):
        pass

    def list_projects(self):
        pass

    def get_project(self, project_id):
        pass

    def get_instance_batch(self, project_id, last_instance_id, batch_size):
        pass

    def put_prediction(self, project_id, instance_id, prediction):
        pass
