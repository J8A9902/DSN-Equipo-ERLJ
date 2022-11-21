from google.cloud import pubsub_v1

def publish_messages(project_id: str, topic_id: str, file_name: str) -> None:
    publisher = pubsub_v1.PublisherClient()
   
    topic_path = publisher.topic_path(project_id, topic_id)

    data = file_name.encode('UTF-8')

    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f"Published messages to {topic_path}.")
    