@echo off
curl -X POST "http://localhost:8000/upload/?filename=test-1.docx" -F "file=@test_data\1_lisbon_earthquake.docx"
pause