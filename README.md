# Context-Aware-Retrieval-Engine-
Mocking: Mock the vertexai.language_models.TextEmbeddingModel and GenerativeModel for the query expansion phase.

Instead of using any pretrained model for creating query expand, i have created own or local python function or model which is expand the query as per your instruction, which is mension in document. I have created mock model of GenerativeModel and TextEmbeddingModel. This all for only Strategy B.


set up = (Follow the 3 step)
1.  py -3.13 -m venv venv
2.  .\venv\Scripts\Activate.ps1
3.  pip install -r requirements.txt

Run only pytest.py file "python pytest.py". 

app.py -> main code file.
pytest.py -> used for testing and create output_test.md file.
output_test.md -> save test output in md file
Documentation_explination.txt -> Documentation
document.txt -> data which is store in vector data based.