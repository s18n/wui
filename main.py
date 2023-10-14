from google_search import GoogleSearchClient
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Label, Footer, Header, Input, Static

# Google search config
api_key = "AIzaSyDcqqHbZXp6TRxcgyphlSJaimWrdqIMwEg"
cse_id = "9768910b5866b414d"
search_client = GoogleSearchClient(api_key, cse_id)

class SearchBarWidget(Static):
  """A search bar widget."""

  def compose(self) -> ComposeResult:
    """Create child widgets of a stopwatch."""
    yield Input(placeholder="Query", id="search_field")

  @on(Input.Submitted)
  def accept_search(self):
    input = self.query_one(Input)
    query = input.value
    search_results = search_client.search_google(query)
    for result in search_results:
      self.mount(Label(result["link"]))
    input.value = ""


class TerminalWebSearch(App):
  """A TUI for air quality information"""

  def compose(self) -> ComposeResult:
    yield Header()
    yield Footer()

    with Container():
      yield SearchBarWidget()

if __name__ == "__main__":
    app = TerminalWebSearch()
    app.run()