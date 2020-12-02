import requests
from username import user_name


def test_dockerhub_repo():
    r = requests.get(
        f"https://hub.docker.com/repositories/docker/{user_name}/simplelayout/"
    )
    assert r.status_code == 200, "无法找到镜像仓库！"
