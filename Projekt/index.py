from pydantic import BaseModel, Field
from typing import List, Optional, ForwardRef

# Forward reference needed for mutual references
DeveloperRef = ForwardRef('Developer')

class Project(BaseModel):
    title: str
    description: Optional[List[str]] = Field(default_factory=list)
    lead_developer: DeveloperRef

class Developer(BaseModel):
    name: str
    experience: Optional[int] = None

# Update forward refs
Project.update_forward_refs()
