from locust import task, FastHttpUser

class TargetURL:
    SEARCH = "/search"

class LocustImpl(FastHttpUser):

    @task
    def search(self):
        search_query = "사랑"  # 검색어 예시
        self.client.get(TargetURL.SEARCH, params={"query": search_query})
