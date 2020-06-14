from .Connector import Connector

from .ApiModels import Faq as Models


class Faq(Connector):

    def search(self, model_id, text, lang=None, variations=None, prod_version=None):
        return Models.Search.fill(**locals()).call(self.client)

    def train_model(self, model_id):
        return Models.TrainModel.fill(**locals()).call(self.client)

    def deploy_model(self, model_id):
        return Models.DeployModel.fill(**locals()).call(self.client)

    def clear_model(self, model_id):
        return Models.ClearModel.fill(**locals()).call(self.client)

    def create_model(self, model_id):
        return Models.CreateModel.fill(**locals()).call(self.client)

    def create_questions(self, model_id, questions):
        return Models.CreateQuestions.fill(**locals()).call(self.client)

    def create_answers(self, model_id, answers):
        return Models.CreateAnswers.fill(**locals()).call(self.client)

    def update_question(self, model_id, question_id, answer_id=None, variations=None):
        return Models.UpdateQuestion.fill(**locals()).call(self.client)

    def update_answer(self, model_id, answer_id, variations=None):
        return Models.UpdateAnswer.fill(**locals()).call(self.client)

    def delete_model(self, model_id):
        return Models.DeleteModel.fill(**locals()).call(self.client)

    def delete_question(self, model_id, question_id):
        return Models.DeleteQuestion.fill(**locals()).call(self.client)

    def delete_answer(self, model_id, answer_id):
        return Models.DeleteAnswer.fill(**locals()).call(self.client)

    def list_questions(self, model_id, page=None, page_size=None, sort=None, ascending=None, id=None, answer_id=None):
        return Models.ListQuestions.fill(**locals()).call(self.client)

    def list_answers(self, model_id, page=None, page_size=None, sort=None, ascending=None, id=None):
        return Models.ListAnswers.fill(**locals()).call(self.client)

    def upload_csv_questions(self, model_id, filename, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateQuestions, "questions", **locals())

    def upload_csv_answers(self, model_id, filename, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateAnswers, "answers", **locals())

