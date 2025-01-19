from crewai_tools import BaseTool, SerperDevTool
from pydantic import BaseModel, Field, EmailStr
from typing import Type, List, Optional
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

print("Current Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

class TicketSearchArgsSchema(BaseModel):
    full_name: str = Field(..., description="The full name of the traveler.")
    email: EmailStr = Field(..., description="The email address to send tickets to.")
    traveling_from: str = Field(..., description="The departure location.")
    traveling_to: str = Field(..., description="The destination location.")
    travel_date: str = Field(..., description="The date of travel in YYYY-MM-DD format.")
    return_date: Optional[str] = Field(None, description="The return date in YYYY-MM-DD format (optional).")
    flight_class: str = Field(..., description="The class of travel (e.g., economy, business).")
    luggage_number: int = Field(..., description="The number of luggage pieces.")
    travel_companions: int = Field(..., description="The number of travel companions.")
    companion_type: Optional[str] = Field(None, description="Type of travel companion (e.g., minor, pet).")
    pet_type: Optional[str] = Field(None, description="Type of pet if the companion is a pet.")
    preferred_flight: Optional[str] = Field(None, description="Preferred flight details or 'open' for an open search.")
    flexible_dates: Optional[bool] = Field(False, description="Indicates if the traveler is flexible with travel dates.")

class TicketSearchTool(BaseTool):
    name: str = "Ticket Search Tool"
    description: str = "Searches for tickets based on various travel details."

    def __init__(self):
        super().__init__()
        self.args_schema = TicketSearchArgsSchema
        # Set the API key as an environment variable
        os.environ["SERPER_API_KEY"] = "5591e3125ff4adc849b11d93ef95a91bfb615972"

    def _run(self, full_name: str, email: str, traveling_from: str, traveling_to: str, 
             travel_date: str, return_date: Optional[str], flight_class: str, 
             luggage_number: int, travel_companions: int, companion_type: Optional[str], 
             pet_type: Optional[str], preferred_flight: Optional[str], 
             flexible_dates: Optional[bool] = False) -> List[str]:
        
        # Initialize the SerperDevTool
        search_tool = SerperDevTool()
        
        # Create a search query based on the travel details
        search_query = f"flights from {traveling_from} to {traveling_to} on {travel_date}"
        
        # Run the search tool with the query
        search_results = search_tool._run(search_query=search_query)
        
        # Return formatted results (search_results is already a string)
        return [
            f"Found tickets from {traveling_from} to {traveling_to} on {travel_date}:",
            f"Traveler: {full_name}, Email: {email}",
            f"Flight Class: {flight_class}, Luggage: {luggage_number}, Companions: {travel_companions}",
            f"Companion Type: {companion_type}, Pet Type: {pet_type}",
            f"Preferred Flight: {preferred_flight if preferred_flight else 'Open Search'}",
            "Search Results:",
            search_results  # Add the search results directly as they're already formatted
        ]

    def _get_travel_details(self, full_name: str, email: str, traveling_from: str, 
                             traveling_to: str, travel_date: str, return_date: Optional[str], 
                             flight_class: str, luggage_number: int, travel_companions: int, 
                             companion_type: Optional[str], pet_type: Optional[str], 
                             preferred_flight: Optional[str], flexible_dates: Optional[bool] = False) -> dict:
        """Returns the travel details as a dictionary."""
        travel_details = {
            "full_name": full_name,
            "email": email,
            "traveling_from": traveling_from,
            "traveling_to": traveling_to,
            "travel_date": travel_date,
            "return_date": return_date,
            "flight_class": flight_class,
            "luggage_number": luggage_number,
            "travel_companions": travel_companions,
            "companion_type": companion_type,
            "pet_type": pet_type,
            "preferred_flight": preferred_flight,
            "flexible_dates": flexible_dates
        }
        return travel_details

# Example usage
ticket_search_tool = TicketSearchTool()
results = ticket_search_tool.run(
    full_name="John Doe",
    email="john.doe@example.com",
    traveling_from="Los Angeles",
    traveling_to="New York",
    travel_date="2023-10-15",
    return_date="2023-10-20",
    flight_class="Economy",
    luggage_number=2,
    travel_companions=1,
    companion_type="Pet",
    pet_type="Dog",
    preferred_flight="Direct"
)
for result in results:
    print(result)

print("Current Environment Variables in Test:")
for key, value in os.environ.items():
    print(f"{key}: {value}") 