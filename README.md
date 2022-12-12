gymlog-tests
TMS_diploma_project


pytest -v -m registration --alluredir reports
pytest -v -m login --alluredir reports
pytest -v -m home_page --alluredir reports
pytest -v -m my_exercises --alluredir reports
pytest -v -m my_settings --alluredir reports
pytest -v -m stretching --alluredir reports
pytest -v -m logout --alluredir reports
allure serve reports