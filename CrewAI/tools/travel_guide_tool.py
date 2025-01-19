import os
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from typing import List, Optional, Type
from crewai_tools import SerperDevTool

class TravelGuideArgsSchema(BaseModel):
    location: str = Field(..., description="The location to search for accommodations and attractions.")
    travel_date: str = Field(..., description="The date of travel in YYYY-MM-DD format.")
    return_date: Optional[str] = Field(None, description="The return date in YYYY-MM-DD format (optional).")

class TravelGuideTool(BaseTool):
    # Type annotations required by Pydantic v2 when overriding fields from BaseTool
    # Without these, Pydantic raises an error about non-annotated attributes
    name: str = "Travel Guide Tool"
    description: str = "Provides information on weather, accommodations, and attractions."
    args_schema: Type[TravelGuideArgsSchema] = TravelGuideArgsSchema

    def __init__(self):
        super().__init__()
        self.args_schema = TravelGuideArgsSchema

    def _run(self, location: str, travel_date: str, return_date: Optional[str] = None) -> List[str]:
        search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

        # Search for weather conditions
        weather_query = f"weather in {location} on {travel_date}"
        weather_results = search_tool._run(search_query=weather_query)

        # Search for hotels and accommodations
        hotel_query = f"hotels in {location} on {travel_date}"
        hotel_results = search_tool._run(search_query=hotel_query)

        # Search for tourist attractions
        attractions_query = f"tourist attractions in {location}"
        attractions_results = search_tool._run(search_query=attractions_query)

        # Format the results
        results = [
            f"Weather in {location} on {travel_date}: {weather_results}",
            f"Hotels in {location}: {hotel_results}",
            f"Tourist Attractions in {location}: {attractions_results}"
        ]

        print(f"args_schema type: {type(self.args_schema)}")

        return results

    def test(self):
        try:
            # Test the tool
            self._run("New York", "2024-05-01")
            print("✓ Test travel agent passed")
        except Exception as e:
            print(f"✗ Test travel agent error: {str(e)}")
            import traceback
            traceback.print_exc() 