import requests

def test_text_correction():
   # API URL
   url = "http://localhost:8090/analyze"
   
   # Test data
   test_data = {
       "questionInput": "Quel animal de la nature vous fascine le plus et pourquoi ?",
       "essayInput": "Le lion me fascine car c'est le roi de la jungle."
   }
   
   print("Sending test request...")
   print(f"Question: {test_data['questionInput']}")
   print(f"Answer: {test_data['essayInput']}\n")
   
   try:
       response = requests.post(url, data=test_data)
       print(f"Status code: {response.status_code}")
       
       if response.ok:
           print("\nResponse content:")
           print(response.text)
           
       else:
           print(f"\nError: {response.status_code}")
           print(response.text)
           
   except requests.exceptions.ConnectionError:
       print("\nConnection Error: Could not connect to the server.")
       print("Make sure the Flask server is running on port 8090")
   except Exception as e:
       print(f"\nError occurred: {str(e)}")

if __name__ == "__main__":
   test_text_correction()