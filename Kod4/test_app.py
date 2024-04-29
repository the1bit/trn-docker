from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """Számláló tesztelése."""
    at = AppTest.from_file("app.py").run()
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[1].value == "Számláló: 2"