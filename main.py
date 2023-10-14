from google_search import GoogleSearchClient
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import OptionList, Footer, Header, Input, Static
from textual.widgets.option_list import Option, Separator


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
    result_option_list = OptionList()

    for result in search_results:
      title = Option(result["title"], disabled=True)
      link = Option(result["link"])
      result_option_list.add_option(title)
      result_option_list.add_option(link)
      result_option_list.add_option(Separator())
   
    self.mount(result_option_list)
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