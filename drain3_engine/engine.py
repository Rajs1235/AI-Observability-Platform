from drain3.template_miner import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig


class Drain3Engine:

    def __init__(self):
        config = TemplateMinerConfig()
        config.load("drain3.ini")
        self.template_miner = TemplateMiner(config=config)

    def process_log(self, message):
        result=self.template_miner.add_log_message(message)
        print(result)
        return (
        result["cluster_id"],
        result["template_mined"],
        result["cluster_size"]
    )

    def process_logs(self, logs):
        results = []

        for log in logs:
            results.append(self.process_log(log))

        return results

    def get_templates(self):
        templates = []

        for cluster in self.template_miner.drain.clusters:
            templates.append({
                "cluster_id": cluster.cluster_id,
                "occurrences": cluster.size,
                "template": cluster.get_template()
            })

        return templates

    def update_repository(self, repository):

     templates = self.get_templates()

     for template in templates:

        repository.save_or_update(

            template["cluster_id"],

            template["template"],

            template["occurrences"]
        )