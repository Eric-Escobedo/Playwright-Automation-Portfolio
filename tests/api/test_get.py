import pytest

def test_get_single_post(playwright):
    api_request_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    response = api_request_context.get("/posts/1")
    assert response.ok
    body = response.json()
    assert body["id"] == 1
    assert isinstance(body["title"], str)
    
    api_request_context.dispose()
  
@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_multiple_posts(api_request_context, post_id):
    response = api_request_context.get(f"/posts/{post_id}")
    
    assert response.status == 200
    body = response.json()
    assert body["id"] == post_id
