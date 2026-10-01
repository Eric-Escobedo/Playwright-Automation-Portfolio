import pytest

def test_update_post(api_request_context):
    updated_post = {
        "id": 1,
        "title": "Mastering API Testing - Updated",
        "body": "Updated the body text with fresh content",
        "userId": 1
    }
    
    response = api_request_context.put("/posts/1", data = updated_post)
    
    assert response.status == 200
    body = response.json()
    assert body["title"] == "Mastering API Testing - Updated"
    
def test_delete_post(api_request_context):
    response = api_request_context.delete("/posts/1")
    assert response.status == 200