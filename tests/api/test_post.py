import pytest

def test_create_post(playwright):
    api_request_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    new_post = {
        "title": "Mastering API Testing",
        "body": "Playwright and Pytest make a killer combo.",
        "userId": 1
    }
    
    response = api_request_context.post("/posts", data=new_post)
    assert response.status == 201
    
    body = response.json()
    assert body["title"] == "Mastering API Testing"
    assert "id" in body
    
    api_request_context.dispose()