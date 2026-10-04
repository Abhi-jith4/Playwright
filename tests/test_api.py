def test_api_get(playwright):
    request=playwright.request.new_context()
    response=request.get("https://reqres.in/api/users/2")
    assert response.status == 200
    json_data=response.json()
    print(json_data)

    assert json_data["data"]["id"] == 2
    assert json_data["data"]["email"] == "janet.weaver@reqres.in"
    assert json_data["data"]["first_name"] == "Janet"
    assert json_data["data"]["last_name"] == "Weaver"

    request.dispose()
    print("Status code:", response.status)
    
    print("API GET request test completed successfully.")